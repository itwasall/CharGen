from typing import List
from random import randint, choice, seed
from attr import attr
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


def capitalize(string: str):
    """
    If you must
    """
    return capitalise(string)


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


def set_name(object, name):
    object.__setattr__(__name__, name)


class BaseAttributeClass:
    """
    A generic class for attribute/ability scores
    """
    def __init__(self, name: str, maximum: int = 0, current: int = 0):
        self.name = name
        self.maximum = maximum
        self.current = current

    def __add__(self, amount: int):
        return BaseAttributeClass(self.name, (self.maximum+amount), (self.current+amount))

    def __iadd__(self, amount: int):
        return self.__add__(amount)

    def __sub__(self, amount: int):
        return BaseAttributeClass(self.name, (self.maximum-amount), (self.current-amount))

    def __isub__(self, amount: int):
        return self.__sub__(amount)

    def __repr__(self):
        return f"{self.name}: {self.current}/{self.maximum}"

class BaseAttributeBlockClass:
    """
    A generic class for representing all of a characters attributes
    """
    def __init__(self, attributes: List = []):
        self.attributes = attributes

    def __add__(self, attribute: BaseAttributeClass):
        self.attributes.append(attribute)
        return BaseAttributeBlockClass(self.attributes)

    def __iadd__(self, attribute: BaseAttributeClass):
        return self.__add__(attribute)

    def __repr__(self):
        return f"{' '.join(attribute.name for attribute in self.attributes)}"


class BaseSkillClass:
    def __init__(self, name):
        self.name = name

    def set_level_names(self, level_names: List[str]):
        self.level_names = {level_name: level for level_name, level in zip(level_names, range(len(level_names)))}



class BaseItemClass:
    """
    A generic class for representing an item in game
    """
    def __init__(self, name: str):
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
    def __init__(self, name: str):
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

    def __iadd__(self, item: BaseItemClass):
        return self.__add__(item)

    def __repr__(self):
        return f"Items:\n   {[item for item in self.items]}"


class Emp():
    def __init__(self, id, name, Add):
        self.id = id
        self.name = name
        self.Add = Add

class Freelance(Emp):
    def __init__(self, id, name, Add, Emails):
        super().__init__(id, name, Add)
        self.Emails = Emails

Emp_1 = Freelance(103, "Jerry", "Noida", "penisbreath@dogfart.com")

print('The ID is: ', Emp_1.id)
print('The Name is: ', Emp_1.name)
print('The Address is: ', Emp_1.Add)
print('The Emails is: ', Emp_1.Emails)