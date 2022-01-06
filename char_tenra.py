from math import ceil
import yaml
from typing import List, Tuple
from random import randint, choice, choices


def roll(throws, sides=0):
    if isinstance(throws, str):
        throws, sides = throws.split("d")
    return sum(randint(1, int(sides)) for _ in range(int(throws)))


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

arc = yaml.safe_load(open('tbz_data/archetype.yaml', 'rt'))
global ARCHETYPE_FLAGS
ARCHETYPE_FLAGS = {'SHINOBI_VOID': False, 'SAMURAI_VOID': False}


def gen_archetypes():
    global ARCHETYPE_FLAGS
    species_roll = roll("1d2")
    archetype_count = 0
    if species_roll > 1:
        species_key = choice(list(arc['species'].keys()))
        if species_key == 'Kugutsu':
            ARCHETYPE_FLAGS['SHINOBI_VOID'] = True
            ARCHETYPE_FLAGS['SAMURAI_VOID'] = True
        archetype_species = [species_key, arc['species'][species_key]]
        archetype_count += 1
    else:
        archetype_species = None
    print(archetype_species)

gen_archetypes()