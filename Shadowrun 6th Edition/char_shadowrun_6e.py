import random
from dataclasses import dataclass, field, asdict
import weakref
from collections import defaultdict

@dataclass(repr=False)
class Attribute:
    __refs__ = []
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
    def __post_init__(self):
        Attribute.__refs__.append(self)

@dataclass(repr=False)
class MatrixAttribute(Attribute):
    name: str
    value: int
    category: str = "Matrix"
    limit: int = 6

    

@dataclass
class Skill:
    __refs__ = []
    name: str
    untrained: bool
    spec: list[str]
    primary_attr: Attribute
    secondary_attr: Attribute = None
    def __post_init__(self):
        Skill.__refs__.append(self)

@dataclass
class Ammunition:
    __refs__ = []
    name:str
    def __post_init__(self):
        Ammunition.__refs__.append(self)


@dataclass
class MatrixAttrs:
    attack: MatrixAttribute
    sleeze: MatrixAttribute
    data_proecssing: MatrixAttribute
    firewall: MatrixAttribute


@dataclass 
class FiringMode:
    name: str
    abbr: str

SINGLE_SHOT = SS = FiringMode('SINGLE_SHOT', 'SS')
SEMI_AUTOMATIC = SA = FiringMode('SEMI_AUTOMATIC', 'SA')
BURST_FIRE = BF = FiringMode('BURST_FIRE', 'BF')
FULLY_AUTOMATIC = FA = FiringMode('FULLY_AUTOMATIC', 'FA')

@dataclass
class VehicleStats:
    hand_on_road: int
    hand_off_road: int
    accel: int
    speed_interval: int
    top_speed: int
    body: int
    armor: int
    pilot: int
    sensor: int
    seat: int

@dataclass(repr=False)
class AttackRating:
    Close: int = None
    Near: int = None
    Medium: int = None
    Far: int = None
    Extreme: int = None
    def __repr__(self):
        attrs = asdict(self)
        return "(" + ", ".join([f'{k}: {d}' for k, d in attrs.items() if attrs[k] is not None]) + ")"

