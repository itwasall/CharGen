"""
    What the shit is this?

    This file holds the core shit for DND, such as AbilityScore, Alignment & Class classes so that I won't have to
        rewrite everything should I ever try and make a character generator for another setting set in 5e
"""
class _Class:
    def __init__(self, name, **kwargs):
        self.name = name
        for k, d in kwargs.items():
            self.__setattr__(k, d)
DEFAULT_CLASS = _Class("Default Class")

class Race:
    def __init__(self, name, **kwargs):
        self.name = name
        for k, d in kwargs.items():
            self.__setattr__(k, d)
DEFAULT_RACE = Race("Default Race")

class Alignment:
    def __init__(self, law_chaos, good_evil):
        self.law_chaos = law_chaos 
        self.good_evil = good_evil
    def __repr__(self):
        return self.__format__()
    def __format__(self):
        if self.law_chaos == "Neutral" and self.good_evil == "Neutral":
            return "True Neutral"
        return f"{self.law_chaos} {self.good_evil}"
        
DEFAULT_ALIGNMENT = Alignment("DEFAULT", "ALIGNMENT")

class Language:
    def __init__(self, name, speakers: None, script: None):
        self.name = name
        if type(speakers) == str:
            self.speakers = [speakers]
        elif type(speakers) != list:
            raise TypeError
        self.speakers = speakers
        self.script = script
    def __repr__(self):
        return self.name
DEFAULT_LANGUAGE = Language("DEFAULT LANGUAGE", "DEFAULT SPEAKERS", "DEFAULT SCRIPT")

class AbilityScore:
    def __init__(self, name, value = 0):
        self.name = name
        self.value = value
        self.modifier = self.get_mod(value)

    def get_mod(self, value):
        if value == 1:
            return -5
        if (value + 1) % 2 == 0:
            value -= 1
        return int(value/2)-5

    def __repr__(self):
        return self.name

    def __add__(self, value):
        self.value += value
        return AbilityScore(self.name, self.value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __sub__(self, value):
        self.value -= value
        return AbilityScore(self.name, self.value)

    def __isub__(self, value):
        return self.__sub__(value)
DEFAULT_ABILITY_SCORE = AbilityScore("DEFAULT ABILITY_SCORE")

def ProficiencyBonus(level):
    return ((level - 1) // 4) + 2

class Skill:
    def __init__(self, name, ab_score, prof: bool = False, bonus = 0, **kwargs):
        self.name = name
        self.ab_score = ab_score
        self.prof = prof
        self.bonus = bonus
        for k, d in kwargs.items():
            self.__setattr__(k, d)

    def __add__(self, value):
        self.bonus += value
        return Skill(self.name, self.ab_score, self.prof)
    
    def __iadd__(self, value):
        return self.__add__(value)

    def __repr__(self):
        return f"({self.ab_score}) {self.name}: +-{self.prof}"

    def set_proficiency_bonus(self, level: int):
        self.prof = True
        self.__add__(self, ProficiencyBonus(level))


"""
    ABILITY SCORES
"""
STR = AbilityScore("Strength")
DEX = AbilityScore("Dexterity")
CON = AbilityScore("Constitution")
INT = AbilityScore("Intelligence")
WIS = AbilityScore("Wisdom")
CHA = AbilityScore("Charisma")

STAT_BLOCK = {"STR": STR, "DEX": DEX, "CON": CON, "INT": INT, "WIS": WIS, "CHA": CHA}

"""
    SKILLS
"""
# ======= STR ======= 
ATHLETICS = Skill("Athletics", ab_score=STR)
# ======= DEX ======= 
ACROBATICS = Skill("Acrobatics", ab_score=DEX)
SLEIGHT_OF_HAND = Skill("Sleight_Of_Hand", ab_score=DEX)
STEALTH = Skill("Stealth", ab_score=DEX)
# ======= INT ======= 
ARCANA = Skill("Arcana", ab_score=INT)
HISTORY = Skill("History", ab_score=INT)
INVESTIGATION = Skill("Investigation", ab_score=INT)
NATURE = Skill("Nature", ab_score=INT)
RELIGION = Skill("Religion", ab_score=INT)
# ======= WIS ======= 
ANIMAL_HANDLING = Skill("Animal_Handling", ab_score=WIS)
INSIGHT = Skill("Insight", ab_score=WIS)
MEDICINE = Skill("Medicine", ab_score=WIS)
PERCEPTION = Skill("Perception", ab_score=WIS)
SURVIVAL = Skill("Survival", ab_score=WIS)
# ======= CHA ======= 
DECEPTION = Skill("Deception", ab_score=CHA)
INTIMIDATION = Skill("Intimidation", ab_score=CHA)
PERFORMANCE = Skill("Performance", ab_score=CHA)
PERSUASION = Skill("Persuasion", ab_score=CHA)


SKILLS = [ATHLETICS, ACROBATICS, SLEIGHT_OF_HAND, STEALTH, ARCANA, HISTORY, INVESTIGATION, NATURE, RELIGION, ANIMAL_HANDLING, INSIGHT, MEDICINE, PERCEPTION, SURVIVAL, DECEPTION, INTIMIDATION, PERFORMANCE, PERSUASION]

BARBARIAN = _Class("Barbarian")
BARD = _Class("Bard")
CLERIC = _Class("Cleric")
DRUID = _Class("Druid")
FIGHTER = _Class("Fighter")
MONK = _Class("Monk")
PALADIN = _Class("Paladin")
RANGER = _Class("Ranger")
ROGUE = _Class("Rogue")
SORCERER = _Class("Sorcerer")
WARLOCK = _Class("Warlock")
WIZARD = _Class("Wizard")

class Classes:
    def __init__(self):
        self.BARBARIAN = BARBARIAN
        self.BARD = BARD
        self.CLERIC = CLERIC
        self.DRUID = DRUID
        self.FIGHTER = FIGHTER
        self.MONK = MONK
        self.PALADIN = PALADIN
        self.RANGER = RANGER
        self.SORCERER = SORCERER
        self.WARLOCK = WARLOCK
        self.WIZARD =250 
