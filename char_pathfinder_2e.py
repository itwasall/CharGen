from typing import List
from chargen import yaml_importer, roll
from random import choice, randint


class AbstractAbilityScore:
    def __init__(self, name):
        self.name = name

abc_str = AbstractAbilityScore('STR')
abc_dex = AbstractAbilityScore('DEX')
abc_con = AbstractAbilityScore('CON')
abc_int = AbstractAbilityScore('INT')
abc_wis = AbstractAbilityScore('WIS')
abc_cha = AbstractAbilityScore('CHA')

class AbilityScore(AbstractAbilityScore):
    def __init__(self, name: str, value: int, modifier: int):
        super().__init__(name)
        self.value = value
        self.modifier = modifier

    def __repr__(self):
        return f"{self.value} ({self.modifier})"

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
    def __init__(self, name: str, desc: str):
        self.name = name
        self.desc = desc

    def __repr__(self):
        return f"{self.name}:\n    {self.desc}"

class AncestoryFeat(AbstractAncestoryClass):
    def __init__(self, name: str, desc: str):
        super().__init__(name, desc)

class AncestoryTrait(AbstractAncestoryClass):
    def __init__(self, name: str, desc: str):
        super().__init__(name, desc)

class AncestoryAbility(AbstractAncestoryClass):
    def __init__(self, name: str, desc: str):
        super().__init__(name, desc)

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


class Character:
    def __init__(
        self,
        ancestory: Ancestory,
        ability_scores: AbilityScores,

    ):
        pass

demo_trait = AncestoryTrait('Demo Trait', 'This is a demo trait')
print(demo_trait)
