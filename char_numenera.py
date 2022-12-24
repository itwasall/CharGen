from typing import List, Tuple
from random import choice, seed
from chargen import roll, yaml_importer, new_seed

chartypes = yaml_importer('numenera_data/classes_new.yaml')
chardescs = yaml_importer('numenera_data/descriptor.yaml')
charfoci = yaml_importer('numenera_data/foci.yaml')

foci_key_exceptions = [
        'trained',
        'cost',
        'choice',
        'pool_bonus',
        'pool_bonus_cond',
        'asset',
        'language_add',
        'train_choice',
        'train_choice2',
        'Servant',
        'Philosophic Confusion',
        'Zap',
        'additional_points'
    ]

pool_bonus_options = [
        'Might', 
        'Speed', 
        'Intellect', 
        'MightSpeed', 
        'MightIntellect', 
        'SpeedIntellect',
        'MightEdge', 
        'SpeedEdge',
        'IntellectEdge',
        'Armour'
    ]

class Cypher:
    def __init__(
        self,
        cypher_name: str,
        cypher_level: str,
        cypher_effect: str,
        wearable: tuple, # (bool, optional str)
        useable: tuple # (bool, optional str)
    ):
        self.cypher_name = cypher_name.capitalize()
        self.cypher_level = roll(cypher_level)
        self.cypher_effect = cypher_effect
        self.wearable = wearable
        self.useable = useable

    def __repr__(self): return self.name

class Ability:
    def __init__(self, name: str, desc: str, subability = None, *args):
        self.name = name
        self.desc = desc
        self.trained = None
        self.cost = [0, None]
        self.pool_bonus = None
        self.pool_bonus_cond = None
        self.language_add = None
        self.train_choice = None
        self.train_choice2 = None
        self.additional_points = None
        self.subability = None
        # Separate if statements here as None type not iterable
        if subability is not None:
            if len(subability) > 1:
                self.subability = Ability(
                                    subability['name'],
                                    subability['desc'],
                                    None,
                                    [subability[key] for idx, key in enumerate(subability.keys()) if idx > 2]
                                )
        if len(args[0]) > 0:
            # Args are in tuple pairs, in the format (param name, param details)
            for items in args:
                [setattr(self, item[0], item[1]) for item in items
                    if item[0] not in ['name', 'desc', 'subability']]

    def __repr__(self):
        return self.repr_message()

    def repr_message(self):
        # Gives different output based on whether or not a sub-abiltiy is present
        if self.subability is None:
            return f"\n    {self.name}"
        else:
            return f"\n{self.name}\n  Subability: {self.subability.name}"



class Focus:
    def __init__(
        self,
        name: str,
        desc: str,
        connection: List,
        equipment: List = None,
        abilities: dict = None,
        minor_effect: str = None,
        major_effect: str = None,
        choice = None
    ):
        self.name = name
        self.desc = desc
        self.connection = connection
        self.equipment = equipment
        self.abilities = self.make_abilities(abilities)
        self.effects = [major_effect, minor_effect]
        if choice is not None:
            seed(new_seed)
            self.choice = choice
            self.chosen = choice(self.choice)

    def make_abilities(self, data):
        abilities = []
        sub_ability = None
        for entry in data:
            if 'subability' in entry.keys():
                sub_ability = entry['subability']
                print(f"subability found in {entry['name']}")

            abl = Ability(
                entry['name'],
                entry['desc'],
                sub_ability,
                [(key, entry[key]) for key in entry.keys() if key not in ['name', 'desc', 'subability']]
            )
            abilities.append(abl)
        return abilities

    def __repr__(self): return self.name


class Stat:
    def __init__(
        self,
        maximum: int,
        current: int = None
    ):
        self.maximum = maximum

        if current is None: 
            self.current = maximum
        else:
            self.current = current

    def __add__(self, x:int):
        self.current += x
        self.maximum += x
        return Stat(self.maximum, self.current)

    def __iadd__(self, x:int):
        return self.__add__(x)

    def __repr__(self):
        return f"{self.maximum}/{self.current}"

