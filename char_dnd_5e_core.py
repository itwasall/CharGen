import random
# random should probably only be used for testing. This file is to store data, not to aide in the processing of a random generation of a character
"""
    What the shit is this?

    This file holds the core shit for DND, such as AbilityScore, Alignment & Class classes so that I won't have to
        rewrite everything should I ever try and make a character generator for another setting set in 5e
"""

def ProficiencyBonus(level):
    return ((level - 1) // 4) + 2

def GetProficentSkills(skills):
    def RandomiseProficientSkills(skills, x):
        proficient_skills = []
        while len(proficient_skills) < x:
            skill = random.choice(skills[f"Choose {x}"])
            if skill in proficient_skills:
                proficient_skills.pop()
            proficient_skills.append(skill)
        return proficient_skills
    prof_data_keys = skills.keys()
    match list(prof_data_keys)[0]:
        case 'Choose 2':
            return RandomiseProficientSkills(skills, 2)
        case 'Choose 3':
            return RandomiseProficientSkills(skills, 3)
        case 'Choose 4':
            return RandomiseProficientSkills(skills, 4)


class _Class:
    items = []
    def __init__(self, name, **kwargs):
        self.name = name
        _Class.items.append(self)
        for k, d in kwargs.items():
            self.__setattr__(k, d)
    
    def __repr__(self):
        return self.name
DEFAULT_CLASS = _Class("Default Class")

class _SubClass:
    items = []
    def __init__(self, name, _class: _Class, **kwargs):
        self.name = name
        self._class = _class
        _SubClass.items.append(self)
        for k, d in kwargs.items():
            self.__setattr__(k, d)

    def __repr__(self):
        return self.name

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
        return (value // 2) - 5

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


class Skill:
    def __init__(self, name, ab_score, prof: bool = False, bonus = 0, **kwargs):
        self.name = name
        self.ab_score = ab_score
        self.prof = prof
        self.bonus = bonus
        self.FORMAT_REPR = False
        for k, d in kwargs.items():
            self.__setattr__(k, d)

    def __add__(self, value):
        self.bonus += value
        return Skill(self.name, self.ab_score, self.prof)
    
    def __iadd__(self, value):
        return self.__add__(value)

    def __repr__(self):
        return self.__format__()
    
    def __format__(self):
        if self.FORMAT_REPR:
            return f"({self.ab_score}) {self.name}: +-{self.prof}"
        else:
            return self.name

    def set_proficiency_bonus(self, level: int):
        self.prof = True
        self.__add__(self, ProficiencyBonus(level))

class Item:
    items = []
    def __init__(self, name, **kwargs):
        self.name = name
        Item.items.append(self)
        for k, d in kwargs.items():
            self.__setattr__(k, d)

    def __repr__(self):
        return self.name

class Coin(Item):
    def __init__(self, name):
        super().__init__(name)

cp = Coin("Copper Piece")
sp = Coin("Silver Piece")
gp = Coin("Gold Piece")

class Weapon(Item):
    def __init__(self, name, cost, wpn_type, **kwargs):
        super().__init__(name)
        self.cost = cost
        self.wpn_type = wpn_type
        for k, d in kwargs.items():
            self.__setattr__(k, d)
        
CLUB = Weapon("Club", cost=[1, sp], wpn_type='Simple', is_melee = True)
DAGGER = Weapon("Dagger", cost=[2, gp], wpn_type='Simple', is_melee=True)
GREATCLUB = Weapon("Greatclub", cost=[2, sp], wpn_type='Simple', is_melee=True)
HANDAXE = Weapon("Handaxe", cost=[5, gp], wpn_type='Simple', is_melee=True)
JAVELIN = Weapon("Javelin", cost=[2, gp], wpn_type='Simple', is_melee=True)
LIGHT_HAMMER = Weapon("Light_Hammer", cost=[2, gp], wpn_type='Simple', is_melee=True)
MACE = Weapon("Mace", cost=[5, gp], wpn_type='Simple', is_melee=True)
QUARTERSTAFF = Weapon("Quarterstaff", cost=[2, sp], wpn_type='Simple', is_melee=True)
SICKLE = Weapon("Sickle", cost=[1, gp], wpn_type='Simple', is_melee=True)
SPEAR = Weapon("Spear", cost=[1, gp], wpn_type='Simple', is_melee=True)

LIGHT_CROSSBOW = Weapon("Light_Crossbow", cost=[25, gp], wpn_type='Simple', is_melee=False)
DART = Weapon("Dart", cost=[5, cp], wpn_type='Simple', is_melee=False)
SHORTBOW = Weapon("Shortbow", cost=[25, gp], wpn_type='Simple', is_melee=False)
SLING = Weapon("Sling", cost=[1, sp], wpn_type='Simple', is_melee=False)

BATTLEAXE = Weapon("Battleaxe", cost=[10, gp], wpn_type='Martial', is_melee=True)
FLAIL = Weapon("Flail", cost=[10, gp], wpn_type='Martial', is_melee=True)
GLAIVE = Weapon("Glaive", cost=[20, gp], wpn_type='Martial', is_melee=True)
GREATAXE = Weapon("Greataxe", cost=[30, gp], wpn_type='Martial', is_melee=True)
GREATSWORD = Weapon("Greatsword", cost=[50, gp], wpn_type='Martial', is_melee=True)
HALBERD = Weapon("Halberd", cost=[20, gp], wpn_type='Martial', is_melee=True)
LANCE = Weapon("Lance", cost=[10, gp], wpn_type='Martial', is_melee=True)
LONGSWORD = Weapon("Longsword", cost=[15, gp], wpn_type='Martial', is_melee=True)
MAUL = Weapon("Maul", cost=[10, gp], wpn_type='Martial', is_melee=True)
MORNINGSTAR = Weapon("Morningstar", cost=[15, gp], wpn_type='Martial', is_melee=True)
PIKE = Weapon("Pike", cost=[5, gp], wpn_type='Martial', is_melee=True)
RAPIER = Weapon("Rapier", cost=[25, gp], wpn_type='Martial', is_melee=True)
SCIMITAR = Weapon("Scimitar", cost=[25, gp], wpn_type='Martial', is_melee=True)
SHORTSWORD = Weapon("Shortsword", cost=[10, gp], wpn_type='Martial', is_melee=True)
TRIDENT = Weapon("Trident", cost=[5, gp], wpn_type='Martial', is_melee=True)
WAR_PICK = Weapon("War_Pick", cost=[5, gp], wpn_type='Martial', is_melee=True)
WARHAMMER = Weapon("Warhammer", cost=[15, gp], wpn_type='Martial', is_melee=True)
WHIP = Weapon("Whip", cost=[2, gp], wpn_type='Martial', is_melee=True)

BLOWGUN = Weapon("Blowgun", cost=[10, gp], wpn_type='Martial', is_melee=False)
HAND_CROSSBOW = Weapon("Hand_Crossbow", cost=[75, gp], wpn_type='Martial', is_melee=False)
HEAVY_CROSSBOW = Weapon("Heavy_Crossbow", cost=[50, gp], wpn_type='Martial', is_melee=False)
LONGBOW = Weapon("Longbow", cost=[50, gp], wpn_type='Martial', is_melee=False)
NET = Weapon("Net", cost=[1, gp], wpn_type='Martial', is_melee=False)

SIMPLE_WEAPONS = [i for i in Item.items if (hasattr(i, "wpn_type") and i.wpn_type == 'Simple')]
MARTIAL_WEAPONS = [i for i in Item.items if (hasattr(i, "wpn_type") and i.wpn_type == 'Martial')]

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

BARBARIAN.proficiencies = {
        'Armor': ['Light', 'Medium', 'Sheilds'],
        'Weapons': [SIMPLE_WEAPONS, MARTIAL_WEAPONS],
        'Tools': None
        }
BARBARIAN.saving_throws = [STR, CON]
BARBARIAN.skills = {'Choose 2': [ANIMAL_HANDLING, ATHLETICS, INTIMIDATION, NATURE, PERCEPTION, SURVIVAL]}
BARBARIAN.hit_dice = "1d12"
BARBARIAN.initial_health = [12, CON.modifier]

BARD.proficiencies = {
        'Armor': ['Light'],
        'Weapons': [SIMPLE_WEAPONS, HAND_CROSSBOW, LONGSWORD, RAPIER, SHORTSWORD],
        'Tools': {'Choose 3': []}
        }
BARD.saving_throws = [DEX, CHA]
BARD.skills = {'Choose 3': SKILLS}
BARD.hit_dice = "1d6"
BARD.initial_health = [8, CON.modifier]

CLERIC.proficiencies = {
        'Armor': ['Light', 'Medium', 'Shield'],
        'Weapons': [SIMPLE_WEAPONS],
        'Tools': None
        }
CLERIC.saving_throws = [WIS, CHA]
CLERIC.skills = {'Choose 2': [HISTORY, INSIGHT, MEDICINE, PERSUASION, RELIGION]}
CLERIC.hit_dice = "1d8"
CLERIC.initial_health = [8, CON.modifier]

DRUID.proficiencies = {
        'Armor': ['Light', 'Medium', 'Shield'],
        'Weapons': [CLUB, DAGGER, DART, JAVELIN, MACE, QUARTERSTAFF, SCIMITAR, SICKLE, SLING, SPEAR],
        'Tools': {'Has': ['Herbalism Kit']}
        }
DRUID.saving_throws = [INT, WIS]
DRUID.skills = {'Choose 2': [ARCANA, ANIMAL_HANDLING, INSIGHT, MEDICINE, NATURE, PERCEPTION, RELIGION, SURVIVAL]}
DRUID.hit_dice = "1d8"
DRUID.initial_health = [8, CON.modifier]

FIGHTER.proficiencies = {
        'Armor': ['All', 'Shield'],
        'Weapons': [SIMPLE_WEAPONS, MARTIAL_WEAPONS],
        'Tools': None
        }
FIGHTER.saving_throws = [STR, CON]
FIGHTER.skills = {'Choose 2': [ACROBATICS, ANIMAL_HANDLING, ATHLETICS, HISTORY, INSIGHT, INTIMIDATION, PERCEPTION, SURVIVAL]}
FIGHTER.hit_dice = "1d10"
FIGHTER.initial_health = [10, CON.modifier]

MONK.proficiencies = {
        'Armor': None,
        'Weapons': [SIMPLE_WEAPONS, SHORTSWORD],
        'Tools': {'Choose 1': []}
        }
MONK.saving_throws = [STR, DEX]
MONK.skills = {'Choose 2': [ACROBATICS, ATHLETICS, HISTORY, INSIGHT, RELIGION, STEALTH]}
MONK.hit_dice = "1d8"
MONK.initial_health = [8, CON.modifier]

PALADIN.proficiencies = {
        'Armor': ['All', 'Shield'],
        'Weapons': [SIMPLE_WEAPONS, MARTIAL_WEAPONS],
        'Tools': None
        }
PALADIN.saving_throws = [WIS, CHA]
PALADIN.skills = {'Choose 2': [ATHLETICS, INSIGHT, INTIMIDATION, MEDICINE, PERSUASION, RELIGION]}
PALADIN.hit_dice = "1d10"
PALADIN.initial_health = [10, CON.modifier]

RANGER.proficiencies = {
        'Armor': ['Light', 'Medium', 'Shield'],
        'Weapons': [SIMPLE_WEAPONS, MARTIAL_WEAPONS],
        'Tools': None
        }
RANGER.saving_throws = [STR, DEX]
RANGER.skills = {'Choose 3': [ANIMAL_HANDLING, ATHLETICS, INSIGHT, INVESTIGATION, NATURE, PERCEPTION, STEALTH, SURVIVAL]}
RANGER.hit_dice = "1d10"
RANGER.initial_health = [10, CON.modifier]

ROGUE.proficiencies = {
        'Armor': ['Light'],
        'Weapons': [SIMPLE_WEAPONS, HAND_CROSSBOW],
        'Tools': {'Has': ['Thieves Tools']}
        }
ROGUE.saving_throws = [DEX, INT]
ROGUE.skills = {'Choose 4': [ACROBATICS, ATHLETICS, DECEPTION, INSIGHT, INTIMIDATION, INVESTIGATION, PERCEPTION, PERFORMANCE, PERSUASION, SLEIGHT_OF_HAND, STEALTH]}
ROGUE.hit_dice = "1d8"
ROGUE.initial_health = [8, CON.modifier]

SORCERER.proficiencies = {
        'Armor': None,
        'Weapons': [DAGGER, DART, SLING, QUARTERSTAFF, LIGHT_CROSSBOW],
        'Tools': None
        }
SORCERER.saving_throws = [CON, CHA]
SORCERER.skills = {'Choose 2': [ARCANA, DECEPTION, INSIGHT, INTIMIDATION, PERSUASION, RELIGION]}
SORCERER.hit_dice = "1d6"
SORCERER.initial_health = [6, CON.modifier]

WARLOCK.proficiencies = {
        'Armor': ['Light'],
        'Weapons': ['Simple'],
        'Tools': None
        }
WARLOCK.saving_throws = [WIS, CHA]
WARLOCK.skills = {'Choose 2': [ARCANA, DECEPTION, HISTORY, INTIMIDATION, INVESTIGATION, NATURE, RELIGION]}
WARLOCK.hit_dice = "1d8"
WARLOCK.initial_health = [8, CON.modifier]

WIZARD.proficiencies = {
        'Armor': None,
        'Weapons': [DAGGER, DART, SLING, QUARTERSTAFF, LIGHT_CROSSBOW],
        'Tools': None
        }
WIZARD.saving_throws = [INT, WIS]
WIZARD.skills = {'Choose 2': [ARCANA, HISTORY, INSIGHT, INVESTIGATION, MEDICINE, RELIGION]}
WIZARD.hit_dice = "1d6"
WIZARD.initial_health = [6, CON.modifier]

CLASSES = [BARBARIAN, BARD, CLERIC, DRUID, FIGHTER, MONK, PALADIN, RANGER, ROGUE, SORCERER, WARLOCK, WIZARD]

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
    """
    print(f"Total subclasses: {len(_SubClass.items)}")
    bingus = lambda x: [subclass for subclass in _SubClass.items if hasattr(subclass, x)]
    print(f"Total xanathar subclasses: {len(bingus('xanathar'))}")
    print(f"{', '.join([subclass.name for subclass in bingus('xanathar')])}")
    """
    roll_class = random.choice(CLASSES)
    print(roll_class)

    def gen_skill_prof(Class: _Class):
        def gen_skill_while(Class: _Class, x):
            proficient_skills = []
            while len(proficient_skills) < x:
                skill = random.choice(Class.skills[f"Choose {x}"])
                if skill in proficient_skills:
                    proficient_skills.pop()
                proficient_skills.append(skill)
            return proficient_skills
        prof_data_keys = Class.skills.keys()
        match list(prof_data_keys)[0]:
            case 'Choose 2':
                return gen_skill_while(Class, 2)
            case 'Choose 3':
                return gen_skill_while(Class, 3)
            case 'Choose 4':
                return gen_skill_while(Class, 4)
        

    print(gen_skill_prof(roll_class))

