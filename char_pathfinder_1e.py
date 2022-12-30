class Statistic:
    def __init__(self, name, value=0, **kwargs):
        self.name = name
        self.value = value
        self.mod = self.get_mod()
        for k, d in kwargs.items():
            self.__setattr__(k, d)

    def get_mod(self):
        return 

STR = Statistic("Strength")
DEX = Statistic("Dexterity")
CON = Statistic("CONSTITUTION")
INT = Statistic("Intelligence")
WIS = Statistic("Wisdom")
CHA = Statistic("Charisma")
