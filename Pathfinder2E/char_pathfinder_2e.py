from typing import List
from chargen import yaml_importer, roll, new_seed, BaseAttributeClass
from random import choice, randint, seed

data_feats = yaml_importer('pathfinder_2e_data/feats.yaml')
data_backgrounds = yaml_importer('pathfinder_2e_data/backgrounds.yaml')

STR = BaseAttributeClass('STR')
DEX = BaseAttributeClass('DEX')
CON = BaseAttributeClass('CON')
INT = BaseAttributeClass('INT')
WIS = BaseAttributeClass('WIS')
CHA = BaseAttributeClass('CHA')

class AbilityScore(BaseAttributeClass):
    def __init__(self, name: str, value: int, modifier: int):
        super().__init__(name, value, value)
        self.modifier = modifier

    def __repr__(self):
        return f"{self.maximum} ({self.modifier})"

class AbilityScores:
    def __init__(
        self,
        strength: AbilityScore,
        dexterity: AbilityScore,
        constiution: AbilityScore,
        intelligence: AbilityScore,
        wisdom: AbilityScore,
        charisma: AbilityScore
    ):
        self.strength = strength
        self.dexterity = dexterity
        self.constiution = constiution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma


class AbstractAncestoryClass:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"{self.name}"

class AncestoryFeat(AbstractAncestoryClass):
    def __init__(self, name: str, *args):
        super().__init__(name)
        self.desc = None
        self.add_skill_proficiency = None
        self.add_weapon_proficiency = None
        self.allow_access_weapon_set = None
        self.add_crit_success = None
        self.add_terrain_adv = None
        self.add_circumstance_bonus = None
        self.add_speed_reduction_ignore = None
        self.add_speed_penalty_reduction = None
        self.add_ancestral_foe = None
        self.add_bonus_damage_to_creature_when_hit = None
        [setattr(self, attr_name, value) for attr_name, value in args[0].items()]


class AncestoryHeritage(AbstractAbilityScore):
    def __init__(self, name: str, *args):
        super().__init__(name)
        self.add_reaction = None
        self.add_crit_saving_throw = None
        self.add_resistance = None
        self.add_circumstance_bonus = None
        self.add_force_movement_reduction = None
        self.add_poison_stage_reduction_by_saving_throw = None
        [setattr(self, attr_name, value) for attr_name, value in args[0].items()]

class AncestoryTrait(AbstractAncestoryClass):
    def __init__(self, name: str):
        super().__init__(name)

class AncestoryAbility(AbstractAncestoryClass):
    def __init__(self, name: str, desc: str):
        super().__init__(name)
        self.desc = desc

class Rarity:
    def __init__(self, name: str):
        self.name = name

class Language:
    def __init__(self, name: str):
        self.name = name

class Ancestory:
    def __init__(
        self,
        name: str,
        rarity: Rarity,
        hit_points: int,
        speed: int,
        ability_boosts: List[AbstractAbilityScore],
        ability_flaws: List[AbstractAbilityScore],
        languages: List[Language],
        feats: List[AncestoryFeat],
        traits: List[AncestoryTrait],
        abilities: List[AncestoryAbility]

    ):
        self.name = name
        self.feats = feats
    def __repr__(self): return self.name


class Background:
    def __init__(
        self,
        name: str,
        desc: str,
        ability_boost: List,
        skill_proficiencies: List,
        skill_feat: str,
    ):
        self.name = name
        self.desc = desc
        self.ability_boost = ability_boost
        self.skill_proficiencies_data = skill_proficiencies
        self.skill_proficiencies = self.reroll_params()
        self.skill_feat = skill_feat

    def reroll_params(self):
        seed(new_seed())
        skill_prof_choices = []
        for it, item in enumerate(self.skill_proficiencies_data):
            if type(item) == list:
                skill_prof_choices.append(choice(item))
            else:
                skill_prof_choices.append(item)
        return skill_prof_choices

    def __repr__(self):
        return f"Name: {self.name}\n  {self.desc}\n"

def make_backgrounds():
    all_backgrounds = {}
    for key in data_backgrounds:
        key_data = data_backgrounds[key]
        all_backgrounds[key] = Background(
            key,
            key_data['desc'],
            key_data['ability_boost'],
            key_data['skill_proficiencies'],
            key_data['skill_feat']
        )
    return all_backgrounds



class Character:
    def __init__(
        self,
        ancestory: Ancestory,
        ability_scores: AbilityScores,
    ):
        pass

bg = make_backgrounds()
print(bg['Acolyte'])
