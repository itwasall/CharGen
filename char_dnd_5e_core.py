import random
# from unpack_test import unpack_new
# random should probably only be used for testing. This file is to store data, not to aide in the processing of a random generation of a character
"""
    What the shit is this?

    This file holds the core shit for DND, such as AbilityScore, Alignment & Class classes so that I won't have to
        rewrite everything should I ever try and make a character generator for another setting set in 5e
"""

def proficiencyBonus(level):
    return ((level - 1) // 4) + 2

def getProficiencies(data):
    def randomiseProficiencies(data, x):
        proficiencies = []
        while len(proficiencies) < x:
            roll = random.choice(data[f"Choose {x}"])
            if roll in proficiencies:
                proficiencies.pop(proficiencies.index(roll))
            proficiencies.append(roll)
        return proficiencies

    prof_data_keys = data.keys()
    match list(prof_data_keys)[0]:
        case 'Choose 1':
            return randomiseProficiencies(data, 1)
        case 'Choose 2':
            return randomiseProficiencies(data, 2)
        case 'Choose 3':
            return randomiseProficiencies(data, 3)
        case 'Choose 4':
            return randomiseProficiencies(data, 4)
        case 'Has':
            return data['Has']

def getEquipment(data):
    def unpackEquipment(data):
        unpacked_items = []
        def rollItems(data, amount):
            items = []
            while len(items) < amount:
                roll = random.choice(data)
                if roll in items:
                    items.pop(items.index(roll))
                items.append(roll)
            return items

        def chooseHowMany(key, data):
            match key:
                case 'Choose 1':
                    return rollItems(data, 1)
                case 'Choose 2':
                    return rollItems(data, 2)
        """
        TODO: Sort out that wack recursion
        """
        for item in data:
            if isinstance(item, dict) and len(item.keys()) == 1:
                unpacked_dict_value = unpackEquipment(list(item.values())[0])
                unpacked_items.append(chooseHowMany(list(item.keys())[0], unpacked_dict_value))
            elif isinstance(item, list):
                for i in item:
                    if isinstance(i, dict) and len(i.keys()) == 1:
                        unpacked_dict_value = unpackEquipment(list(i.values())[0])
                        unpacked_items.append(chooseHowMany(list(i.keys())[0], unpacked_dict_value))
                    else:
                        unpacked_items.append(i) 
            else:
                unpacked_items.append(item) 
        return unpacked_items
    flatten = lambda *n: (e for a in n for e in (flatten(*a) if isinstance(a, (tuple, list)) else (a,)))    
    """ I stole this lambda from stackoverflow and have no idea how it works but it does, thanks samplebias!"""
    return list(flatten(unpackEquipment(data)))


def flatten(*n): 
    return (e for a in n for e in (flatten(*a) if isinstance(a, (tuple, list)) else (a,)))    


def makeItemList(attribute, attr_value=None):
    if attr_value == None:
        return [item for item in Item.items if hasattr(item, attribute)]
    else:
        return [item for item in Item.items 
                if (hasattr(item, attribute) and item.__getattribute__(attribute) == attr_value)]

class AbstractBaseClass:
    def __init__(self, name, **kwargs):
        self.name = name
        for k, d in kwargs.items():
            self.__setattr__(k, d)

    def __repr__(self):
        return self.__format__()

    def __format__(self):
        return self.name

    def _getattr(self, attribute):
        return self.__getattribute__(attribute)

class ABC(AbstractBaseClass):
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)

class _Class(ABC):
    items = []
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        _Class.items.append(self)
DEFAULT_CLASS = _Class("Default Class")

class _ClassMechanic(ABC):
    items = []
    def __init__(self, name, _class: _Class, **kwargs):
        super().__init__(name, **kwargs)
        self._class = _class
        _ClassMechanic.items.append(self)

class _SubClass(ABC):
    items = []
    def __init__(self, name, _class: _Class, **kwargs):
        super().__init__(name, **kwargs)
        self._class = _class
        _SubClass.items.append(self)

class Race(ABC):
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
DEFAULT_RACE = Race("Default Race")

class SubRace(ABC):
    items = []
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        SubRace.items.append(self)

class RaceMechanic(ABC):
    items = []
    def __init__(self, name, category, **kwargs):
        super().__init__(name, **kwargs)
        self.category = category
        RaceMechanic.items.append(self)

class Background(ABC):
    items = []
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        Background.items.append(self)

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

class Language(ABC):
    items = []
    def __init__(self, name, speakers: None, script: None, **kwargs):
        super().__init__(name, **kwargs)
        if type(speakers) == str:
            self.speakers = [speakers]
        elif type(speakers) != list:
            raise TypeError
        self.speakers = speakers
        self.script = script
        Language.items.append(self)
DEFAULT_LANGUAGE = Language("DEFAULT LANGUAGE", "DEFAULT SPEAKERS", "DEFAULT SCRIPT")

