import random
from dataclasses import dataclass, field
from weakref import WeakSet
from collections import defaultdict

@dataclass
class Items:
    items: list = field(default_factory=list)
    def append(self, x):
        self.items.append(x)

ATTRIBUTES = Items()
SKILLS = Items()
METATYPES = Items()


@dataclass(repr=False)
class Attribute:
    __refs__ = defaultdict(WeakSet)
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
    @classmethod
    def get_instances(cls):
        return cls.__refs__[cls]
    

@dataclass
class Skill:
    name: str
    untrained: bool
    spec: list[str]
    primary_attr: Attribute
    secondary_attr: Attribute = None

@dataclass
class Metatype:
    name: str
    attr_changes: list[(Attribute, int)]
    racial_qualities: list = None

@dataclass
class Quality:
    name: str
    positive: bool
    cost: int
    conflict: list[str] = field(default_factory=list)
    requries_resolve: bool = False



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
ATTRIBUTES.append(BODY)
ATTRIBUTES.append(AGILITY)
ATTRIBUTES.append(REACTION)
ATTRIBUTES.append(STRENGTH)
ATTRIBUTES.append(LOGIC)
ATTRIBUTES.append(WILLPOWER)
ATTRIBUTES.append(INTUITION)
ATTRIBUTES.append(CHARISMA)
ATTRIBUTES.append(EDGE)
ATTRIBUTES.append(ESSENCE)
ATTRIBUTES.append(MAGIC)
ATTRIBUTES.append(RESONANCE)

HUMAN = Metatype('Human', [(EDGE, 7)])
DWARF = Metatype('Dwarf', [(BODY, 7), (REACTION, 5), (STRENGTH, 8), (WILLPOWER, 7)], ['Toxin Resistance', 'Thermographic Vision'])
ELF = Metatype('Elf', [(AGILITY, 7), (CHARISMA, 8)], ['Low-light Vision'])
ORK = Metatype('Ork', [(BODY, 8), (STRENGTH, 8), (CHARISMA, 5)], ['Low-light Vision', 'Built Tough 1'])
TROLL = Metatype('Troll', [(BODY, 9), (AGILITY, 5), (STRENGTH, 9), (CHARISMA, 5)], ['Dermal Deposits', 'Thermographic Vision', 'Built Tough 2'])

ASTRAL = Skill('Astral', False, ['Astral Combat', 'Astral Signatures', 'Emotional States', 'Spirit Types'], INTUITION, WILLPOWER)
CON = Skill('Con', True, ['Acting', 'Disguise', 'Impersonation', 'Performance'], WILLPOWER)

AMBIDEXTROUS = Quality('Ambidextrous', True, 4)
ANALYTICAL_MIND = Quality('Analytical_mind', True, 4)
# Requires resolve
APTITUDE_SKILL = Quality('Aptitude_skill', True, 4, [], True)
ASTRAL_CHAMELON = Quality('Astral_chamelon', True, 4)
BLANDNESS = Quality('Blandness', True, 4)
BUILT_TOUGH_1 = Quality('Built Tough 1', True, 4, ['Built Tough 2', 'Built Tough 3', 'Built Tough 4'])
BUILT_TOUGH_2 = Quality('Built Tough 2', True, 4, ['Built Tough 1', 'Built Tough 3', 'Built Tough 4'])
BUILT_TOUGH_3 = Quality('Built Tough 3', True, 4, ['Built Tough 1', 'Built Tough 2', 'Built Tough 4'])
BUILT_TOUGH_4 = Quality('Built Tough 4', True, 4, ['Built Tough 1', 'Built Tough 2', 'Built Tough 3'])
CATLIKE = Quality('Catlike', True, 4)
DERMAL_DEPOSITS = Quality('Dermal_deposits', True, 4)
DOUBLE_JOINTED = Quality('Double_jointed', True, 4)
# Requires resolve
ELEMENTAL_RESISTANCE = Quality('Elemental_resistance', True, 4, [], True)
# Requires resolve
EXCEPTIONAL_ATTRIBUTE = Quality('Exceptional_attribute', True, 4, [], True)
FIRST_IMPRESSION = Quality('First_impression', True, 4)
FOCUSED_CONCERNTRATION_1 = Quality('Focused Concerntration 1', True, 4, ['Focused Concerntration 2', 'Focused Concerntration 3'])
FOCUSED_CONCERNTRATION_2 = Quality('Focused Concerntration 2', True, 4, ['Focused Concerntration 1', 'Focused Concerntration 3'])
FOCUSED_CONCERNTRATION_3 = Quality('Focused Concerntration 3', True, 4, ['Focused Concerntration 1', 'Focused Concerntration 2'])
GEARHEAD = Quality('Gearhead', True, 4)
GUTS = Quality('Guts', True, 4)
HARDENING = Quality('Hardening', True, 4)
HIGH_PAIN_TOLERANCE = Quality('High_pain_tolerance', True, 4)
HOME_GROUND = Quality('Home_ground', True, 4)
HUMAN_LOOKING = Quality('Human_looking', True, 4)
INDOMITABLE = Quality('Indomitable', True, 4)
JURYRIGGER = Quality('Juryrigger', True, 4)
LONG_REACH = Quality('Long_reach', True, 4)
LOW_LIGHT_VISION = Quality('Low_light_vision', True, 4)
MAGIC_RESISTANCE = Quality('Magic_resistance', True, 4)
MENTOR_SPIRIT = Quality('Mentor_spirit', True, 4)
PHOTOGRAPHIC_MEMORY = Quality('Photographic_memory', True, 4)
QUICK_HEALER = Quality('Quick_healer', True, 4)
RESISTANCE_PATHOGENS = Quality('Resistance_pathogens', True, 4)
# Requires resolve
SPIRIT_AFFINITY = Quality('Spirit Affinity', True, 4, ['Sprite Affinity'], True)
# Requires resolve
SPRITE_AFFINITY = Quality('Sprite Affinity', True, 4, ['Spirit Affinity'], True)
THERMOGRAPHIC_VISION = Quality('Thermographic_vision', True, 4)
TOUGHNESS = Quality('Toughness', True, 4)
TOXIN_RESISTANCE = Quality('Toxin_resistance', True, 4)
WILL_TO_LIVE_1 = Quality('Will_to_live_1', True, 4)
WILL_TO_LIVE_2 = Quality('Will_to_live_2', True, 4)
WILL_TO_LIVE_3 = Quality('Will_to_live_3', True, 4)
WILL_TO_LIVE_1.conflict = [WILL_TO_LIVE_2.name, WILL_TO_LIVE_3.name]
WILL_TO_LIVE_2.conflict = [WILL_TO_LIVE_1.name, WILL_TO_LIVE_3.name]
WILL_TO_LIVE_3.conflict = [WILL_TO_LIVE_1.name, WILL_TO_LIVE_2.name]

print(Attribute.get_instances())
