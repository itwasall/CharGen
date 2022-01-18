from typing import List, Tuple
from random import choice
from chargen import roll, yaml_importer

chartypes = yaml_importer('numenera_data/classes_new.yaml')
chardescs = yaml_importer('numenera_data/descriptor.yaml')
charfoci = yaml_importer('numenera_data/foci.yaml')

character = {
    'Name': str,
    'Type': str,
    'Focus': str,
    'Descriptor': str,
    'StatPools': {
        'StatMight': List[int], # [Total, Remaining, Edge]
        'StatSpeed': List[int], # [Total, Remaining, Edge]
        'StatIntellect': List[int]  # [Total, Remaining, Edge]
    },
    'Equipment': List,
    'Weapon': List, # [Weapon Name, Weapon Damage]
    'Armour': List, # [Armour Name, Armour Damage]
    'Cyphers': {
        'CypherName': {
            'CypherEffect': str,
            'CypherLevel': tuple((str, int)), # ("1d4", 2) -> 1d4 + 2
            'CypherWearable': tuple((bool, str)), # (y/n, conditions)
            'CypherUsable': tuple((bool, str)), # (y/n, conditions)
        },
    }, 
    'Oddities': List[str], # [Oddity description]
}

def gen_character(
    settype: str = None,
    setdesc: str = None,
    setfoci: str = None
):
    if settype is None or settype not in list(chartypes.keys()):
        choice_type = choice(list(chartypes.keys()))
        character_type = (choice_type, chartypes[choice_type])
    else:
        character_type = (settype, chartypes[settype])
    if setdesc is None or setdesc not in list(chardescs.keys()):
        choice_desc = choice(list(chardescs.keys()))
        character_descriptor = (choice_desc, chardescs[choice_desc])
    else:
        character_descriptor = (setdesc, chartypes[setdesc])
    if setfoci is None or setfoci not in list(charfoci.keys()):
        choice_foci = choice(list(charfoci.keys()))
        character_focus = (choice_foci, charfoci[choice_foci])
    else:
        character_focus = (setfoci, charfoci[setfoci])
    return (character_type, character_descriptor, character_focus)

character_type, character_descriptor, character_focus = gen_character(setfoci='Sees Beyond')
character['Type'] = character_type[0]
character['Descriptor'] = character_descriptor[0]
character['Focus'] = character_focus[0]


print(character)

