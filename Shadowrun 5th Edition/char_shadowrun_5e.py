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


def get_priorities(character: Core.Character):
    table_choices = ['A', 'B', 'C', 'D', 'E']
    table_categories = ['Metatype', 'Attributes', 'MagicResonance', 'Skills', 'Resources']
    selected_items = {'Metatype': None, 'Attributes': None, 'MagicResonance': None, 'Skills': None, 'Resources': None}
    for category in table_categories:
        priority_chosen = random.choice(table_choices)
        table_choices.pop(table_choices.index(priority_chosen))
        selected_items[category] = Core.PRIORITY_TABLE_FLIPPED[category][priority_chosen]
    # while selected_items['Resources'] == 6000:
    #    get_priorities(character)
    return selected_items


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
    # ch.print_stats()
    dominant_stats = [attribute for attribute in rollable_stats if attribute.value >= 4]
    # if len(dominant_stats) < 1:
    #    raise ValueError("No dominant stats!")
    # print(dominant_stats)


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


def get_skills(ch: Core.Character, tbl, skill_cap = 50, attr_influence = None, **kwargs):

    character_skills = {}
    character_specialisations = {}
    skill_points_table = tbl['Skills']
    if ch.MagicResoUser is not None:
        if 'Skills' in tbl['MagicResonance'][ch.MagicResoUser].keys():
            magic_reso_skills = resolve_magic_resonance_skills(ch, tbl['MagicResonance'][ch.MagicResoUser]['Skills'])
            print(f"Magic/Resonance Skills:\n {magic_reso_skills}")
            for k, d in magic_reso_skills.items():
                character_skills[k] = d
        else:
            pass


    list_of_skills_raw = [skill for skill in Core.Skill.items if skill.skill_type == "Active"]
    list_of_groups_raw = [group for group in Core.SkillGroup.items]
    weight_skills = [1 for _ in list_of_skills_raw]
    weight_groups = [1 for _ in list_of_groups_raw]

    list_of_skills = {}
    list_of_groups = {}
    for idx, i in enumerate(list_of_skills_raw):
        list_of_skills[i] = weight_skills[idx]
    for idx, i in enumerate(list_of_groups_raw):
        list_of_groups[i] = weight_groups[idx]



    if "builds" in kwargs:
        if kwargs['builds']['IS_DECKER']:
            for _ in range(2):
                decker_skill = random.choice(Core.DECKER_SKILLS)
                character_skills[decker_skill.name] = decker_skill
                character_skills[decker_skill.name].rating += 1
                list_of_skills[decker_skill] += 3
            pass
        if kwargs['builds']['IS_RIGGER']:
            for _ in range(2):
                rigger_skill = random.choice(Core.RIGGER_SKILLS)
                character_skills[rigger_skill.name] = rigger_skill 
                character_skills[rigger_skill.name].rating += 1
                list_of_skills[rigger_skill] += 3
            pass
        if kwargs['builds']['IS_FACE']:
            for _ in range(2):
                face_skill = random.choice(Core.FACE_SKILLS)
                character_skills[face_skill.name] = face_skill 
                character_skills[face_skill.name].rating += 1
                list_of_skills[face_skill] += 3
            pass

    skill_points, group_points = skill_points_table


    # Non-magic users can't select magic skills/groups
    # Non-resonance users can't select resonance skills/group
    if ch.Magic is None:
        for sk in Core.MAGIC_SKILLS:
            list_of_skills[sk] = 0
        for sk in Core.MAGIC_SKILL_GROUPS:
            list_of_groups[sk] = 0

    if ch.Resonance is None:
        for sk in Core.RESONANCE_SKILLS:
            list_of_skills[sk] = 0
        list_of_groups[Core.TASKING] = 0


    # Adjusting weights based on highest physical and mental attributes
    if attr_influence is not None:
        for attr in attr_influence:
            skills_of_same_attribute = [s for s in list_of_skills.keys() if s.attribute.name == attr.name]
            for i in skills_of_same_attribute:
                list_of_skills[i] += 3
            for group in list_of_groups:
                if group.skills[0].attribute == attr.name:
                    list_of_groups[group] += 3

    # Group Skill Points spend
    # for _ in range(group_points):
    while group_points > 0:
        ROLL_GROUP = random.choices(list(list_of_groups.keys()), list(list_of_groups.values()))[0]
        for skill in ROLL_GROUP.skills:
            if skill.name not in character_skills.keys():
                character_skills[skill.name] = skill
                character_skills[skill.name].group = ROLL_GROUP.name
                character_skills[skill.name].rating += 1
            else:
                character_skills[skill.name].rating += 1
        # Adjusting weights based on groups already selected
        list_of_groups[ROLL_GROUP] += random.randint(1, 2)
        same_attribute_list = [s for s in list_of_skills.keys() if s.attribute == skill.attribute and s.name != skill.name]
        for same_attr in same_attribute_list:
            list_of_skills[same_attr] += random.randint(1, 3)
                
        group_points -= 1
            
    # Individual Skill Points spend
    while skill_points > 0:
        # Rolling for skill specialisations
        skills_for_spec = [d for k, d in character_skills.items() if d.rating > 4 and d.group == False]
        if len(skills_for_spec) > 1 and random.randint(1,100) > 80: 
            ROLL_SPEC = random.choice(skills_for_spec)
            while len(ROLL_SPEC.spec) < 1:
                ROLL_SPEC = random.choice(skills_for_spec)
            ROLL_SPECIALISATION = random.choice(ROLL_SPEC.spec)
            if isinstance(character_skills[ROLL_SPEC.name].spec, list): 
                character_skills[ROLL_SPEC.name].spec = ROLL_SPECIALISATION
                skill_points -=  1
            else:
                pass
        
        ROLL_SKILL = random.choices(list(list_of_skills.keys()), list(list_of_skills.values()))[0]
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
            match list_of_skills[ROLL_SKILL]:
                case 1,2,3:
                    list_of_skills[ROLL_SKILL] += random.randint(1, 5)
                case _:
                    list_of_skills[ROLL_SKILL] += random.randint(1,2)
            same_attribute_list = [skill for skill in list_of_skills if skill.attribute == ROLL_SKILL.attribute and skill.name != ROLL_SKILL.name]
            for same_attr in same_attribute_list:
                list_of_skills[same_attr] += random.randint(1, 3)
            else:
                pass
            skill_points -= 1
    
    return character_skills


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


