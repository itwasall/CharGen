from chargen import yaml_importer, roll

import random


def make_ability_effect(mod: int = 0,
                        effect_type: str = None,
                        checks: list = None,
                        circumstances: str = None,
                        stat_used: list = None,
                        target_number=None):
    effect = {
        'Type': effect_type,
        'Mod': mod,
        'Cond': checks,
        'Circumstances': circumstances,
        'Stat_Used': stat_used,
        'Target Number': target_number
    }
    return effect


class ClassAbility:
    def __init__(self, name, desc, effect):
        self.name = name
        self.desc = desc
        self.effect = effect


well_traveled_desc = "As a minstrel who makes their earning by constant travel. you've learned how to travel safely"
well_traveled = ClassAbility('Well Traveled', well_traveled_desc,
                             make_ability_effect(1, 'check_bonus', ['Traveling', 'Direction', 'Camping']))


class CharacterClass:
    def __init__(self, name):
        self.name = name
        self.abilities = {}

    def add_ability(self, ability):
        if not isinstance(ability, dict):
            pass
        else:
            self.abilities[ability.name] = {
                'Name': ability.name,
                'Desc': ability.desc,
                'Skill Effect': ability.effect
            }


Minstrel = CharacterClass('Minstrel')
Minstrel.add_ability(well_traveled)


class CharacterType:
    def __init__(self):
        pass


class WeaponType:
    def __init__(self, name, accuracy=0, damage=0, handed: str = None, base_price: int = 0):
        self.name = name
        self.accuracy = 0
        self.damage = 0
        self.handed = handed
        self.base_price = base_price
        if isinstance(accuracy, list):
            self.accuracy_formula(accuracy[0], accuracy[1])
        if isinstance(damage, list):
            self.damage_formula(damage[0], damage[1])

    def accuracy_formula(self, ops: list, mod: int):
        self.accuracy = [[score for score in ops], mod]

    def damage_formula(self, ops, mod):
        self.damage = [[score for score in ops], mod]


character = {
    'Details': {
        'Name': str,
        'Age': int,
        'Gender': str,
        'Image Colour': str,
        'Outward Appearance': str,
        'Hometown': str,
        'Reason for Journeying': str,
        'Personality': str
    },
    'Class': CharacterClass,
    'Type': CharacterType,
    'Ability Scores': {
        'Strength': int,
        'Dexterity': int,
        'Intelligence': int,
        'Spirit': int
    },
    'Resources': {
        'HP': {
            'Max': int,
            'Current': int
        },
        'MP': {
            'Max': int,
            'Current': int
        }
    },
    'Carrying Capacity': int,
    'Mastered Weapon': WeaponType,
    'Inventory': {
        'Gold': int,
        'Personal Item': str,
        'Items': list
    }
}

ch_strength = character['Ability Scores']['Strength']
ch_dexterity = character['Ability Scores']['Dexterity']
ch_intelligence = character['Ability Scores']['Intelligence']
ch_spirit = character['Ability Scores']['Spirit']

wt_light_blade = WeaponType(
    'Light Blade',
    [[ch_strength, ch_intelligence], 1],
    [[ch_intelligence], -1],
    'One-Handed',
    base_price=400
)
wt_blade = WeaponType(
    'Blade',
    [[ch_dexterity, ch_strength], 1],
    [[ch_strength]],
    'One-Handed',
    base_price=700
)
wt_polearm = WeaponType(
    'Polearm',
    [[ch_dexterity, ch_strength]],
    [[ch_strength]],
    'Two-Handed',
    base_price=350
)
wt_axe = WeaponType(
    'Axe',
    [[ch_strength, ch_strength], -1],
    [[ch_strength]],
    'Two-Handed',
    base_price=500
)
wt_bow = WeaponType(
    'Bow',
    [[ch_intelligence, ch_dexterity], -2],
    [[ch_dexterity]],
    'Two-Handed',
    base_price=750,
)
wt_unarmed = WeaponType(
    'Unarmed',
    [[ch_dexterity, ch_strength]],
    [[ch_strength], -1],
    'Two-Handed'
)
