import random

class Character:
    def __init__(self):
        pass


class AbstractBaseClass:
    def __init__(self, name, **kwargs):
        self.name = name
        for k, d in kwargs.items():
            self.__setattr__(k, d)

    def __repr__(self):
        return self.name

class Characteristic(AbstractBaseClass):
    def __init__(self, name, **kwargs):
        super().__init__(self, name, **kwargs)
        self.base_value = 0
        self.current_value = -0

    def set_value(self, value):
        self.base_value = value
        if sel
