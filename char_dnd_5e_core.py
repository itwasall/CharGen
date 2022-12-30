import random
# random should probably only be used for testing. This file is to store data, not to aide in the processing of a random generation of a character
"""
    What the shit is this?

    This file holds the core shit for DND, such as AbilityScore, Alignment & Class classes so that I won't have to
        rewrite everything should I ever try and make a character generator for another setting set in 5e
"""

def ProficiencyBonus(level):
    return ((level - 1) // 4) + 2

def GetProficiencies(data):

    def RandomiseProficiencies(data, x):
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
            return RandomiseProficiencies(data, 1)
        case 'Choose 2':
            return RandomiseProficiencies(data, 2)
        case 'Choose 3':
            return RandomiseProficiencies(data, 3)
        case 'Choose 4':
            return RandomiseProficiencies(data, 4)
        case 'Has':
            return data['Has']



def MakeItemList(attribute, attr_value=None):
    if attr_value == None:
        return [item for item in Item.items if hasattr(item, attribute)]
    else:
        return [item for item in Item.items if (hasattr(item, attribute) and item.__getattribute__(attribute) == attr_value)]

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

class Background:
    def __init__(self, name, **kwargs):
        self.name = name
        for k, d in kwargs.items():
            self.__setattr__(k, d)

    def __repr__(self):
        return self.name

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
    def __init__(self, name, value):
        super().__init__(name)
        self.value = value

class Weapon(Item):
    def __init__(self, name, cost, wpn_type, **kwargs):
        super().__init__(name)
        self.cost = cost
        self.wpn_type = wpn_type
        for k, d in kwargs.items():
            self.__setattr__(k, d)

class Armor(Item):
    def __init__(self, name, cost, arm_type, ac, **kwargs):
        super().__init__(name)
        self.cost = cost
        self.arm_type = arm_type
        self.ac = ac
        for k, d in kwargs.items():
            self.__setattr__(k, d)

class Tool(Item):
    def __init__(self, name, cost, tool_type=None, **kwargs):
        super().__init__(name)
        self.cost = cost
        self.tool_type = tool_type
        for k, d in kwargs.items():
            self.__setattr__(k, d)

class Vehicle(Item):
    def __init__(self, name, vehicle_type=None, **kwargs):
        super().__init__(name)
        self.vehicle_type = vehicle_type
        for k, d in kwargs.items():
            self.__setattr__(k ,d)



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
    VEHICLES 
"""
# MOUNTS
CAMEL = Vehicle("Camel", cost=[50, gp], speed=50, vehicle_type='Land', subtype='Animal')
DONKEY = Vehicle("Donkey", cost=[8, gp], speed=40, vehicle_type='Land', subtype='Animal')
ELEPHANT = Vehicle("Elephant", cost=[200, gp], speed=40, vehicle_type='Land', subtype='Animal')
HORSE_DRAFT = Vehicle("Horse_Draft", cost=[50, gp], speed=40, vehicle_type='Land', subtype='Animal')
HORSE_RIDING = Vehicle("Horse_Riding", cost=[75, gp], speed=60, vehicle_type='Land', subtype='Animal')
MASTIFF = Vehicle("Mastiff", cost=[25, gp], speed=40, vehicle_type='Land', subtype='Animal')
PONY = Vehicle("Pony", cost=[30, gp], speed=40, vehicle_type='Land', subtype='Animal')
WARHORSE = Vehicle("Warhorse", cost=[400, gp], speed=60, vehicle_type='Land', subtype='Animal')
# DRAWN VEHICLES        
BARDING = Vehicle("Barding", vehicle_type='Land', subtype='Vehicle')
BIT_AND_BRIDLE = Vehicle("Bit_and_Bridle", vehicle_type='Land', subtype='Vehicle')
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
SAILING_SHIP = Vehicle("Sailing_Ship", cost=[10_000, gp], vehicle_type='Water')
WARSHIP = Vehicle("Warship", cost=[25_000, gp], vehicle_type='Water')

LAND_VEHICLES = MakeItemList("vehicle_type", "Land")
WATER_VEHICLES = MakeItemList("vehicle_type", "Water")
"""
    WEAPONS
"""
# Simple Melee
CLUB = Weapon("Club", cost=[1, sp], wpn_type='Simple', is_melee = True, category='Weapon')
DAGGER = Weapon("Dagger", cost=[2, gp], wpn_type='Simple', is_melee=True, category='Weapon')
GREATCLUB = Weapon("Greatclub", cost=[2, sp], wpn_type='Simple', is_melee=True, category='Weapon')
HANDAXE = Weapon("Handaxe", cost=[5, gp], wpn_type='Simple', is_melee=True, category='Weapon')
JAVELIN = Weapon("Javelin", cost=[2, gp], wpn_type='Simple', is_melee=True, category='Weapon')
LIGHT_HAMMER = Weapon("Light_Hammer", cost=[2, gp], wpn_type='Simple', is_melee=True, category='Weapon')
MACE = Weapon("Mace", cost=[5, gp], wpn_type='Simple', is_melee=True, category='Weapon')
QUARTERSTAFF = Weapon("Quarterstaff", cost=[2, sp], wpn_type='Simple', is_melee=True, category='Weapon')
SICKLE = Weapon("Sickle", cost=[1, gp], wpn_type='Simple', is_melee=True, category='Weapon')
SPEAR = Weapon("Spear", cost=[1, gp], wpn_type='Simple', is_melee=True, category='Weapon')
# Simple Ranged
LIGHT_CROSSBOW = Weapon("Light_Crossbow", cost=[25, gp], wpn_type='Simple', is_melee=False, category='Weapon')
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
WAR_PICK = Weapon("War_Pick", cost=[5, gp], wpn_type='Martial', is_melee=True, category='Weapon')
WARHAMMER = Weapon("Warhammer", cost=[15, gp], wpn_type='Martial', is_melee=True, category='Weapon')
WHIP = Weapon("Whip", cost=[2, gp], wpn_type='Martial', is_melee=True, category='Weapon')
# Martial Ranged
BLOWGUN = Weapon("Blowgun", cost=[10, gp], wpn_type='Martial', is_melee=False, category='Weapon')
HAND_CROSSBOW = Weapon("Hand_Crossbow", cost=[75, gp], wpn_type='Martial', is_melee=False, category='Weapon')
HEAVY_CROSSBOW = Weapon("Heavy_Crossbow", cost=[50, gp], wpn_type='Martial', is_melee=False, category='Weapon')
LONGBOW = Weapon("Longbow", cost=[50, gp], wpn_type='Martial', is_melee=False, category='Weapon')
NET = Weapon("Net", cost=[1, gp], wpn_type='Martial', is_melee=False, category='Weapon')

SIMPLE_WEAPONS = MakeItemList("wpn_type", "Simple")
MELEE_SIMPLE_WEAPONS = [wpn for wpn in SIMPLE_WEAPONS if wpn.is_melee == True]
RANGED_SIMPLE_WEAPONS = [wpn for wpn in SIMPLE_WEAPONS if wpn.is_melee == False]

MARTIAL_WEAPONS = MakeItemList("wpn_type", "Martial")
MELEE_MARTIAL_WEAPONS = [wpn for wpn in MARTIAL_WEAPONS if wpn.is_melee == True]
RANGED_MARTIAL_WEAPONS = [wpn for wpn in MARTIAL_WEAPONS if wpn.is_melee == False]

"""
    ARMOR
"""
# LIGHT ARMOR
PADDED = Armor("Padded", cost=[5, gp], arm_type='Light', ac=[11, DEX], category='Armor')
LEATHER_ARMOR = Armor("Leather", cost=[10, gp], arm_type='Light', ac=[11, DEX], category='Armor')
STUDDED_LEATHER_ARMOR = Armor("Studded_Leather", cost=[45, gp], arm_type='Light', ac=[12, DEX], category='Armor')
# MEDIUM ARMOR
HIDE = Armor("Hide", cost=[10, gp], arm_type='Medium', ac=[12, DEX], category='Armor')
CHAIN_SHIRT = Armor("Chain_Shirt", cost=[50, gp], arm_type='Medium', ac=[13, DEX], category='Armor')
SCALE_MAIL = Armor("Scale_Mail", cost=[50, gp], arm_type='Medium', ac=[14, DEX], category='Armor')
BREASTPLATE = Armor("Breastplate", cost=[400, gp], arm_type='Medium', ac=[14, DEX], category='Armor')
HALF_PLATE = Armor("Half_Plate", cost=[750, gp], arm_type='Medium', ac=[15, DEX], category='Armor')
# HEAVY ARMOR
RING_MAIL = Armor("Ring_Mail", cost=[30, gp], arm_type='Heavy', ac=[14, None], category='Armor')
CHAIN_MAIL = Armor("Chain_Mail", cost=[75, gp], arm_type='Heavy', ac=[16, None], category='Armor')
SPLINT = Armor("Splint", cost=[200, gp], arm_type='Heavy', ac=[17, None], category='Armor')
PLATE = Armor("Plate", cost=[1500, gp], arm_type='Heavy', ac=[18, None], category='Armor')
# SHIELD
SHIELD = Armor("Shield", cost=[10, gp], arm_type='Shield', ac=[2, None], category='Armor')

LIGHT_ARMOR = MakeItemList("arm_type", "Light")
MEDIUM_ARMOR = MakeItemList("arm_type", "Medium")
HEAVY_ARMOR = MakeItemList("arm_type", "Heavy")
SHIELDS = MakeItemList("arm_type", "Shield")
ALL_ARMOR = LIGHT_ARMOR + MEDIUM_ARMOR + HEAVY_ARMOR

"""
    ADVENTURING GEAR
"""
# REGULAR
ABACUS = Item("Abacus", cost=[2, gp], category="Adventuring Gear")
ACID_VIAL = Item("Acid_Vial", cost=[25, gp], category="Adventuring Gear")
ALCHEMISTS_FIRE = Item("Alchemists_Fire", cost=[50, gp], category="Adventuring Gear")
ANTITOXIN_VIAL = Item("Antitoxin_Vial", cost=[50, gp], category="Adventuring Gear")
BACKPACK = Item("Backpack", cost=[2, gp], category="Adventuring Gear")
BALL_BEARINGS = Item("Ball_Bearings", cost=[1, gp], quantity=1000, category="Adventuring Gear")
BARREL = Item("Barrel", cost=[2, gp], category="Adventuring Gear")
BASKET = Item("Basket", cost=[4, sp], category="Adventuring Gear")
BEDROLL = Item("Bedroll", cost=[1, gp], category="Adventuring Gear")
BELL = Item("Bell", cost=[1, gp], category="Adventuring Gear")
BLANKET = Item("Blanket", cost=[5, sp], category="Adventuring Gear")
BLOCK_AND_TACKLE = Item("Block_and_Tackle", cost=[1, gp], category="Adventuring Gear")
BOOK = Item("Book", cost=[25, gp], category="Adventuring Gear")
BOTTLE_GLASS = Item("Bottle_Glass", cost=[2, gp], category="Adventuring Gear")
BUCKET = Item("Bucket", cost=[5, cp], category="Adventuring Gear")
CALTROPS = Item("Caltrops", cost=[1, gp], quantity=20, category="Adventuring Gear")
CANDLE = Item("Candle", cost=[1, cp], category="Adventuring Gear")
CASE_CROSSBOW_BOLT = Item("Case_Crossbow_Bolt", cost=[1, gp], category="Adventuring Gear")
CASE_MAP_SCROLL = Item("Case_Map_Scroll", cost=[1, gp], category="Adventuring Gear")
CHAIN = Item("Chain", cost=[5, gp], quantity=10, category="Adventuring Gear")
CHALK = Item("Chalk", cost=[1, cp], quantity=1, category="Adventuring Gear")
CHEST = Item("Chest", cost=[5, gp], category="Adventuring Gear")
CLIMBERS_KIT = Item("Climbers_Kit", cost=[25, gp], category="Adventuring Gear")
CLOTHES_COMMON = Item("Clothes_Common", cost=[5, sp], category="Adventuring Gear")
CLOTHES_COSTUME = Item("Clothes_Costume", cost=[5, gp], category="Adventuring Gear")
CLOTHES_FINE = Item("Clothes_Fine", cost=[15, gp], category="Adventuring Gear")
CLOTHES_TRAVELERS = Item("Clothes_Travelers", cost=[2, gp], category="Adventuring Gear")
COMPONENT_POUCH = Item("Component_Pouch", cost=[25, gp], category="Adventuring Gear")
CROWBAR = Item("Crowbar", cost=[2, gp], category="Adventuring Gear")
FISHING_TACKLE = Item("Fishing_Tackle", cost=[1, gp], category="Adventuring Gear")
FLASK = Item("Flask", cost=[2, cp], category="Adventuring Gear")
GRAPPING_HOOK = Item("Grapping_Hook", cost=[2, gp], category="Adventuring Gear")
HAMMER = Item("Hammer", cost=[1, gp], category="Adventuring Gear")
SLEDGEHAMMER = Item("Sledgehammer", cost=[2, gp], category="Adventuring Gear")
HEALERS_KIT = Item("Healers_Kit", cost=[5, gp], category="Adventuring Gear")
HOLY_WATER = Item("Holy_Water", cost=[25, gp], category="Adventuring Gear")
HOURGLASS = Item("Hourglass", cost=[25, gp], category="Adventuring Gear")
INK = Item("Ink", cost=[10, gp], quantity=1, category="Adventuring Gear")
INK_PEN = Item("Ink_Pen", cost=[2, cp], category="Adventuring Gear")
JUG = Item("Jug", cost=[2, cp], category="Adventuring Gear")
LADDER = Item("Ladder", cost=[1, sp], quantity=10, category="Adventuring Gear")
LAMP = Item("Lamp", cost=[5, sp], category="Adventuring Gear")
LANTURN_BULLSEYE = Item("Lanturn_Bullseye", cost=[10, gp], category="Adventuring Gear")
LANTURN_HOODED = Item("Lanturn_Hooded", cost=[5, gp], category="Adventuring Gear")
LOCK = Item("Lock", cost=[10, gp], category="Adventuring Gear")
MAGNIFYING_GLASS = Item("Magnifying_Glass", cost=[100, gp], category="Adventuring Gear")
MANACLES = Item("Manacles", cost=[2, gp], category="Adventuring Gear")
MESS_KIT = Item("Mess_Kit", cost=[2, sp], category="Adventuring Gear")
MIRROR = Item("Mirror", cost=[5, gp], category="Adventuring Gear")
OIL = Item("Oil", cost=[1, sp], category="Adventuring Gear")
PAPER = Item("Paper", cost=[2, sp], quantity=1, category="Adventuring Gear")
PARCHMENT = Item("Parchment", cost=[1, sp], quantity=1, category="Adventuring Gear")
PERFUME = Item("Perfume", cost=[5, gp], category="Adventuring Gear")
PICK = Item("Pick", cost=[2, gp], category="Adventuring Gear")
PITON = Item("Piton", cost=[5, cp], category="Adventuring Gear")
POISON_VIAL = Item("Poison_Vial", cost=[100, gp], category="Adventuring Gear")
POLE = Item("Pole", cost=[5, cp], quantity=10, category="Adventuring Gear")
POT = Item("Pot", cost=[2, gp], category="Adventuring Gear")
POTION_OF_HEALING = Item("Potion_of_Healing", cost=[50, gp], category="Adventuring Gear")
POUCH = Item("Pouch", cost=[5, sp], category="Adventuring Gear")
QUIVER = Item("Quiver", cost=[1, gp], category="Adventuring Gear")
RAM_PORTABLE = Item("Ram_Portable", cost=[4, gp], category="Adventuring Gear")
RATIONS = Item("Rations", cost=[5, sp], quantity=1, category="Adventuring Gear")
ROBES = Item("Robes", cost=[1, gp], category="Adventuring Gear")
ROPE_HEMPEN = Item("Rope_hempen", cost=[1, gp], quantity=50, category="Adventuring Gear")
ROPE_SILK = Item("Rope_Silk", cost=[10, gp], quantity=50, category="Adventuring Gear")
SACK = Item("Sack", cost=[1, cp], category="Adventuring Gear")
SCALE_MERCHANTS = Item("Scale_Merchants", cost=[5, gp], category="Adventuring Gear")
SEALING_WAX = Item("Sealing_Wax", cost=[5, sp], category="Adventuring Gear")
SHOVEL = Item("Shovel", cost=[2, gp], category="Adventuring Gear")
SIGNAL_WHISTLE = Item("Signal_Whistle", cost=[5, cp], category="Adventuring Gear")
SIGNET_RING = Item("Signet_Ring", cost=[5, gp], category="Adventuring Gear")
SOAP = Item("Soap", cost=[2, cp], category="Adventuring Gear")
SPELLBOOK = Item("Spellbook", cost=[50, gp], category="Adventuring Gear")
IRON_SPIKES = Item("Iron_Spikes", cost=[1, gp], quantity=10, category="Adventuring Gear")
SPYGLASS = Item("Spyglass", cost=[1000, gp], category="Adventuring Gear")
TENT_TWO_PERSON = Item("Tent_Two_Person", cost=[2, gp], category="Adventuring Gear")
TINDERBOX = Item("Tinderbox", cost=[5, sp], category="Adventuring Gear")
TORCH = Item("Torch", cost=[1, cp], category="Adventuring Gear")
VIAL = Item("Vial", cost=[1, gp], category="Adventuring Gear")
WATERSKIN = Item("Waterskin", cost=[2, sp], category="Adventuring Gear")
WHETSTONE = Item("Whetstone", cost=[1, cp], category="Adventuring Gear")
# AMMUNITION
ARROWS = Item("Arrows", cost=[1, gp], ammunition=True, quantity=20, category="Adventuring Gear")
BLOWGUN_NEEDLES = Item("Blowgun_Needles", cost=[1, gp], ammunition=True, quantity=50, category="Adventuring Gear")
CROSSBOW_BOLTS = Item("Crossbow_Bolts", cost=[1, gp], ammunition=True, quantity=20, category="Adventuring Gear")
SLING_BULLETS = Item("Sling_Bullets", cost=[4, cp], ammunition=True, quantity=20, category="Adventuring Gear")
# ARCANE_FOCUS
CRYSTAL = Item("Crystal", cost=[10, gp], arcane_focus=True, category="Adventuring Gear")
ORB = Item("Orb", cost=[20, gp], arcane_focus=True, category="Adventuring Gear")
ROD = Item("Rod", cost=[10, gp], arcane_focus=True, category="Adventuring Gear")
STAFF = Item("Staff", cost=[5, gp], arcane_focus=True, category="Adventuring Gear")
WAND = Item("Wand", cost=[10, gp], arcane_focus=True, category="Adventuring Gear")
# DRUIDIC_FOCUS
SPRIG_OF_MISTLETOE = Item("Sprig_of_Mistletoe", cost=[1, gp], druidic_focus=True, category="Adventuring Gear")
TOTEM = Item("Totem", cost=[1, gp], druidic_focus=True, category="Adventuring Gear")
WOODEN_STAFF = Item("Wooden_Staff", cost=[5, gp], druidic_focus=True, category="Adventuring Gear")
YEW_WAND = Item("Yew_Wand", cost=[100, gp], druidic_focus=True, category="Adventuring Gear")
# HOLY_SYMBOL
AMULET = Item("Amulet", cost=[5, gp], holy_symbol=True, category="Adventuring Gear")
EMBLEM = Item("Emblem", cost=[5, gp], holy_symbol=True, category="Adventuring Gear")
RELIQUARY = Item("Reliquary", cost=[5, gp], holy_symbol=True, category="Adventuring Gear")
# ITEM LISTS
ARCANE_FOCUS = MakeItemList("arcane_focus")
DRUIDIC_FOCUS = MakeItemList("druidic_focus")
HOLY_SYMBOL = MakeItemList("holy_symbol")

"""
    TOOLS
"""
DISGUISE_KIT = Tool("Disguise_Kit", cost=[25,gp], category="Tool")
FORGERY_KIT = Tool("Forgery_Kit", cost=[15,gp], category="Tool")
HERBALISM_KIT = Tool("Herbalism_Kit", cost=[5,gp], category="Tool")
NAVIGATORS_TOOLS = Tool("Navigators_Tools", cost=[25,gp], category="Tool")
POISONERS_KIT = Tool("Poisoners_Kit", cost=[50,gp], category="Tool")
THIEVES_TOOLS = Tool("Thieves_Tools", cost=[25,gp], category="Tool")
# ARTISAN
ALCHEMISTS_SUPPLIES = Tool("Alchemists_Supplies", cost=[50, gp], tool_type='Artisan', category="Tool")
BREWERS_SUPPLIES = Tool("Brewers_Supplies", cost=[20, gp], tool_type='Artisan', category="Tool")
CALLIGRAPHY_SUPPLIES = Tool("Calligraphy_Supplies", cost=[10, gp], tool_type='Artisan', category="Tool")
CARPENTERS_TOOLS = Tool("Carpenters_Tools", cost=[8, gp], tool_type='Artisan', category="Tool")
CARTOGRAPHERS_TOOLS = Tool("Cartographers_Tools", cost=[15, gp], tool_type='Artisan', category="Tool")
COBBLERS_TOOLS = Tool("Cobblers_Tools", cost=[5, gp], tool_type='Artisan', category="Tool")
COOKING_UTENSILS = Tool("Cooking_Utensils", cost=[1, gp], tool_type='Artisan', category="Tool")
GLASSBLOWERS_TOOLS = Tool("Glassblowers_Tools", cost=[30, gp], tool_type='Artisan', category="Tool")
JEWLERS_TOOLS = Tool("Jewlers_Tools", cost=[25, gp], tool_type='Artisan', category="Tool")
LEATHER_ARMORWORKERS_TOOLS = Tool("Leatherworkers_Tools", cost=[5, gp], tool_type='Artisan', category="Tool")
MASONS_TOOLS = Tool("Masons_Tools", cost=[10, gp], tool_type='Artisan', category="Tool")
PAINTERS_SUPPLIES = Tool("Painters_Supplies", cost=[10, gp], tool_type='Artisan', category="Tool")
SMITHS_TOOLS = Tool("Smiths_Tools", cost=[10, gp], tool_type='Artisan', category="Tool")
TINKERS_TOOLS = Tool("Tinkers_Tools", cost=[50, gp], tool_type='Artisan', category="Tool")
WEAVERS_TOOLS = Tool("Weavers_Tools", cost=[1, gp], tool_type='Artisan', category="Tool")
WOODCARVERS_TOOLS = Tool("Woodcarvers_Tools", cost=[1, gp], tool_type='Artisan', category="Tool")
# GAMING
DICE_SET = Tool("Dice_Set", cost=[1,sp], tool_type='Gaming', category="Tool")
DRAGONCHESS_SET = Tool("Dragonchess_Set", cost=[1,gp], tool_type='Gaming', category="Tool")
PLAYING_CARD_SET = Tool("Playing_Card_Set", cost=[5,gp], tool_type='Gaming', category="Tool")
THREE_DRAGON_ANTE_SET = Tool("Three_Dragon_Ante_Set", cost=[1,gp], tool_type='Gaming', category="Tool")
# INSTRUMENT
BAGPIPES = Tool("Bagpipes", cost=[30, gp], tool_type='Instrument', category="Tool")
DRUM = Tool("Drum", cost=[6, gp], tool_type='Instrument', category="Tool")
DULCIMER = Tool("Dulcimer", cost=[25, gp], tool_type='Instrument', category="Tool")
FLUTE = Tool("Flute", cost=[2, gp], tool_type='Instrument', category="Tool")
LUTE = Tool("Lute", cost=[35, gp], tool_type='Instrument', category="Tool")
LYRE = Tool("Lyre", cost=[30, gp], tool_type='Instrument', category="Tool")
HORN = Tool("Horn", cost=[3, gp], tool_type='Instrument', category="Tool")
PAN_FLUTE = Tool("Pan_Flute", cost=[12, gp], tool_type='Instrument', category="Tool")
SHAWM = Tool("Shawm", cost=[2, gp], tool_type='Instrument', category="Tool")
VIOL = Tool("Viol", cost=[30, gp], tool_type='Instrument', category="Tool")
# TOOL LISTS
ARTISAN_TOOLS = MakeItemList("tool_type", "Artisan")
MUSICAL_INSTRUMENT = MakeItemList("tool_type", "Instrument")
GAMING_TOOLS = MakeItemList("tool_type", "Gaming")
TOOLS = MakeItemList("category", "Tool")
"""
    MISC ITEMS
"""
ALMS_BOX = Item("Alms Box")
CENSER = Item("Censer")
BLOCK_OF_INCENSE = Item("Block_of_Incense")
BAG_OF_SAND = Item("Bag_of_Sand")

"""
    BACKGROUND SPECIFIC GEAR
"""
# ACOLYTE
PRAYER_BOOK = Item("Prayer_Book", background='Acolyte')
PRAYER_WHEEL = Item("Prayer_Wheel", background='Acolyte')
STICKS_OF_INCENSE = Item("Sticks_of_Incense", quantity=5, background='Acolyte')
VESTMENTS = Item("Vestments", background='Acolyte')
# CHARLATAN
STOPPERED_BOTTLES = Item("Stoppered_Bottles", background='Charlatan')
WEIGHTED_DICE = Item("Weighted_Dice", background='Charlatan')
DECK_OF_MARKED_CARDS = Item("Deck_of_Marked_Cards", background='Charlatan')
SIGNET_RING_OF_IMAGINARY_DUKE = Item("Signet_Ring_of_Imaginary_Duke", background='Charlatan')
CHARLATAN_ITEMS = MakeItemList("background", "Charlatan")
# Criminal
DARK_HOOD = Item("Dark Hood", background='Criminal')
# Entertainer
LOVE_LETTER = Item("Love_Letter", background='Entertainer')
LOCK_OF_HAIR = Item("Lock_of_Hair", background='Entertainer')
ADMIRER_TRINKET = Item("Admirer_Trinket", background='Entertainer')
ENTERTAINER_ITEMS = MakeItemList("background", 'Entertainer')
# GUILD_ARTISAN
LETTER_OF_INTRODUCTION = Item("Letter_of_Introduction", background='Guild Artisan')
# NOBLE
SCROLL_OF_PEDIGREE = Item("Scroll_of_Pedigree", background='Noble')
# OUTLANDER
HUNTING_TRAP = Item("Hunting_Trap", background='Outlander')
ANIMAL_TROPHY = Item("Animal_Trophy", background='Outlander')
# SAGE
QUILL = Item("Quill", background='Sage')
LETTER_FROM_DEAD_COLLEAGUE = Item("Letter_from_Dead_Colleague", background='Sage')
# SAILOR
BELAYING_PIN = Item("Belaying_Pin", background='Sailor')
LUCKY_CHARM = Item("Lucky Charm", background='Sailor')
# SOLDIER
INSIGNIA_OF_RANK = Item("Insignia_of_Rank", background='Solider')
TROPHY_FROM_FALLEN_ENEMY = Item("Trophy_from_Fallen_Enemy", background='Solider')
BONE_DICE = Item("Bone_Dice", background='Solider')
DECK_OF_CARDS = Item("Deck_of_Cards", background='Solider')
# URCHIN
SMALL_KNIFE = Item("Small_Knife", background='Urchin')
MAP_OF_HOMETOWN = Item("Map_of_Hometown", background='Urchin')
PET_MOUSE = Item("Pet_Mouse", background='Urchin')
PARENTAL_TOKEN_OF_REMEMBERANCE = Item("Parental_Token_of_Rememberance", background='Urchin')
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
ACOLYTE = Background("Acolyte", skill_profs=[INSIGHT, RELIGION], tool_profs=[], language=[{'Choose 2': []}], equipment=[{'Choose 1': HOLY_SYMBOL}, {'Choose 1': [PRAYER_BOOK, PRAYER_WHEEL]}, VESTMENTS, CLOTHES_COMMON], money=[15, gp])
CHARLATAN = Background("Charlatan", skill_profs=[DECEPTION, SLEIGHT_OF_HAND], tool_profs=[DISGUISE_KIT, FORGERY_KIT], equipment=[CLOTHES_FINE, DISGUISE_KIT, {'Choose 1': CHARLATAN_ITEMS}], money=[15, gp])
CRIMINAL = Background("Criminal", skill_profs=[DECEPTION, STEALTH], tool_profs=[{'Choose 1': GAMING_TOOLS}, THIEVES_TOOLS], equipment=[CROWBAR, CLOTHES_COMMON, DARK_HOOD], money=[15, gp])
ENTERTAINER = Background("Entertainer", skill_profs=[ACROBATICS, PERFORMANCE], tool_profs=[DISGUISE_KIT, {'Choose 1': MUSICAL_INSTRUMENT}], equipment=[{'Choose 1': MUSICAL_INSTRUMENT}, {'Choose 1': ENTERTAINER_ITEMS}, CLOTHES_COSTUME], money=[15, gp])
FOLK_HERO = Background("Folk_Hero", skill_profs=[ANIMAL_HANDLING, SURVIVAL], tool_profs=[{'Choose 1': ARTISAN_TOOLS}, ("TODO: VEHICLES")], equipment=[{'Choose 1': ARTISAN_TOOLS}, SHOVEL, POT, CLOTHES_COMMON], money=[10, gp])
GUILD_ARTISAN = Background("Guild_Artisan", skill_profs=[INSIGHT, PERSUASION], tool_profs=[{'Choose 1': ARTISAN_TOOLS}], language=[{'Choose 1': []}], equipment=[{'Choose 1': ARTISAN_TOOLS}, LETTER_OF_INTRODUCTION, CLOTHES_TRAVELERS], money=[15, gp])
HERMIT = Background("Hermit", skill_profs=[MEDICINE, RELIGION], tool_profs=[HERBALISM_KIT], language=[{'Choose 1':[]}], equipment=[CASE_MAP_SCROLL, BLANKET, CLOTHES_COMMON, HERBALISM_KIT], money=[5, gp])
NOBLE = Background("Noble", skill_profs=[HISTORY, PERSUASION], tool_profs=[{'Choose 1': GAMING_TOOLS}], language=[{'Choose 1': []}], equipment=[CLOTHES_FINE, SIGNET_RING, SCROLL_OF_PEDIGREE], money=[25, gp])
OUTLANDER = Background("Outlander", skill_profs=[ATHLETICS, SURVIVAL], tool_profs=[{'Choose 1': MUSICAL_INSTRUMENT}], language=[{'Choose 1': []}], equipment=[STAFF, HUNTING_TRAP, ANIMAL_TROPHY], money=[10, gp])
SAGE = Background("Sage", skill_profs=[ARCANA, HISTORY], tool_profs=[], language=[{'Choose 2': []}], equipment=[INK, QUILL, LETTER_FROM_DEAD_COLLEAGUE], money=[10, gp])
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

BARBARIAN.proficiencies = {
        'Armor': LIGHT_ARMOR + MEDIUM_ARMOR + SHIELDS,
        'Weapons': SIMPLE_WEAPONS + MARTIAL_WEAPONS,
        'Tools': None
        }
BARBARIAN.saving_throws = [STR, CON]
BARBARIAN.skills = {'Choose 2': [ANIMAL_HANDLING, ATHLETICS, INTIMIDATION, NATURE, PERCEPTION, SURVIVAL]}
BARBARIAN.hit_dice = "1d12"
BARBARIAN.initial_health = [12, CON.modifier]
BARBARIAN.starting_money = ["2d4", 10, gp]
BARBARIAN.equipment = [ {'Choose 1': [GREATAXE, {'Choose 1': MARTIAL_WEAPONS}]}, {'Choose 1': [[HANDAXE, HANDAXE], {'Choose 1': SIMPLE_WEAPONS}]}, JAVELIN, JAVELIN, JAVELIN, JAVELIN]
BARBARIAN.equipment_pack = EXPLORERS_PACK


BARD.proficiencies = {
        'Armor': LIGHT_ARMOR,
        'Weapons': SIMPLE_WEAPONS + [HAND_CROSSBOW, LONGSWORD, RAPIER, SHORTSWORD],
        'Tools': {'Choose 3': MUSICAL_INSTRUMENT}
        }
BARD.saving_throws = [DEX, CHA]
BARD.skills = {'Choose 3': SKILLS}
BARD.hit_dice = "1d6"
BARD.initial_health = [8, CON.modifier]
BARD.starting_money = ["5d4", 10, gp]
BARD.equipment = [ {'Choose 1': [RAPIER, LONGSWORD, {'Choose 1': SIMPLE_WEAPONS}]}, {'Choose 1': [LUTE, {'Choose 1': MUSICAL_INSTRUMENT}]}, LEATHER_ARMOR, DAGGER ]
BARD.equipment_pack = {'Choose 1': [DIPLOMATS_PACK, ENTERTAINERS_PACK]},

CLERIC.proficiencies = {
        'Armor': LIGHT_ARMOR + MEDIUM_ARMOR + SHIELDS,
        'Weapons': SIMPLE_WEAPONS,
        'Tools': None
        }
CLERIC.saving_throws = [WIS, CHA]
CLERIC.skills = {'Choose 2': [HISTORY, INSIGHT, MEDICINE, PERSUASION, RELIGION]}
CLERIC.hit_dice = "1d8"
CLERIC.initial_health = [8, CON.modifier]
CLERIC.starting_money = ["5d4", 10, gp]
CLERIC.equipment = [ {'Choose 1': [MACE, WARHAMMER]}, {'Choose 1': [SCALE_MAIL, LEATHER_ARMOR, CHAIN_MAIL]}, {'Choose 1': [[LIGHT_CROSSBOW, CROSSBOW_BOLTS], {'Choose 1': SIMPLE_WEAPONS}]}, SHIELD, {'Choose 1': HOLY_SYMBOL} ]
CLERIC.equipment_pack = {'Choose 1': [PRIESTS_PACK, EXPLORERS_PACK]}

DRUID.proficiencies = {
        'Armor': LIGHT_ARMOR + MEDIUM_ARMOR + SHIELDS,
        'Weapons': [CLUB, DAGGER, DART, JAVELIN, MACE, QUARTERSTAFF, SCIMITAR, SICKLE, SLING, SPEAR],
        'Tools': {'Has': [HERBALISM_KIT]}
        }
DRUID.saving_throws = [INT, WIS]
DRUID.skills = {'Choose 2': [ARCANA, ANIMAL_HANDLING, INSIGHT, MEDICINE, NATURE, PERCEPTION, RELIGION, SURVIVAL]}
DRUID.hit_dice = "1d8"
DRUID.initial_health = [8, CON.modifier]
DRUID.starting_money = ["2d4", 10, gp]
DRUID.equipment = [ {'Choose 1': [SHIELD, {'Choose 1': SIMPLE_WEAPONS}]}, {'Choose 1': [SCIMITAR, {'Choose 1': MELEE_SIMPLE_WEAPONS}]}, LEATHER_ARMOR, {'Choose 1': DRUIDIC_FOCUS} ]
DRUID.equipment_pack = EXPLORERS_PACK

FIGHTER.proficiencies = {
        'Armor': ALL_ARMOR + SHIELDS,
        'Weapons': SIMPLE_WEAPONS + MARTIAL_WEAPONS,
        'Tools': None
        }
FIGHTER.saving_throws = [STR, CON]
FIGHTER.skills = {'Choose 2': [ACROBATICS, ANIMAL_HANDLING, ATHLETICS, HISTORY, INSIGHT, INTIMIDATION, PERCEPTION, SURVIVAL]}
FIGHTER.hit_dice = "1d10"
FIGHTER.initial_health = [10, CON.modifier]
FIGHTER.starting_money = ["5d4", 10, gp]
FIGHTER.equipment = [ {'Choose 1': [CHAIN_MAIL, [LEATHER_ARMOR, LONGBOW, ARROWS]]}, {'Choose 1': [[{'Choose 1': MARTIAL_WEAPONS}, SHIELD], {'Choose 2': MARTIAL_WEAPONS}]}, {'Choose 1': [[LIGHT_CROSSBOW, CROSSBOW_BOLTS], [HANDAXE, HANDAXE]]}, ]
FIGHTER.equipment_pack = {'Choose 1': [DUNGEONEERS_PACK, EXPLORERS_PACK]}

MONK.proficiencies = {
        'Armor': None,
        'Weapons': SIMPLE_WEAPONS +  [SHORTSWORD],
        'Tools': {'Choose 1': MUSICAL_INSTRUMENT + ARTISAN_TOOLS}
        }
MONK.saving_throws = [STR, DEX]
MONK.skills = {'Choose 2': [ACROBATICS, ATHLETICS, HISTORY, INSIGHT, RELIGION, STEALTH]}
MONK.hit_dice = "1d8"
MONK.initial_health = [8, CON.modifier]
MONK.starting_money = ["5d4", 1, gp]
MONK.equipment = [{'Choose 1': [SHORTSWORD, {'Choose 1':SIMPLE_WEAPONS}]}] + [DART for _ in range(10)]
MONK.equipment_pack = {'Choose 1': [EXPLORERS_PACK, DUNGEONEERS_PACK]}

PALADIN.proficiencies = {
        'Armor': ALL_ARMOR + SHIELDS,
        'Weapons': SIMPLE_WEAPONS + MARTIAL_WEAPONS,
        'Tools': None
        }
PALADIN.saving_throws = [WIS, CHA]
PALADIN.skills = {'Choose 2': [ATHLETICS, INSIGHT, INTIMIDATION, MEDICINE, PERSUASION, RELIGION]}
PALADIN.hit_dice = "1d10"
PALADIN.initial_health = [10, CON.modifier]
PALADIN.starting_money = ["5d4", 10, gp]
PALADIN.equipment = [ {'Choose 1': [[{'Choose 1': MARTIAL_WEAPONS}, SHIELD], {'Choose 2': MARTIAL_WEAPONS}]}, {'Choose 1': [[JAVELIN for _ in range(5)], {'Choose 1': MELEE_SIMPLE_WEAPONS}]}, CHAIN_MAIL, {'Choose 1': HOLY_SYMBOL} ]
PALADIN.equipment_pack = {'Choose 1': [PRIESTS_PACK, EXPLORERS_PACK]}

RANGER.proficiencies = {
        'Armor': LIGHT_ARMOR + MEDIUM_ARMOR + SHIELDS,
        'Weapons': SIMPLE_WEAPONS + MARTIAL_WEAPONS,
        'Tools': None
        }
RANGER.saving_throws = [STR, DEX]
RANGER.skills = {'Choose 3': [ANIMAL_HANDLING, ATHLETICS, INSIGHT, INVESTIGATION, NATURE, PERCEPTION, STEALTH, SURVIVAL]}
RANGER.hit_dice = "1d10"
RANGER.initial_health = [10, CON.modifier]
RANGER.starting_money = ["5d4", 10, gp]
RANGER.equipment = [ {'Choose 1': [LEATHER_ARMOR, SCALE_MAIL]}, {'Choose 1': [[SHORTSWORD, SHORTSWORD], {'Choose 2': MELEE_SIMPLE_WEAPONS}]}, LONGBOW, QUIVER, ARROWS ] 
RANGER.equipment_pack = {'Choose 1': [DUNGEONEERS_PACK, EXPLORERS_PACK]}

ROGUE.proficiencies = {
        'Armor': LIGHT_ARMOR,
        'Weapons': SIMPLE_WEAPONS + [HAND_CROSSBOW],
        'Tools': {'Has': [THIEVES_TOOLS]}
        }
ROGUE.saving_throws = [DEX, INT]
ROGUE.skills = {'Choose 4': [ACROBATICS, ATHLETICS, DECEPTION, INSIGHT, INTIMIDATION, INVESTIGATION, PERCEPTION, PERFORMANCE, PERSUASION, SLEIGHT_OF_HAND, STEALTH]}
ROGUE.hit_dice = "1d8"
ROGUE.initial_health = [8, CON.modifier]
ROGUE.starting_money = ["4d4", 10, gp]
ROGUE.equipment = [ {'Choose 1': [RAPIER, SHORTSWORD]}, {'Choose 1': [[SHORTBOW, QUIVER, ARROWS], SHORTSWORD]}, LEATHER_ARMOR, DAGGER, DAGGER, THIEVES_TOOLS ]
ROGUE.equipment_pack = {'Choose 1': [BURGLURS_PACK, DUNGEONEERS_PACK, EXPLORERS_PACK]}

SORCERER.proficiencies = {
        'Armor': None,
        'Weapons': [DAGGER, DART, SLING, QUARTERSTAFF, LIGHT_CROSSBOW],
        'Tools': None
        }
SORCERER.saving_throws = [CON, CHA]
SORCERER.skills = {'Choose 2': [ARCANA, DECEPTION, INSIGHT, INTIMIDATION, PERSUASION, RELIGION]}
SORCERER.hit_dice = "1d6"
SORCERER.initial_health = [6, CON.modifier]
SORCERER.starting_money = ["3d4", 10, gp]
SORCERER.equipment = [ {'Choose 1': [[LIGHT_CROSSBOW, CROSSBOW_BOLTS], {'Choose 1': SIMPLE_WEAPONS}]}, {'Choose 1': [COMPONENT_POUCH, {'Choose 1': ARCANE_FOCUS}]}, DAGGER, DAGGER ]
SORCERER.equipment_pack = {'Choose 1': [DUNGEONEERS_PACK, EXPLORERS_PACK]}

WARLOCK.proficiencies = {
        'Armor': LIGHT_ARMOR,
        'Weapons': SIMPLE_WEAPONS,
        'Tools': None
        }
WARLOCK.saving_throws = [WIS, CHA]
WARLOCK.skills = {'Choose 2': [ARCANA, DECEPTION, HISTORY, INTIMIDATION, INVESTIGATION, NATURE, RELIGION]}
WARLOCK.hit_dice = "1d8"
WARLOCK.initial_health = [8, CON.modifier]
WARLOCK.starting_money = ["4d4", 10, gp]
WARLOCK.equipment = [ {'Choose 1': [[LIGHT_CROSSBOW, CROSSBOW_BOLTS], {'Choose 1': SIMPLE_WEAPONS}]}, {'Choose 1': [COMPONENT_POUCH, {'Choose 1': ARCANE_FOCUS}]}, DAGGER, DAGGER, LEATHER_ARMOR, {'Choose 1': SIMPLE_WEAPONS} ]
WARLOCK.equipment_pack = {'Choose 1': [SCHOLARS_PACK, DUNGEONEERS_PACK]}

WIZARD.proficiencies = {
        'Armor': None,
        'Weapons': [DAGGER, DART, SLING, QUARTERSTAFF, LIGHT_CROSSBOW],
        'Tools': None
        }
WIZARD.saving_throws = [INT, WIS]
WIZARD.skills = {'Choose 2': [ARCANA, HISTORY, INSIGHT, INVESTIGATION, MEDICINE, RELIGION]}
WIZARD.hit_dice = "1d6"
WIZARD.initial_health = [6, CON.modifier]
WIZARD.starting_money = ["4d4", 10, gp]
WIZARD.equipment = [ {'Choose 1': [QUARTERSTAFF, DAGGER]}, {'Choose 1': [COMPONENT_POUCH, {'Choose 1': ARCANE_FOCUS}]}, SPELLBOOK ]
WIZARD.equipment_pack = {'Choose 1': [SCHOLARS_PACK, EXPLORERS_PACK]}

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
"""
    RACE
"""
DRAGONBORN = Race("Dragonborn")
DWARF = Race("Dwarf")
ELF = Race("Elf")
GNOME = Race("Gnome")
HALFLING = Race("Halfling")
HALF_ELF = Race("Half_Elf")
HALF_ORC = Race("Half_Orc")
HUMAN = Race("Human")
TIEFLING = Race("Tiefling")

def Choose(data: list):
    return random.choice(data)

def Unpack(data: list):
    print("unpack launched")
    output = []
    for item in data:
        if type(item) == dict:
            print("item is dict")
            item_keys = list(item.keys())
            match item_keys[0]:
                case "Choose 1":
                    output.append(Unpack(item[item_keys[0]]))
        elif type(item) == list:
            print("item is list")
            output.append(random.choice(item))
        else:
            print("item is not dict")
    return output


        

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
    tool_prof = GetProficiencies(roll_class.proficiencies['Tools'])
    x = Unpack(BARD.equipment)
    print(x)