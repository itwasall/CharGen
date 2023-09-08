from random import randint, choices, choice
from chargen import yaml_importer

role = yaml_importer('cyberpunk_red_data//roles.yaml')
life = yaml_importer('cyberpunk_red_data//lifepath.yaml')

def role_gen():
    char_role = choice(role)
    return char_role['name']

def life_path():
    culture_origin = choice(life['cultural_origins'])
    language = choice(culture_origin['lang'])
    style = ["",""]
    style[0] = choice(life['style']['clothing'])
    style[1] = choice(life['style']['hair'])
    return culture_origin['region'], language, style[0], style[1]


def char_gen():
    char_role = role_gen()
    char_personality = choice(life['personality'])
    char_affectation = choice(life['affectation'])
    char_motivation = choice(life['motivations'])
    char_relationship = choice(life['relationships'])
    char_mostValuedPerson = choice(life['valued_person'])
    char_mostValuedPossesion = choice(life['valued_possesion'])
    char_culturalOrigin, char_language, char_clothing, char_hair = life_path()

    print(char_role)

char_gen()
