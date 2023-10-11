from random import randint, choice, choices
from math import ceil, floor
import yaml

data = yaml.safe_load(open('/home/refrshrs/code/python/CharGen/dnd_3.5e_data/_core.yaml', 'rt'))
race = data['races']
skills = data['skills']
for r in race:
    if r['name'] == 'Dwarf':
        dwarf = r

def chargen(d):
    char = {}
    char['race'] = d['name']
    char['speed'] = d['base_speed']
    char['age'] = randint(d['age'][0], d['age'][1])
    char['height'] = randint(d['height'][0], d['height'][1])
    char['weight'] = randint(d['weight'][0], d['weight'][1])
    if d['racial_language'] != 'None':
        char['languages'] = ['Common', d['racial_language']]
    else:
        char['languages'] = ['Common']
    char['bonuses'] = []
    for bonus in d['bonuses']:
        if isinstance(bonus, dict):
            if 'darkvision' in bonus.keys():
                char['darkvision'] = bonus['darkvision']
            elif 'extra_language' in bonus.keys():
                if isinstance(bonus['extra_language'], list):
                    bonus_lang = choice(bonus['extra_language'])
                    while bonus_lang in char['languages']:
                        bonus_lang = choice(bonus['extra_language'])
                    char['languages'].append(bonus_lang)
        elif bonus == 'stonecutting':
            char['bonuses'].append('+2 to Search checks on stonework within 10 feet')
        elif bonus == 'stability':
            char['bonuses'].append('+4 to ability checks against being knocked down')
        elif bonus == 'poison_res':
            char['bonuses'].append('+2 to saving throws against poison')

    print(char)

chargen(dwarf)
