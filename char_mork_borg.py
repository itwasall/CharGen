import yaml
from random import randint, choice, choices

def roll(dice_string):
    throws, sides = dice_string.split('d')
    return sum(randint(1, int(sides)) for _ in range(int(throws)))

def expand(dic):
    ret = {}
    for key in dic:
        if type(key) == range:
            ret.update({i: dic[key] for i in key})
        else:
            ret[key] = dic[key]
    return ret


monk_borg_data = yaml.safe_load(open('mork_borg_data/data.yaml', 'rt'))
starting_items = monk_borg_data['starting_items']

ability_score_bonuses = expand({
    range(1, 4): -3,
    range(5, 6): -2,
    range(7, 8): -1,
    range(9, 12): 0,
    range(13, 14): 1,
    range(15, 16): 2,
    range(17, 20): 3
})


def gen_character():
    init_silver = roll("2d6") * 10
    init_food = f'{roll("1d4")} days of food'
    init_gear = [
        choice(starting_items['item_1']),
        choice(starting_items['item_2']),
        choice(starting_items['item_3'])
    ]
    init_gear.append(f'Silver: {init_silver}')
    init_gear.append(f'Rations: {init_food}')
    abilities = {'Agility': 0, 'Prescence': 0, 'Strength': 0, 'Toughness': 0}
    for ability in abilities:
        abilities[ability] = ability_score_bonuses[roll("3d6")]
    return init_gear, abilities



print(gen_character())