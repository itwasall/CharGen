from typing import List, Tuple
from random import choice
from chargen import roll, yaml_importer

chartypes = yaml_importer('numenera_data/classes_new.yaml')
chardescs = yaml_importer('numenera_data/descriptor.yaml')
charfoci = yaml_importer('numenera_data/foci.yaml')

foci_key_exceptions = ['trained', 'cost', 'choice', 'pool_bonus', 'pool_bonus_cond', 'asset', 'language_add', 'train_choice', 'train_choice2', 'Servant', 'Philosophic Confusion', 'Zap', 'additional_points']
pool_bonus_options = ['Might', 'Speed', 'Intellect', 'MightSpeed', 'MightIntellect', 'SpeedIntellect', 'MightEdge', 'SpeedEdge', 'IntellectEdge', 'Armour']

character = {
    'Name': str,
    'Type': "",
    'Focus': tuple((str, str)),
    'Descriptor': tuple((str, str)),
    'StatPools': {
        'StatMight': List[int],  # [Total, Remaining, Edge]
        'StatSpeed': List[int],  # [Total, Remaining, Edge]
        'StatIntellect': List[int]  # [Total, Remaining, Edge]
    },
    'Equipment': List,
    'Weapon': List,  # [Weapon Name, Weapon Damage]
    'Armour': List,  # [Armour Name, Armour Damage]
    'Abilities': List,
    'Inabilities': List,
    'Cyphers': {
        'CypherName': {
            'CypherEffect': str,
            'CypherLevel': tuple((str, int)),  # ("1d4", 2) -> 1d4 + 2
            'CypherWearable': tuple((bool, str)),  # (y/n, conditions)
            'CypherUsable': tuple((bool, str)),  # (y/n, conditions)
        },
    },
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

    total_might = init_stat_pools[0]['Might']
    total_speed = init_stat_pools[0]['Speed']
    total_intellect = init_stat_pools[0]['Intellect']
    edge_might = init_stat_pools[1]['Might']
    edge_speed = init_stat_pools[1]['Speed']
    edge_intellect = init_stat_pools[1]['Intellect']

    stat_pool_list = [total_might, total_speed, total_intellect, edge_might, edge_speed, edge_intellect]

    for it, pool in enumerate(list(character['StatPools'].keys())):
        character['StatPools'][pool] = stat_pool_list[it]

    return character



x = gen_character(verbose=True)
for k in list(x.keys()):
    print(f"{k}: {x[k]}")