from typing import Tuple
from typing_extensions import IntVar
import yaml
from random import randint, choice, choices
from itertools import permutations

def roll(dicestring: str):
    throws, sides = dicestring.split('d')
    return sum(randint(1, sides) for _ in range(throws))

mechanica_data = yaml.safe_load(open('tbz_data/mechanica.yaml', 'rt'))

mechanica = [mechanica_data['sensor'], mechanica_data['arm'], mechanica_data['torso'], mechanica_data['leg'], mechanica_data['weapon_interface']]

slots = {i:mechanica_data['slots'][i] for i in mechanica_data['slots']}

for slot in slots.keys():
    print(slots[slot]['slot'])


part_names = ['sensor', 'arm', 'torso', 'leg', 'weapon_interface']

def gen_kijin(parts=None):
    mechanica_parts: Tuple = ()
    weapon_interface_guarentee: bool = False
    torso_guarentee: bool = False
    attempt_count = 0
    if not parts:
        number_of_parts = choices([1, 2, 3, 4], weights=[50, 25, 20, 5])[0]
        if number_of_parts >= 3 and randint(1,3) >= 2:
            weapon_interface_guarentee = True
        if number_of_parts >= 2 and randint(1,2) == 2:
            torso_guarentee = True
        while (len(mechanica_parts) <= 0
            or ("weapon_interface" in mechanica_parts and len(mechanica_parts) <= 1)
            or (weapon_interface_guarentee and 'weapon_interface' not in mechanica_parts)
            or (torso_guarentee and 'torso' not in mechanica_parts)):
            mechanica_parts = choice(list(permutations(part_names, number_of_parts)))
            attempt_count += 1
            print(f"attempt: {attempt_count}")
    return [i for i in mechanica_parts]


print(gen_kijin())
