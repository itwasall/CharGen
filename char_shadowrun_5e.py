import chargen
import random
import char_shadowrun_5e_data as Core
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

def generate_character():
    # PHASE 1: CONCEPT
    character = Core.Character()
    priority_table = get_priorities(character)
    metatype = random.choice(priority_table['Metatype'])
    attribute_points = priority_table['Attributes']
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
    character.print_stats()
    print(f"======\nRolling with {priority_table['Attributes']} points")
    roll_stats(character, attribute_points)
    # Attribute Points

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
    if len(dominant_stats) < 1:
        raise ValueError("No dominant stats!")
    print(dominant_stats)

def karma_qualities(ch: Core.Character):
    pass
    

def skills_gen(ch: Core.Character, skills: list):
    skill_points = skills[0]
    skill_group_points = skills[1]
    ch.Skills = {'Single': {}, 'Group': {}}
    while skill_points > 0:
        pass
        



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
