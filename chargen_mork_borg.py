from random import randint, choice, choices

def roll(dice_string):
    throws, sides = dice_string.split('d')
    return sum(randint(1, int(sides)) for _ in range(int(throws)))

ITEM_ONE = [
    'nothing',
    'Backpack for 7 normal-sized items',
    'Sack for 10 normal-sized items',
    'Small Wagon', 
    'Donkey'
] 
ITEM_TWO = [
    "30 feet of rope",
    "Presence + 4 torches",
    "Lanturn with oil for Presence + 6 hours",
    "Magnesium strip",
    "Random unclean scroll",
    "Sharp needle",
    "Medicle chest with Presence + 4 uses (stops bleeding/infection and heals 1d6 HP)",
    "Metal file and lockpicks",
    "Bear trap (Prescence DR14 to stop, 1d8 damage)",
    "Bomb (sealed bottle, 1d10 damage)",
    "A bottle of red poison with 1d4 doses (Toughness DR12 or 1d10 damage)",
    "Silver crucifix"
]
ITEM_THREE = [
    "Life elixer of 1d4 doses (heals 1d6 HP and removes infection)",
    "Random sacred scroll",
    "Small but vicious dog (1d6+2 HP, punch/bite 1d4, only obeys you)",
    "1d4 monkeys that ignore but love you (1d4 + 2 HP, punch/bite 1d4)",
    "Exquisite perfume worth 25s",
    "Toolbox containing 10 nails, tongs, hammer, small saw and drill",
    "15 feet of heavy chain",
    "Grappling hook",
    "Shield (-1 HP or have the shield break to ignore 1 attack)",
    "Crowbar (1d4 damage)",
    "Lard (any function as 5 meals in a pinch)",
    "Tent"
]


def gen_character():
    init_silver = roll("2d6") * 10
    init_food = f'{roll("1d4")} days of food'


