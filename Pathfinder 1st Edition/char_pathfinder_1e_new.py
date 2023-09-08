import random

def dice(dicestring):
    throws, sides = dicestring.split('d')
    return sum([random.randint(1, int(sides)) for _ in range(int(throws))])

def get_mod(score):
    return (score//2) - 5


class AbilityScore:
    def __init__(self, name, value=0):
        self.name = name
        self.value = value
        self.mod = get_mod(self.value)

    def __add__(self, amt):
        self.value += amt
        return AbilityScore(self.name, self.value)

    def __iadd__(self, amt):
        return self.__add__(amt)

    def __repr__(self):
        return f'{self.name}: {self.value}({self.mod})'

STR = AbilityScore('Strength')
DEX = AbilityScore('Dexterity')
CON = AbilityScore('Constitution')
INT = AbiltiyScore('Intelligence')
WIS = AbilityScore('Wisdom')
CHA = AbilityScore('Charisma')

class ABC:
    def __init__(self, name, **kwargs):
        self.name = name
        for k, d in kwargs:
            self.__setattr__(k, d)
    
    def __repr__(self):
        return self.__format__()

    def __format__(self):
        return self.name


class Skill(ABC):
    items = []
    def __init__(self, name, ab_score, trained=False, **kwargs):
        super().__init__(name, kwargs)
        self.ab_score = ab_score
        self.trained = trained
        Skill.items.append(self)

ACROBATICS = Skill('Acrobatics', ab_score=DEX)
APPRAISE = Skill('Appraise', ab_score=INT)
BLUFF = Skill('Bluff', ab_score=CHA)
CLIMB = Skill('Climb', ab_score=STR)
CRAFT = Skill('Craft', ab_score=INT)
DIPLOMACY = Skill('Diplomacy', ab_score=CHA)
DISABLE_DEVICE = Skill('Disable Device', ab_score=DEX, trained=True)
DISGUISE = Skill('Disguise', ab_score=CHA)
ESCAPE_ARTIST = Skill('Escape Artist', ab_score=DEX)
FLY = Skill('Fly', ab_score=DEX)
HANDLE_ANIMAL = Skill('Handle Animal', ab_score=CHA, trained=True)
HEAL = Skill('Heal', ab_score=WIS)
INTIMIDATE = Skill('Intimidate', ab_score=CHA)
KNOWLEDGE_ARCANA = Skill('Knowledge (Arcana)', ab_score=INT, trained=True)
KNOWLEDGE_DUNGEONEERING = Skill('Knowledge (Dungeoneering)', ab_score=INT, trained=True)
KNOWLEDGE_ENGINEERING = Skill('Knowledge (Engineering)', ab_score=INT, trained=True)
KNOWLEDGE_GEOGRAPHY = Skill('Knowledge (Geography)', ab_score=INT, trained=True)
KNOWLEDGE_HISTORY = Skill('Knowledge (History)', ab_score=INT, trained=True)
KNOWLEDGE_LOCAL = Skill('Knowledge (Local)', ab_score=INT, trained=True)
KNOWLEDGE_NATURE = Skill('Knowledge (Nature)', ab_score=INT, trained=True)
KNOWLEDGE_NOBILITY = Skill('Knowledge (Nobility)', ab_score=INT, trained=True)
KNOWLEDGE_PLANES = Skill('Knowledge (Planes)', ab_score=INT, trained=True)
KNOWLEDGE_RELIGION = Skill('Knowledge (Religion)', ab_score=INT, trained=True)
LINGUISTICS = Skill('Linguistics', ab_score=INT, trained=True)
PERCEPTION = Skill('Perception', ab_score=WIS)
PERFORM = Skill('Perform', ab_score=CHA)
PROFESSION = Skill('Profession', ab_score=WIS, trained=True)
RIDE = Skill('Ride', ab_score=DEX)
SENSE_MOTIVE = Skill('Sense Motive', ab_score=WIS)
SLEIGHT_OF_HAND = Skill('Sleight of Hand', ab_score=DEX, trained=True)
SPELLCRAFT = Skill('Spellcraft', ab_score=INT, trained=True)
STEALTH = Skill('Stealth', ab_score=DEX)
SURVIVAL = Skill('Survival', ab_score=WIS)
SWIM = Skill('Swim', ab_score=STR)
USE_MAGIC_DEVICE = Skill('Use Magic Device', ab_score=CHA, trained=True)

class Item(ABC):
    items = []
    def __init__(self, name, **kwargs):
        super().__init__(name, kwargs)
        Item.items.append(self)


class Weapon(Item):
    items = []
    def __init__(self, name, type, range, damage, attack_bonus, crit, ammo=None, **kwargs):
        super().__init__(name, kwargs)
        Weapon.items.append(self)
        self.type = type
        self.range = range
        self.damage = damage
        self.attack_bonus = attack_bonus
        self.crit = crit
        self.ammo = ammo


class Race(ABC):
    items = []
    def __init__(self, name, **kwargs):
        super().__init__(name, kwargs)
        Race.items.append(self)

DWARF = Race('Dwarf', ab_bonus={CON: 2, WIS: 2, CHA: -2}, size='Medium', )


class Char:
    def __init__(self):
        # MACRO PLAYER INFO
        self.name = None
        self.race = None
        self.alignment = None
        self.level = 1
        self.deity = None
        self.homeland = None
        # COSMETIC PLAYER INFO
        self.size = 0
        self.gender = None
        self.age = 0
        self.height = 0
        self.weight = 0
        self.hair = None
        self.eyes = None
        # MATH
        self.scores = {'STR': 0, 'DEX': 0, 'CON': 0, 'INT': 0, 'WIS': 0, 'CHA': 0}
        self.score_mods = {key:get_mod(self.scores[key]) for key in self.scores.keys()}
        self.hp_total = 0
        self.hp_dr = 0
        self.speed = {'Base': 0, 'Armor': 0, 'Fly': 0, 'Swim': 0, 'Climb': 0, 'Burrow': 0}
        self.armor_class = {'Total': 0, 'Armor Bonus': 0, 'Shield Bonus': 0, 'Natural Armor': 0, 'Deflection': 0, 'Misc': 0}
        self.touch_armor_class = 0
        self.flatfooted_armor_class = 0
        self.fortitude = 0
        self.reflex = 0
        self.will = 0
        self.base_attack_bonus = 0
        self.spell_resistance = 0
        self.CMB = 0
        self.combat_maneuver_defence = 0
        self.skills = {}
        # POSSESSIONS
        self.weapons = []
        self.gear = []
        self.money = {'cp': 0, 'sp': 0, 'gp': 0, 'pp': 0}

CHARACTER = Char()
