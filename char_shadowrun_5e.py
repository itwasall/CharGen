import chargen
import random
import char_shadowrun_5e_data as Core
from collections import OrderedDict
"""
    GOALS

Lets set out some design goals and then have nowhere to formally put them.

    1) Generate Character 
    2) Lil TUI Interface that allows the user to, once a character is fully generated, scroll through menus to look at a weapon in more detail for example.
    2a) I am scrapping this idea immediately after I had it because adding all the different and differing stats for the multitude of pieces of gear is long boring and isn't
            required. A page number reference will suffice.
"""
"""
    USAGE
    dice("2d6")
"""
def dice(dice_string):
    sides, throws = dice_string.split("d")
    return sum([random.randint(1, int(sides)) for _ in range(int(throws))])

# returns all not dunder and non 'items' attributes for a class in {attr_name: attr_value} format
def attrAsDict(_class):
    return {i: _class.__getattribute__(i) for i in dir(_class) if not i.startswith("__") and i != 'items'}

def get_rating(item: Core.Gear):
    if "rating" not in attrAsDict(item).keys():
        return 1
    if isinstance(item.rating, int):
        return item.rating
    elif isinstance(item.rating, str):
        return 0
    elif isinstance(item.rating, list):
        return random.choice(range(item.rating[0], item.rating[2]))
    else:
        raise ValueError(f'{item.name} has bad rating data')

def get_item_cost(item: Core.Gear):
    # When an item's cost is dependant on another items rating or capacity
    def item_requirement_handler(item: Core.Gear, rand=True):
        if isinstance(item.requires, list):
            match item.requires[0]:
                case "Subtype":
                    print(item.requires[1])
                    print([i for i in Core.Gear.items if i.subtype == item.requires[1]])
                    return random.choice([i for i in Core.Gear.items if i.subtype == item.requires[1]])
                case "Category":
                    if item.requires[1] == item.category:
                        return random.choice([i for i in Core.Gear.items if i.category == item.requires[1] and i.subtype != item.requires[1]])
                    return random.choice([i for i in Core.Gear.items if i.category== item.requires[1]])
        elif isinstance(item.requires, Gear):
            return item.requires
        elif isinstance(item.requires, tuple):
            return random.choice(item.requires)

    req_item_flag = False
    if isinstance(item.cost, int):
        return item.cost
    item_attrs = attrAsDict(item)
    item_cost = item.cost
    if 'requires' in item_attrs.keys():
        req_item = item_requirement_handler(item)
        req_item_flag = True
        print(req_item)
    match item.cost[0]:
        case 'Rating':
            if req_item_flag:
                item_cost[0] = get_rating(req_item)
            else:
                item_cost[0] = get_rating(item)
                print(f'{item.name} rating is {item_cost[0]}')
        case 'Capacity':
            item_cost[0] = random.choice(range(item.capacity[0], item.capacity[2]))
            print(f'{item.name} capacity is {item_cost[0]}')
        case 'WeaponCost':
            item_cost[0] = get_item_cost(req_item)
        case 'Range':
            return random.randint(item_cost[1], item_cost[2])
        case _:
            print(item_cost[0])
            raise ValueError()
    match item.cost[1]:
        case "*":
            return item_cost[0] * item_cost[2]
        case "+":
            return item_cost[0] + item_cost[2]
    return item_cost

def get_priorities(character: Core.Character):
    table_choices = ['A', 'B', 'C', 'D', 'E']
    table_categories = ['Metatype', 'Attributes', 'MagicResonance', 'Skills', 'Resources']
    selected_items = {'Metatype': None, 'Attributes': None, 'MagicResonance': None, 'Skills': None, 'Resources': None}
    for category in table_categories:
        priority_chosen = random.choice(table_choices)
        table_choices.pop(table_choices.index(priority_chosen))
        selected_items[category] = Core.PRIORITY_TABLE_FLIPPED[category][priority_chosen]
    return selected_items


