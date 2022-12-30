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
        super().__init__(name)
        _Class.items.append(self)

class AbilityScore(ABC):
    def __init__(self, name, value = 0, **kwargs):
        super().__init__(name)
        self.value = value
        self.mod = self.get_mod()

    def __add__(self, amt):
        self.value += amt
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
        self.STR = STR
        self.DEX = DEX
        self.CON = CON
        self.INT = INT
        self.WIS = WIS
        self.CHA = CHA

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

BARBARIAN = _Class("Barbarian")
BARD = _Class("Bard")
CLERIC = _Class("Cleric")
FIGHTER = _Class("Fighter")
PALADIN = _Class("Paladin")
RANGER = _Class("Ranger")
ROGUE = _Class("Rogue")
SORCERER = _Class("Sorcerer")
WIZARD = _Class("Wizard")
_CLASSES = _Class.items

STR = AbilityScore("Strength")
DEX = AbilityScore("Dexterity")
CON = AbilityScore("Constitution")
INT = AbilityScore("Intelligence")
WIS = AbilityScore("Wisdom")
CHA = AbilityScore("Charisma")
ABILITYSCORES = [STR, DEX, CON, INT, WIS, CHA]


