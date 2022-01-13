from random import randint, choice, choices
from chargen import roll, expand, yaml_importer

monk_borg_data = yaml_importer('mork_borg_data/data.yaml')
starting_items = monk_borg_data['starting_items']

ability_score_bonuses = expand({
        range(1, 5): -3,
        range(5, 7): -2,
        range(7, 9): -1,
        range(9, 13): 0,
        range(13, 15): 1,
        range(15, 17): 2,
        range(17, 20): 3
})

def add_to_items(container, item):
    if container.remaining_size >= 1:
        container.append(item)
    else:
        pass
    return container


def gen_character():
    hp, party_initiative = 0, 0
    abilities = {'Agility': 0, 'Prescence': 0, 'Strength': 0, 'Toughness': 0}

    for ability in abilities:
        abilities[ability] = ability_score_bonuses[roll("3d6")]
    hp = abilities['Toughness'] + roll('1d8')
    if hp < 1:
        hp = 1

    party_initiative = abilities['Agility'] + roll('1d6')
    init_silver = roll("2d6") * 10
    init_food = f'{roll("1d4")} days of food'
    init_gear = [
        choice(starting_items['item_1']),
        choice(starting_items['item_2']),
        choice(starting_items['item_3'])
    ]
    init_gear.append(f'Silver: {init_silver}')
    init_gear.append(f'Rations: {init_food}')
    return abilities, hp, party_initiative


print(ability_score_bonuses)
print(gen_character())
