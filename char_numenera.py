from typing import List, Dict
from chargen import roll, yaml_importer

character_classes = yaml_importer('numenera_data\\classes_new.yaml')

character = {
    'Name': str,
    'Focus': str,
    'Job/Class': str,
    'Stat Pools': {
        'Might': List, # [Total, Remaining, Edge]
        'Speed': List, # [Total, Remaining, Edge]
        'Intellect': List  # [Total, Remaining, Edge]
    },
    'Equipment': List,
    'Weapon': List, # [Weapon Name, Weapon Damage]
    'Armour': List, # [Armour Name, Armour Damage]
    'Cyphers': Dict, # {Cypher Name: {Effect: "", Level: "", Wearable: [y/n, conditions], Usable: [y/n, conditions]}
    'Oddities': List
}