def get_highest_attr(ch: Core.Character):
    non_special_attrs = ch.PhysicalAttributes + ch.MentalAttributes
    highest = 0
    highest_attrs = []
    second_highest = 0
    second_attrs = []
    for idx, i in enumerate(non_special_attrs):
        if non_special_attrs[idx].value > highest:
            second_highest = highest
            highest = non_special_attrs[idx].value
    highest_attrs = [attr for attr in non_special_attrs if attr.value == highest]
    if len(highest_attrs) > 1:
        return highest_attrs
    else:
        second_attrs = [attr for attr in non_special_attrs if attr.value == second_highest]
        second_highest = highest
        while len(second_attrs) == 0:
            second_attrs = [attr for attr in non_special_attrs if attr.value == second_highest]
            second_highest -= 1
        return [highest_attrs[0], second_attrs[0]]


    """def current_highest():
        x = []
        highest = max(non_special_values)
        if len(value_to_attr[highest]) == 1:
            x = value_to_attr[highest]
            return x
        else:
            while len(value_to_attr[highest]) >= 1:
                choice = value_to_attr[highest]
                x.append(choice[0])
                value_to_attr[highest].remove(choice[0])
                if len(return_list) == 2:
                    return return_list

    return_list = []
                            
    non_special_attrs = ch.PhysicalAttributes + ch.MentalAttributes
    non_special_values = [attr.value for attr in non_special_attrs]
    # Making dict of {4: 'Intuition'}
    value_to_attr = {}
    for v in non_special_values:
        value_to_attr[v] = [a.name for a in non_special_attrs if a.value == v]

    return_list.append(current_highest())
    """


def roll_stats(ch: Core.Character, attr: int):
    rollable_stats = [
            ch.Body, ch.Agility, ch.Reaction, ch.Strength, ch.Willpower,
            ch.Logic, ch.Intuition, ch.Charisma, ch.Edge
            ]
    while attr > 0:
        stat_roll = random.choice(rollable_stats)
        if stat_roll.value + 1 <= stat_roll.limit:
            stat_roll.value += 1
            attr -= 1
    ch.print_stats()
    dominant_stats = [attribute for attribute in rollable_stats if attribute.value >= 4]
    # if len(dominant_stats) < 1:
    #    raise ValueError("No dominant stats!")
    print(dominant_stats)

def karma_qualities(ch: Core.Character):
    pass

def add_spell(ch: Core.Character):
    pass

def resolve_magic_resonance_skills(ch: Core.Character, tbl):
    skills = {}
    match tbl['Type']:
        case 'Magic':
            for _ in range(tbl['Quantity']):
                while True:
                    chosen = random.choice(Core.MAGIC_SKILLS)
                    if chosen not in skills.keys():
                        break
                skills[chosen.name] = chosen
                skills[chosen.name].rating = tbl['Rating']
        case 'Resonance':
            for _ in range(tbl['Quantity']):
                while True:
                    chosen = random.choice(Core.RESONANCE_SKILLS)
                    if chosen not in skills.keys():
                        break
                skills[chosen.name] = chosen
                skills[chosen.name].rating = tbl['Rating']
        case 'Magic Group':
            groups_chosen = []
            for _ in range(tbl['Quantity']):
                while True:
                    chosen = random.choice(Core.MAGIC_SKILL_GROUPS)
                    if chosen not in groups_chosen:
                        break
                groups_chosen.append(chosen)
            for group in groups_chosen:
                for skill in group.skills:
                    skills[skill.name] = skill
                    skills[skill.name].rating = tbl['Rating']
                    skills[skill.name].group = group.name
        case 'Active':
            for _ in range(tbl['Quantity']):
                while True:
                    chosen = random.choice(Core.ACTIVE_SKILLS)
                    if chosen not in skills.keys():
                        break
                skills[chosen.name] = chosen
                skills[chosen.name].rating = tbl['Rating']
    return skills

def add_complex_form(ch: Core.Character):
    if type(ch.Complex_forms) != list:
        ch.Complex_forms = []
    ch.Complex_forms.append(random.choice(Core.ComplexForm.items))

    
def resolve_magic_resonance(ch: Core.Character, tbl):
    # tbl = priority_table['MagicResonance']
    if tbl is None:
        return
    _type = random.choice(list(tbl.keys()))
    ch.MagicResoUser = str(_type)
    print(f'//////\nUh oh! Looks like you\'re a {_type}')
    for key in list(tbl[_type].keys()):
        if key == "Magic":
            ch.Magic = Core.Attribute("Magic")
            ch.Magic.value = tbl[_type][key]
            print(ch.Magic)
        elif key == "Resonance":
            ch.Resonance = Core.Attribute("Resonance")
            ch.Resonance.value = tbl[_type][key]
            print(ch.Resonance)
        elif key == "Spells":
            for i in range(tbl[_type][key]):
                add_spell(ch)
        # elif key == "Skills":
        #    print("resolve magi/res Skills")
        #    print(f"You get {tbl[_type]['Skills']['Quantity']} different skills  at rating {tbl[_type]['Skills']['Rating']}")
        #    resolve_magic_resonance_skills(ch, tbl[_type][key])
        elif key == "Complex Forms":
            for i in range(tbl[_type][key]):
                add_complex_form(ch)


