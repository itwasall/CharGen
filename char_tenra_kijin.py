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
    # Chooses between 1-5 mechanica parts to have
    #  1 part:  50% chance
    #  2 parts: 30% chance
    #  3 parts: 15% chance
    #  4 parts: 5% chance
    number_of_parts = choices(range(1,5), [10, 6, 3, 1])
    for i in range(number_of_parts[0]):
        # Choose part
        choice_part = choice(kijin_parts)
        # If part has already been chosen, choose another part
        while choice_part in kijin['mechanica_parts'].keys():
            choice_part = choice(kijin_parts)
        # Get's the chosen part's details
        choice_class = choice(list(parts[choice_part]['classes'].keys()))
        # Accumulate the attribute penalty
        total_attribute_penalty += parts[choice_part]['classes'][choice_class]['attribute_penalty']
        kijin['mechanica_parts'][choice_part] = {}
        kijin['mechanica_parts'][choice_part][choice_class] = parts[choice_part]['classes'][choice_class]
    kijin['total_attribute_penalty'] = total_attribute_penalty

    for part in kijin['mechanica_parts']:
        """
        part: The body part replaced with mechanica
        part_class: The "Hei", "Kou" or "Otsu" class mechanica the part slots into

        e.g. Part: Eyes, Part Class: Kou
        """
        # print(part)
        for number_of_slots in range([
            kijin['mechanica_parts'][part][part_class]['mechanica_slots'] 
            for part_class 
            in kijin['mechanica_parts'][part]
            ][0]
        ):
            # Grabs all the mechanica slots 
            #   (i.e. the things that actually do stuff, like the Leg Compartment or the Booster Module)
            # and adds them to a dictionary 
            choice_slots = [
                [slot,mech_data['slots'][slot]]
                for slot 
                in mech_data['slots'] 
                if mech_data['slots'][slot]['slot'] == part
            ]
            # Chooses a slot to put in to the character
            choice_slot = choice(choice_slots)
            while choice_slot in kijin[part]['slots'].keys():
                choice_slot = choice(choice_slots)
            kijin[part]['slots'][choice_slot][0] = choice_slot[1]
            # print(choice_slot)
            # print(choice_slot.keys())

    return kijin

print(gen_mechanica_parts())