class StatPool:
    def __init__(self, might: Stat, speed: Stat, intel: Stat):
        self.might = might
        self.speed = speed
        self.intel = intel

    def __add__(self, value: int, stat: str):
        match stat.capitalize():
            case "Might":
                self.might += value
            case "Speed":
                self.speed += value
            case "Intellect":
                self.intel += value
            case _:
                pass

    def __repr__(self):
        return f"Might: {self.might} Speed: {self.speed} Intellect: {self.intel}"

class Edge:
    def __init__(
        self,
        edge_might: int,
        edge_speed: int,
        edge_intel: int
    ):
        self.edge_might = edge_might
        self.edge_speed = edge_speed
        self.edge_intel = edge_intel

    def __add__(self, value: int, edge: str):
        match edge.capitalize():
            case "Might":
                self.edge_might += value
            case "Speed":
                self.edge_speed += value
            case "Intellect":
                self.edge_intel += value
            case _:
                pass

    def __repr__(self):
        return f"Might Edge: {self.edge_might} Speed Edge: {self.edge_speed} Intellect Edge: {self.edge_intel}"

character = {
    'Name': str,
    'Type': "",
    'Focus': tuple((str, str)),
    'Descriptor': tuple((str, str)),
    'StatPools': StatPool,
    'Edge': Edge,
    'Equipment': List,
    'Weapon': List,  # [Weapon Name, Weapon Damage]
    'Armour': List,  # [Armour Name, Armour Damage]
    'Abilities': List,
    'Inabilities': List,
    'Cyphers': List[Cypher],
    'Oddities': List[str],  # [Oddity description]
    'Skills': dict
}

def choose(data):
    try:
        return choice(list(data.keys()))
    except AttributeError:
        raise AttributeError()

def keylist(data):
    return list(data.keys())


def gen_character(
        set_type: str = None,
        set_desc: str = None,
        set_foci: str = None,
        verbose: bool = False,
):
    if set_type is None or set_type not in keylist(chartypes):
        set_type = choose(chartypes)
        while set_type == "bs_im_not_rewriting":
            set_type = choose(chartypes)
    character_type = (set_type, chartypes[set_type])

    if set_desc is None or set_desc not in keylist(chardescs):
        gen_desc = choose(chardescs)
        character_descriptor = (gen_desc, chardescs[gen_desc])
    else:
        character_descriptor = (set_desc, chartypes[set_desc])

    if set_foci is None or set_foci not in keylist(charfoci):
        gen_foci = choose(charfoci)
        character_focus = (gen_foci, charfoci[gen_foci])
    else:
        character_focus = (set_foci, charfoci[set_foci])

    if verbose:
            print(f'DEBUG: {set_type}')
            print(f'DEBUG: {gen_desc}')
            print(f'DEBUG: {gen_foci}')

    character['Type'] = character_type[0]
    character['Descriptor'] = character_descriptor[0]
    character['Focus'] = character_focus[0]

    init_stat_pools = [character_type[1]['stat_pool_start'], character_type[1]['edge']]

    print(init_stat_pools)

    total_might = Stat(init_stat_pools[0]['Might'])
    total_speed = Stat(init_stat_pools[0]['Speed'])
    total_intellect = Stat(init_stat_pools[0]['Intellect'])
    character_edge = Edge(init_stat_pools[1]['Might'], init_stat_pools[1]['Speed'], init_stat_pools[1]['Intellect'])

    # characrer_stats = [total_might, total_speed, total_intellect, edge_might, edge_speed, edge_intellect]

    character['StatPools'] = StatPool(total_might, total_speed, total_intellect)
    character['Edge']

    return character



x = gen_character(verbose=True)
for k in list(x):
    print(f"{k}: {x[k]}")

# character['StatPools'].__add__(2, 'Might')
# print(character['StatPools'])

if not True:
    print(character['StatPools'])

    all_foci = {}
    for foci in charfoci:
        focus = charfoci[foci]
        all_foci[foci] = Focus(
            foci,
            focus['desc'],
            focus['connection'],
            [focus['equipment'] if 'equipment' in keys else None for keys in focus][0],
            focus['abilities'],
            [focus['minor_effect'] if 'minor_effect' in keys else None for keys in focus][0],
            focus['major_effect'],
            [focus['choice'] if 'choice' in keys else None for keys in focus][0],
        )
        print(all_foci[foci].name, all_foci[foci].abilities)
