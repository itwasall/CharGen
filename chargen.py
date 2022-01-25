from random import randint
from yaml import safe_load


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

def capitalise(string):
    string_words = string.split(" ")
    for it, word in enumerate(string_words):
        if it != 0 and word.lower() in ['the', 'of', 'as', 'by', 'a', 'to', 'and', 'my']:
            pass
        else:
            string_words[it] = string_words[it].capitalize()
    return " ".join(string_words)


def yaml_importer(path: str) -> dict:
    return safe_load(open(path, 'rt'))