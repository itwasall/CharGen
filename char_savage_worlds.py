#!/usr/bin/env python
# -*- coding: utf-8 -*-
from chargen import *
from savage_worlds_data import hinderances as SavageDataHinderances
from math import floor

DIE_TYPES = ["1d4", "1d6", "1d8", "1d10", "1d12"]
DIE_TYPES_RNG = range(len(DIE_TYPES))
BASE_ATTRIBUTE_POINTS = 5
BASE_SKILL_POINTS = 12

class SavageBaseAttributeClass(BaseAttributeClass):
    def __init__(self, name: str = "BaseClass"):
        super().__init__(name, 0, 0)
        self.levels = {cost+1: die for cost, die in zip(DIE_TYPES_RNG, DIE_TYPES)}
        self.level = 1
    def test_levels(self):
        try:
            self.levels[self.level]
        except KeyError:
            bonus = self.level - max(self.levels.keys())
            self.levels[self.level] = f"1d12 + {bonus}"

class SavageAttributeClass(SavageBaseAttributeClass):
    def __init__(self, name: str, level:int = 1):
        super().__init__(name)
        self.test_levels()
        self.level = level
        self.die_type = self.levels[self.level]
    def __add__(self, level: int):
        return SavageAttributeClass(self.name, level)
    def __iadd__(self, level: int):
        return self.__add__(level)
    def __repr__(self):
        self.test_levels()
        return f"{self.name} - {self.levels[self.level]}"

class SavageDerivedStat:
    def __init__(self, name: str, value_function):
        self.name = name
        self.value = self.calculate_value(value_function)

    def calculate_value(self, value_function):
        return value_function

class SavageBaseSkillClass(BaseSkillClass):
    def __init__(
        self,
        name: str,
        attribute: SavageAttributeClass,
        core_skill: bool = False,
        level:int = 0
    ):
        super().__init__(name)
        self.attribute = attribute
        self.core_skill = core_skill
        # Core skills start with 1d4, which is equivilent to level 1 here
        self.level = int(self.core_skill) + level

    def test_levels(self):
        try:
            self.level_names[self.level]
        except KeyError:
            bonus = self.level - max(self.level_names.keys())
            self.level_names[self.level] = f"1d12 + {bonus}"



def calc_parry_stat(fighting_die_type: str = '0'):
    """
    Returns the calculated Parry stat.
    The formula is [2 + [dice_type / 2]], rounding down when necessary
        For 1d6, the result would be [2 + [6 / 2]] or 5
    """
    if fighting_die_type == '0':
        return 2
    elif fighting_die_type in DIE_TYPES:
        return 2 + floor((int(fighting_die_type.split('d')[1]) / 2))
    elif fighting_die_type.startswith("1d12"):
    # For fighting_die_type's of "1d12 + [mod]", append half the [mod] value to the parry
    #   stat, rounding down
        return 2 + 6 + floor(int(fighting_die_type.split(' ')[2])/2)

def calc_toughness_stat(vigor_die_type: str = '0', armor: int = 0):
    if vigor_die_type == '0':
        return f"{2+armor} ({armor})"
    elif vigor_die_type in DIE_TYPES:
        return f"{2 + floor((int(vigor_die_type.split('d')[1]) / 2)) + armor} ({armor})"
    elif vigor_die_type.startswith("1d12"):
        return f"{2 + 6 + floor(int(vigor_die_type.split(' ')[2])/2) + armor} ({armor})"

Agility = SavageAttributeClass('Agility')
Smarts = SavageAttributeClass('Smarts')
Spirit = SavageAttributeClass('Spirit')
Strength = SavageAttributeClass('Strength')
Vigor = SavageAttributeClass('Vigor')

def get_skill_list():
    Academics = SavageBaseSkillClass('Academics', Smarts)
    Athletics = SavageBaseSkillClass('Athletics', Agility, core_skill=True)
    Battle = SavageBaseSkillClass('Battle', Smarts)
    Boating = SavageBaseSkillClass('Boating', Agility)
    Common_Knowledge = SavageBaseSkillClass('Common Knowledge', Smarts, core_skill=True)
    Driving = SavageBaseSkillClass('Driving', Agility)
    Electronics = SavageBaseSkillClass('Electronics', Smarts)
    Faith = SavageBaseSkillClass('Faith', Spirit)
    Fighting = SavageBaseSkillClass('Fighting', Agility)
    Focus = SavageBaseSkillClass('Focus', Spirit)
    Gambling = SavageBaseSkillClass('Gambling', Smarts)
    Hacking = SavageBaseSkillClass('Hacking', Smarts)
    Healing = SavageBaseSkillClass('Healing', Smarts)
    Intimidation = SavageBaseSkillClass('Intimidation', Spirit)
    Language = SavageBaseSkillClass('Language', Smarts)
    Notice = SavageBaseSkillClass('Notice', Smarts, core_skill=True)
    Occult = SavageBaseSkillClass('Occult', Smarts)
    Performance = SavageBaseSkillClass('Performance', Spirit)
    Persuasion = SavageBaseSkillClass('Persuasion', Spirit, core_skill=True)
    Piloting = SavageBaseSkillClass('Piloting', Agility)
    Psionics = SavageBaseSkillClass('Psionics', Smarts)
    Repair = SavageBaseSkillClass('Repair', Smarts)
    Research = SavageBaseSkillClass('Research', Smarts)
    Riding = SavageBaseSkillClass('Riding', Agility)
    Science = SavageBaseSkillClass('Science', Smarts)
    Shooting = SavageBaseSkillClass('Shooting', Agility)
    Spellcasting = SavageBaseSkillClass('Spellcasting', Smarts)
    Stealth = SavageBaseSkillClass('Stealth', Agility, core_skill=True)
    Survival = SavageBaseSkillClass('Survival', Smarts)
    Taunt = SavageBaseSkillClass('Taunt', Smarts)
    Thievery = SavageBaseSkillClass('Thievery', Agility)
    Weird_Science = SavageBaseSkillClass('Weird Science', Smarts)

    BasicSkillList = [
        Academics, Athletics, Battle, Boating, Common_Knowledge, Driving, Electronics, Faith,
        Fighting, Focus, Gambling, Hacking, Healing, Intimidation, Language, Notice, Occult,
        Performance, Persuasion, Piloting, Psionics, Repair, Research, Riding, Science, Shooting,
        Spellcasting, Stealth, Survival, Taunt, Thievery, Weird_Science
        ]
    return BasicSkillList
