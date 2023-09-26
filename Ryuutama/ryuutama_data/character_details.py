from random import choice, randint
from more_itertools import first
from yaml import safe_load

data_ht = safe_load(open('ryuutama_data/hometown.yaml', 'rt'))
data_name = safe_load(open('ryuutama_data/name.yaml', 'rt'))

char_name: str
char_age: int
char_gender: str
char_hometown: str
char_reason_for_journey: str
char_personality: str


def gen_hometown(lang = None):
    nm1, nm2, nm3 = data_ht['nm1'], data_ht['nm2'], data_ht['nm3']
    nm4, nm5, nm6 = data_ht['nm4'], data_ht['nm5'], data_ht['nm6']
    language = [0, 1, 2]
    if lang is None or lang not in language:
        lang = choice(language)
    # This code has been shamelessly copied over from fantasyTowns.js courtesy of
    #   fantasynamegenerators.com/fantasy-town-names.php lol sorry
    if lang == 1:
        rnd, rnd2 = choice(nm3), choice(nm4)
        if (nm3.index(rnd) > 5) and (nm3.index(rnd) < 28):
            while (nm4.index(rnd2) < 21):
                rnd2 = choice(nm4)
    elif lang == 2:
        rnd, rnd2 = choice(nm5), choice(nm6)
    else:
        rnd, rnd2 = choice(nm1), choice(nm2)
        while (rnd == rnd2):
            rnd2 = choice(nm2)
    hometown = rnd.capitalize() + rnd2
    return hometown

def gen_gender(nb: bool = False, chosen: str = None):
    if not chosen:
        if nb:
            return 'Non-Binary'
        else:
            return choice(['Male', 'Female'])
    else:
        return chosen

def gen_name(gender = None, first_name_only: bool = None):
    if gender is None:
        gender = gen_gender(choice([0, 1]))
    if first_name_only is None:
        first_name_only = choice([0, 1])
    nm1, nm2, nm3, nm4 = data_name['nm1'], data_name['nm2'], data_name['nm3'], data_name['nm4']
    nm5, nm6, nm7, nm8 = data_name['nm5'], data_name['nm6'], data_name['nm7'], data_name['nm8']
    rnd3, rnd4 = choice(nm5), choice(nm6)
    if gender.capitalize() == 'Female':
        rnd, rnd2 = choice(nm1), choice(nm2)
    elif gender.capitalize() == 'Male':
        rnd, rnd2 = choice(nm3), choice(nm4)
    else:
        rnd, rnd2 = choice(nm7), choice(nm8)
    if first_name_only:
        return rnd + rnd2
    else:
        return rnd3 + rnd4 + " " + rnd + rnd2

def gen_age(lower_bound: int = 15, upper_bound: int = 35):
    return randint([lower_bound, upper_bound])

print([gen_hometown() for _ in range(10)])
print([gen_name() for _ in range(10)])