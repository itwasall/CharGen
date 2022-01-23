from typing import List

from chargen import yaml_importer, roll

from random import choice, shuffle


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

    def __repr__(self):
        return self.name


class CharacterType:
    def __init__(self, name):
        self.name = name


class AttackType(CharacterType):
    def __init__(self):
        super().__init__("Attack Type")
        self.abilities = {
            'Toughness': "Add +4 to Max HP",
            'Power': "+1 Bonus to damage rolls during combat",
            'Weapon Focus': "Gain 1 more Mastered Weapon"
        }

    def __repr__(self):
        return self.name


class TechnicalType(CharacterType):
    def __init__(self):
        super().__init__("Technical Type")
        self.abilities = {
            'Accurate': "Gain an extra +1 bonus to any check when using Concentration, for a bonus of +2",
            'Quick': "+1 Bonus to Initiative checks in combat",
            'Pocket': "Your Carrying Capacity is increased by +3"
        }

    def __repr__(self):
        return self.name


class MagicType(CharacterType):
    def __init__(self):
        super().__init__("Magic Type")
        self.abilities = {
            'Will': "Add +4 to Max MP",
            'Spellbook': "Acquire 2 Incantation spells per level",
            'Seasonal Sorcerer': "Acquire Seasonal Magic"
        }

    def __repr__(self):
        return self.name


class WeaponType:
    def __init__(self, name, accuracy=0, damage=0, handed: str = None, base_price: int = 0):
        self.name = name
        self.accuracy = 0
        self.damage = 0
        self.handed = handed
        self.base_price = base_price
        if isinstance(accuracy, list):
            if len(accuracy) < 2:
                self.accuracy_formula(accuracy[0], 0)
            else:
                self.accuracy_formula(accuracy[0], accuracy[1])

        if isinstance(damage, list):
            if len(damage) < 2:
                self.damage_formula(damage[0], 0)
            else:
                self.damage_formula(damage[0], damage[1])

    def accuracy_formula(self, ops: list, mod: int):
        self.accuracy = [[score for score in ops], mod]

    def damage_formula(self, ops, mod):
        self.damage = [[score for score in ops], mod]

    def __repr__(self):
        return self.name


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
        'Gold':int,
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

wl_light_blade = ['Dagger', 'Shortsword', 'Wakizashi']
wl_blade = ['Broadsword', 'Rapier', 'Katana']
wl_polearm = ['Longspear', 'Trident', 'Lance']
wl_axe = ['Battleaxe', 'Greataxe']
wl_bow = ['Shortbow', 'Longbow', 'Crossbow']

def get_weapon(character):
    master_weapon = character['Mastered Weapon'].name
    if master_weapon == 'Light Blade':
        weapon = choice(wl_light_blade)
    elif master_weapon == 'Blade':
        weapon = choice(wl_blade)
    elif master_weapon == 'Polearm':
        weapon = choice(wl_polearm)
    elif master_weapon == 'Axe':
        weapon = choice(wl_axe)
    elif master_weapon == 'Bow':
        weapon = choice(wl_bow)
    elif master_weapon == 'Unarmed':
        weapon = 'Fists'
    if weapon != 'Fists':
        character['Inventory']['Items'] = [weapon]
    else:
        pass

Minstrel = CharacterClass('Minstrel', ['Well-traveled', 'Knowledge of Tradition', 'Music'])

Merchant = CharacterClass('Merchant', ['Well-spoken', 'Animal Owner', 'Trader'])

Hunter = CharacterClass('Hunter', ['Animal Tracking', 'Trapping', 'Hunting'])

Healer = CharacterClass('Healer', ['Healing', 'First-Aid', 'Herb Gathering'])

Farmer = CharacterClass('Farmer', ['Robust', 'Animal Owner', 'Side-job'])

Artisan = CharacterClass('Artisan', ['Trapping', 'Crafting', 'Repair'])

Noble = CharacterClass('Noble', ['Etiquette', 'Refined Education', 'Weapon Grace'])

ab_average_set = [6, 6, 6, 6]
ab_standard_set = [4, 6, 6, 8]
ab_specialised_set = [4, 4, 8, 8]

ryuu_classes = [Minstrel, Merchant, Hunter, Healer, Farmer, Artisan, Noble]
ryuu_types = [AttackType, TechnicalType, MagicType]
ryuu_mastered_weapon = [wt_light_blade, wt_blade, wt_polearm, wt_axe, wt_bow, wt_unarmed]
ryuu_ability_score_sets = [ab_standard_set, ab_average_set, ab_specialised_set]


def gen_chanaracter():
    # Stage one: Pick class
    char_class = choice(ryuu_classes)
    character['Class'] = char_class
    # Stage two: Pick type
    char_type = choice(ryuu_types)
    character['Type'] = char_type
    # Stage three: Determine starting ability scores
    char_ability_score = choice(ryuu_ability_score_sets)
    shuffle(char_ability_score)
    for it, ability_score in enumerate(list(character['Ability Scores'].keys())):
        character['Ability Scores'][ability_score] = char_ability_score[it]
    character['Resources']['HP']['Current'], character['Resources']['HP']['Max'] = char_ability_score[0] * 2, \
                                                                                   char_ability_score[0] * 2
    character['Resources']['MP']['Current'], character['Resources']['MP']['Max'] = char_ability_score[3] * 2, \
                                                                                   char_ability_score[3] * 2
    character['Carrying Capacity'] = char_ability_score[0] + 3

    # Stage four: Choose mastered weapon
    char_mastered_weapon = choice(ryuu_mastered_weapon)
    character['Mastered Weapon'] = char_mastered_weapon
    # Stage five: Determine personal item
    character['Inventory']['Personal Item'] = "to be genned"
    get_weapon(character)

    # Stage six: Shop for items
    character['Inventory']['Gold'] = 1000

    # Stage seven: Pick character details


gen_chanaracter()
print(character)
