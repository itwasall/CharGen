from chargen import yaml_importer
import parts
import random


slot_data = yaml_importer('../tbz_data/mechanica.yaml')['slots']


def slot_choice(kijin, body_part: str = None):
    valid_body_part_slots = ['Arm', 'Leg', 'Torso', 'Sensor']
    if body_part is None:
        pass
    else:
        for part_place in valid_body_part_slots:
            if body_part == part_place:
                slot_query = [slot for slot in slot_data if slot_data[slot]['slot'] == part_place.lower()]
                random_slot = random.choice(slot_query)
                while random_slot in kijin.mechanica_slots[part_place]:
                    random_slot = random.choice(slot_query)
                kijin.mechanica_slots[part_place][random_slot] = slot_data[random_slot]
                if 'weapon' in list(slot_data[random_slot].keys()):
                    kijin.weapon_list.append(random_slot)
            else:
                continue
    print("==== SLOTS =====")
    for k in kijin.mechanica_slots.keys():
        print(list(kijin.mechanica_slots[k].keys()))
    print("==== WEAPON LIST ====")
    print(kijin.weapon_list)



class kij:
    def __init__(self):
        self.mechanica = {
            'Arm': None,
            'Leg': None,
            'Torso': None,
            'Sensor': None
        }
        self.mechanica_slots = {}
        self.total_attribute_penalty = 0
        self.attribute_budget = 0
        self.weapon_list = []

    def __repr__(self):
        return f"{self.mechanica}\n{self.total_attribute_penalty}\n{self.attribute_budget}"


k = kij()

k.mechanica['Arm'] = parts.arm_hei
k.mechanica_slots['Arm'] = {}
k.mechanica['Torso'] = parts.torso_otsu
k.mechanica_slots['Torso'] = {}

k.total_attribute_penalty += k.mechanica['Arm'].attribute_penalty


slot_choice(k, 'Arm')
slot_choice(k, 'Torso')