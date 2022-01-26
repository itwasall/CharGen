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
