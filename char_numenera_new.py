import random

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
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        _Stat.items.append(self)
        self.value = 0

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

# Character Types
GLAIVE = _CharType("Glaive", )
NANO = _CharType("Nano")
JACK = _CharType("Jack")
ARKUS = _CharType("Arkus")
WRIGHT = _CharType("Wright")
DELVES = _CharType("Delves")