def karma_qualities(ch: Core.Character, k: Core.KarmaLogger):
    ch.Qualities = {}
    total_karma = 25
    positive_karma = 0
    negative_karma = 0
    k.append(f'Beginning karma logging.\n   {total_karma} is Karma total') 
    NEGATIVE_TOO_HIGH = False
    POSITIVE_TOO_HIGH = False
    quality_weights = [1 for _ in Core.Quality.items]
    inc = 0
    while total_karma > 0:
        ch.Karma = total_karma
        # There's an infinite loop I can't be bothered to fix right now, this will do
        inc += 1
        if inc > 100000:
            break
        if total_karma < 10 and random.randint(0,1) == 1:
            break
        ROLL_KARMA = random.choices(Core.Quality.items, quality_weights)[0]
        if ROLL_KARMA.name in ch.Qualities.keys():
            if hasattr(ROLL_KARMA, "quantity"):
                # Some qualities can be taken multiple times. The cap is called "quantity" and the 
                #   current amount of levels taken is "level".
                if hasattr(ch.Qualities[ROLL_KARMA.name], "level"):
                    if ch.Qualities[ROLL_KARMA.name].level > ROLL_KARMA.quantity:
                        continue
                else:
                    raise ValueError("Quality with quant already selected but has no level value in character dict")
            else:
                continue
        # If a quality in the same group has already been taken, continue (SEE DATA)
        if hasattr(ROLL_KARMA, "group"):
            if ROLL_KARMA.group in [d.group for d in ch.Qualities.values() if hasattr(d, "group")]:
                continue
        # Negative qualities cannot total more than ABS(25)
        if hasattr(ROLL_KARMA, "negative"):
            if negative_karma + ROLL_KARMA.cost > 25:
                NEGATIVE_TOO_HIGH = True
                continue
                # continue
        # Positive qualities cannot total more than ABS(25)
        elif positive_karma + ROLL_KARMA.cost > 25:
            POSITIVE_TOO_HIGH = True
            continue
            # continue
        if total_karma - ROLL_KARMA.cost < 0 or (NEGATIVE_TOO_HIGH and not POSITIVE_TOO_HIGH) or (POSITIVE_TOO_HIGH and not NEGATIVE_TOO_HIGH):
            continue
        if hasattr(ROLL_KARMA, "negative"):
            negative_karma += ROLL_KARMA.cost
            total_karma += ROLL_KARMA.cost
            k.append(f'(NEG) {ROLL_KARMA.name} has been bought. Costing {ROLL_KARMA.cost}.\n   {total_karma} is Karma total.\n   Negative Karma is at {negative_karma}')
        else:
            positive_karma += ROLL_KARMA.cost
            total_karma -= ROLL_KARMA.cost
            k.append(f'(POS) {ROLL_KARMA.name} has been bought. Costing {ROLL_KARMA.cost}.\n   {total_karma} is Karma total\n   Positive Karma is at {positive_karma}')

        # Pretty output & roll for quality specific params here
        ROLL_KARMA = resolve_quality(ROLL_KARMA, ch)

        ch.Qualities[ROLL_KARMA.name] = ROLL_KARMA
        if hasattr(ROLL_KARMA, "quantity"):
            if hasattr(ch.Qualities[ROLL_KARMA.name], "level"):
                ch.Qualities[ROLL_KARMA.name].level += 1
            else:
                ch.Qualities[ROLL_KARMA.name].level = 1
            quality_weights[Core.Quality.items.index(ROLL_KARMA)] += 10
        if NEGATIVE_TOO_HIGH and POSITIVE_TOO_HIGH:
            break
    # print(ch.Qualities)


