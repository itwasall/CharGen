import math
import yaml

skills = yaml.safe_load(open('tbz_data/skills.yaml'))
dict_skills = {}

for i in skills['skills']:
    dict_skills[i['skill_name']] = i

for k, d in dict_skills.items():
    print(k, dict_skills[k])
ceil = math.ceil


class Character():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.sex = ""
        self.concept = ""
        self.archetypes = ""
        self.karma_cost = 0
        self.attribute_cost = 0
        self.attr_body = 0
        self.attr_agility = 0
        self.attr_senses = 0
        self.attr_knowledge = 0
        self.attr_spirit = 0
        self.attr_empathy  = 0
        self.attr_station = 0
        self.vitality = self.attr_body + self.attr_spirit
        self.soul = 2 * (self.attr_spirit + self.attr_knowledge)
        self.kiai_spent = 0
        self.kiai_current = 0
        self.karma_total = 0
        self.karma_armourRider = 0
        self.karma_armourMeikyo = 0
        self.fates = {}
        self.wound_light = self.attr_body
        self.wound_heavy = ceil(self.attr_body / 2)
        self.wound_critial = ceil(self.attr_body / 4)
        self.wounds = [self.wound_light, self.wound_heavy, self.wound_critial]
        self.weapons = {}
        self.possessions = []

test = Character()
