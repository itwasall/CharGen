from typing import List
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

class Container:
    def __init__(self, name: str, size: int):
        self.name = name
        self.maximum_size = size
        self.current_size = size
        self.contents = []

    def add_item(self, item: str):
        if self.current_size >= 1:
            self.contents.append(item)
            self.current_size -= 1
        else:
            pass

    def add_items(self, items: List):
        for item in items:
            self.add_item(item)

    def __repr__(self):
        return f"{self.name} of {self.maximum_size} size.\nContains {', '.join(item for item in self.contents)}"

class Poison:
    def __init__(self, name: str, effect: str, doses: int):
        self.name = name
        self.effect = effect
        self.maximum_doses = doses
        self.current_doses = doses

    def __repr__(self):
        return f"{self.name}: {self.effect}.\nHas {self.maximum_doses} doses total and {self.current_doses} remaining."

class Rope:
    def __init__(self, name: str, length: int, measurment: str):
        self.name = name
        self.length = length
        self.measurement = measurment

    def __repr__(self):
        return f"{self.name} of {self.length}{self.measurement}"


backpack = Container('Backpack', 7)
sack = Container('Sack', 10)
small_wagon = Container('Small Wagon', 1_000)
toolbox = Container('Toolbox', 4)
toolbox.add_items(['10 Nails', 'Hammer', 'Small Saw', 'Tongs'])

heavy_chain = Rope('Heavy Chain', 15, 'feet')
rope = Rope('Rope', 30, 'feet')

black_poison = Poison('Black Poison', f'Toughness DR14 or {roll("1d6")} damage & blind for one hour', 3)
red_poison = Poison('Red Poison', f'Toughness DR12 or {roll("1d10")} damage', 3)


def gen_starting_items(abilities):
    prescence = abilities['Prescence']
    item_set_1 = ["Nothing", "Nothing", backpack, sack, small_wagon]
    item_set_2 = [rope, f"{prescence + 4} torches", f"Lanturn with oil for {prescence + 6} hours", f"Magnesium Strip", f""]

def gen_character(classless: bool = True):
    if classless:
        ability_rerolls = 2
    hp, party_initiative = 0, 0
    abilities = {'Agility': 0, 'Prescence': 0, 'Strength': 0, 'Toughness': 0}

    for ability in abilities:
        if classless:
            if ability_rerolls > 0:
                dice_rolls = [roll('1d6') for _ in range(3)]
                if ability_score_bonuses[sum(dice_rolls)] < 0:
                    dice_rolls.pop()
                    dice_rolls.append(roll('1d6'))
                    ability_rerolls -= 1

            abilities[ability] = ability_score_bonuses[sum(dice_rolls)]
        else:
            abilities[ability] = ability_score_bonuses[sum(roll('1d6') for _ in range(3))]





    hp = abilities['Toughness'] + roll('1d8')
    if hp < 1:
        hp = 1
    carrying_capacity = abilities['Strength'] + 8

    party_initiative = abilities['Agility'] + roll('1d6')
    init_silver = roll("2d6") * 10
    init_food = f'{roll("1d4")} days of food'
    return abilities, hp, party_initiative


print(ability_score_bonuses)
print(gen_character())