def resolve_quality(q: Core.Quality, ch: Core.Character):
    # Just a dump for all the quality-specific rolling options
    if "Allergy" in q.name:
        if "Common" in q.name:
            x = {5: 'Mild', 10: 'Moderate', 15: 'Severe', 20: 'Extreme'}
            common_allergies = ['Peanuts', 'Pollutants', 'Grass']
            q.name = f"{x[q.cost]} Allergy ({random.choice(common_allergies)})"
        if "Uncommon" in q.name:
            x = {10: 'Mild', 15: 'Moderate', 20: 'Severe', 25: 'Extreme'}
            uncommon_allergies = ['Dogs', 'Grass', 'Seafood', 'Sunlight']
            q.name = f"{x[q.cost]} Allergy ({random.choice(uncommon_allergies)})"
    if "Addiction" in q.name:
        x = {4: 'Mild', 9: 'Moderate', 20: 'Severe', 25: 'Burnout'}
        q.name = f"{x[q.cost]} Addiction ({random.choice(q.opts)})"
    if "Resistance to Pathogens or Toxins" in q.name:
        q.name = f"Resistance to {random.choice(q.opts)}"
    if "Mentor Spirit" in q.name:
        q.name = f"Mentor Spirit ({random.choice(q.opts)})"
    if "(Natural)" in q.name:
        q.name = f"Natural Immunity (Organic)"
    if "Prejudiced" in q.name:
        if "Common" in q.name:
            x = {5: 'Bias', 7: 'Outspoken', 10: 'Radical'}
            common_prejudices = ['Human', 'Metahuman', 'Troll', 'Ork', 'Elve', 'Dwarf']
            q.name = f"Prejudiced - {x[q.cost]} against {random.choice([i for i in common_prejudices if i != ch.Metatype.name])}s"
        if "Specific" in q.name:
            x = {3: 'Bias', 5: 'Outspoken', 8: 'Radical'}
            specific_prejudices = ['The Awakened', 'technomancers', 'shapeshifters', 'aspected magicians']
            q.name = f"Prejudiced - {x[q.cost]} against {random.choice(specific_prejudices)}"
    return q


