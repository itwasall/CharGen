from typing import List, Tuple
from random import choice, seed
from chargen import roll, yaml_importer, new_seed

chartypes = yaml_importer('numenera_data/classes_new.yaml')
chardescs = yaml_importer('numenera_data/descriptor.yaml')
charfoci = yaml_importer('numenera_data/foci.yaml')

foci_key_exceptions = [
    'trained', 'cost', 'choice', 'pool_bonus', 'pool_bonus_cond', 'asset', 'language_add', 'train_choice', 'train_choice2', 'Servant', 'Philosophic Confusion', 'Zap', 'additional_points']
pool_bonus_options = ['Might', 'Speed', 'Intellect', 'MightSpeed', 'MightIntellect', 'SpeedIntellect', 'MightEdge', 'SpeedEdge', 'IntellectEdge', 'Armour']

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
        # Separate if statements here as None type not iterable
        if subability is not None:
            if len(subability) > 1:
                self.subability = Ability(
                    subability['name'],
                    subability['desc'],
                    None,
                    [subability[key] for it, key in enumerate(subability.keys()) if it > 2]
                )
        else:
            self.subability = None
        if len(args[0]) > 0:
            # Args are in tuple pairs, in the format (param name, param details)
            for items in args:
                [setattr(self, item[0], item[1]) for item in items
                    if item[0] not in ['name', 'desc', 'subability']]

    def __repr__(self):
        return self.repr_message()

    def repr_message(self):
        # Gives different output based on whether or not a subabiltiy is present
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
        for entry in data:
            if 'subability' in entry.keys():
                print(f"subability found in {entry['name']}")
                abl = Ability(
                    entry['name'],
                    entry['desc'],
                    entry['subability'],
                    [(key, entry[key]) for key in entry.keys() if key not in ['name', 'desc', 'subability']]
                )
            else:
                abl = Ability(
                    entry['name'],
                    entry['desc'],
                    None,
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
        new_current = self.current + x
        new_maximum = self.maximum + x
        return Stat(new_maximum, new_current)
    def __iadd__(self, x:int):
        return self.__add__(x)

    def __repr__(self):
        return f"{self.maximum}/{self.current}"

class StatPool:
    def __init__(
        self,
        might: Stat,
        speed: Stat,
        intellect: Stat,
    ):
        self.Might = might
        self.Speed = speed
        self.Intellect = intellect

    def __add__(self, value: int, stat: str):
        stat = stat.capitalize()
        if stat not in ['Might', 'Speed', 'Intellect']:
            pass
        elif stat == 'Might':
            self.Might += value
        elif stat == 'Speed':
            self.Speed += value
        elif stat == 'Intellect':
            self.Intellect += value

    def __repr__(self):
        return f"Might: {self.Might} Speed: {self.Speed} Intellect: {self.Intellect}"

class Edge:
    def __init__(
        self,
        might_edge: int,
        speed_edge: int,
        intellect_edge: int
    ):
        self.might_edge = might_edge
        self.speed_edge = speed_edge
        self.intellect_edge = intellect_edge

    def __add__(self, value: int, edge: str):
        edge = edge.capitalize()
        if edge not in ['Might', 'Speed', 'Intellect']:
            pass
        elif edge == 'Might':
            self.might_edge += value
        elif edge == 'Speed':
            self.speed_edge += value
        elif edge == 'Intellect':
            self.intellect_edge += value

    def __repr__(self):
        return f"Might Edge: {self.might_edge} Speed Edge: {self.speed_edge} Intellect Edge: {self.intellect_edge}"

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


def gen_character(
        settype: str = None,
        setdesc: str = None,
        setfoci: str = None,
        verbose: bool = False,
):
    if settype is None or settype not in list(chartypes.keys()):
        choice_type = choice(list(chartypes.keys()))
        while choice_type == "bs_im_not_rewriting":
            choice_type = choice(list(chartypes.keys()))
        character_type = (choice_type, chartypes[choice_type])
        if verbose:
            print(f'DEBUG: {choice_type}')
    else:
        character_type = (settype, chartypes[settype])
    if setdesc is None or setdesc not in list(chardescs.keys()):
        choice_desc = choice(list(chardescs.keys()))
        character_descriptor = (choice_desc, chardescs[choice_desc])
        if verbose:
            print(f'DEBUG: {choice_desc}')
    else:
        character_descriptor = (setdesc, chartypes[setdesc])
    if setfoci is None or setfoci not in list(charfoci.keys()):
        choice_foci = choice(list(charfoci.keys()))
        character_focus = (choice_foci, charfoci[choice_foci])
        if verbose:
            print(f'DEBUG: {choice_foci}')
    else:
        character_focus = (setfoci, charfoci[setfoci])

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
for k in list(x.keys()):
    print(f"{k}: {x[k]}")

character['StatPools'].__add__(2, 'Might')

print(character['StatPools'])

all_foci = {}
for foci in charfoci.keys():
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
