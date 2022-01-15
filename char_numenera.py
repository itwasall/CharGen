from typing import List, Tuple
from chargen import roll, yaml_importer

# character_classes = yaml_importer('numenera_data/classes_new.yaml')

character = {
    'Name': str,
    'Class': str,
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

print(character)
