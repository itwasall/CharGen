from chargen import yaml_importer, roll

import random


class ClassAbility:
    def __init__(self, name, desc, effect, usable, stat_used, tn=None):
        self.name = name
        self.desc = desc
        self.effect = effect
        self.usable = usable
        self.stat_used = stat_used
        self.tn = tn


class CharacterClass:
    def __init__(self, name, skills):
        self.name = name
        self.abilities = {}
        self.skills = [skill for skill in skills]

    def add_ability(self, ability):
        if not isinstance(ability, dict):
            pass
        else:
            self.abilities[ability.name] = {
                'Name': ability.name,
                'Desc': ability.desc,
                'Skill Effect': ability.effect
            }


class CharacterType:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class AttackType(CharacterType):
    def __init__(self):
        super().__init__("Attack Type")
        self.abilities = {
            'Toughness': "Add +4 to Max HP",
            'Power': "+1 Bonus to damage rolls during combat",
            'Weapon Focus': "Gain 1 more Mastered Weapon"
        }


class TechnicalType(CharacterType):
    def __init__(self):
        super().__init__("Technical Type")
        self.abilities = {
            'Accurate': "Gain an extra +1 bonus to any check when using Concentration, for a bonus of +2",
            'Quick': "+1 Bonus to Initiative checks in combat",
            'Pocket': "Your Carrying Capacity is increased by +3"
        }


class MagicType(CharacterType):
    def __init__(self):
        super().__init__("Magic Type")
        self.abilities = {
            'Will': "Add +4 to Max MP",
            'Spellbook': "Acquire 2 Incantation spells per level",
            'Seasonal Sorcerer': "Acquire Seasonal Magic"
        }


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
        'Personality': str,
        'Level': int
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

Minstrel = CharacterClass('Minstrel', ['Well-traveled', 'Knowledge of Tradition', 'Music'])

Merchant = CharacterClass('Merchant', ['Well-spoken', 'Animal Owner', 'Trader'])

Hunter = CharacterClass('Hunter', ['Animal Tracking', 'Trapping', 'Hunting'])

Healer = CharacterClass('Healer', ['Healing', 'First-Aid', 'Herb Gathering'])

Farmer = CharacterClass('Farmer', ['Robust', 'Animal Owner', 'Side-job'])

Artisan = CharacterClass('Artisan', ['Trapping', 'Crafting', 'Repair'])

Noble = CharacterClass('Noble', ['Etiquette', 'Refined Education', 'Weapon Grace'])
