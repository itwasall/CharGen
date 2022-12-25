from typing import Tuple, List
import chargen

class Metatype:
    def __init__(metatype_name: str, self):
        self.metatype_name = metatype_name

    def __repr__(self):
        return self.metatype_name

class _Class:
    def __init__(class_name: str, self):
        self.class_name = class_name

    def __repr__(self):
        return self.class_name

class ConditionMonitor:
    def __init__(condition_physical: int = 0, condition_stun: int = 0, self):
        self.condition_physical = condition_physical
        self.condition_stun = condition_stun

    def __add__(amount: int, _type: str, self):
        if _type.capitalize() == "Physical":
            self.condition_physical += amount
        elif _type.capitalize() == "Stun":
            self.condition_stun += amount
        else:
            pass


class Attribute:
    def __init__(
            attribute_type: str,
            attribute_name: str,
            value: int = 0, 
            self
        ):
        self.attribute_type = attribute_type
        self.attribute_name = attribute_name
        self.value = value

    def __add__(amount: int, self):
        self.value += amount
        return Attribute(
                self.attribute_type, 
                self.attribute_name, 
                self.value
                )

    def __repr__(self):
        return " ".join([self.attribute_name, "Type:", self.attribute_type, "Value:", self.value])

Body = Attribute("Body", "Physical")
Agility = Attribute("Agility", "Physical")
Reaction = Attribute("Reaction", "Physical")
Strength = Attribute("Strength", "Physical")
Willpower = Attribute("Willpower", "Mental")
Logic = Attribute("Logic", "Mental")
Intuition = Attribute("Intuition", "Mental")
Charisma = Attribute("Charisma", "Mental")
Edge = Attribute("Edge", "Special")
Essence = Attribute("Essence", "Special")
Magic = Attribute("Magic", "Special")

class Skill:
    def __init__(skill_name: str, attribute: Attribute, rating: int = 0, dice_pool: int = 0, self):
        self.skill_name = skill_name
        self.attribute = attribute
        self.rating = rating
        self.dice_pool = dice_pool

    def set_rating(amount: int, self):
        self.rating = amount

    def set_dice_pool(amount: int, self):
        self.dice_pool = dice_pool

Astral = Skill("Astral", Intuition)
Athletics = Skill("Athletics", Agility)
CloseCombat = Skill("Close Combat", Agility)
Engineering = Skill("Engineering", Logic)
Firearms = Skill("Firearms", Agility)
Perception = Skill("Perception", Intuition)
Sorcery = Skill("Sorcery", Magic)
Stealth = Skill("Stealth", Agility)


def create_attributes():
    attributes = {
            'Body': [Body.attribute_type, Body.value],
            'Agility': [Agility.attribute_type, Agility.value],
            'Reaction': [Reaction.attribute_type, Reaction.value],
            'Strength': [Strength.attribute_type, Strength.value],
            'Willpower': [Willpower.attribute_type, Willpower.value],
            'Logic': [Logic.attribute_type, Logic.value],
            'Intuition': [Intuition.attribute_type, Intuition.value],
            'Charisma': [Charisma.attribute_type, Charisma.value],
            'Edge': [Edge.attribute_type, Edge.value],
            'Essence': [Essence.attribute_type, Essence.value],
            'Magic': [Magic.attribute_type, Magic.value],
            }
    return attributes 

Dwarf = Metatype("Dwarf")
Elf = Metatype("Elf")
Human = Metatype("Human")
Ork = Metatype("Ork")
Troll = Metatype("Troll")

character = {
        "Name": "",
        "Metatype": Metatype,
        "Class":
        "Ethnicity": "",
        "Age": 0,
        "Height": "0m",
        "Weight": "0kg",
        "Movement": [0, 0, "+0"],
        "Composure": 0,
        "Judge Intentions": 0,
        "Memory": 0,
        "Lift/Carry": 0,
        "Defense Rating": 0,
        "Initiative": "0",
        "Condition Monitor": ConditionMonitor
        }
