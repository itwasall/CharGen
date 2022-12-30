"""
    What the shit is this?

    This file holds the core shit for DND, such as AbilityScore, Alignment & Class classes so that I won't have to
        rewrite everything should I ever try and make a character generator for another setting set in 5e
"""
class _Class:
    items = []
    def __init__(self, name, **kwargs):
        self.name = name
        _Class.items.append(self)
        for k, d in kwargs.items():
            self.__setattr__(k, d)
DEFAULT_CLASS = _Class("Default Class")

class _SubClass:
    items = []
    def __init__(self, name, _class: _Class, **kwargs):
        self.name = name
        self._class = _class
        _SubClass.items.append(self)
        for k, d in kwargs.items():
            self.__setattr__(k, d)

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

"""
    CLASSES
"""
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
ARTIFICER = _Class("Artificer", tasha=True)

"""
    SUBCLASSES
"""
# BARBARIAN
PATH_OF_THE_BESERKER = _SubClass("Path_of_the_Beserker", _class=BARBARIAN)
PATH_OF_THE_TOTEM_WARRIOR = _SubClass("Path_of_the_Totem_Warrior", _class=BARBARIAN)
PATH_OF_THE_ZEALOT = _SubClass("Path_of_the_Zealot", _class=BARBARIAN, xanathar=True)
PATH_OF_THE_ANCESTRAL_GUARDIAN = _SubClass("Path_of_the_Ancestral_Guardian", _class=BARBARIAN, xanathar=True)
PATH_OF_THE_STORM_HERALD = _SubClass("Path_of_the_Storm_Herald", _class=BARBARIAN, xanathar=True)
PATH_OF_THE_BEAST = _SubClass("Path_of_the_Beast", _class=BARBARIAN, tasha=True)
PATH_OF_WILD_MAGIC = _SubClass("Path_of_Wild_Magic", _class=BARBARIAN, tasha=True)
# BARD
COLLEGE_OF_LORE = _SubClass("College_of_Lore", _class=BARD)
COLLEGE_OF_VALOR = _SubClass("College_of_Valor", _class=BARD)
COLLEGE_OF_GLAMOUR = _SubClass("College_of_Glamour", _class=BARD, xanathar=True)
COLLEGE_OF_SWORDS = _SubClass("College_of_Swords", _class=BARD, xanathar=True)
COLLEGE_OF_WHISPERS = _SubClass("College_of_Whispers", _class=BARD, xanathar=True)
COLLEGE_OF_CREATION = _SubClass("College_of_Creation", _class=BARD, tasha=True)
COLLEGE_OF_ELOQUENCE = _SubClass("College_of_Eloquence", _class=BARD, tasha=True)
# CLERIC
KNOWLEDGE_DOMAIN = _SubClass("Knowledge_Domain", _class=CLERIC)
LIFE_DOMAIN = _SubClass("Life_Domain", _class=CLERIC)
LIGHT_DOMAIN = _SubClass("Light_Domain", _class=CLERIC)
NATURE_DOMAIN = _SubClass("Nature_Domain", _class=CLERIC)
TEMPEST_DOMAIN = _SubClass("Tempest_Domain", _class=CLERIC)
TRICKERY_DOMAIN = _SubClass("Trickery_Domain", _class=CLERIC)
WAR_DOMAIN = _SubClass("War_Domain", _class=CLERIC)
FORGE_DOMAIN = _SubClass("Forge_Domain", _class=CLERIC, xanathar=True)
GRAVE_DOMAIN = _SubClass("Grave_Domain", _class=CLERIC, xanathar=True)
ORDER_DOMAIN = _SubClass("Order_Domain", _class=CLERIC, ravnica=True, tasha=True)
PEACE_DOMAIN = _SubClass("Peace_Domain", _class=CLERIC, tasha=True)
TWILIGHT_DOMAIN = _SubClass("Twilight_Domain", _class=CLERIC, tasha=True)
# DRUID
CIRCLE_OF_THE_LAND = _SubClass("Circle_of_the_Land", _class=DRUID)
CIRCLE_OF_THE_MOON = _SubClass("Circle_of_the_Moon", _class=DRUID)
CIRCLE_OF_DREAMS = _SubClass("Circle_of_Dreams", _class=DRUID, xanathar=True)
CIRCLE_OF_THE_SHEPHERD = _SubClass("Circle_of_the_Shepherd", _class=DRUID, xanathar=True)
CIRCLE_OF_SPORES = _SubClass("Circle_of_Spores", _class=DRUID, ravnica=True, tasha=True)
CIRCLE_OF_STARS = _SubClass("Circle_of_Stars", _class=DRUID, tasha=True)
CIRCLE_OF_WILDFIRE = _SubClass("Circle_of_Wildfire", _class=DRUID, tasha=True)
# FIGHTER 
BATTLE_MASTER = _SubClass("Battle_Master", _class=FIGHTER)
CHAMPTION = _SubClass("Chamption", _class=FIGHTER)
ELDRITCH_KNIGHT = _SubClass("Eldritch_Knight", _class=FIGHTER)
CAVALIER = _SubClass("Cavalier", _class=FIGHTER, xanathar=True)
ARCANE_ARCHER = _SubClass("Arcane_Archer", _class=FIGHTER, xanathar=True)
SAMURAI = _SubClass("Samurai", _class=FIGHTER, xanathar=True)
PSI_WARRIOR = _SubClass("Psi_Warrior", _class=FIGHTER, tasha=True)
RUNE_KNIGHT = _SubClass("Rune_Knight", _class=FIGHTER, tasha=True)
# MONK
WAY_OF_SHADOW = _SubClass("Way_of_Shadow", _class=MONK)
WAY_OF_THE_FOUR_ELEMENTS = _SubClass("Way_of_the_Four_Elements", _class=MONK)
WAY_OF_THE_OPEN_HAND = _SubClass("Way_of_the_Open_Hand", _class=MONK)
WAY_OF_THE_SUN_SOUL = _SubClass("Way_of_the_Sun_Soul", _class=MONK, xanathar=True)
WAY_OF_THE_DRUNKEN_MASTER = _SubClass("Way_of_the_Drunken_Master", _class=MONK, xanathar=True)
WAY_OF_THE_KENSEI = _SubClass("Way_of_the_Kensei", _class=MONK, xanathar=True)
WAY_OF_THE_ASCENDANT_DRAGON = _SubClass("Way_of_the_Ascendant_Dragon", _class=MONK, fizbans=True)
WAY_OF_MERCY = _SubClass("Way_of_Mercy", _class=MONK, tasha=True)
WAY_OF_THE_ASTRAL_SELF = _SubClass("Way_of_the_Astral_Self", _class=MONK, tasha=True)
# PALADIN
OATH_OF_DEVOTION = _SubClass("Oath_of_Devotion", _class=PALADIN)
OATH_OF_THE_ANCIENTS = _SubClass("Oath_of_the_Ancients", _class=PALADIN)
OATH_OF_VENGEANCE = _SubClass("Oath_of_Vengeance", _class=PALADIN)
OATH_OF_CONQUEST = _SubClass("Oath_of_Conquest", _class=PALADIN, xanathar=True)
OATH_OF_REDEMPTION = _SubClass("Oath_of_Redemption", _class=PALADIN, xanathar=True)
OATH_OF_GLORY = _SubClass("Oath_of_Glory", _class=PALADIN, tasha=True)
OATH_OF_THE_WATCHERS = _SubClass("Oath_of_the_Watchers", _class=PALADIN, tasha=True)
# RANGER
BEAST_MASTER = _SubClass("Beast_Master", _class=RANGER)
HUNTER = _SubClass("Hunter", _class=RANGER)
GLOOM_STALKER = _SubClass("Gloom_Stalker", _class=RANGER, xanathar=True)
HORIZON_WALKER = _SubClass("Horizon_Walker", _class=RANGER, xanathar=True)
MONSTER_SLAYER = _SubClass("Monster_Slayer", _class=RANGER, xanathar=True)
FEY_WANDERER = _SubClass("Fey_Wanderer", _class=RANGER, tasha=True)
SWARMKEEPER = _SubClass("Swarmkeeper", _class=RANGER, tasha=True)
DRAKEWARDEN = _SubClass("Drakewarden", _class=RANGER, fizbans=True)
# ROGUE
ARCANE_TRICKSTER = _SubClass("Arcane_Trickster", _class=ROGUE)
ASSASSIN = _SubClass("Assassin", _class=ROGUE)
SCOUT = _SubClass("Scout", _class=ROGUE, xanathar=True)
THIEF = _SubClass("Thief", _class=ROGUE)
INQUISITIVE = _SubClass("Inquisitive", _class=ROGUE, xanathar=True)
MASTERMIND = _SubClass("Mastermind", _class=ROGUE, xanathar=True)
SWASHBUCKLER = _SubClass("Swashbuckler", _class=ROGUE, xanathar=True)
PHANTOM = _SubClass("Phantom", _class=ROGUE, tasha=True)
SOULKNIFE = _SubClass("Soulknife", _class=ROGUE, tasha=True)
# SORCERER
DRACONIC_BLOODLINE = _SubClass("Draconic_Bloodline", _class=SORCERER)
WILD_MAGIC = _SubClass("Wild_Magic", _class=SORCERER)
DIVINE_SOUL = _SubClass("Divine_Soul", _class=SORCERER, xanathar=True)
SHADOW_MAGIC = _SubClass("Shadow_Magic", _class=SORCERER, xanathar=True)
STORM_SORCERY = _SubClass("Storm_Sorcery", _class=SORCERER, xanathar=True)
ABERRANT_MIND = _SubClass("Aberrant_Mind", _class=SORCERER, tasha=True)
CLOCKWORK_SOUL = _SubClass("Clockwork_Soul", _class=SORCERER, tasha=True)
# WARLOCK
THE_ARCHFEY = _SubClass("The_Archfey", _class=WARLOCK)
THE_FIEND = _SubClass("The_Fiend", _class=WARLOCK)
THE_GREAT_OLD_ONE = _SubClass("The_Great_Old_One", _class=WARLOCK)
THE_CELESTIAL = _SubClass("The_Celestial", _class=WARLOCK, xanathar=True)
THE_HEXBLADE = _SubClass("The_Hexblade", _class=WARLOCK, xanathar=True)
THE_FATHOMLESS = _SubClass("The_Fathomless", _class=WARLOCK, tasha=True)
THE_GENIE = _SubClass("The_Genie", _class=WARLOCK, tasha=True)
# WIZARD
SCHOOL_OF_ABJURATION = _SubClass("School_of_Abjuration", _class=WIZARD)
SCHOOL_OF_CONJURATION = _SubClass("School_of_Conjuration", _class=WIZARD)
SCHOOL_OF_DIVINATION = _SubClass("School_of_Divination", _class=WIZARD)
SCHOOL_OF_ENCHANTMENT = _SubClass("School_of_Enchantment", _class=WIZARD)
SCHOOL_OF_EVOCATION = _SubClass("School_of_Evocation", _class=WIZARD)
SCHOOL_OF_ILLUSION = _SubClass("School_of_Illusion", _class=WIZARD)
SCHOOL_OF_NECROMANCY = _SubClass("School_of_Necromancy", _class=WIZARD)
SCHOOL_OF_TRANSMUTATION = _SubClass("School_of_Transmutation", _class=WIZARD)
WAR_MAGIC = _SubClass("War_Magic", _class=WIZARD, xanathar=True)
ORDER_OF_SCRIBES = _SubClass("Order_of_Scribes", _class=WIZARD, tasha=True)
# ARTIFICER
ALCHEMIST = _SubClass("Alchemist", _class=ARTIFICER, tasha=True)
ARMORER = _SubClass("Armorer", _class=ARTIFICER, tasha=True)
ARTILLERIST = _SubClass("Artillerist", _class=ARTIFICER, tasha=True)
BATTLE_SMITH = _SubClass("Battle_Smith", _class=ARTIFICER, tasha=True)

if __name__ == "__main__":
    print(f"Total subclasses: {len(_SubClass.items)}")
    bingus = lambda x: [subclass for subclass in _SubClass.items if hasattr(subclass, x)]
    print(f"Total xanathar subclasses: {len(bingus('xanathar'))}")
    print(f"{', '.join([subclass.name for subclass in bingus('xanathar')])}")
