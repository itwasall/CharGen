from chargen import roll, yaml_importer
from typing import List
from random import randint, choice, choices

mech_data = yaml_importer('tbz_data/mechanica.yaml')

parts = mech_data['mechanica']
slots = mech_data['slots']

kijin_parts = ['sensor', 'arm', 'leg', 'torso']
kijin_part_special = ['weapon_interface', 'homeopathic_bullet_skin']

kijin_layout = {
    'Notice Bonus': int,
    'Attribute Penalty': int,
    'Mechanica': {
        'Class': str,
        'Number of Slots': int,
        'Slots': dict,
    },
}

def gen_mechanica_parts():
    kijin = {}
    kijin['mechanica_parts'] = {}
    total_attribute_penalty = 0
    number_of_parts = choices(range(1,5), [10, 6, 3, 1])
    for i in range(number_of_parts[0]):
        choice_part = choice(kijin_parts)
        if choice_part in kijin['mechanica_parts'].keys():
            choice_part = choice(kijin_parts)
        choice_class = choice(list(parts[choice_part]['classes'].keys()))
        total_attribute_penalty += parts[choice_part]['classes'][choice_class]['attribute_penalty']
        kijin['mechanica_parts'][choice_part] = {}
        kijin['mechanica_parts'][choice_part][choice_class] = parts[choice_part]['classes'][choice_class]
    kijin['total_attribute_penalty'] = total_attribute_penalty

    for part in kijin['mechanica_parts']:
        for number_of_slots in range([kijin['mechanica_parts'][part][part_class]['mechanica_slots'] for part_class in kijin['mechanica_parts'][part]][0]):
            choice_slots = [mech_data['slots'][slot] for slot in mech_data['slots'] if mech_data['slots'][slot]['slot'] == part]
            choice_slot = choice(choice_slots)
            print(choice_slot)

    return kijin

print(gen_mechanica_parts())
