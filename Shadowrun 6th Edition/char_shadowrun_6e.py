import random
from attrs import define, field


@define
class Attribute:
    items = []
    name: str = field(alias="name")
    value: int = field()
    category: str = field()

    def __add__(self, x):
        return Attribute(name=self.name, value=self.value+x)


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

