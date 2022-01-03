from math import ceil
import yaml
from typing import List, Tuple

skills = yaml.safe_load(open('tbz_data/skills.yaml'))
dict_skills = {}

for i in skills['skills']:
    dict_skills[i['skill_name']] = i

for k, d in dict_skills.items():
    print(k, dict_skills[k])


class Character():
    def __init__(
            self,
            name: str,
            main_archetype: str,
            archetypes: List[str],
            attribute_cost: int,
            karma: int,
            attribute_body: int,
            attribute_agility: int,
            attribute_senses: int,
            attribute_knowledge: int,
            attribute_spirit: int,
            attribute_empathy: int,
            attribute_station: int,
            vitality: int,
            soul: int,
            wounds: Tuple[int, int, int, int],
            equipment: List[str],
            rider_karma: int = 0,
            meikyo_karma: int = 0,
            armour_attribute_body: int = 0,
            armour_attribute_agility: int = 0,
            armour_attribute_senses: int = 0,


    ):
        self.name = name
        self.main_archetype = main_archetype
        self.archetypes = archetypes
        self.attribute_cost = attribute_cost
        self.karma = karma
        self.attribute_body = attribute_body
        self.attribute_agility = attribute_agility
        self.attribute_senses = attribute_senses
        self.attribute_knowledge = attribute_knowledge
        self.attribute_spirit = attribute_spirit
        self.attribute_empathy = attribute_empathy
        self.attribute_station = attribute_station
        self.attributes = [
            self.attribute_body,
            self.attribute_agility,
            self.attribute_senses,
            self.attribute_knowledge,
            self.attribute_spirit,
            self.attribute_empathy,
            self.attribute_station
        ]
        self.vitality = vitality
        self.soul = soul
        self.wounds = wounds

        self.rider_karma = rider_karma
        self.meikyo_karma = meikyo_karma

        self.armour_attribute_body = armour_attribute_body
        self.armour_attribute_agility = armour_attribute_agility
        self.armour_attribute_senses = armour_attribute_senses
        self.armour_attributes = [
            self.armour_attribute_body,
            self.armour_attribute_agility,
            self.armour_attribute_senses
        ]