def leftover_karma(ch: Core.Character, k: Core.KarmaLogger):
    karma_budget = ch.Karma
    karma_menu = {
            'Bound Spirits': 1,
            'Complex Forms': 4,
            'Spells': 5,
            'Bond Foci': 'Variable',
            'Contacts': '2 minimum. 1 per loyalty rating',
            'Registering Sprites': 1
            }
    pass


def add_spell(ch: Core.Character):
    ROLL_SPELL = random.choice(Core.Spell.items)
    while ROLL_SPELL in ch.Spells:
        ROLL_SPELL = random.choice(Core.Spell.items)
    ch.Spells.append(ROLL_SPELL)
    pass


def add_complex_form(ch: Core.Character):
    ROLL_COMPLEX = random.choice(Core.ComplexForm.items)
    while ROLL_COMPLEX.name in ch.Complex_forms.keys():
        ROLL_COMPLEX = random.choice(Core.ComplexForm.items)
    ch.Complex_forms[ROLL_COMPLEX.name] = ROLL_COMPLEX
    pass

    
def resolve_magic_resonance(ch: Core.Character, tbl):
    # tbl = priority_table['MagicResonance']
    if tbl is None:
        return
    _type = random.choice(list(tbl.keys()))
    ch.MagicResoUser = str(_type)
    print(f'Uh oh! Looks like you\'re a {_type}')
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
            ch.Spells = []
            for i in range(tbl[_type][key]):
                add_spell(ch)
        # elif key == "Skills":
        #    print("resolve magi/res Skills")
        #    print(f"You get {tbl[_type]['Skills']['Quantity']} different skills  at rating {tbl[_type]['Skills']['Rating']}")
        #    resolve_magic_resonance_skills(ch, tbl[_type][key])
        elif key == "Complex Forms":
            ch.Complex_forms = {}
            for i in range(tbl[_type][key]):
                add_complex_form(ch)


def format_skills(character_skills):
    # Getting debug output_by_group. Sorts skills by group first, then by ranking
    output_by_group = {'Non-Grouped': {}}
    output_by_attr = {}
    def format_skills_group_rating():
        print("====")
        print("ACTIVE SKILLS")
        print("    by Group/Rating:")
        for k, d in character_skills.items():
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

    def format_skills_attribute():
        character_skill_attributes = list(dict.fromkeys([character_skills[skill].attribute.name for skill in character_skills.keys()]))
        output_by_attr = {
                'Body': None, 'Agility': None, 'Strength': None, 'Reaction': None,
                'Logic': None, 'Willpower': None, 'Intuition': None, 'Charisma': None,
                'Magic': None, 'Resonance': None
        }
        for key in list(output_by_attr.keys()):
            attribute_skills = [s for s in character_skills.keys() if character_skills[s].attribute.name == key]
            if len(attribute_skills) == 0:
                output_by_attr.pop(key)
            else:
                output_by_attr[key] = attribute_skills

        # output_by_attr = {attr: [s for s in character_skills.keys() if character_skills[s].attribute.name == attr] for attr in character_skill_attributes}
        print("===")
        print("    by Attribute:")
        print("===")
        sorted(output_by_attr)

        for attr in output_by_attr.keys():
            # for idx, skill in enumerate(output_by_attr[attr]):
                # if isinstance(skill, Core.MeleeWeapon):
                    # output_by_attr[attr][skill] = output_by_attr[attr][skill].name
            # if Core.MeleeWeapon in [skill for skill in output_by_attr[attr]]:
            #    output_by_attr[attr][idx] = output_by_attr[attr][idx].name 
            # else:
            print(f'---> {attr}')
            print(", ".join([f'{skill} ({character_skills[skill].rating})' for skill in output_by_attr[attr]]))

    format_skills_group_rating()
    format_skills_attribute()


def buy_gear(ch: Core.Character, nuyen: int):

    vehicle_skill_ratings = [i.rating for i in ch.Skills['Active'].values() if i in Core.VEHICLE_SKILLS]
    print(vehicle_skill_ratings)
    pass


