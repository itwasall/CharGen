#!/usr/bin/env python
# -*- coding: utf-8 -*-

from yaml import safe_load
from random import choice, randint

kijin = {
    'bodyparts':{},
    'mechanica':{}
}

kijin_data = safe_load(open('tbz_data/mechanica.yaml', 'rt'))

mechanica = kijin_data['slots']

sensor_mechanica = {k:d for k, d in mechanica.items() if mechanica[k]['slot'] == 'sensor'}
arm_mechanica = {k:d for k, d in mechanica.items() if mechanica[k]['slot'] == 'arm'}
torso_mechanica = {k:d for k, d in mechanica.items() if mechanica[k]['slot'] == 'torso'}
leg_mechanica = {k:d for k, d in mechanica.items() if mechanica[k]['slot'] == 'leg'}

kijin_bodyparts = ['sensor', 'arm', 'torso', 'leg']

# This dict contains information like how many slots a Kou class Arm mechanica has
kijin_classes = kijin_data['mechanica']

def gen_kijin_bodyparts(max_parts = 1):
    num_bodyparts_to_change = randint(1, max_parts)
    bodyparts_to_change = []
    for _ in range(num_bodyparts_to_change):
        random_bodypart = choice(kijin_bodyparts)
        while random_bodypart in bodyparts_to_change:
            random_bodypart = choice(kijin_bodyparts)
        bodyparts_to_change.append(random_bodypart)
    return bodyparts_to_change

def gen_kijin_bodypart_class(bodypart):
    if bodypart == 'sensor':
        random_bodypart_class = choice(['Kou', 'Otsu', 'Hei', 'Rotating Visor'])
    elif bodypart in ['arm', 'torso', 'leg']:
        random_bodypart_class = choice(['Kou', 'Otsu', 'Hei'])
    return {random_bodypart_class:kijin_classes[bodypart]['classes'][random_bodypart_class]}

def gen_kijin_mechanica(kijin, bodypart):
    random_mechanica_part = choice([mech_part for mech_part in kijin_data if bodypart == kijin_data[mech_part]['slot']])
    if len(kijin['mechanica']) < kijin['mechanica'][bodypart]['mechanica_slot']:
        kijin['mechanica'][bodypart][random_mechanica_part]
    else:
        print("Fuck up has occured")
    pass

kijin['bodyparts'] = gen_kijin_bodyparts(3)
for bp in kijin['bodyparts']:
    kijin[bp] = {}
    kijin[bp] = gen_kijin_bodypart_class(kijin, bodypart)

gen_kijin_mechanica(kijin, 'arm')
print(kijin)

# random_bodyparts = gen_kijin_bodyparts(3)
# random_bodyparts_classes = {bodypart:gen_kijin_bodypart_class(bodypart) for bodypart in random_bodyparts}
# print(f'Classes {random_bodyparts_classes}')



