import chargen

class Attribute:
    def __init__(name: str, self, value: int = 0):
        self.name = name
        self.value = value
        self.attribute_limit = 0

    def __add___(amount: int, self):
        self.value += amount
        return Attribute(self.name, self.value)

    def set_attribute_limit(value: int, self):
        self.attribute_limit = value
        return

    def set_attribute_value(value: int, self):
        self.value = value
        return


class Attributes:
    def __init__(self):
        self.Body = Attribute("Body")
        self.Agility = Attribute("Agility")
        self.Reaction = Attribute("Reaction")
        self.Strength = Attribute("Strength")
        self.Charisma = Attribute("Charisma")
        self.Intuition = Attribute("Intuition")
        self.Logic = Attribute("Logic")
        self.Willpower = Attribute("Willpower")
        self.Edge = Attribute("Edge")
        self.Essence = Attribute("Essence")

        self.AttributeList = self.rebuild_attribute_list()

    def rebuild_attribute_list(self):
        return [self.Body, self.Agility, self.Reaction, self.Strength, self.Willpower, self.Logic, self.Intuition, self.Charisma, self.Edge, self.Essence]

    def set_starting_limit_values(data: dict, self):
        for value in data.keys():
            match value:
                case ["Body", "BODY"]:
                    self.Body.set_attribute_value(data[value][0])
                    self.Body.set_attribute_limit(data[value][1])
                case ["Agility", "AGI"]:
                    self.Agility.set_attribute_value(data[value][0])
                    self.Agility.set_attribute_limit(data[value][1])
                case ["Reaction", "REA"]:
                    self.Reaction.set_attribute_value(data[value][0])
                    self.Reaction.set_attribute_limit(data[value][1])
                case ["Strength", "STR"]:
                    self.Strength.set_attribute_value(data[value][0])
                    self.Strength.set_attribute_limit(data[value][1])
                case ["Willpower", "WIL"]:
                    self.Willpower.set_attribute_value(data[value][0])
                    self.Willpower.set_attribute_limit(data[value][1])
                case ["Logic", "LOG"]:
                    self.Logic.set_attribute_value(data[value][0])
                    self.Logic.set_attribute_limit(data[value][1])
                case ["Intuition", "INT"]:
                    self.Intuition.set_attribute_value(data[value][0])
                    self.Intuition.set_attribute_limit(data[value][1])
                case ["Charisma", "CHA"]:
                    self.Charisma.set_attribute_value(data[value][0])
                    self.Charisma.set_attribute_limit(data[value][1])
                case ["Edge", "EDG"]:
                    self.Edge.set_attribute_value(data[value][0])
                    self.Edge.set_attribute_limit(data[value][1])
                case ["Essence", "ESS"]:
                    self.Essence.set_attribute_value(data[value][0])
                    raise ValueError("Essence does not have a limit")
                case _:
                    pass

class Metatype:
    def __init__(name: str, self):
        self.name = name
        self.racial_attributes = Attributes()

    def __repr__(self):
        return self.name

Human = Metatype("Human")
Human.racial_attributes.set_starting_limit_values({'BODY': [1,6], 'AGI': [1, 6], 'REA': [1, 6], 'STR': [1, 6], 'WIL': [1, 6], 'LOG': [1, 6], 'INT': [1, 6], 'CHA': [1, 6], 'EDG': [2, 7], 'ESS': [6]})
Elf = Metatype("Elf")
Elf.racial_attributes.set_starting_limit_values({'BODY': [1,6], 'AGI': [2, 7], 'REA': [1, 6], 'STR': [1, 6], 'WIL': [1, 6], 'LOG': [1, 6], 'INT': [1, 6], 'CHA': [3, 8], 'EDG': [1, 6], 'ESS': [6]})
Dwarf = Metatype("Dwarf")
Dwarf.racial_attributes.set_starting_limit_values({'BODY': [3,8], 'AGI': [1, 6], 'REA': [1, 5], 'STR': [3, 8], 'WIL': [2, 7], 'LOG': [1, 6], 'INT': [1, 6], 'CHA': [1, 6], 'EDG': [1, 6], 'ESS': [6]})
Ork = Metatype("Ork")
Ork.racial_attributes.set_starting_limit_values({'BODY': [1,6], 'AGI': [1, 6], 'REA': [1, 6], 'STR': [1, 6], 'WIL': [1, 6], 'LOG': [1, 6], 'INT': [1, 6], 'CHA': [1, 6], 'EDG': [1, 6], 'ESS': [6]})
Troll = Metatype("Troll")
Troll.racial_attributes.set_starting_limit_values({'BODY': [1,6], 'AGI': [1, 6], 'REA': [1, 6], 'STR': [1, 6], 'WIL': [1, 6], 'LOG': [1, 6], 'INT': [1, 6], 'CHA': [1, 6], 'EDG': [1, 6], 'ESS': [6]})



class ConditionMonitor:
    def __init__(self, overflow: int, physical: int = 0, stun : int = 0):
        self.damagetrack_physical = physical
        self.damagetrack_stun = stun
        self.overflow = overflow

    def __add__(amount: int, _type: str, self):
        if _type.capitalize() == "Physical":
            self.damagetrack_physical += amount
        elif _type.capitalize() == "Stun":
            self.damagetrack_stun += amount
        elif _type.capitalize() == "Overflow":
            self.overflow += amount
        else:
            pass
        return ConditionMonitor(self.overflow, self.damagetrack_physical, self.damagetrack_stun)

class Qualitiy:
    def __init__(name: str, polarity: int, cost, self):
        self.name = name
        # Positive qualities have a polarity of 1, thus making their cost positive.
        # Negative qualities have a polarity of -1, thus making their cost negative (or in essence, adding points)
        self.polarity = polarity
        self.quantity = 1 # The number of times this quality can be taken. Some qualities can be taken multiple times naturally
        self.cost = self.calc_cost(cost)
        if type(self.cost) == bool:
            raise TypeError(f"Cost calculation errored the fuck out. How do you explain this? {self.cost}")

    def calc_cost(cost, self):
        if type(cost) == int:
            return cost
        if type(cost) == list:
            if len(cost) != 3:
                return False
            match cost[1]:
                case "or":
                    return [cost[0], cost[2]]
                case "each":
                    self.quantity = cost[2]
                    return cost[0]
                case "to":
                    return [i for i in range(cost[0], cost[2])]
                case 6: # Catches 'Dependant(s) Quality
                    return cost
                case _:
                    return False
        pass

character = {
    'Name': "",
    'Metatype': Metatype
}