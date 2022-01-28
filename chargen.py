from random import randint, choice, seed
from yaml import safe_load
from string import ascii_letters


def roll(dice_string):
    """Dice rolling funciton
    Args:
        dice_string (str): in the format of "1d6" or "xdy"
    Returns:
        sum of rolls
    """
    throws, sides = dice_string.split('d')
    return sum(randint(1, int(sides)) for _ in range(int(throws)))


def expand(dictionary):
    return_dictionary = {}
    for key in dictionary:
        value = dictionary[key]
        if isinstance(key, range):
            return_dictionary.update({i: value for i in key})
        else:
            return_dictionary[key] = value
    return return_dictionary

def capitalise(string: str):
    """Returns a capitalised version of a string in title format

    Args:
        string str: input string

    Returns:
        str: return string

    e.g. "the cliff of doom" -> "The Cliff of Doom"
    """
    string_words = string.split(" ")
    for it, word in enumerate(string_words):
        if it != 0 and word.lower() in ['the', 'is', 'of', 'as', 'by', 'a', 'to', 'and', 'my']:
            pass
        else:
            string_words[it] = string_words[it].capitalize()
    return " ".join(string_words)

def new_seed():
    """Generates a new random seed from an random assortment of 
        letters of a random length

       This mainly saves having to import 'ascii_letters' from strings
       over and over cuz that shit is verbose as all hell
    """
    seed_string = "".join(choice(ascii_letters) for _ in range(randint(5, 10)))
    return seed_string
    
def yaml_importer(path: str) -> dict:
    return safe_load(open(path, 'rt'))


class BaseAttributeClass:
    """
    A generic class for attribute/ability scores
    """
    def __init__(self, name: str, maximum: int = 0, current: int = 0):
        self.name = name
        self.maximum = maximum
        self.current = current

    def __add__(self, x):
        return BaseAttributeClass(self.name, (self.maximum+x), (self.current+x))

    def __iadd__(self, x):
        return self.__add__(x)

    def __sub__(self, x):
        return BaseAttributeClass(self.name, (self.maximum-x), (self.current-x))

    def __isub__(self, x):
        return self.__sub__(x)

    def __repr__(self):
        return f"{self.name}: {self.current}/{self.maximum}"
    

class BaseItemClass:
    """
    A generic class for representing an item in game
    """
    def __init__(self, name):
        self.name = name

    def isitem(self):
        """
        This function is used to verify an object is class BaseItemClass,
            or is the child of BaseItemClass
        """
        return True

    def __repr__(self):
        return self.name

class BaseWeaponClass(BaseItemClass):
    """
    A generic class for representing a weapon in game
    """
    def __init__(self, name):
        super().__init__(name)


class BaseInventoryClass:
    """
    A generic class for representing a character's inventory 
    """
    def __init__(self, items: list = []):
        self.items = items

    def __add__(self, item: BaseItemClass):
        try:
            item.isitem()
            self.items.append(item) 
            return BaseInventoryClass(items = self.items)
        except:
            raise TypeError

    def __iadd__(self, item):
        return self.__add__(item)

    def __repr__(self):
        return f"Items:\n   {[item for item in self.items]}"