def resolve_specific_skill(ch: Core.Character, s: Core.Skill):
    match s.name:
        case "Exotic Melee Weapon":
            exotic_melee_weapon = random.choice([i for i in Core.MeleeWeapon.items if hasattr(i, "subtype") and i.subtype=="Exotic Melee Weapon"])
            ch.Skills['Active'][f"{s.name}"].name = exotic_melee_weapon
            # ch.Skills['Active'].pop(s.name)
    return ch



def generate_character():
    karma_log = Core.KarmaLogger()
    # PHASE 1: CONCEPT
    character = Core.Character()
    priority_table = get_priorities(character)
    metatype = random.choice(priority_table['Metatype'])
    attribute_points = priority_table['Attributes']
    nuyen = priority_table['Resources']
    # Initialising Stuff
    edge_shit = metatype[1]
    metatype = metatype[0]
    # metatype.attributes.init_stat_block()
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
    print(character.Metatype.name)
    # print(f"======\nRolling with {priority_table['Attributes']} points")
    roll_stats(character, attribute_points)
    highest_attrs = get_highest_attr(character)
    # STEP 3: MAGIC/RESONANCE
    magic_reso = priority_table['MagicResonance']
    resolve_magic_resonance(character, magic_reso)
    # STEP 3.5: DETERMING NON-MAGIC/RESONANCE CHAR BUILD CHOICES
    IS_DECKER = False
    IS_RIGGER = False
    IS_FACE = False
    alt_builds = ['Decker', 'Rigger', 'Face', None]
    if priority_table['MagicResonance'] is None:
        build = random.choices(alt_builds, [1, 1, 1, 5])
        if build == 'Decker':
            IS_DECKER = True
            print(f'Character is decker')
        elif build == 'Rigger':
            IS_RIGGER = True
            print('Character is rigger')
        elif build == 'Face':
            IS_FACE = True
            print('Character is face')
    skill_builds = {'IS_DECKER': IS_DECKER, 'IS_RIGGER': IS_RIGGER, 'IS_FACE': IS_FACE}
    # STEP 4: QUALITIES
    karma_qualities(character, karma_log)
    print(character.Qualities)
    print(character.Spells)
    # STEP 5: SKILLS
    character.Skills['Active'] = get_skills(character, priority_table, attr_influence=highest_attrs, skill_cap=20, builds=skill_builds)
    if 'Exotic Melee Weapon' in character.Skills['Active']:
        character = resolve_specific_skill(character, Core.EXOTIC_MELEE_WEAPON)
    format_skills(character.Skills['Active'])
    for k, d in character.Skills.items():
        if d is None:
            pass
        else:
            for i, j in character.Skills[k].items():
                # print(j)
                pass
    print("character karma is ", character.Karma)
    print(nuyen)
    buy_gear(character, nuyen)
    print('Karma logs:')
    print(karma_log)
                
    # Attribute Points


    # PHASE 2: PR
    pass

def alt_generate_character():
    character = Core.Character()
    table_choices = ['A', 'B', 'C', 'D', 'E']
    table_categories = ['Metatype', 'Attributes', 'MagicResonance', 'Skills', 'Resources']
    selected_items = {'Metatype': None, 'Attributes': None, 'MagicResonance': None, 'Skills': None, 'Resources': None}
    character_focus = random.choice(Core.Archetype.items)
    if character_focus in [archetype for archetype in Core.Archetype.items if 
            (hasattr(archetype, "magic") and archetype.magic == True) or 
            (hasattr(archetype, "resonance") and archetype.resonance==True)]:
        is_awakened = True
    else:
        is_awakened = False
    if is_awakened:
        awakened_table_value = random.choice(['A', 'B', 'C'])
        table_choices.pop(table_choices.index(awakened_table_value))
        selected_items['MagicResonance'] = Core.PRIORITY_TABLE_FLIPPED['MagicResonance'][awakened_table_value]
    else:
        selected_items['MagicResonance'] = Core.PRIORITY_TABLE_FLIPPED['MagicResonance']['E']
        table_choices.pop(table_choices.index('E'))
    print(character_focus)
    print(selected_items['MagicResonance'])

generate_character()
