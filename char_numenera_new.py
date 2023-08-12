import random
import yaml

cyphers = yaml.safe_load(open('.\\numenera_data\\cyphers.yaml', 'rt', encoding='utf-8'))

def roll(dicestring):
    if isinstance(dicestring, int):
        return dicestring
    if "+" in dicestring:
        dicestring, mods = dicestring.split('+')
    else: 
        mods = 0
    throws, sides = [int(_) for _ in dicestring.split('d')]
    return sum([int(mods), sum([random.randint(1, sides) for _ in range(throws)])])

for key in cyphers.keys():
    cyphers[key]['Level'] = roll(cyphers[key]['Level'])
    print(key, cyphers[key]['Level'])
    

class AbstractBaseClass:
    def __init__(self, name, **kwargs):
        self.name = name
        for k, d in kwargs.items():
            self.__setattr__(k, d)

    def __repr__(self):
        return self.__format__()

    def __format__(self):
        return self.name

    def _getattr(self, attribute):
        return self.__getattribute__(attribute)

class _Stat(AbstractBaseClass):
    items = []
    def __init__(self, name, value=0, **kwargs):
        super().__init__(name, **kwargs)
        _Stat.items.append(self)
        self.value = value

    def __add__(self, x: int):
        return _Stat(self.name, value=self.value+x)

class _CharType(AbstractBaseClass):
    items = []
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        _CharType.items.append(self)
DEFAULT_CHARTYPE = _CharType("Default Character Type")

class _CharDescriptor(AbstractBaseClass):
    items = []
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        _CharDescriptor.items.append(self)
DEFAULT_CHARDESCRIPTOR = _CharDescriptor("Default Character Descriptor")

class _CharFocus(AbstractBaseClass):
    items = []
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        _CharFocus.items.append(self)
DEFAULT_CHARFOCUS = _CharFocus("Default Character Focus")

# Stats
MIGHT = _Stat("Might")
SPEED = _Stat("Speed")
INTELLECT = _Stat("Intellect")

class Character:
    def __init__(self, name):
        self.name = name
        self.char_type = None
        self.char_desc = None
        self.char_focus = None
        self.stats = {
            'Might': MIGHT,
            'Speed': SPEED,
            'Intellect': INTELLECT
        }
        self.edge = {
            'Might': 0,
            'Speed': 0,
            'Intellect': 0
        }
        self.skills = {}
        self.numenera = {}


def genCharacter():
    pass


# Character Types
GLAIVE = _CharType("Glaive", stats=(11, 10, 7))
NANO = _CharType("Nano")
JACK = _CharType("Jack")
ARKUS = _CharType("Arkus")
WRIGHT = _CharType("Wright")
DELVES = _CharType("Delves")