def get_skills(ch: Core.Character, tbl, skill_cap = 50, attr_influence = None, **kwargs):
    """
    def init_shit():
        for s in Core.Skill.items:
            if hasattr(s, 'group'):
                s.group = False
            s.rating = 0
        Core.refresh_priority_table()
    
    init_shit()
    """
    character_skills = {}
    skill_points_table = tbl['Skills']
    if ch.MagicResoUser is not None:
        if 'Skills' in tbl['MagicResonance'][ch.MagicResoUser].keys():
            magic_reso_skills = resolve_magic_resonance_skills(ch, tbl['MagicResonance'][ch.MagicResoUser]['Skills'])
            print(f"Magic/Resonance Skills:\n {magic_reso_skills}")
            for k, d in magic_reso_skills.items():
                character_skills[k] = d
        else:
            pass

    skill_points, group_points = skill_points_table


    list_of_skills = [skill for skill in Core.Skill.items if skill.skill_type == "Active"]
    list_of_groups = [group for group in Core.SkillGroup.items]

    # Non-magic users can't select magic skills/groups
    # Non-resonance users can't select resonance skills/group
    if ch.Magic is None:
        for _ in Core.MAGIC_SKILLS:
            list_of_skills.pop(list_of_skills.index(_))
        for _ in Core.MAGIC_SKILL_GROUPS:
            list_of_groups.pop(list_of_groups.index(_))

    if ch.Resonance is None:
        for _ in Core.RESONANCE_SKILLS:
            list_of_skills.pop(list_of_skills.index(_))
        list_of_groups.pop(list_of_groups.index(Core.TASKING))

    weight_skills = [1 for _ in list_of_skills]
    weight_groups = [1 for _ in list_of_groups]

    # Adjusting weights based on highest physical and mental attributes
    if attr_influence is not None:
        for attr in attr_influence:
            skills_of_same_attribute = [s for s in list_of_skills if s.attribute == attr.name]
            for i in skills_of_same_attribute:
                weight_skills[list_of_skills.index(i)] += 30
            for group in list_of_groups:
                if group.skills[0].attribute == attr.name:
                    weight_groups[list_of_groups.index(group)] += 3



    # Group Skill Points spend
    # for _ in range(group_points):
    while group_points > 0:
        ROLL_GROUP = random.choices(list_of_groups, weight_groups)[0]
        for skill in ROLL_GROUP.skills:
            # print(f"Roll group {ROLL_GROUP.name} processing {skill.name}")
            if skill.name not in character_skills.keys():
                character_skills[skill.name] = skill
                character_skills[skill.name].group = ROLL_GROUP.name
                character_skills[skill.name].rating += 1
            else:
                character_skills[skill.name].rating += 1
        # Adjusting weights based on groups already selected
        weight_groups[list_of_groups.index(ROLL_GROUP)] += random.randint(1, 2)
        same_attribute_list = [s for s in list_of_skills if s.attribute == skill.attribute and s.name != skill.name]
        for same_attr in same_attribute_list:
            weight_skills[list_of_skills.index(same_attr)] += random.randint(1, 3)
                
        group_points -= 1
            
    # Individual Skill Points spend
    # for _ in range(skill_points):
    while skill_points > 0:
        ROLL_SKILL = random.choices(list_of_skills, weight_skills)[0]
        non_grouped_skills_count = len([i for i in character_skills.keys() if character_skills[i].group == False])
        if ROLL_SKILL.name in character_skills.keys() and character_skills[ROLL_SKILL.name].group != False:
            pass
        elif ROLL_SKILL.name not in character_skills.keys() and non_grouped_skills_count >= skill_cap:
            pass
        else:
            if ROLL_SKILL.name not in character_skills.keys():
                character_skills[ROLL_SKILL.name] = ROLL_SKILL
            elif character_skills[ROLL_SKILL.name].rating >= 12:
                continue
            character_skills[ROLL_SKILL.name].rating += 1
            # Adjusting weights based on skills already selected
            match weight_skills[list_of_skills.index(ROLL_SKILL)]:
                case 1,2,3:
                    weight_skills[list_of_skills.index(ROLL_SKILL)] += random.randint(1,5)
                case _:
                    weight_skills[list_of_skills.index(ROLL_SKILL)] += random.randint(1,2)
            same_attribute_list = [skill for skill in list_of_skills if skill.attribute == ROLL_SKILL.attribute and skill.name != ROLL_SKILL.name]
            for same_attr in same_attribute_list:
                weight_skills[list_of_skills.index(same_attr)] += random.randint(1, 3)
            else:
                pass
            skill_points -= 1
    
    return character_skills

