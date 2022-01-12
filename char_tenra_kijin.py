from typing import Tuple, List
import yaml
from random import randint, choice, choices
from itertools import permutations

def roll(dicestring: str):
    throws, sides = dicestring.split('d')
    return sum(randint(1, sides) for _ in range(throws))

mechanica_data = yaml.safe_load(open('tbz_data/mechanica.yaml', 'rt'))

mechanica = mechanica_data['mechanica']

def gen_parts(mechanica_name, no_part_flag: bool = False):
    if no_part_flag:
       return [part for part in mechanica_data['slots'] if ('no_slot' in mechanica_data['slots'][part]['slot'] 
                                                            and mechanica_name in mechanica_data['slots'][part]['replaces'])]
    else:
        return [part for part in mechanica_data['slots'] if mechanica_data['slots'][part]['slot'] == mechanica_name]

sensor_parts = gen_parts('sensor')
arm_parts = gen_parts('arm')
torso_parts = gen_parts('torso')
leg_parts = gen_parts('legs')
no_slot_parts = gen_parts('no_part')
no_slot_parts_arm = gen_parts('arm', no_part_flag = True)
no_slot_parts_skin = gen_parts('skin', no_part_flag = True)


part_names = ['sensor', 'arm', 'torso', 'leg', 'weapon_interface', 'homeopathic bullet skin']

def gen_kijin(parts: List = None, verbose: bool = False):
    """Generates a Kijin Mechanica.
    args:
        parts: List = Used to specify which mechanica parts you'll use. This is not choosing which mechanica you'll get, just the body parts
            the character will be replacing. e.g. ['arm', 'torso']
        verbose: bool = There's some debug shit that's disabled by default
    """
    # Removing 'homeopathic bullet skin' from part_names list. Needed earlier, not required now.
    part_names.pop(part_names.index(part_names[-1:][0]))
    mechanica_parts: Tuple = ()
    weapon_interface_guarentee: bool = False
    torso_guarentee: bool = False
    attempt_count = 0
    if not parts:
        # Choosing the number of parts, chances are:
        #   1 Part:  1/2 | 2 Parts: 1/4
        #   3 Parts: 1/5 | 4 Parts: 1/20
        number_of_parts = choices([1, 2, 3, 4], weights=[50, 25, 20, 5])[0]
        # In order to make each mechanica part have interesting slots, if more than 3 slots are selected, a roll is made with a 2/3 chance of success that
        #   one of those mechanica parts is going to be the Weapon Interface
        if number_of_parts >= 3 and randint(1,3) >= 2:
            weapon_interface_guarentee = True
        # As the torso has access to the Heart Engine, a mechanica part whose sole purpose is to power other mechanica parts, if more than 2 parts are selected
        #   there's a 1/2 chance that one of those parts is going to be the torso.
        if number_of_parts >= 2 and randint(1,2) == 2:
            torso_guarentee = True
        while (len(mechanica_parts) <= 0
            # Prevents the situation where you only have the Weapon Interface. As it's job is to boost the power of other mechanica, it makes no sense
            #   to take this by itself.
            or ("weapon_interface" in mechanica_parts and len(mechanica_parts) <= 1)
            or (weapon_interface_guarentee and 'weapon_interface' not in mechanica_parts)
            or (torso_guarentee and 'torso' not in mechanica_parts)):
            mechanica_parts = choice(list(permutations(part_names, number_of_parts)))
            attempt_count += 1
            if verbose:
                print(f"attempt: {attempt_count}")
    else:
        mechanica_parts = parts

    return [i for i in mechanica_parts]


print(gen_kijin())
print(gen_kijin(['arm', 'leg']))
