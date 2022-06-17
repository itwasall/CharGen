#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chargen import yaml_importer

data_classes = yaml_importer('dnd_5e_data/classes.yaml')
jobs = data_classes['classes']
backgrounds = yaml_importer('dnd_5e_data/backgrounds.yaml')
equip = yaml_importer('dnd_5e_data/equipment.yaml')
lang = yaml_importer('dnd_5e_data/languages.yaml')
races = yaml_importer('dnd_5e_data/races.yaml')
skills = yaml_importer('dnd_5e_data/skills.yaml')
weapons = yaml_importer('dnd_5e_data/weapons.yaml')
magic = yaml_importer('dnd_5e_data/magic.yaml')

class AbilityScores:
    def __init__(self):
        self.STR = 0
        self.STR_MOD = self.get_ability_mod(self.STR)
        self.STR_SAV = 0
        self.DEX = 0
        self.DEX_MOD = self.get_ability_mod(self.DEX)
        self.DEX_SAV = 0
        self.CON = 0
        self.CON_MOD = self.get_ability_mod(self.CON)
        self.CON_SAV = 0
        self.INT = 0
        self.INT_MOD = self.get_ability_mod(self.INT)
        self.INT_SAV = 0
        self.WIS = 0
        self.WIS_MOD = self.get_ability_mod(self.WIS)
        self.WIS_SAV = 0
        self.CHA = 0
        self.CHA_MOD = self.get_ability_mod(self.CHA)
        self.CHA_SAV = 0

    def set_values(self, values: list):
        if len(values) != 6:
            return ValueError
        self.STR = values[0]
        self.DEX = values[1]
        self.CON = values[2]
        self.INT = values[3]
        self.WIS = values[4]
        self.CHA = values[5]
    
    def get_ability_mod(self, ability_score):
        if not ability_score:
            return ValueError
        mod_dict = {
            1: -5, 
            2: -4, 
            3: -4, 
            4: -3, 
            5: -3, 
            6: -2, 
            7: -2,
            8: -1, 
            9: -1,
            10: 0,
            11: 0,
            12: 1,
            13: 1,
            14: 2,
            15: 2,
            16: 3,
            17: 3,
            18: 4,
            19: 4,
            20: 5
        }
        return mod_dict[ability_score]

char_abilityScores = AbilityScores()

class Skills:
    def __init__(self):

        self.skill_list = {
            'Acrobatics': 0,
            'Animal Handling': 0,
            'Arcana': 0,
            'Athletics': 0,
            'Deception': 0,
            'History': 0,
            'Insight': 0,
            'Intimidation': 0,
            'Investigation': 0,
            'Medicine': 0,
            'Nature': 0,
            'Perception': 0,
            'Persuasion': 0,
            'Religion': 0,
            'Sleight Of Hand': 0,
            'Stealth': 0,
            'Survival': 0
        }
        self.update_skills()

    def update_skills(self):

        self.acrobatics = self.skill_list['Acrobatics']
        self.animal_handling = self.skill_list['Animal Handling']
        self.arcana = self.skill_list['Arcana'] 
        self.athletics = self.skill_list['Athletics']
        self.deception = self.skill_list['Deception']
        self.history = self.skill_list['History']
        self.insight = self.skill_list['Insight']
        self.intimidation = self.skill_list['Intimidation']
        self.investigation = self.skill_list['Investigation']
        self.medicine = self.skill_list['Medicine']
        self.nature = self.skill_list['Nature']
        self.perception = self.skill_list['Perception']
        self.persuasion = self.skill_list['Persuasion']
        self.religion = self.skill_list['Religion']
        self.sleight_of_hand = self.skill_list['Sleight Of Hand']
        self.stealth = self.skill_list['Stealth']
        self.survival = self.skill_list['Survival']


    def change_skill(self, skill_name: str, skill_amt: int):
        if skill_name not in list(self.skill_list.keys()):
            return ValueError
        self.skill_list[skill_name] = skill_amt
        self.update_skills()

char_skillList = Skills()

class Character:
    def __init__(
        self,
        name: str = "",
        age: int = 0,
        height: str = "",
        race: str = "",
        char_class: str = "",
        ability_scores: AbilityScores = char_abilityScores,
        skills: Skills = char_skillList
    ):
        self.name = name
        self.age = age
        self.height = height
        self.race = race
        self.character_class = char_class
        self.ability_scores = ability_scores
        self.skills = skills


j = Character('name', 1, 'big', 'yes', 'nice', char_abilityScores)

print(j.skills.skill_list)
j.skills.change_skill('Animal Handling', 2)
print(j.skills.animal_handling)