class AbilityScore:
    def __init__(self, name, value = 0):
        self.name = name
        self.value = value
        self.get_mod()

    def get_mod(self):
        self.modifier = (self.value // 2) - 5

    def __repr__(self):
        return self.__format__()

    def __format__(self, *args, **kwargs):
        if self.modifier > 0:
            return f"{self.name} - {self.value} (+{self.modifier})"
        elif self.modifier == 0:
            return f"{self.name} - {self.value} (+-{self.modifier})"
        elif self.modifier < 0:
            return f"{self.name} - {self.value} ({self.modifier})"

    def __add__(self, value:int):
        self.value = self.value + value
        return AbilityScore(self.name, self.value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __sub__(self, value):
        self.value -= value
        return AbilityScore(self.name, self.value)

    def __isub__(self, value):
        return self.__sub__(value)
DEFAULT_ABILITY_SCORE = AbilityScore("DEFAULT ABILITY_SCORE")


class Skill(ABC):
    def __init__(self, name, ab_score, prof: bool = False, bonus = 0, **kwargs):
        super().__init__(name, **kwargs)
        self.ab_score = ab_score
        self.prof = prof
        self.bonus = bonus
        self.FORMAT_REPR = False

    def __add__(self, value):
        self.bonus += value
        return Skill(self.name, self.ab_score, self.prof)
    
    def __iadd__(self, value):
        return self.__add__(value)
    
    def __format__(self):
        if self.FORMAT_REPR:
            return f"({self.ab_score}) {self.name}: +-{self.prof}"
        else:
            return self.name

    def set_proficiency_bonus(self, level: int):
        self.prof = True
        self.__add__(self, proficiencyBonus(level))

class Item(ABC):
    items = []
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        Item.items.append(self)

class Coin(Item):
    def __init__(self, name, value):
        super().__init__(name)
        self.value = value

class Weapon(Item):
    def __init__(self, name, cost, wpn_type, **kwargs):
        super().__init__(name, **kwargs)
        self.cost = cost
        self.wpn_type = wpn_type

class Armor(Item):
    def __init__(self, name, cost, arm_type, ac, **kwargs):
        super().__init__(name, **kwargs)
        self.cost = cost
        self.arm_type = arm_type
        self.ac = ac

class Tool(Item):
    def __init__(self, name, cost, tool_type=None, **kwargs):
        super().__init__(name, **kwargs)
        self.cost = cost
        self.tool_type = tool_type

class Vehicle(Item):
    def __init__(self, name, vehicle_type=None, **kwargs):
        super().__init__(name, **kwargs)
        self.vehicle_type = vehicle_type
"""
    ABILITY SCORES
"""
STR = AbilityScore("STR")
DEX = AbilityScore("DEX")
CON = AbilityScore("CON")
INT = AbilityScore("INT")
WIS = AbilityScore("WIS")
CHA = AbilityScore("CHA")

STAT_BLOCK = {"STR": STR, "DEX": DEX, "CON": CON, "INT": INT, "WIS": WIS, "CHA": CHA}

"""
    ALIGNMENTS
"""
LAWFUL_GOOD = Alignment("Lawful", "Good")
LAWFUL_NEUTRAL = Alignment("Lawful", "Neutral")
LAWFUL_EVIL = Alignment("Lawful", "Evil")
NEUTRAL_GOOD = Alignment("Neutral", "Good")
NEUTRAL_NEUTRAL = Alignment("Neutral", "Neutral")
NEUTRAL_EVIL = Alignment("Neutral", "Evil")
CHAOTIC_GOOD = Alignment("Chaotic", "Good")
CHAOTIC_NEUTRAL = Alignment("Chaotic", "Neutral")
CHAOTIC_EVIL = Alignment("Chaotic", "Evil")

"""
    MONEY
"""
cp = Coin("Copper Piece", value=1)
sp = Coin("Silver Piece", value=10)
ep = Coin("Electrum Piece", value=50)
gp = Coin("Gold Piece", value=100)
pp = Coin("Platinum Piece", value=1000)

"""
    SKILLS
"""
# ======= STR ======= 
ATHLETICS = Skill("Athletics", ab_score=STR)
# ======= DEX ======= 
ACROBATICS = Skill("Acrobatics", ab_score=DEX)
SLEIGHT_OF_HAND = Skill("Sleight of Hand", ab_score=DEX)
STEALTH = Skill("Stealth", ab_score=DEX)
# ======= INT ======= 
ARCANA = Skill("Arcana", ab_score=INT)
HISTORY = Skill("History", ab_score=INT)
INVESTIGATION = Skill("Investigation", ab_score=INT)
NATURE = Skill("Nature", ab_score=INT)
RELIGION = Skill("Religion", ab_score=INT)
# ======= WIS ======= 
ANIMAL_HANDLING = Skill("Animal Handling", ab_score=WIS)
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
    LANGUAGES
"""
# STANDARD LANGUAGES
COMMON = Language("Common", speakers='Humans', script='Common')
DWARVISH = Language("Dwarvish", speakers='Dwarves', script='Dwarvish')
ELVISH = Language("Elvish", speakers='Elves', script='Elvish')
GIANT = Language("Giant", speakers=['Ogres', 'Giants'], script='Dwarvish')
GNOMISH = Language("Gnomish", speakers='Gnomes', script='Dwarvish')
GOBLIN = Language("Goblin", speakers='Goblins', script='Dwarvish')
HALFLING = Language("Halfling", speakers='Halflings', script='Common')
ORC = Language("Orc", speakers='Orcs', script='Dwarvish')
# EXOTIC LANGUAGES
ABYSSAL = Language("Abyssal", speakers='Demons', script='Infernal', exotic=True)
CELESTIAL = Language("Celestial", speakers='Celestials', script='Celestial', exotic=True)
DEEP_SPEECH = Language("Deep Speech", speakers=['Mind Flayers', 'Beholders'], script=None, exotic=True)
DRACONIC = Language("Draconic", speakers=['Dragons', 'Dragonborn'], script='Draconic', exotic=True)
INFERNAL = Language("Infernal", speakers='Devils', script='Infernal', exotic=True)
PRIMORDIAL = Language("Primordial", speakers='Elementals', script='Dwarvish', exotic=True)
SYLVAN = Language("Sylvan", speakers='Fey creatures', script='Elvish', exotic=True)
UNDERCOMMON = Language("Undercommon", speakers='Underdark Traders', script='Elvish', exotic=True)
LANGUAGES = [COMMON, DWARVISH, ELVISH, GIANT, GNOMISH, GOBLIN, HALFLING, ORC, ABYSSAL, DEEP_SPEECH, INFERNAL, PRIMORDIAL, SYLVAN, UNDERCOMMON]

"""
    VEHICLES 
"""
# MOUNTS
CAMEL = Vehicle("Camel", cost=[50, gp], speed=50, vehicle_type='Land', subtype='Animal')
DONKEY = Vehicle("Donkey", cost=[8, gp], speed=40, vehicle_type='Land', subtype='Animal')
ELEPHANT = Vehicle("Elephant", cost=[200, gp], speed=40, vehicle_type='Land', subtype='Animal')
HORSE_DRAFT = Vehicle("Horse Draft", cost=[50, gp], speed=40, vehicle_type='Land', subtype='Animal')
HORSE_RIDING = Vehicle("Horse Riding", cost=[75, gp], speed=60, vehicle_type='Land', subtype='Animal')
MASTIFF = Vehicle("Mastiff", cost=[25, gp], speed=40, vehicle_type='Land', subtype='Animal')
PONY = Vehicle("Pony", cost=[30, gp], speed=40, vehicle_type='Land', subtype='Animal')
WARHORSE = Vehicle("Warhorse", cost=[400, gp], speed=60, vehicle_type='Land', subtype='Animal')
# DRAWN VEHICLES        
BARDING = Vehicle("Barding", vehicle_type='Land', subtype='Vehicle')
BIT_AND_BRIDLE = Vehicle("Bit and Bridle", vehicle_type='Land', subtype='Vehicle')
CARRIAGE = Vehicle("Carriage", vehicle_type='Land', subtype='Vehicle')
CART = Vehicle("Cart", vehicle_type='Land', subtype='Vehicle')
CHARIOT = Vehicle("Chariot", vehicle_type='Land', subtype='Vehicle')
FEED = Vehicle("Feed", vehicle_type='Land', subtype='Vehicle')
SADDLEBAGS = Vehicle("Saddlebags", vehicle_type='Land', subtype='Vehicle')
SLED = Vehicle("Sled", vehicle_type='Land', subtype='Vehicle')
STABLING = Vehicle("Stabling", vehicle_type='Land', subtype='Vehicle')
WAGON = Vehicle("Wagon", vehicle_type='Land', subtype='Vehicle')
# WATER VEHICLES
GALLEY = Vehicle("Galley", cost=[30_000, gp], vehicle_type='Water')
KEELBOAT = Vehicle("Keelboat", cost=[3000, gp], vehicle_type='Water')
LONGSHIP = Vehicle("Longship", cost=[10_000, gp], vehicle_type='Water')
ROWBOAT = Vehicle("Rowboat", cost=[50, gp], vehicle_type='Water')
SAILING_SHIP = Vehicle("Sailing Ship", cost=[10_000, gp], vehicle_type='Water')
WARSHIP = Vehicle("Warship", cost=[25_000, gp], vehicle_type='Water')

LAND_VEHICLES = makeItemList("vehicle_type", "Land")
WATER_VEHICLES = makeItemList("vehicle_type", "Water")

"""
    WEAPONS
"""
# Simple Melee
CLUB = Weapon("Club", cost=[1, sp], wpn_type='Simple', is_melee = True, category='Weapon')
DAGGER = Weapon("Dagger", cost=[2, gp], wpn_type='Simple', is_melee=True, category='Weapon')
GREATCLUB = Weapon("Greatclub", cost=[2, sp], wpn_type='Simple', is_melee=True, category='Weapon')
HANDAXE = Weapon("Handaxe", cost=[5, gp], wpn_type='Simple', is_melee=True, category='Weapon')
JAVELIN = Weapon("Javelin", cost=[2, gp], wpn_type='Simple', is_melee=True, category='Weapon')
LIGHT_HAMMER = Weapon("Light Hammer", cost=[2, gp], wpn_type='Simple', is_melee=True, category='Weapon')
MACE = Weapon("Mace", cost=[5, gp], wpn_type='Simple', is_melee=True, category='Weapon')
QUARTERSTAFF = Weapon("Quarterstaff", cost=[2, sp], wpn_type='Simple', is_melee=True, category='Weapon')
SICKLE = Weapon("Sickle", cost=[1, gp], wpn_type='Simple', is_melee=True, category='Weapon')
SPEAR = Weapon("Spear", cost=[1, gp], wpn_type='Simple', is_melee=True, category='Weapon')
# Simple Ranged
LIGHT_CROSSBOW = Weapon("Light Crossbow", cost=[25, gp], wpn_type='Simple', is_melee=False, category='Weapon')
DART = Weapon("Dart", cost=[5, cp], wpn_type='Simple', is_melee=False, category='Weapon')
SHORTBOW = Weapon("Shortbow", cost=[25, gp], wpn_type='Simple', is_melee=False, category='Weapon')
SLING = Weapon("Sling", cost=[1, sp], wpn_type='Simple', is_melee=False, category='Weapon')
# Martial Melee
BATTLEAXE = Weapon("Battleaxe", cost=[10, gp], wpn_type='Martial', is_melee=True, category='Weapon')
FLAIL = Weapon("Flail", cost=[10, gp], wpn_type='Martial', is_melee=True, category='Weapon')
GLAIVE = Weapon("Glaive", cost=[20, gp], wpn_type='Martial', is_melee=True, category='Weapon')
GREATAXE = Weapon("Greataxe", cost=[30, gp], wpn_type='Martial', is_melee=True, category='Weapon')
GREATSWORD = Weapon("Greatsword", cost=[50, gp], wpn_type='Martial', is_melee=True, category='Weapon')
HALBERD = Weapon("Halberd", cost=[20, gp], wpn_type='Martial', is_melee=True, category='Weapon')
LANCE = Weapon("Lance", cost=[10, gp], wpn_type='Martial', is_melee=True, category='Weapon')
LONGSWORD = Weapon("Longsword", cost=[15, gp], wpn_type='Martial', is_melee=True, category='Weapon')
MAUL = Weapon("Maul", cost=[10, gp], wpn_type='Martial', is_melee=True, category='Weapon')
MORNINGSTAR = Weapon("Morningstar", cost=[15, gp], wpn_type='Martial', is_melee=True, category='Weapon')
PIKE = Weapon("Pike", cost=[5, gp], wpn_type='Martial', is_melee=True, category='Weapon')
RAPIER = Weapon("Rapier", cost=[25, gp], wpn_type='Martial', is_melee=True, category='Weapon')
SCIMITAR = Weapon("Scimitar", cost=[25, gp], wpn_type='Martial', is_melee=True, category='Weapon')
SHORTSWORD = Weapon("Shortsword", cost=[10, gp], wpn_type='Martial', is_melee=True, category='Weapon')
TRIDENT = Weapon("Trident", cost=[5, gp], wpn_type='Martial', is_melee=True, category='Weapon')
WAR_PICK = Weapon("War Pick", cost=[5, gp], wpn_type='Martial', is_melee=True, category='Weapon')
WARHAMMER = Weapon("Warhammer", cost=[15, gp], wpn_type='Martial', is_melee=True, category='Weapon')
WHIP = Weapon("Whip", cost=[2, gp], wpn_type='Martial', is_melee=True, category='Weapon')
# Martial Ranged
BLOWGUN = Weapon("Blowgun", cost=[10, gp], wpn_type='Martial', is_melee=False, category='Weapon')
HAND_CROSSBOW = Weapon("Hand Crossbow", cost=[75, gp], wpn_type='Martial', is_melee=False, category='Weapon')
HEAVY_CROSSBOW = Weapon("Heavy Crossbow", cost=[50, gp], wpn_type='Martial', is_melee=False, category='Weapon')
LONGBOW = Weapon("Longbow", cost=[50, gp], wpn_type='Martial', is_melee=False, category='Weapon')
NET = Weapon("Net", cost=[1, gp], wpn_type='Martial', is_melee=False, category='Weapon')

SIMPLE_WEAPONS = makeItemList("wpn_type", "Simple")
MELEE_SIMPLE_WEAPONS = [wpn for wpn in SIMPLE_WEAPONS if wpn.is_melee == True]
RANGED_SIMPLE_WEAPONS = [wpn for wpn in SIMPLE_WEAPONS if wpn.is_melee == False]
SIMPLE_WEAPONS_PROF = Weapon("Simple Weapons", cost=[0, cp], wpn_type='List', category='Weapon')

MARTIAL_WEAPONS = makeItemList("wpn_type", "Martial")
MELEE_MARTIAL_WEAPONS = [wpn for wpn in MARTIAL_WEAPONS if wpn.is_melee == True]
RANGED_MARTIAL_WEAPONS = [wpn for wpn in MARTIAL_WEAPONS if wpn.is_melee == False]
MARTIAL_WEAPONS_PROF = Weapon("Martial Weapons", cost=[0, cp], wpn_type='List', category='Weapon')

"""
    ARMOR
"""
# LIGHT ARMOR
PADDED = Armor("Padded Armor", cost=[5, gp], arm_type='Light', ac=[11, DEX], category='Armor')
LEATHER_ARMOR = Armor("Leather Armor", cost=[10, gp], arm_type='Light', ac=[11, DEX], category='Armor')
STUDDED_LEATHER_ARMOR = Armor("Studded Leather", cost=[45, gp], arm_type='Light', ac=[12, DEX], category='Armor')
# MEDIUM ARMOR
HIDE = Armor("Hide", cost=[10, gp], arm_type='Medium', ac=[12, DEX], category='Armor')
CHAIN_SHIRT = Armor("Chain Shirt", cost=[50, gp], arm_type='Medium', ac=[13, DEX], category='Armor')
SCALE_MAIL = Armor("Scale Mail", cost=[50, gp], arm_type='Medium', ac=[14, DEX], category='Armor')
BREASTPLATE = Armor("Breastplate", cost=[400, gp], arm_type='Medium', ac=[14, DEX], category='Armor')
HALF_PLATE = Armor("Half Plate", cost=[750, gp], arm_type='Medium', ac=[15, DEX], category='Armor')
# HEAVY ARMOR
RING_MAIL = Armor("Ring Mail", cost=[30, gp], arm_type='Heavy', ac=[14, None], category='Armor')
CHAIN_MAIL = Armor("Chain Mail", cost=[75, gp], arm_type='Heavy', ac=[16, None], category='Armor')
SPLINT = Armor("Splint", cost=[200, gp], arm_type='Heavy', ac=[17, None], category='Armor')
PLATE = Armor("Plate", cost=[1500, gp], arm_type='Heavy', ac=[18, None], category='Armor')
# SHIELD
SHIELD = Armor("Shield", cost=[10, gp], arm_type='Shield', ac=[2, None], category='Armor')

LIGHT_ARMOR = makeItemList("arm_type", "Light")
LIGHT_ARMOR_PROF = Armor("Light Armor", cost=[0, cp], arm_type='Category', ac=None, category='Armor')
MEDIUM_ARMOR = makeItemList("arm_type", "Medium")
MEDIUM_ARMOR_PROF = Armor("Medium Armor", cost=[0, cp], arm_type='Category', ac=None, category='Armor')
HEAVY_ARMOR = makeItemList("arm_type", "Heavy")
HEAVY_ARMOR_PROF = Armor("Heavy Armor", cost=[0, cp], arm_type='Category', ac=None, category='Armor')
SHIELDS = makeItemList("arm_type", "Shield")
ALL_ARMOR = LIGHT_ARMOR + MEDIUM_ARMOR + HEAVY_ARMOR
ALL_ARMOR_PROF = Armor("All Armor", cost=[0, cp], arm_type='Category', ac=None, category='Armor')

"""
    ADVENTURING GEAR
"""
# REGULAR
ABACUS = Item("Abacus", cost=[2, gp], category="Adventuring Gear")
ACID_VIAL = Item("Acid Vial", cost=[25, gp], category="Adventuring Gear")
ALCHEMISTS_FIRE = Item("Alchemists Fire", cost=[50, gp], category="Adventuring Gear")
ANTITOXIN_VIAL = Item("Antitoxin Vial", cost=[50, gp], category="Adventuring Gear")
BACKPACK = Item("Backpack", cost=[2, gp], category="Adventuring Gear")
BALL_BEARINGS = Item("Ball Bearings", cost=[1, gp], quantity=1000, category="Adventuring Gear")
BARREL = Item("Barrel", cost=[2, gp], category="Adventuring Gear")
BASKET = Item("Basket", cost=[4, sp], category="Adventuring Gear")
BEDROLL = Item("Bedroll", cost=[1, gp], category="Adventuring Gear")
BELL = Item("Bell", cost=[1, gp], category="Adventuring Gear")
BLANKET = Item("Blanket", cost=[5, sp], category="Adventuring Gear")
BLOCK_AND_TACKLE = Item("Block and Tackle", cost=[1, gp], category="Adventuring Gear")
BOOK = Item("Book", cost=[25, gp], category="Adventuring Gear")
BOTTLE_GLASS = Item("Bottle Glass", cost=[2, gp], category="Adventuring Gear")
BUCKET = Item("Bucket", cost=[5, cp], category="Adventuring Gear")
CALTROPS = Item("Caltrops", cost=[1, gp], quantity=20, category="Adventuring Gear")
CANDLE = Item("Candle", cost=[1, cp], category="Adventuring Gear")
CASE_CROSSBOW_BOLT = Item("Case Crossbow Bolt", cost=[1, gp], category="Adventuring Gear")
CASE_MAP_SCROLL = Item("Case Map Scroll", cost=[1, gp], category="Adventuring Gear")
CHAIN = Item("Chain", cost=[5, gp], quantity=10, category="Adventuring Gear")
CHALK = Item("Chalk", cost=[1, cp], quantity=1, category="Adventuring Gear")
CHEST = Item("Chest", cost=[5, gp], category="Adventuring Gear")
CLIMBERS_KIT = Item("Climbers Kit", cost=[25, gp], category="Adventuring Gear")
CLOTHES_COMMON = Item("Clothes Common", cost=[5, sp], category="Adventuring Gear")
CLOTHES_COSTUME = Item("Clothes Costume", cost=[5, gp], category="Adventuring Gear")
CLOTHES_FINE = Item("Clothes Fine", cost=[15, gp], category="Adventuring Gear")
CLOTHES_TRAVELERS = Item("Clothes Travelers", cost=[2, gp], category="Adventuring Gear")
COMPONENT_POUCH = Item("Component Pouch", cost=[25, gp], category="Adventuring Gear")
CROWBAR = Item("Crowbar", cost=[2, gp], category="Adventuring Gear")
FISHING_TACKLE = Item("Fishing Tackle", cost=[1, gp], category="Adventuring Gear")
FLASK = Item("Flask", cost=[2, cp], category="Adventuring Gear")
GRAPPING_HOOK = Item("Grapping Hook", cost=[2, gp], category="Adventuring Gear")
HAMMER = Item("Hammer", cost=[1, gp], category="Adventuring Gear")
SLEDGEHAMMER = Item("Sledgehammer", cost=[2, gp], category="Adventuring Gear")
HEALERS_KIT = Item("Healers Kit", cost=[5, gp], category="Adventuring Gear")
HOLY_WATER = Item("Holy Water", cost=[25, gp], category="Adventuring Gear")
HOURGLASS = Item("Hourglass", cost=[25, gp], category="Adventuring Gear")
INK = Item("Ink", cost=[10, gp], quantity=1, category="Adventuring Gear")
INK_PEN = Item("Ink Pen", cost=[2, cp], category="Adventuring Gear")
JUG = Item("Jug", cost=[2, cp], category="Adventuring Gear")
LADDER = Item("Ladder", cost=[1, sp], quantity=10, category="Adventuring Gear")
LAMP = Item("Lamp", cost=[5, sp], category="Adventuring Gear")
LANTURN_BULLSEYE = Item("Lanturn Bullseye", cost=[10, gp], category="Adventuring Gear")
LANTURN_HOODED = Item("Lanturn Hooded", cost=[5, gp], category="Adventuring Gear")
LOCK = Item("Lock", cost=[10, gp], category="Adventuring Gear")
MAGNIFYING_GLASS = Item("Magnifying Glass", cost=[100, gp], category="Adventuring Gear")
MANACLES = Item("Manacles", cost=[2, gp], category="Adventuring Gear")
MESS_KIT = Item("Mess Kit", cost=[2, sp], category="Adventuring Gear")
MIRROR = Item("Mirror", cost=[5, gp], category="Adventuring Gear")
OIL = Item("Oil", cost=[1, sp], category="Adventuring Gear")
PAPER = Item("Paper", cost=[2, sp], quantity=1, category="Adventuring Gear")
PARCHMENT = Item("Parchment", cost=[1, sp], quantity=1, category="Adventuring Gear")
PERFUME = Item("Perfume", cost=[5, gp], category="Adventuring Gear")
PICK = Item("Pick", cost=[2, gp], category="Adventuring Gear")
PITON = Item("Piton", cost=[5, cp], category="Adventuring Gear")
POISON_VIAL = Item("Poison Vial", cost=[100, gp], category="Adventuring Gear")
POLE = Item("Pole", cost=[5, cp], quantity=10, category="Adventuring Gear")
POT = Item("Pot", cost=[2, gp], category="Adventuring Gear")
POTION_OF_HEALING = Item("Potion of Healing", cost=[50, gp], category="Adventuring Gear")
POUCH = Item("Pouch", cost=[5, sp], category="Adventuring Gear")
QUIVER = Item("Quiver", cost=[1, gp], category="Adventuring Gear")
RAM_PORTABLE = Item("Ram Portable", cost=[4, gp], category="Adventuring Gear")
RATIONS = Item("Rations", cost=[5, sp], quantity=1, category="Adventuring Gear")
ROBES = Item("Robes", cost=[1, gp], category="Adventuring Gear")
ROPE_HEMPEN = Item("Rope hempen", cost=[1, gp], quantity=50, category="Adventuring Gear")
ROPE_SILK = Item("Rope Silk", cost=[10, gp], quantity=50, category="Adventuring Gear")
SACK = Item("Sack", cost=[1, cp], category="Adventuring Gear")
SCALE_MERCHANTS = Item("Scale Merchants", cost=[5, gp], category="Adventuring Gear")
SEALING_WAX = Item("Sealing Wax", cost=[5, sp], category="Adventuring Gear")
SHOVEL = Item("Shovel", cost=[2, gp], category="Adventuring Gear")
SIGNAL_WHISTLE = Item("Signal Whistle", cost=[5, cp], category="Adventuring Gear")
SIGNET_RING = Item("Signet Ring", cost=[5, gp], category="Adventuring Gear")
SOAP = Item("Soap", cost=[2, cp], category="Adventuring Gear")
SPELLBOOK = Item("Spellbook", cost=[50, gp], category="Adventuring Gear")
IRON_SPIKES = Item("Iron Spikes", cost=[1, gp], quantity=10, category="Adventuring Gear")
SPYGLASS = Item("Spyglass", cost=[1000, gp], category="Adventuring Gear")
TENT_TWO_PERSON = Item("Tent Two Person", cost=[2, gp], category="Adventuring Gear")
TINDERBOX = Item("Tinderbox", cost=[5, sp], category="Adventuring Gear")
TORCH = Item("Torch", cost=[1, cp], category="Adventuring Gear")
VIAL = Item("Vial", cost=[1, gp], category="Adventuring Gear")
WATERSKIN = Item("Waterskin", cost=[2, sp], category="Adventuring Gear")
WHETSTONE = Item("Whetstone", cost=[1, cp], category="Adventuring Gear")
# AMMUNITION
ARROWS = Item("Arrows", cost=[1, gp], ammunition=True, quantity=20, category="Adventuring Gear")
BLOWGUN_NEEDLES = Item("Blowgun Needles", cost=[1, gp], ammunition=True, quantity=50, category="Adventuring Gear")
CROSSBOW_BOLTS = Item("Crossbow Bolts", cost=[1, gp], ammunition=True, quantity=20, category="Adventuring Gear")
SLING_BULLETS = Item("Sling Bullets", cost=[4, cp], ammunition=True, quantity=20, category="Adventuring Gear")
# ARCANE_FOCUS
CRYSTAL = Item("Crystal", cost=[10, gp], arcane_focus=True, category="Adventuring Gear")
ORB = Item("Orb", cost=[20, gp], arcane_focus=True, category="Adventuring Gear")
ROD = Item("Rod", cost=[10, gp], arcane_focus=True, category="Adventuring Gear")
STAFF = Item("Staff", cost=[5, gp], arcane_focus=True, category="Adventuring Gear")
WAND = Item("Wand", cost=[10, gp], arcane_focus=True, category="Adventuring Gear")
# DRUIDIC_FOCUS
SPRIG_OF_MISTLETOE = Item("Sprig of Mistletoe", cost=[1, gp], druidic_focus=True, category="Adventuring Gear")
TOTEM = Item("Totem", cost=[1, gp], druidic_focus=True, category="Adventuring Gear")
WOODEN_STAFF = Item("Wooden Staff", cost=[5, gp], druidic_focus=True, category="Adventuring Gear")
YEW_WAND = Item("Yew Wand", cost=[100, gp], druidic_focus=True, category="Adventuring Gear")
# HOLY_SYMBOL
AMULET = Item("Amulet", cost=[5, gp], holy_symbol=True, category="Adventuring Gear")
EMBLEM = Item("Emblem", cost=[5, gp], holy_symbol=True, category="Adventuring Gear")
RELIQUARY = Item("Reliquary", cost=[5, gp], holy_symbol=True, category="Adventuring Gear")
# ITEM LISTS
ARCANE_FOCUS = makeItemList("arcane_focus")
DRUIDIC_FOCUS = makeItemList("druidic_focus")
HOLY_SYMBOL = makeItemList("holy_symbol")

"""
    TOOLS
"""
DISGUISE_KIT = Tool("Disguise Kit", cost=[25,gp], category="Tool")
FORGERY_KIT = Tool("Forgery Kit", cost=[15,gp], category="Tool")
HERBALISM_KIT = Tool("Herbalism Kit", cost=[5,gp], category="Tool")
NAVIGATORS_TOOLS = Tool("Navigators Tools", cost=[25,gp], category="Tool")
POISONERS_KIT = Tool("Poisoners Kit", cost=[50,gp], category="Tool")
THIEVES_TOOLS = Tool("Thieves Tools", cost=[25,gp], category="Tool")
# ARTISAN
ALCHEMISTS_SUPPLIES = Tool("Alchemists Supplies", cost=[50, gp], tool_type='Artisan', category="Tool")
BREWERS_SUPPLIES = Tool("Brewers Supplies", cost=[20, gp], tool_type='Artisan', category="Tool")
CALLIGRAPHY_SUPPLIES = Tool("Calligraphy Supplies", cost=[10, gp], tool_type='Artisan', category="Tool")
CARPENTERS_TOOLS = Tool("Carpenters Tools", cost=[8, gp], tool_type='Artisan', category="Tool")
CARTOGRAPHERS_TOOLS = Tool("Cartographers Tools", cost=[15, gp], tool_type='Artisan', category="Tool")
COBBLERS_TOOLS = Tool("Cobblers Tools", cost=[5, gp], tool_type='Artisan', category="Tool")
COOKING_UTENSILS = Tool("Cooking Utensils", cost=[1, gp], tool_type='Artisan', category="Tool")
GLASSBLOWERS_TOOLS = Tool("Glassblowers Tools", cost=[30, gp], tool_type='Artisan', category="Tool")
JEWLERS_TOOLS = Tool("Jewlers Tools", cost=[25, gp], tool_type='Artisan', category="Tool")
LEATHERWORKERS_TOOLS = Tool("Leatherworkers Tools", cost=[5, gp], tool_type='Artisan', category="Tool")
MASONS_TOOLS = Tool("Masons Tools", cost=[10, gp], tool_type='Artisan', category="Tool")
PAINTERS_SUPPLIES = Tool("Painters Supplies", cost=[10, gp], tool_type='Artisan', category="Tool")
SMITHS_TOOLS = Tool("Smiths Tools", cost=[10, gp], tool_type='Artisan', category="Tool")
TINKERS_TOOLS = Tool("Tinkers Tools", cost=[50, gp], tool_type='Artisan', category="Tool")
WEAVERS_TOOLS = Tool("Weavers Tools", cost=[1, gp], tool_type='Artisan', category="Tool")
WOODCARVERS_TOOLS = Tool("Woodcarvers Tools", cost=[1, gp], tool_type='Artisan', category="Tool")
# GAMING
DICE_SET = Tool("Dice Set", cost=[1,sp], tool_type='Gaming', category="Tool")
DRAGONCHESS_SET = Tool("Dragonchess Set", cost=[1,gp], tool_type='Gaming', category="Tool")
PLAYING_CARD_SET = Tool("Playing Card Set", cost=[5,gp], tool_type='Gaming', category="Tool")
THREE_DRAGON_ANTE_SET = Tool("Three Dragon Ante Set", cost=[1,gp], tool_type='Gaming', category="Tool")
# INSTRUMENT
BAGPIPES = Tool("Bagpipes", cost=[30, gp], tool_type='Instrument', category="Tool")
DRUM = Tool("Drum", cost=[6, gp], tool_type='Instrument', category="Tool")
DULCIMER = Tool("Dulcimer", cost=[25, gp], tool_type='Instrument', category="Tool")
FLUTE = Tool("Flute", cost=[2, gp], tool_type='Instrument', category="Tool")
LUTE = Tool("Lute", cost=[35, gp], tool_type='Instrument', category="Tool")
LYRE = Tool("Lyre", cost=[30, gp], tool_type='Instrument', category="Tool")
HORN = Tool("Horn", cost=[3, gp], tool_type='Instrument', category="Tool")
PAN_FLUTE = Tool("Pan Flute", cost=[12, gp], tool_type='Instrument', category="Tool")
SHAWM = Tool("Shawm", cost=[2, gp], tool_type='Instrument', category="Tool")
VIOL = Tool("Viol", cost=[30, gp], tool_type='Instrument', category="Tool")
# TOOL LISTS
ARTISAN_TOOLS = makeItemList("tool_type", "Artisan")
MUSICAL_INSTRUMENT = makeItemList("tool_type", "Instrument")
GAMING_TOOLS = makeItemList("tool_type", "Gaming")
TOOLS = makeItemList("category", "Tool")

"""
    MISC ITEMS
"""
ALMS_BOX = Item("Alms Box")
CENSER = Item("Censer")
BLOCK_OF_INCENSE = Item("Block of Incense")
BAG_OF_SAND = Item("Bag of Sand")

"""
    BACKGROUND SPECIFIC GEAR
"""
# ACOLYTE
PRAYER_BOOK = Item("Prayer Book", background='Acolyte')
PRAYER_WHEEL = Item("Prayer Wheel", background='Acolyte')
STICKS_OF_INCENSE = Item("Sticks of Incense", quantity=5, background='Acolyte')
VESTMENTS = Item("Vestments", background='Acolyte')
# CHARLATAN
STOPPERED_BOTTLES = Item("Stoppered Bottles", background='Charlatan')
WEIGHTED_DICE = Item("Weighted Dice", background='Charlatan')
DECK_OF_MARKED_CARDS = Item("Deck of Marked Cards", background='Charlatan')
SIGNET_RING_OF_IMAGINARY_DUKE = Item("Signet Ring of Imaginary Duke", background='Charlatan')
CHARLATAN_ITEMS = makeItemList("background", "Charlatan")
# Criminal
DARK_HOOD = Item("Dark Hood", background='Criminal')
# Entertainer
LOVE_LETTER = Item("Love Letter", background='Entertainer')
LOCK_OF_HAIR = Item("Lock of Hair", background='Entertainer')
ADMIRER_TRINKET = Item("Admirer Trinket", background='Entertainer')
ENTERTAINER_ITEMS = makeItemList("background", 'Entertainer')
# GUILD_ARTISAN
LETTER_OF_INTRODUCTION = Item("Letter of Introduction", background='Guild Artisan')
# NOBLE
SCROLL_OF_PEDIGREE = Item("Scroll of Pedigree", background='Noble')
# OUTLANDER
HUNTING_TRAP = Item("Hunting Trap", background='Outlander')
ANIMAL_TROPHY = Item("Animal Trophy", background='Outlander')
# SAGE
QUILL = Item("Quill", background='Sage')
LETTER_FROM_DEAD_COLLEAGUE = Item("Letter from Dead Colleague", background='Sage')
# SAILOR
BELAYING_PIN = Item("Belaying Pin", background='Sailor')
LUCKY_CHARM = Item("Lucky Charm", background='Sailor')
# SOLDIER
INSIGNIA_OF_RANK = Item("Insignia of Rank", background='Solider')
TROPHY_FROM_FALLEN_ENEMY = Item("Trophy from Fallen Enemy", background='Solider')
BONE_DICE = Item("Bone Dice", background='Solider')
DECK_OF_CARDS = Item("Deck of Cards", background='Solider')
# URCHIN
SMALL_KNIFE = Item("Small Knife", background='Urchin')
MAP_OF_HOMETOWN = Item("Map of Hometown", background='Urchin')
PET_MOUSE = Item("Pet Mouse", background='Urchin')
PARENTAL_TOKEN_OF_REMEMBERANCE = Item("Parental Token of Rememberance", background='Urchin')
# Shit uhhh
VEHICLES_WATER = Item("Water Vehicles")
VEHICLES_LAND = Item("Land Vehicles")

"""
    ITEM PACKS
"""
BURGLURS_PACK = [BACKPACK, BALL_BEARINGS, BELL] + [CANDLE for _ in range(5)] + [CROWBAR, HAMMER, LANTURN_HOODED, WATERSKIN, ROPE_HEMPEN] + [PITON for _ in range(10)]
DIPLOMATS_PACK = [CHEST, CASE_MAP_SCROLL, CASE_MAP_SCROLL, CLOTHES_FINE, INK, INK_PEN, LAMP, FLASK, FLASK] + [PAPER for _ in range(5)] + [PERFUME, SEALING_WAX, SOAP]
DUNGEONEERS_PACK = [BACKPACK, CROWBAR, HAMMER] + [PITON for _ in range(10)] + [TORCH for _ in range(10)] + [RATIONS for _ in range(10)] + [TINDERBOX, WATERSKIN, ROPE_HEMPEN]
ENTERTAINERS_PACK = [BACKPACK, BEDROLL] + [CLOTHES_COSTUME for _ in range(2)] + [CANDLE for _ in range(5)] + [RATIONS for _ in range(5)] + [WATERSKIN, DISGUISE_KIT]
EXPLORERS_PACK = [BACKPACK, BEDROLL, MESS_KIT, TINDERBOX] + [TORCH for _ in range(10)] + [RATIONS for _ in range(10)] + [WATERSKIN, ROPE_HEMPEN]
PRIESTS_PACK = [BACKPACK, BLANKET] + [CANDLE for _ in range(10)] + [TINDERBOX, ALMS_BOX, CENSER, VESTMENTS, WATERSKIN, ROPE_HEMPEN] + [RATIONS for _ in range(2)] + [BLOCK_OF_INCENSE for _ in range(2)]
SCHOLARS_PACK = [BACKPACK, BOOK, INK, INK_PEN, SMALL_KNIFE, BAG_OF_SAND] + [PARCHMENT for _ in range(10)]

"""
    BACKGROUND
"""
ACOLYTE = Background("Acolyte", skill_profs=[INSIGHT, RELIGION], tool_profs=[], language=[{'Choose 2': Language.items}], equipment=[{'Choose 1': HOLY_SYMBOL}, {'Choose 1': [PRAYER_BOOK, PRAYER_WHEEL]}, VESTMENTS, CLOTHES_COMMON], money=[15, gp])
CHARLATAN = Background("Charlatan", skill_profs=[DECEPTION, SLEIGHT_OF_HAND], tool_profs=[DISGUISE_KIT, FORGERY_KIT], equipment=[CLOTHES_FINE, DISGUISE_KIT, {'Choose 1': CHARLATAN_ITEMS}], money=[15, gp])
CRIMINAL = Background("Criminal", skill_profs=[DECEPTION, STEALTH], tool_profs=[{'Choose 1': GAMING_TOOLS}, THIEVES_TOOLS], equipment=[CROWBAR, CLOTHES_COMMON, DARK_HOOD], money=[15, gp])
ENTERTAINER = Background("Entertainer", skill_profs=[ACROBATICS, PERFORMANCE], tool_profs=[DISGUISE_KIT, {'Choose 1': MUSICAL_INSTRUMENT}], equipment=[{'Choose 1': MUSICAL_INSTRUMENT}, {'Choose 1': ENTERTAINER_ITEMS}, CLOTHES_COSTUME], money=[15, gp])
FOLK_HERO = Background("Folk Hero", skill_profs=[ANIMAL_HANDLING, SURVIVAL], tool_profs=[{'Choose 1': ARTISAN_TOOLS}, ("TODO: VEHICLES")], equipment=[{'Choose 1': ARTISAN_TOOLS}, SHOVEL, POT, CLOTHES_COMMON], money=[10, gp])
GUILD_ARTISAN = Background("Guild Artisan", skill_profs=[INSIGHT, PERSUASION], tool_profs=[{'Choose 1': ARTISAN_TOOLS}], language=[{'Choose 1': Language.items}], equipment=[{'Choose 1': ARTISAN_TOOLS}, LETTER_OF_INTRODUCTION, CLOTHES_TRAVELERS], money=[15, gp])
HERMIT = Background("Hermit", skill_profs=[MEDICINE, RELIGION], tool_profs=[HERBALISM_KIT], language=[{'Choose 1': Language.items}], equipment=[CASE_MAP_SCROLL, BLANKET, CLOTHES_COMMON, HERBALISM_KIT], money=[5, gp])
NOBLE = Background("Noble", skill_profs=[HISTORY, PERSUASION], tool_profs=[{'Choose 1': GAMING_TOOLS}], language=[{'Choose 1': Language.items}], equipment=[CLOTHES_FINE, SIGNET_RING, SCROLL_OF_PEDIGREE], money=[25, gp])
OUTLANDER = Background("Outlander", skill_profs=[ATHLETICS, SURVIVAL], tool_profs=[{'Choose 1': MUSICAL_INSTRUMENT}], language=[{'Choose 1': Language.items}], equipment=[STAFF, HUNTING_TRAP, ANIMAL_TROPHY], money=[10, gp])
SAGE = Background("Sage", skill_profs=[ARCANA, HISTORY], tool_profs=[], language=[{'Choose 2': Language.items}], equipment=[INK, QUILL, LETTER_FROM_DEAD_COLLEAGUE], money=[10, gp])
SAILOR = Background("Sailor", skill_profs=[ATHLETICS, PERCEPTION], tool_profs=[NAVIGATORS_TOOLS, VEHICLES_WATER], equipment=[BELAYING_PIN, LUCKY_CHARM, CLOTHES_COMMON], money=[10, gp])
SOLDIER = Background("Soldier", skill_profs=[ATHLETICS, INTIMIDATION], tool_profs=[{'Choose 1': GAMING_TOOLS}, VEHICLES_LAND], equipment=[INSIGNIA_OF_RANK, TROPHY_FROM_FALLEN_ENEMY, {'Choose 1': [BONE_DICE, DECK_OF_CARDS]}], money=[10, gp])
URCHIN = Background("Urchin", skill_profs=[SLEIGHT_OF_HAND, STEALTH], tool_profs=[DISGUISE_KIT, THIEVES_TOOLS], equipment=[SMALL_KNIFE, MAP_OF_HOMETOWN, PET_MOUSE, PARENTAL_TOKEN_OF_REMEMBERANCE, CLOTHES_COMMON], money=[10, gp])




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

BARBARIAN.proficiencies = { 'Armor': [LIGHT_ARMOR_PROF, MEDIUM_ARMOR_PROF, SHIELDS], 'Weapons': [SIMPLE_WEAPONS_PROF, MARTIAL_WEAPONS_PROF], 'Tools': None }
BARBARIAN.saving_throws = [STR, CON]
BARBARIAN.skills = {'Choose 2': [ANIMAL_HANDLING, ATHLETICS, INTIMIDATION, NATURE, PERCEPTION, SURVIVAL]}
BARBARIAN.hit_dice = "1d12"
BARBARIAN.initial_health = [12, CON.modifier]
BARBARIAN.starting_money = ["2d4", 10, gp]
BARBARIAN.equipment = [ {'Choose 1': [GREATAXE, {'Choose 1': MARTIAL_WEAPONS}]}, {'Choose 1': [(HANDAXE, HANDAXE), {'Choose 1': SIMPLE_WEAPONS}]}, JAVELIN, JAVELIN, JAVELIN, JAVELIN]
BARBARIAN.equipment_pack = EXPLORERS_PACK


BARD.proficiencies = { 'Armor': [LIGHT_ARMOR_PROF], 'Weapons': [SIMPLE_WEAPONS_PROF, HAND_CROSSBOW, LONGSWORD, RAPIER, SHORTSWORD], 'Tools': {'Choose 3': MUSICAL_INSTRUMENT} }
BARD.saving_throws = [DEX, CHA]
BARD.skills = {'Choose 3': SKILLS}
BARD.hit_dice = "1d6"
BARD.initial_health = [8, CON.modifier]
BARD.starting_money = ["5d4", 10, gp]
BARD.equipment = [ {'Choose 1': [RAPIER, LONGSWORD, {'Choose 1': SIMPLE_WEAPONS}]}, {'Choose 1': [LUTE, {'Choose 1': MUSICAL_INSTRUMENT}]}, LEATHER_ARMOR, DAGGER ]
BARD.equipment_pack = {'Choose 1': [DIPLOMATS_PACK, ENTERTAINERS_PACK]},

CLERIC.proficiencies = { 'Armor': [LIGHT_ARMOR_PROF, MEDIUM_ARMOR_PROF, SHIELDS], 'Weapons': [SIMPLE_WEAPONS_PROF], 'Tools': None }
CLERIC.saving_throws = [WIS, CHA]
CLERIC.skills = {'Choose 2': [HISTORY, INSIGHT, MEDICINE, PERSUASION, RELIGION]}
CLERIC.hit_dice = "1d8"
CLERIC.initial_health = [8, CON.modifier]
CLERIC.starting_money = ["5d4", 10, gp]
CLERIC.equipment = [ {'Choose 1': [MACE, WARHAMMER]}, {'Choose 1': [SCALE_MAIL, LEATHER_ARMOR, CHAIN_MAIL]}, {'Choose 1': [[LIGHT_CROSSBOW, CROSSBOW_BOLTS], {'Choose 1': SIMPLE_WEAPONS}]}, SHIELD, {'Choose 1': HOLY_SYMBOL} ]
CLERIC.equipment_pack = {'Choose 1': [PRIESTS_PACK, EXPLORERS_PACK]}

DRUID.proficiencies = { 'Armor': [LIGHT_ARMOR_PROF, MEDIUM_ARMOR_PROF, SHIELDS], 'Weapons': [CLUB, DAGGER, DART, JAVELIN, MACE, QUARTERSTAFF, SCIMITAR, SICKLE, SLING, SPEAR], 'Tools': {'Has': [HERBALISM_KIT]} }
DRUID.saving_throws = [INT, WIS]
DRUID.skills = {'Choose 2': [ARCANA, ANIMAL_HANDLING, INSIGHT, MEDICINE, NATURE, PERCEPTION, RELIGION, SURVIVAL]}
DRUID.hit_dice = "1d8"
DRUID.initial_health = [8, CON.modifier]
DRUID.starting_money = ["2d4", 10, gp]
DRUID.equipment = [ {'Choose 1': [SHIELD, {'Choose 1': SIMPLE_WEAPONS}]}, {'Choose 1': [SCIMITAR, {'Choose 1': MELEE_SIMPLE_WEAPONS}]}, LEATHER_ARMOR, {'Choose 1': DRUIDIC_FOCUS} ]
DRUID.equipment_pack = EXPLORERS_PACK

FIGHTER.proficiencies = { 'Armor': [ALL_ARMOR_PROF, SHIELDS], 'Weapons': [SIMPLE_WEAPONS_PROF, MARTIAL_WEAPONS_PROF], 'Tools': None }
FIGHTER.saving_throws = [STR, CON]
FIGHTER.skills = {'Choose 2': [ACROBATICS, ANIMAL_HANDLING, ATHLETICS, HISTORY, INSIGHT, INTIMIDATION, PERCEPTION, SURVIVAL]}
FIGHTER.hit_dice = "1d10"
FIGHTER.initial_health = [10, CON.modifier]
FIGHTER.starting_money = ["5d4", 10, gp]
FIGHTER.equipment = [ {'Choose 1': [CHAIN_MAIL, (LEATHER_ARMOR, LONGBOW, ARROWS)]}, {'Choose 1': MARTIAL_WEAPONS}, {'Choose 1': [MARTIAL_WEAPONS, SHIELD]}, {'Choose 1': [(LIGHT_CROSSBOW, CROSSBOW_BOLTS), (HANDAXE, HANDAXE)]}]
FIGHTER.equipment_pack = {'Choose 1': [DUNGEONEERS_PACK, EXPLORERS_PACK]}

MONK.proficiencies = { 'Armor': None, 'Weapons': [SIMPLE_WEAPONS_PROF, SHORTSWORD], 'Tools': {'Choose 1': MUSICAL_INSTRUMENT + ARTISAN_TOOLS} }
MONK.saving_throws = [STR, DEX]
MONK.skills = {'Choose 2': [ACROBATICS, ATHLETICS, HISTORY, INSIGHT, RELIGION, STEALTH]}
MONK.hit_dice = "1d8"
MONK.initial_health = [8, CON.modifier]
MONK.starting_money = ["5d4", 1, gp]
MONK.equipment = [{'Choose 1': [SHORTSWORD, {'Choose 1':SIMPLE_WEAPONS}]}] + [DART for _ in range(10)]
MONK.equipment_pack = {'Choose 1': [EXPLORERS_PACK, DUNGEONEERS_PACK]}

PALADIN.proficiencies = { 'Armor': [ALL_ARMOR_PROF, SHIELDS], 'Weapons': [SIMPLE_WEAPONS_PROF, MARTIAL_WEAPONS_PROF], 'Tools': None }
PALADIN.saving_throws = [WIS, CHA]
PALADIN.skills = {'Choose 2': [ATHLETICS, INSIGHT, INTIMIDATION, MEDICINE, PERSUASION, RELIGION]}
PALADIN.hit_dice = "1d10"
PALADIN.initial_health = [10, CON.modifier]
PALADIN.starting_money = ["5d4", 10, gp]
PALADIN.equipment = [ {'Choose 1': [ [{'Choose 1': MARTIAL_WEAPONS}, SHIELD], [{'Choose 1': MARTIAL_WEAPONS}, {'Choose 1': MARTIAL_WEAPONS}] ]}, {'Choose 1': [ [JAVELIN for _ in range(5)], {'Choose 1': MELEE_SIMPLE_WEAPONS} ]}, CHAIN_MAIL, {'Choose 1': HOLY_SYMBOL} ]
PALADIN.equipment_pack = {'Choose 1': [PRIESTS_PACK, EXPLORERS_PACK]}

RANGER.proficiencies = { 'Armor': [LIGHT_ARMOR_PROF, MEDIUM_ARMOR_PROF, SHIELDS], 'Weapons': [SIMPLE_WEAPONS_PROF, MARTIAL_WEAPONS_PROF], 'Tools': None }
RANGER.saving_throws = [STR, DEX]
RANGER.skills = {'Choose 3': [ANIMAL_HANDLING, ATHLETICS, INSIGHT, INVESTIGATION, NATURE, PERCEPTION, STEALTH, SURVIVAL]}
RANGER.hit_dice = "1d10"
RANGER.initial_health = [10, CON.modifier]
RANGER.starting_money = ["5d4", 10, gp]
RANGER.equipment = [ {'Choose 1': [LEATHER_ARMOR, SCALE_MAIL]}, {'Choose 1': [[SHORTSWORD, SHORTSWORD], {'Choose 2': MELEE_SIMPLE_WEAPONS}]}, LONGBOW, QUIVER, ARROWS ] 
RANGER.equipment_pack = {'Choose 1': [DUNGEONEERS_PACK, EXPLORERS_PACK]}

ROGUE.proficiencies = { 'Armor': [LIGHT_ARMOR_PROF], 'Weapons': [SIMPLE_WEAPONS_PROF, HAND_CROSSBOW], 'Tools': {'Has': [THIEVES_TOOLS]} }
ROGUE.saving_throws = [DEX, INT]
ROGUE.skills = {'Choose 4': [ACROBATICS, ATHLETICS, DECEPTION, INSIGHT, INTIMIDATION, INVESTIGATION, PERCEPTION, PERFORMANCE, PERSUASION, SLEIGHT_OF_HAND, STEALTH]}
ROGUE.hit_dice = "1d8"
ROGUE.initial_health = [8, CON.modifier]
ROGUE.starting_money = ["4d4", 10, gp]
ROGUE.equipment = [ {'Choose 1': [RAPIER, SHORTSWORD]}, {'Choose 1': [[SHORTBOW, QUIVER, ARROWS], SHORTSWORD]}, LEATHER_ARMOR, DAGGER, DAGGER, THIEVES_TOOLS ]
ROGUE.equipment_pack = {'Choose 1': [BURGLURS_PACK, DUNGEONEERS_PACK, EXPLORERS_PACK]}

SORCERER.proficiencies = { 'Armor': None, 'Weapons': [DAGGER, DART, SLING, QUARTERSTAFF, LIGHT_CROSSBOW], 'Tools': None }
SORCERER.saving_throws = [CON, CHA]
SORCERER.skills = {'Choose 2': [ARCANA, DECEPTION, INSIGHT, INTIMIDATION, PERSUASION, RELIGION]}
SORCERER.hit_dice = "1d6"
SORCERER.initial_health = [6, CON.modifier]
SORCERER.starting_money = ["3d4", 10, gp]
SORCERER.equipment = [ {'Choose 1': [[LIGHT_CROSSBOW, CROSSBOW_BOLTS], {'Choose 1': SIMPLE_WEAPONS}]}, {'Choose 1': [COMPONENT_POUCH, {'Choose 1': ARCANE_FOCUS}]}, DAGGER, DAGGER ]
SORCERER.equipment_pack = {'Choose 1': [DUNGEONEERS_PACK, EXPLORERS_PACK]}

WARLOCK.proficiencies = { 'Armor': [LIGHT_ARMOR_PROF], 'Weapons': [SIMPLE_WEAPONS_PROF], 'Tools': None }
WARLOCK.saving_throws = [WIS, CHA]
WARLOCK.skills = {'Choose 2': [ARCANA, DECEPTION, HISTORY, INTIMIDATION, INVESTIGATION, NATURE, RELIGION]}
WARLOCK.hit_dice = "1d8"
WARLOCK.initial_health = [8, CON.modifier]
WARLOCK.starting_money = ["4d4", 10, gp]
WARLOCK.equipment = [ {'Choose 1': [[LIGHT_CROSSBOW, CROSSBOW_BOLTS], {'Choose 1': SIMPLE_WEAPONS}]}, {'Choose 1': [COMPONENT_POUCH, {'Choose 1': ARCANE_FOCUS}]}, DAGGER, DAGGER, LEATHER_ARMOR, {'Choose 1': SIMPLE_WEAPONS} ]
WARLOCK.equipment_pack = {'Choose 1': [SCHOLARS_PACK, DUNGEONEERS_PACK]}

WIZARD.proficiencies = { 'Armor': None, 'Weapons': [DAGGER, DART, SLING, QUARTERSTAFF, LIGHT_CROSSBOW], 'Tools': None }
WIZARD.saving_throws = [INT, WIS]
WIZARD.skills = {'Choose 2': [ARCANA, HISTORY, INSIGHT, INVESTIGATION, MEDICINE, RELIGION]}
WIZARD.hit_dice = "1d6"
WIZARD.initial_health = [6, CON.modifier]
WIZARD.starting_money = ["4d4", 10, gp]
WIZARD.equipment = [ {'Choose 1': [QUARTERSTAFF, DAGGER]}, {'Choose 1': [COMPONENT_POUCH, {'Choose 1': ARCANE_FOCUS}]}, SPELLBOOK ]
WIZARD.equipment_pack = {'Choose 1': [SCHOLARS_PACK, EXPLORERS_PACK]}

CLASSES = [BARBARIAN, BARD, CLERIC, DRUID, FIGHTER, MONK, PALADIN, RANGER, ROGUE, SORCERER, WARLOCK, WIZARD]

"""
    CLASS MECHANICS
This contains all class abilities and other generative choices specific to one's class at level one
"""
# FIGHTER
FIGHTINGSTYLE_ARCHERY = _ClassMechanic("Archery", _class=FIGHTER)
FIGHTINGSTYLE_DEFENCE = _ClassMechanic("Defence", _class=FIGHTER)
FIGHTINGSTYLE_DUELING = _ClassMechanic("Dueling", _class=FIGHTER)
FIGHTINGSTYLE_GREAT_WEAPON_FIGHTING = _ClassMechanic("Great Weapon Fighting", _class=FIGHTER)
FIGHTINGSTYLE_PROTECTION = _ClassMechanic("Protection", _class=FIGHTER)
FIGHTINGSTYLE_TWO_WEAPON_FIGHTING = _ClassMechanic("Two Weapon Fighting", _class=FIGHTER)

"""
    SUBCLASSES
"""
# BARBARIAN
PATH_OF_THE_BESERKER = _SubClass("Path of the Beserker", _class=BARBARIAN)
PATH_OF_THE_TOTEM_WARRIOR = _SubClass("Path of the Totem Warrior", _class=BARBARIAN)
PATH_OF_THE_ZEALOT = _SubClass("Path of the Zealot", _class=BARBARIAN, xanathar=True)
PATH_OF_THE_ANCESTRAL_GUARDIAN = _SubClass("Path of the Ancestral Guardian", _class=BARBARIAN, xanathar=True)
PATH_OF_THE_STORM_HERALD = _SubClass("Path of the Storm Herald", _class=BARBARIAN, xanathar=True)
PATH_OF_THE_BEAST = _SubClass("Path of the Beast", _class=BARBARIAN, tasha=True)
PATH_OF_WILD_MAGIC = _SubClass("Path of Wild Magic", _class=BARBARIAN, tasha=True)
# BARD
COLLEGE_OF_LORE = _SubClass("College of Lore", _class=BARD)
COLLEGE_OF_VALOR = _SubClass("College of Valor", _class=BARD)
COLLEGE_OF_GLAMOUR = _SubClass("College of Glamour", _class=BARD, xanathar=True)
COLLEGE_OF_SWORDS = _SubClass("College of Swords", _class=BARD, xanathar=True)
COLLEGE_OF_WHISPERS = _SubClass("College of Whispers", _class=BARD, xanathar=True)
COLLEGE_OF_CREATION = _SubClass("College of Creation", _class=BARD, tasha=True)
COLLEGE_OF_ELOQUENCE = _SubClass("College of Eloquence", _class=BARD, tasha=True)
# CLERIC
KNOWLEDGE_DOMAIN = _SubClass("Knowledge Domain", _class=CLERIC)
LIFE_DOMAIN = _SubClass("Life Domain", _class=CLERIC)
LIGHT_DOMAIN = _SubClass("Light Domain", _class=CLERIC)
NATURE_DOMAIN = _SubClass("Nature Domain", _class=CLERIC)
TEMPEST_DOMAIN = _SubClass("Tempest Domain", _class=CLERIC)
TRICKERY_DOMAIN = _SubClass("Trickery Domain", _class=CLERIC)
WAR_DOMAIN = _SubClass("War Domain", _class=CLERIC)
FORGE_DOMAIN = _SubClass("Forge Domain", _class=CLERIC, xanathar=True)
GRAVE_DOMAIN = _SubClass("Grave Domain", _class=CLERIC, xanathar=True)
ORDER_DOMAIN = _SubClass("Order Domain", _class=CLERIC, ravnica=True, tasha=True)
PEACE_DOMAIN = _SubClass("Peace Domain", _class=CLERIC, tasha=True)
TWILIGHT_DOMAIN = _SubClass("Twilight Domain", _class=CLERIC, tasha=True)
# DRUID
CIRCLE_OF_THE_LAND = _SubClass("Circle of the Land", _class=DRUID)
CIRCLE_OF_THE_MOON = _SubClass("Circle of the Moon", _class=DRUID)
CIRCLE_OF_DREAMS = _SubClass("Circle of Dreams", _class=DRUID, xanathar=True)
CIRCLE_OF_THE_SHEPHERD = _SubClass("Circle of the Shepherd", _class=DRUID, xanathar=True)
CIRCLE_OF_SPORES = _SubClass("Circle of Spores", _class=DRUID, ravnica=True, tasha=True)
CIRCLE_OF_STARS = _SubClass("Circle of Stars", _class=DRUID, tasha=True)
CIRCLE_OF_WILDFIRE = _SubClass("Circle of Wildfire", _class=DRUID, tasha=True)
# FIGHTER 
BATTLE_MASTER = _SubClass("Battle Master", _class=FIGHTER)
CHAMPTION = _SubClass("Chamption", _class=FIGHTER)
ELDRITCH_KNIGHT = _SubClass("Eldritch Knight", _class=FIGHTER)
CAVALIER = _SubClass("Cavalier", _class=FIGHTER, xanathar=True)
ARCANE_ARCHER = _SubClass("Arcane_Archer", _class=FIGHTER, xanathar=True)
SAMURAI = _SubClass("Samurai", _class=FIGHTER, xanathar=True)
PSI_WARRIOR = _SubClass("Psi Warrior", _class=FIGHTER, tasha=True)
RUNE_KNIGHT = _SubClass("Rune Knight", _class=FIGHTER, tasha=True)
# MONK
WAY_OF_SHADOW = _SubClass("Way of Shadow", _class=MONK)
WAY_OF_THE_FOUR_ELEMENTS = _SubClass("Way of the Four Elements", _class=MONK)
WAY_OF_THE_OPEN_HAND = _SubClass("Way of the Open Hand", _class=MONK)
WAY_OF_THE_SUN_SOUL = _SubClass("Way of the Sun Soul", _class=MONK, xanathar=True)
WAY_OF_THE_DRUNKEN_MASTER = _SubClass("Way of the Drunken Master", _class=MONK, xanathar=True)
WAY_OF_THE_KENSEI = _SubClass("Way of the Kensei", _class=MONK, xanathar=True)
WAY_OF_THE_ASCENDANT_DRAGON = _SubClass("Way of the Ascendant Dragon", _class=MONK, fizbans=True)
WAY_OF_MERCY = _SubClass("Way of Mercy", _class=MONK, tasha=True)
WAY_OF_THE_ASTRAL_SELF = _SubClass("Way of the Astral Self", _class=MONK, tasha=True)
# PALADIN
OATH_OF_DEVOTION = _SubClass("Oath of Devotion", _class=PALADIN)
OATH_OF_THE_ANCIENTS = _SubClass("Oath of the Ancients", _class=PALADIN)
OATH_OF_VENGEANCE = _SubClass("Oath of Vengeance", _class=PALADIN)
OATH_OF_CONQUEST = _SubClass("Oath of Conquest", _class=PALADIN, xanathar=True)
OATH_OF_REDEMPTION = _SubClass("Oath of Redemption", _class=PALADIN, xanathar=True)
OATH_OF_GLORY = _SubClass("Oath of Glory", _class=PALADIN, tasha=True)
OATH_OF_THE_WATCHERS = _SubClass("Oath of the Watchers", _class=PALADIN, tasha=True)
# RANGER
BEAST_MASTER = _SubClass("Beast Master", _class=RANGER)
HUNTER = _SubClass("Hunter", _class=RANGER)
GLOOM_STALKER = _SubClass("Gloom Stalker", _class=RANGER, xanathar=True)
HORIZON_WALKER = _SubClass("Horizon Walker", _class=RANGER, xanathar=True)
MONSTER_SLAYER = _SubClass("Monster Slayer", _class=RANGER, xanathar=True)
FEY_WANDERER = _SubClass("Fey Wanderer", _class=RANGER, tasha=True)
SWARMKEEPER = _SubClass("Swarmkeeper", _class=RANGER, tasha=True)
DRAKEWARDEN = _SubClass("Drakewarden", _class=RANGER, fizbans=True)
# ROGUE
ARCANE_TRICKSTER = _SubClass("Arcane Trickster", _class=ROGUE)
ASSASSIN = _SubClass("Assassin", _class=ROGUE)
SCOUT = _SubClass("Scout", _class=ROGUE, xanathar=True)
THIEF = _SubClass("Thief", _class=ROGUE)
INQUISITIVE = _SubClass("Inquisitive", _class=ROGUE, xanathar=True)
MASTERMIND = _SubClass("Mastermind", _class=ROGUE, xanathar=True)
SWASHBUCKLER = _SubClass("Swashbuckler", _class=ROGUE, xanathar=True)
PHANTOM = _SubClass("Phantom", _class=ROGUE, tasha=True)
SOULKNIFE = _SubClass("Soulknife", _class=ROGUE, tasha=True)
# SORCERER
DRACONIC_BLOODLINE = _SubClass("Draconic Bloodline", _class=SORCERER)
WILD_MAGIC = _SubClass("Wild Magic", _class=SORCERER)
DIVINE_SOUL = _SubClass("Divine Soul", _class=SORCERER, xanathar=True)
SHADOW_MAGIC = _SubClass("Shadow Magic", _class=SORCERER, xanathar=True)
STORM_SORCERY = _SubClass("Storm Sorcery", _class=SORCERER, xanathar=True)
ABERRANT_MIND = _SubClass("Aberrant Mind", _class=SORCERER, tasha=True)
CLOCKWORK_SOUL = _SubClass("Clockwork Soul", _class=SORCERER, tasha=True)
# WARLOCK
THE_ARCHFEY = _SubClass("The Archfey", _class=WARLOCK)
THE_FIEND = _SubClass("The Fiend", _class=WARLOCK)
THE_GREAT_OLD_ONE = _SubClass("The Great Old One", _class=WARLOCK)
THE_CELESTIAL = _SubClass("The Celestial", _class=WARLOCK, xanathar=True)
THE_HEXBLADE = _SubClass("The Hexblade", _class=WARLOCK, xanathar=True)
THE_FATHOMLESS = _SubClass("The Fathomless", _class=WARLOCK, tasha=True)
THE_GENIE = _SubClass("The Genie", _class=WARLOCK, tasha=True)
# WIZARD
SCHOOL_OF_ABJURATION = _SubClass("School of Abjuration", _class=WIZARD)
SCHOOL_OF_CONJURATION = _SubClass("School of Conjuration", _class=WIZARD)
SCHOOL_OF_DIVINATION = _SubClass("School of Divination", _class=WIZARD)
SCHOOL_OF_ENCHANTMENT = _SubClass("School of Enchantment", _class=WIZARD)
SCHOOL_OF_EVOCATION = _SubClass("School of Evocation", _class=WIZARD)
SCHOOL_OF_ILLUSION = _SubClass("School of Illusion", _class=WIZARD)
SCHOOL_OF_NECROMANCY = _SubClass("School of Necromancy", _class=WIZARD)
SCHOOL_OF_TRANSMUTATION = _SubClass("School of Transmutation", _class=WIZARD)
WAR_MAGIC = _SubClass("War Magic", _class=WIZARD, xanathar=True)
ORDER_OF_SCRIBES = _SubClass("Order of Scribes", _class=WIZARD, tasha=True)
# ARTIFICER
ALCHEMIST = _SubClass("Alchemist", _class=ARTIFICER, tasha=True)
ARMORER = _SubClass("Armorer", _class=ARTIFICER, tasha=True)
ARTILLERIST = _SubClass("Artillerist", _class=ARTIFICER, tasha=True)
BATTLE_SMITH = _SubClass("Battle_Smith", _class=ARTIFICER, tasha=True)

"""
    RACE MECHANICS
"""
# Dragonborn
DRAGON_ANCESTORY_BLACK = RaceMechanic("Black", category="Dragon Ancestory", dmg_type='Acid')
DRAGON_ANCESTORY_BLUE = RaceMechanic("Blue", category="Dragon Ancestory", dmg_type='Lightning')
DRAGON_ANCESTORY_BRASS = RaceMechanic("Brass", category="Dragon Ancestory", dmg_type='Fire')
DRAGON_ANCESTORY_BRONZE = RaceMechanic("Bronze", category="Dragon Ancestory", dmg_type='Lightning')
DRAGON_ANCESTORY_COPPER = RaceMechanic("Copper", category="Dragon Ancestory", dmg_type='Acid')
DRAGON_ANCESTORY_GOLD = RaceMechanic("Gold", category="Dragon Ancestory", dmg_type='Fire')
DRAGON_ANCESTORY_GREEN = RaceMechanic("Green", category="Dragon Ancestory", dmg_type='Poison')
DRAGON_ANCESTORY_RED = RaceMechanic("Red", category="Dragon Ancestory", dmg_type='Fire')
DRAGON_ANCESTORY_WHITE = RaceMechanic("White", category="Dragon Ancestory", dmg_type='Cold')
DRAGON_ANCESTORY_SILVER = RaceMechanic("Silver", category="Dragon Ancestory", dmg_type='Cold')
DRAGON_ANCESTORIES = [item for item in RaceMechanic.items if item.category=='Dragon Ancestory']

"""
    RACE
"""
DRAGONBORN = Race("Dragonborn", ab_score=[(STR, 2), (CON, 1)], age=[15, 80], alignment=("None", "Good"), size='Medium', speed=30, language=[COMMON, DRACONIC], ancestory={'Choose 1': DRAGON_ANCESTORIES}, traits=['Breath Weapon'])
DWARF = Race("Dwarf", ab_score=[(CON, 2)], age=[50, 350], alignment=("Lawful", "None"), size='Small', speed=25, language=[COMMON, DWARVISH], racial_prof={'Weapon': [BATTLEAXE, HANDAXE, LIGHT_HAMMER, WARHAMMER], 'Tool': {'Choose 1': [SMITHS_TOOLS, BREWERS_SUPPLIES, MASONS_TOOLS]}})
ELF = Race("Elf", ab_score=[(DEX, 2)], age=[100, 750], alignment=("Chaotic", "None"), size='Medium', speed=30, language=[COMMON, ELVISH], racial_prof={'Skill': [PERCEPTION]}, darkvision=60, has_subrace=True)
GNOME = Race("Gnome", ab_score=[(INT, 2)], age=[40, 350], alignment=("None", "Good"), size='Small', speed=25, language=[COMMON, GNOMISH], darkvision=60, has_subrace=True)
HALFLING = Race("Halfling", ab_score=[(DEX, 2)], age=[20, 150], alignment=("Lawful", "Good"), size='Small', speed=25, language=[COMMON, HALFLING], has_subrace=True)
HALF_ELF = Race("Half-Elf", ab_score=[(CHA, 2), {'Choose 2': [STR, DEX, CON, INT, WIS], 'Bonus': 2}], age=[20,180], alignment=('Chaotic', 'None'), size='Medium', speed=30, language=[COMMON, ELVISH, {'Choose 1': [l for l in Language.items if l.name != 'Elvish' or l.name != 'Common']}], darkvision=60, racial_prof={'Skills': {'Choose 2': SKILLS}})
HALF_ORC = Race("Half-Orc", ab_score=[(STR, 2), (CON, 1)], age=[14,75], alignment=('Chaotic', 'Evil'), size='Medium', speed=30, language=[COMMON, ORC], darkvision=60, racial_prof={'Skill': [INTIMIDATION]})
HUMAN = Race("Human", ab_score=[(STR, 1), (DEX, 1), (CON, 1), (INT, 1), (WIS, 1), (CHA, 1)], age=[18,80], alignment=("None", "None"), size='Medium', speed=30, language=[COMMON])
TIEFLING = Race("Tiefling", ab_score=[(INT, 1), (CHA, 2)], age=[18, 75], alignment=('None', 'Evil'), size='Medium', speed=30, language=[COMMON, INFERNAL], thaumaturgy_cantrip=True)
RACES = [DRAGONBORN, DWARF, ELF, GNOME, HALFLING, HALF_ELF, HALF_ORC, HUMAN, TIEFLING]

"""
    SUB RACES
"""
HILL_DWARF = SubRace("Hill_Dwarf", race=DWARF, ab_score=[(WIS, 1)], racial_prof={}, hit_point_increase=1)
MOUNTAIN_DWARF = SubRace("Mountain_Dwarf", race=DWARF, ab_score=[(STR, 2)], racial_prof={'Armor': [LIGHT_ARMOR_PROF, MEDIUM_ARMOR_PROF]})
HIGH_ELF = SubRace("High Elf", race=ELF, ab_score=[(INT, 1)], racial_prof={'Weapon': [LONGSWORD, SHORTSWORD, SHORTBOW, LONGBOW]}, language={'Choose 1': [language for language in Language.items if language not in ELF.language]}, cantrip=True)
WOOD_ELF = SubRace("Wood Elf", race=ELF, ab_score=[(WIS, 1)], racial_prof={'Weapon': [LONGSWORD, SHORTSWORD, SHORTBOW, LONGBOW]}, speed=35)
DARK_ELF = SubRace("Dark Elf", race=ELF, ab_score=[(CHA, 1)], darkvision=120, racial_prof={'Weapon': [RAPIER, SHORTSWORD, HAND_CROSSBOW]})
FOREST_GNOME = SubRace("Forest_Gnome", race=GNOME, ab_score=[(DEX, 1)], racial_prof={}, minor_illusion_cantrip=True)
ROCK_GNOME = SubRace("Rock_Gnome", race=GNOME, ab_score=[(CON, 1)], racial_prof={'Tool': [TINKERS_TOOLS]})
LIGHTFOOT_HALFLING = SubRace("Lightfoot_Halfling", race=HALFLING, ab_score=[(CHA, 1)], racial_prof={})
STOUT_HALFLING = SubRace("Stout_Halfling", race=HALFLING, ab_score=[(CON, 1)], racial_prof={})
SUBRACES=[HILL_DWARF, MOUNTAIN_DWARF, HIGH_ELF, WOOD_ELF, DARK_ELF, FOREST_GNOME, ROCK_GNOME, LIGHTFOOT_HALFLING, STOUT_HALFLING]





    


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
        

    roll_class = MONK 
    tool_prof = getProficiencies(roll_class.proficiencies['Tools'])
    for __class in CLASSES:
        print(__class)
        print(getEquipment(__class.equipment))
