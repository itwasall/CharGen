from chargen import roll, yaml_importer
from typing import List
from random import randint, choice

mech_data = yaml_importer('tbz_data/mechanica.yaml')

parts = mech_data['mechanica']
slots = mech_data['slots']

kijin_parts = ['sensor', 'arm', 'leg', 'torso']
kijin_part_special = ['weapon_interface', 'homeopathic_bullet_skin']

partname = "placeholder"

kijin = {
    'Notice Bonus': int,
    'Attribute Penalty': int,
    'Mechanica': {
        'Class': str,
        'Number of Slots': int,
        'Slots': dict,
    },
}

def gen_mechanica_parts():
    kijin_mechanica = []
    attribute_penalty_limit = randint(2, 20)
    while attribute_penalty_limit > 0:
        bodypart = choice(kijin_parts)
        while bodypart in [x[0] for x in kijin_mechanica]:
            bodypart = choice(kijin_parts)
            if kijin_parts in [x[bodypart] for x in kijin_mechanica]:
                break
        print(bodypart)
        list_bodypart_class = [c for c in parts[bodypart]['classes']]
        bodypart_class = parts[bodypart]['classes'][choice(list_bodypart_class)]
        print(bodypart_class)
        attribute_penalty_limit -= bodypart_class['attribute_penalty']
        kijin_mechanica.append([bodypart, bodypart_class])
    return kijin_mechanica

print(gen_mechanica_parts())
        