@dataclass(kw_only=True, repr=False)
class Gear:
    __refs__ = []
    name: str
    avail: str
    cost: int
    category: str
    legality: str = 'Legal'
    active_program_slots: int = 0
    ammo: Ammunition = None
    ar: AttackRating = None
    ma: MatrixAttrs = None
    blast: int = 0
    damage_value: int = 0
    defence_rating: int = 0
    device_rating: int = 0
    essence: float = 0.0
    fm: FiringMode = None
    mount: str = None
    rating: int = 0
    vs: VehicleStats = None
    def __post_init__(self):
        Gear.__refs__.append(self)
    def __repr__(self):
        attrs = asdict(self)
        (trimmed_attrs = [a for a in attrs if attrs[a] if attrs[a] is not None or attrs[a] != 0]
        return ", ".join(list())
            

COMBAT_AXE = Gear(name='Combat Axe', damage_value=5, ar=AttackRating(9), avail=4, cost=500, category='Blade')
SURVIVAL_KNIFE = Gear(name='Survival Knife', damage_value=3, ar=AttackRating(8, 2), avail=2, cost=220, category='Blade')
print(f"\n\n{COMBAT_AXE}\n\n{SURVIVAL_KNIFE}\n\n")

@dataclass
class Metatype:
    __refs__ = []
    name: str
    attr_changes: list[(Attribute, int)]
    racial_qualities: list = None
    def __post_init__(self):
        Metatype.__refs__.append(self)

@dataclass
class Quality:
    __refs__ = []
    name: str
    positive: bool
    cost: int
    conflict: list[str] = field(default_factory=list)
    requries_resolve: bool = False
    def __post_init__(self):
        Quality.__refs__.append(self)



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
MATRIX_ATTACK = MatrixAttribute('Attack', 0)
MATRIX_SLEAZE = MatrixAttribute('Sleaze', 0)
MATRIX_DATA_PROCESSING = MatrixAttribute('Data Processing', 0)
MATRIX_FIREWALL = MatrixAttribute('Firewall', 0)

HUMAN = Metatype('Human', [(EDGE, 7)])
DWARF = Metatype('Dwarf', [(BODY, 7), (REACTION, 5), (STRENGTH, 8), (WILLPOWER, 7)], ['Toxin Resistance', 'Thermographic Vision'])
ELF = Metatype('Elf', [(AGILITY, 7), (CHARISMA, 8)], ['Low-light Vision'])
ORK = Metatype('Ork', [(BODY, 8), (STRENGTH, 8), (CHARISMA, 5)], ['Low-light Vision', 'Built Tough 1'])
TROLL = Metatype('Troll', [(BODY, 9), (AGILITY, 5), (STRENGTH, 9), (CHARISMA, 5)], ['Dermal Deposits', 'Thermographic Vision', 'Built Tough 2'])

ASTRAL = Skill('Astral', False, ['Astral Combat', 'Astral Signatures', 'Emotional States', 'Spirit Types'], INTUITION, WILLPOWER)
CON = Skill('Con', True, ['Acting', 'Disguise', 'Impersonation', 'Performance'], WILLPOWER)

AMBIDEXTROUS = Quality('Ambidextrous', True, 4)
ANALYTICAL_MIND = Quality('Analytical Mind', True, 4)
# Requires resolve
APTITUDE_SKILL = Quality('Aptitude Skill', True, 4, [], True)
ASTRAL_CHAMELON = Quality('Astral Chamelon', True, 4)
BLANDNESS = Quality('Blandness', True, 4)
BUILT_TOUGH_1 = Quality('Built Tough 1', True, 4, ['Built Tough 2', 'Built Tough 3', 'Built Tough 4'])
BUILT_TOUGH_2 = Quality('Built Tough 2', True, 4, ['Built Tough 1', 'Built Tough 3', 'Built Tough 4'])
BUILT_TOUGH_3 = Quality('Built Tough 3', True, 4, ['Built Tough 1', 'Built Tough 2', 'Built Tough 4'])
BUILT_TOUGH_4 = Quality('Built Tough 4', True, 4, ['Built Tough 1', 'Built Tough 2', 'Built Tough 3'])
CATLIKE = Quality('Catlike', True, 4)
DERMAL_DEPOSITS = Quality('Dermal Deposits', True, 4)
DOUBLE_JOINTED = Quality('Double Jointed', True, 4)
# Requires resolve
ELEMENTAL_RESISTANCE = Quality('Elemental Resistance', True, 4, [], True)
# Requires resolve
EXCEPTIONAL_ATTRIBUTE = Quality('Exceptional Attribute', True, 4, [], True)
FIRST_IMPRESSION = Quality('First Impression', True, 4)
FOCUSED_CONCERNTRATION_1 = Quality('Focused Concerntration 1', True, 4, ['Focused Concerntration 2', 'Focused Concerntration 3'])
FOCUSED_CONCERNTRATION_2 = Quality('Focused Concerntration 2', True, 4, ['Focused Concerntration 1', 'Focused Concerntration 3'])
FOCUSED_CONCERNTRATION_3 = Quality('Focused Concerntration 3', True, 4, ['Focused Concerntration 1', 'Focused Concerntration 2'])
GEARHEAD = Quality('Gearhead', True, 4)
GUTS = Quality('Guts', True, 4)
HARDENING = Quality('Hardening', True, 4)
HIGH_PAIN_TOLERANCE = Quality('High Pain Tolerance', True, 4)
HOME_GROUND = Quality('Home Ground', True, 4)
HUMAN_LOOKING = Quality('Human-looking', True, 4)
INDOMITABLE = Quality('Indomitable', True, 4)
JURYRIGGER = Quality('Juryrigger', True, 4)
LONG_REACH = Quality('Long Reach', True, 4)
LOW_LIGHT_VISION = Quality('Low-light Vision', True, 4)
MAGIC_RESISTANCE = Quality('Magic Resistance', True, 4)
MENTOR_SPIRIT = Quality('Mentor Spirit', True, 4)
PHOTOGRAPHIC_MEMORY = Quality('Photographic Memory', True, 4)
QUICK_HEALER = Quality('Quick Healer', True, 4)
RESISTANCE_PATHOGENS = Quality('Resistance Pathogens', True, 4)
# Requires resolve
SPIRIT_AFFINITY = Quality('Spirit Affinity', True, 4, ['Sprite Affinity'], True)
# Requires resolve
SPRITE_AFFINITY = Quality('Sprite Affinity', True, 4, ['Spirit Affinity'], True)
THERMOGRAPHIC_VISION = Quality('Thermographic Vision', True, 4)
TOUGHNESS = Quality('Toughness', True, 4)
TOXIN_RESISTANCE = Quality('Toxin Resistance', True, 4)
WILL_TO_LIVE_1 = Quality('Will to Live 1', True, 4, ['Will to Live 2', 'Will to Live 3'])
WILL_TO_LIVE_2 = Quality('Will to Live 2', True, 4, ['Will to Live 1', 'Will to Live 3'])
WILL_TO_LIVE_3 = Quality('Will to Live 3', True, 4, ['Will to Live 1', 'Will to Live 2'])

AMMO_BELT = Ammunition('Belt')
AMMO_CLIP = Ammunition('Clip')
AMMO_CYLINDER = Ammunition('Cylinder')
AMMO_MAGAZINE = Ammunition('Magazine')
AMMO_MISSILE = Ammunition('Missile')
AMMO_MUZZLE = Ammunition('Muzzle')

print(Attribute.__refs__)

