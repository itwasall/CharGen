import char_dnd_5e_core as Core
import char_dnd_5e_new as CharGen

LEVEL = {
    1: {'Prof Bonus': 2, 'Rages': 2, 'Rage Damage': 2, 'Features': ['Rage', 'Unarmoured Defense']},
    2: {'Prof Bonus': 2, 'Rages': 2, 'Rage Damage': 2, 'Features': ['Reckless Attack', 'Danger Sense']},
    3: {'Prof Bonus': 2, 'Rages': 3, 'Rage Damage': 2, 'Features': ['Primal Path']},
    4: {'Prof Bonus': 2, 'Rages': 3, 'Rage Damage': 2, 'Features': ['Ability Score Improvement']},
    5: {'Prof Bonus': 3, 'Rages': 3, 'Rage Damage': 2, 'Features': ['Extra Attack', 'Fast Movement']},
    6: {'Prof Bonus': 3, 'Rages': 4, 'Rage Damage': 2, 'Features': ['Path Feature']},
    7: {'Prof Bonus': 3, 'Rages': 4, 'Rage Damage': 2, 'Features': ['Feral Instinct']},
    8: {'Prof Bonus': 3, 'Rages': 4, 'Rage Damage': 2, 'Features': ['Ability Score Improvement']},
    9: {'Prof Bonus': 4, 'Rages': 4, 'Rage Damage': 3, 'Features': ['Brutal Critial (1 die)']},
    10: {'Prof Bonus': 4, 'Rages': 4, 'Rage Damage': 3, 'Features': ['Path Feature']},
    11: {'Prof Bonus': 4, 'Rages': 4, 'Rage Damage': 3, 'Features': ['Relentless Rage']},
    12: {'Prof Bonus': 4, 'Rages': 5, 'Rage Damage': 3, 'Features': ['Ability Score Improvement']},
    13: {'Prof Bonus': 5, 'Rages': 5, 'Rage Damage': 3, 'Features': ['Brutal Critical (2 die)']},
    14: {'Prof Bonus': 5, 'Rages': 5, 'Rage Damage': 3, 'Features': ['Path Feature']},
    15: {'Prof Bonus': 5, 'Rages': 5, 'Rage Damage': 3, 'Features': ['Persistent Rage']},
    16: {'Prof Bonus': 5, 'Rages': 5, 'Rage Damage': 4, 'Features': ['Ability Score Improvement']},
    17: {'Prof Bonus': 6, 'Rages': 6, 'Rage Damage': 4, 'Features': ['Brutal Critical (3 die)']},
    18: {'Prof Bonus': 6, 'Rages': 6, 'Rage Damage': 4, 'Features': ['Indomitable Might']},
    19: {'Prof Bonus': 6, 'Rages': 6, 'Rage Damage': 4, 'Features': ['Ability Score Improvement']},
    20: {'Prof Bonus': 6, 'Rages': 6, 'Rage Damage': 4, 'Features': ['Primal Champion']}
}

bar = Core.BARBARIAN

bar.level = 1

test = CharGen.genCharacter(force_class='Barbarian')