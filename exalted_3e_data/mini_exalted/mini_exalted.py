import sys
from random import choice
from typing import List, Dict

if not sys.platform == "linux":
    sys.path.append("F:\\CharGen")
else:
    sys.path.append("/home/refrshrs/code/python/CharGenNew/CharGen")


from exalted_3e_data import data
from exalted_3e_data.data import LIST_ABILITIES, LIST_ATTRIBUTE, LIST_CASTE


class Character:
    def __init__(
        self,
        name: str,
        details: Dict = None,
        caste: data.ExaltedCasteClass = None,
        abilities: List[data.ExaltedAbilityClass]  = LIST_ABILITIES,
        attributes: List[data.ExaltedAttributeClass] = LIST_ATTRIBUTE
    ):
        if details is not None:
            self.details = {
                'Name': name,
                'Player Name': [details['playerName'] if 'playerName' in list(details.keys) else None][0],
                'Concept': [details['concept'] if 'concept' in list(details.keys) else None][0],
                'Anima': [details['anima'] if 'anima' in list(details.keys) else None][0],
                'Caste': [details['caste'] if 'caste' in list(details.keys) else None][0],
                'Supernal Ability': [details['supernalAbility'] if 'supernalAbility' in list(details.keys) else None][0],
            }
        else:
            self.details = {'Name': name, 'PlayerName': None, 'Concept': None, 'Caste': None, 'Anima': None, 'Supernal Ability': None}
        self.caste = caste
        self.abilities = abilities
        self.attributes = attributes
        self.charms = None


def select_caste(character: Character):
    character.caste = dumb_caste_ability_exception(choice(LIST_CASTE))
    # If ability is listed in the character caste, mark the "is_caste" flag as True for that ability
    for ability in character.abilities:
        if ability.name in character.caste.abilities:
            ability.is_caste = True
        else:
            continue
    character.details['Caste'] = character.caste.name


def dumb_caste_ability_exception(caste):
    if "Brawl/Martial Arts" in caste.abilities:
        caste.abilities.pop(caste.abilities.index('Brawl/Martial Arts'))
        caste.abilities.append(choice(['Brawl', 'Martial Arts']))
    return caste


jerry = Character('Jerry')
select_caste(jerry)
print(jerry.attributes)
print(jerry.caste)
print([ab for ab in jerry.abilities if ab.is_caste])
print(jerry.details)
