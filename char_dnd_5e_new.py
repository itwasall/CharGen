import random

import char_dnd_5e_core as Core


class PartyMember:
    def __init__( self, name: str = None, **kwargs):
        """ Macro Character Stuff """
        self.name = name
        self.race = Core.DEFAULT_RACE
        self.subrace = None
        self._class = Core.DEFAULT_CLASS
        self._subclass = None
        self.languages = [Core.DEFAULT_LANGUAGE]
        """ Ability Scores """
        self.STR = Core.STR
        self.DEX = Core.DEX
        self.CON = Core.CON
        self.INT = Core.INT
        self.WIS = Core.WIS
        self.CHA = Core.CHA
        """ Skills """
        # STR
        self.athletics = Core.ATHLETICS
        # DEX
        self.acrobatics = Core.ACROBATICS
        self.sleight_of_hand = Core.SLEIGHT_OF_HAND
        self.stealth = Core.STEALTH
        # INT
        self.arcana = Core.ARCANA
        self.history = Core.HISTORY
        self.investigation = Core.INVESTIGATION
        self.nature = Core.NATURE
        self.religion = Core.RELIGION
        # WIS
        self.animal_handling = Core.ANIMAL_HANDLING
        self.insight = Core.INSIGHT
        self.medicine = Core.MEDICINE
        self.perception = Core.PERCEPTION
        self.survival = Core.SURVIVAL
        # CHA
        self.deception = Core.DECEPTION
        self.intimidation = Core.INTIMIDATION
        self.performance = Core.PERFORMANCE
        self.persuasion = Core.PERSUASION
        """ Equipment & Proficiencies """
        self.proficiencies = {'Weapon': [], 'Armor': [], 'Tool': []}
        """ Combat Stats """
        self.AC = 0
        self.initiative = 0
        self.speed = 0
        self.hit_points = 0
        self.current_hit_points = 0
        """ Possessions """
        self.money = { Core.cp: 0, Core.sp: 0, Core.ep: 0, Core.gp: 0, Core.pp: 0 }
        self.equipment = []


        for k, d in kwargs.items():
            self.__setattr__(k, d)
    
    def __repr__(self):
        return self.__format__()

    def __format__(self):
        return self.name

global CHARACTER
CHARACTER = PartyMember('Jeff')

def diceRoll(dicestring, summed=True):
    throws, sides = dicestring.split("d")
    if summed:
        return sum([random.randint(1, int(sides)) for _ in range(int(throws))])
    else:
        rolls = [random.randint(1, int(sides)) for _ in range(int(throws))]
        rolls.sort()
        return rolls

def sortReverse(l: list):
    l.sort()
    l.reverse()
    return l

def attrAsDict(_class):
    return [{i: _class._getattr(i)} for i in dir(_class) if not i.startswith("__")]

def genAlignment(weights: tuple):
    is_weight_a = random.randint(0, 100)
    if is_weight_a > 30 and isinstance(weights[0], str) and weights[0] != 'None':
        alignment_a = weights[0]
    else:
        alignment_a = random.choice(['Lawful', 'Chaotic', 'Neutral'])
    is_weight_b = random.randint(0, 100)
    if is_weight_b > 30 and isinstance(weights[1], str) and weights[1] != 'None':
        alignment_b = weights[1]
    else:
        alignment_b = random.choice(['Good', 'Evil', 'Neutral'])
    return Core.Alignment(alignment_a, alignment_b)


def genRace():
    char_race = random.choice(Core.RACES)

    char_race_attributes = attrAsDict(char_race)
    
    for attr in char_race_attributes:
        match list(attr.keys())[0]:
            case '_getattr':
                char_race_attributes.pop(char_race_attributes.index(attr))
            case 'has_subrace':
                char_race_attributes.pop(char_race_attributes.index(attr))
                char_subrace = random.choice([subrace for subrace in Core.SUBRACES if subrace.race == char_race])
            case 'alignment':
                char_race_attributes.pop(char_race_attributes.index(attr))
                print("yes alignment")
                char_alignment = genAlignment(attr['alignment'])
            case 'age':
                char_race_attributes.pop(char_race_attributes.index(attr))
                char_age = random.randint(attr['age'][0], attr['age'][1])
            case 'size':
                char_race_attributes.pop(char_race_attributes.index(attr))
                char_size = attr['size']
            case _:
                char_subrace = None
                char_alignment = genAlignment((False, False))
                char_size = "SIZE NOT FOUND"
    print(char_race, char_subrace, char_age)
    print(char_race_attributes)
    print(char_alignment)
    print(char_size)



def genCharacter():

    ability_score_rolls = []
    for _ in range(6):
        rolls = diceRoll("4d6", summed=False)
        sortReverse(rolls)
        rolls.pop()
        ability_score_rolls.append(rolls)
    
    ability_score_rolls.sort()

    genRace()

    char_race = random.choice(Core.RACES)
    if hasattr(char_race, "has_subrace"):
        char_subrace = random.choice([subrace for subrace in Core.SUBRACES if subrace.race == char_race])
    else:
        char_subrace = None

#    print(char_race, char_subrace)
    char_class = random.choice(Core.CLASSES)


print(genCharacter())