def format_skills(character_skills):
    # Getting debug output_by_group. Sorts skills by group first, then by ranking
    output_by_group = {'Non-Grouped': {}}
    output_by_attr = {}
    print("====")
    print("ACTIVE SKILLS")
    print("    by Group/Rating:")
    print("---")
    for k, d in character_skills.items():
        if d.attribute.name not in output_by_attr.keys():
            output_by_attr[d.attribute.name] = [d.name]
        else:
            output_by_attr[d.attribute.name].append(d.name)
        if d.group != False:
            if d.group not in output_by_group.keys():
                output_by_group[d.group] = {}
                if d.rating not in output_by_group[d.group].keys():
                    output_by_group[d.group][d.rating] = [d.name]
                else:
                    output_by_group[d.group][d.rating].append(d.name)
            else:
                if d.rating not in output_by_group[d.group].keys():
                    output_by_group[d.group][d.rating] = [d.name]
                else:
                    output_by_group[d.group][d.rating].append(d.name)
        else:
            if d.rating not in output_by_group['Non-Grouped'].keys():
                output_by_group['Non-Grouped'][d.rating] = [d.name]
            else:
                output_by_group['Non-Grouped'][d.rating].append(d.name)

    for group in output_by_group.keys():
        output_by_group[group] = OrderedDict(sorted(output_by_group[group].items(), key=lambda t: t[0]))
        print("---\n -->", group)
        for rating in output_by_group[group].keys():
            print(rating, output_by_group[group][rating])
    print("===")
    print("    by Attribute:")
    print("===")

    for attr in output_by_attr.keys():
        print(f'---> {attr}')
        print(", ".join([skill for skill in output_by_attr[attr]]))

    print("===")
    print("    Magic:")
    print(", ".join([skill for skill in character_skills.keys() if skill in [i.name for i in Core.MAGIC_SKILLS]]))
    print("===")
    print("    Resonance:")
    print(", ".join([skill for skill in character_skills.keys() if skill in Core.MAGIC_SKILLS]))


def generate_character():
    # PHASE 1: CONCEPT
    character = Core.Character()
    priority_table = get_priorities(character)
    metatype = random.choice(priority_table['Metatype'])
    attribute_points = priority_table['Attributes']
    # Initialising Stuff
    edge_shit = metatype[1]
    metatype = metatype[0]
    metatype.attributes.init_stat_block()
    character.Metatype = metatype
    for attribute in metatype.attributes.List:
        match attribute.name:
            case 'Body':
                character.Body = metatype.attributes.Body
            case 'Agility':
                character.Agility = metatype.attributes.Agility
            case 'Reaction':
                character.Reaction = metatype.attributes.Reaction
            case 'Strength':
                character.Strength = metatype.attributes.Strength
            case 'Willpower':
                character.Willpower = metatype.attributes.Willpower
            case 'Logic':
                character.Logic = metatype.attributes.Logic
            case 'Intuition':
                character.Intuition = metatype.attributes.Intuition
            case 'Charisma':
                character.Charisma = metatype.attributes.Charisma
            case 'Edge':
                character.Edge = metatype.attributes.Edge
            case 'Essence':
                character.Essence = metatype.attributes.Essence
    character.redo_attr()
    # STEP 1: ATTRIBUTES
    print(f"======\nRolling with {priority_table['Attributes']} points")
    roll_stats(character, attribute_points)
    highest_attrs = get_highest_attr(character)
    # STEP 3: MAGIC/RESONANCE
    magic_reso = priority_table['MagicResonance']
    resolve_magic_resonance(character, magic_reso)
    # STEP 4: QUALITIES
    # STEP 5: SKILLS
    character.Skills = get_skills(character, priority_table, attr_influence=highest_attrs, skill_cap=20)
    format_skills(character.Skills)
    # Attribute Points


    # PHASE 2: PR
    pass
"""
print(STRENGTH.what_is())
print(BIOTECHNOLOGY.what_is())
print(THROWING.what_is())
print(ELF.what_is())
print(STREETSAMURAI.what_is())
print(DEFINANCE_EX_SHOCKER.what_is())
print(DEFINANCE_EX_SHOCKER.damage)
print(SENSOR_RFID.category)
print([f"{i}" for i in dir(SINGLE_SENSOR) if not i.startswith("__")])
print(SINGLE_SENSOR.sensor_function)
"""
generate_character()
