import random
from dataclasses import dataclass
from typing import Optional


@dataclass(repr=False)
class Attribute:
    items = []
    name: str 
    value: int
    category: str
    limit: int = 6
    show_info: bool = False
    def __add__(self, x):
        return Attribute(name=self.name, value=self.value + x, category=self.category)
    def __sub__(self, x):
        return Attribute(name=self.name, value=self.value - x, category=self.category)
    def __repr__(self):
        if self.show_info:
            return f'\'{self.name}: {self.value}/{self.limit}\''
        return f'\'{self.name}\''

@dataclass
class Skill:
    name: str
    untrained: bool
    spec: list[str]
    primary_attr: Attribute
    secondary_attr: Optional[Attribute] = None

@dataclass
class Metatype:
    name: str
    attr_changes: list[(Attribute, int)]
    racial_qualities: list = None


BODY = Attribute('Body', 0, 'Physical')
AGILITY = Attribute('Agility', 0, 'Physical')
REACTION = Attribute('Reaction', 0, 'Physical')
STRENGTH = Attribute('Strength', 0, 'Physical')
LOGIC = Attribute('Logic', 0, 'Mental')
WILLPOWER = Attribute('Willpower', 0, 'Mental')
INTUITION = Attribute('Intuition', 0, 'Mental')
CHARISMA = Attribute('Charisma', 0, 'Mental')
EDGE = Attribute('Edge', 0, 'Special')
ESSENCE = Attribute('Essence', 0, 'Special')
MAGIC = Attribute('Magic', 0, 'Special')
RESONANCE = Attribute('Resonance', 0, 'Special')


HUMAN = Metatype('Human', [(EDGE, 7)])
DWARF = Metatype('Dwarf', [(BODY, 7), (REACTION, 5), (STRENGTH, 8), (WILLPOWER, 7)], ['Toxin Resistance', 'Thermographic Vision'])

ASTRAL = Skill('Astral', False, ['Astral Combat', 'Astral Signatures', 'Emotional States', 'Spirit Types'], INTUITION, WILLPOWER)
CON = Skill('Con', True, ['Acting', 'Disguise', 'Impersonation', 'Performance'], WILLPOWER)

print(BODY)
AGILITY.show_info = True
print(AGILITY)
AGILITY.show_info = False

print(HUMAN)
print(DWARF)

print(ASTRAL)
print(CON)
