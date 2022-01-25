from chargen import yaml_importer, roll
from random import choice, randint


class Character:
    def __init__(self):
        pass

class StatBlock:
    def __init__(self):
        pass

class Stat:
    def __init__(self, value: int, modifier: int):
        self.value = value
        self.modifier = modifier

    def __repr__(self):
        return f"{self.value} ({self.modifier})"

    def v_add(self, amt):
        self.value += amt

    def m_add(self, amt):
        self.modifier += amt
