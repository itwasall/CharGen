import sys
from random import choice
sys.path.append("F:\\CharGen")

from exalted_3e_data import data
from exalted_3e_data.data import LIST_ABILITIES, LIST_ATTRIBUTE, LIST_CASTE


class Character:
    def __init__(self):
        self.caste = None
        self.abilities = {}
        self.attributes = [k for k in LIST_ATTRIBUTE]

def select_caste(character: Character):
    caste_choice = choice(LIST_CASTE)
    for ability in caste_choice.abilities:
        if ability == "Brawl/Martial Arts":
            ability = choice(["Brawl", "Martial Arts"])
        character.abilities[ability] = [ab for ab in LIST_ABILITIES if ab.name == ability][0]
        character.abilities[ability].is_caste = True

jerry = Character()
select_caste(jerry)
print(jerry.abilities)
print(jerry.attributes)