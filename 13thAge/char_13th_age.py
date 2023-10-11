from dataclasses import dataclass

class ABC():
    def __init__(self, name, **kwargs):
        self.name = name
        for k, d in kwargs.items():
            self.__setattr__(k, d)
    def __repr__(self):
        return self.name

@dataclass
class Race:
    name: str

class _Class(ABC):
    items = []
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        _Class.items.append(self)

class DamageType(ABC):
    items = []
    def __init__(self, name, **kwargs):
        super().__init__(name)
        DamageType.items.append(self)

@dataclass
class AbilityScore(ABC):
    name: str
    value: int
    mod: int = 0
    def get_mod(self):
        return (self.value // 2) - 5
    def __add__(self, x):
        print(self.name)
        print(self.value)
        print(x)
        print(self.value + x)
        return AbilityScore(name=self.name, value=self.value + x, mod=self.mod)

class Character(ABC):
    def __init__(self, name="Jeff", race=None, _class=None, **kwargs):
        super().__init__(name)
        self.race = race 
        self._class = _class 
        self.level = 1
        self.STR = STR
        self.DEX = DEX
        self.CON = CON
        self.INT = INT
        self.WIS = WIS
        self.CHA = CHA
        self.ac = 0
        self.physical_defence = 0
        self.mental_defence = 0
        self.initiative_bonus = self.DEX.mod + self.level
        self.hit_points = self.calc_hit_points()

    def calc_hit_points(self):
        return (self.CON.mod + 7) * 3

STR = AbilityScore("Strength", 1)
DEX = AbilityScore("Dexterity", 1)
CON = AbilityScore("Constitution", 1)
INT = AbilityScore("Intelligence", 1)
WIS = AbilityScore("Wisdom", 1)
CHA = AbilityScore("Charisma", 1)
ABILITY_SCORES = [STR, DEX, CON, INT, WIS, CHA]

HUMAN = Race("Human")
GNOME = Race("Gnome")
DWARF = Race("Dwarf")
DARK_ELF = Race("Dark_Elf")
WOOD_ELF = Race("Wood_Elf")
HIGH_ELF = Race("High_Elf")
HALF_ELF = Race("Half_Elf")
HALF_ORC = Race("Half_Orc")
HALFLING = Race("Halfling")

"""
    _Class Style Guide
hit_points
    [[7, CON.mod], 3] == (7 + CON.mod) * 3
"""
BARBARIAN = _Class("Barbarian", ab_bonus=[STR, CON], hit_points=[[7, CON.mod], 3])
BARD = _Class("Bard")
CLERIC = _Class("Cleric")
FIGHTER = _Class("Fighter")
PALADIN = _Class("Paladin")
RANGER = _Class("Ranger")
ROGUE = _Class("Rogue")
SORCERER = _Class("Sorcerer")
WIZARD = _Class("Wizard")
_CLASSES = _Class.items

def calc_hit_points(character):
    return sum(character._class.hit_points[0]) * character._class.hit_points[1]

ACID = DamageType("Acid")
COLD = DamageType("Cold")
FIRE = DamageType("Fire")
FORCE = DamageType("Force")
HOLY = DamageType("Holy")
LIGHTNING = DamageType("Lightning")
NEGATIVE_ENERGY = DamageType("Negative_Energy")
POISON = DamageType("Poison")
PSYCHIC = DamageType("Psychic")
THUNDER = DamageType("Thunder")
DAMAGE_TYPES = DamageType.items

jeff = Character(name="Jeff", _class=BARBARIAN)

print(jeff.CON)
CON += 7
print(jeff.CON)
jeff2 = Character(name="Jeff", _class=BARBARIAN)
print(jeff2.hit_points)
# print(BARBARIAN.hit_points)
