class ABC:
    def __init__(self, name, **kwargs):
        self.name = name
        for k, d in kwargs.items():
            self.__setattr__(k, d)

    def __repr__(self):
        return self.name

    # def __add__(self):
    #     return None

    # def __iadd__(self, *args):
    #    return self.__add__(args)


class Race(ABC):
    items = []
    def __init__(self, name, **kwargs):
        super().__init__(name)
        Race.items.append(self)

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

class AbilityScore(ABC):
    def __init__(self, name, value = 0, **kwargs):
        super().__init__(name)
        self.value = value
        self.mod = self.get_mod()

    def __add__(self, amt):
        self.value += amt
        self.mod = self.get_mod()
        return AbilityScore(self.name, self.value)

    def __iadd__(self, amt):
        return self.__add__(amt)

    
    def get_mod(self):
        return (self.value//2) - 5

    def __repr__(self):
        return self.__format__()
    
    def __format__(self):
        return f"{self.name}: {self.value} ({self.mod})"

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

STR = AbilityScore("Strength")
DEX = AbilityScore("Dexterity")
CON = AbilityScore("Constitution")
INT = AbilityScore("Intelligence")
WIS = AbilityScore("Wisdom")
CHA = AbilityScore("Charisma")
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
RACES = Race.items

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

print(jeff.hit_points)
CON += 7
jeff2 = Character(name="Jeff", _class=BARBARIAN)
print(jeff2.hit_points)
# print(BARBARIAN.hit_points)
