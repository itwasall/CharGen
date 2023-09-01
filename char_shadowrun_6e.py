import random
from typing import Dict

def attrAsDict(_class):
    return {i: _class.__getattribute__(i) for i in dir(_class) if not i.startswith("__") and i != 'items'}

def roll(dicestring: str):
    if "+" in dicestring:
        dicestring, mods = "+".split(dicestring)
    else:
        mods = 0
    throws, sides = int("d".split(dicestring))
    return sum([mods, sum([random.randint(1, s) for _ in range(throws)])])

class AbstractBaseClass():
    def __init__(self, name, **kwargs):
        self.name = name
        for k, d in kwargs.items():
            self.__setattr__(k, d)

    def __repr__(self):
        return self.name

class ReturnObj(dict):
    def __init__(self, name="Return Object", **kwargs):
        self.name = name
        for k, d in kwargs.items():
            self.__setattr__(k, d)
    def set(self, attr, value=None):
        self.__setattr__(attr, value)
    def __repr__(self):
        #return f"{attrAsDict(self)}"
        return "\n".join([i for i in dir(self) if i not in [j for j in dir(dict)]])


class Metatype(AbstractBaseClass):
    items = []
    def __init__(self, name, **kwargs):
        Metatype.items.append(self)
        super().__init__(name, **kwargs)

class Archetype(AbstractBaseClass):
    items = []
    def __init__(self, name, **kwargs):
        Archetype.items.append(self)
        super().__init__(name, **kwargs)

# ARCHETYPE
ADEPT = Archetype('Adept', ID=0)
FACE = Archetype('Face')
RIGGER = Archetype('Rigger')
STREET_SAMURAI = Archetype('Street Samurai')
STREET_SHAMAN = Archetype('Street Shaman')
TECHNOMANCER = Archetype('Technomancer')
WEAPONS_SPECIALIST = Archetype('Weapons Specialist')

class Quality(AbstractBaseClass):
    items = []
    def __init__(self, name, **kwargs):
        Quality.items.append(self)
        super().__init__(name, **kwargs)

# QUALITIES
# POSITIVE
AMBIDEXTROUS = Quality('Ambidextrous', cost=4)
ANALYTICAL_MIND = Quality('Analytical Mind', cost=3)
APTITUDE = Quality('Aptitude', cost=12)
ASTRAL_CHAMELEON = Quality('Astral Chameleon', cost=9)
BLANDNESS = Quality('Blandness', cost=8)
BUILT_TOUGH = Quality('Built Tough', cost=4, levels=4)
CAT_LIKE = Quality('Cat-like', cost=12)
DERMAL_DEPOSITS = Quality('Dermal Deposits', cost=7)
DOUBLE_JOINTED = Quality('Double-jointed', cost=12)
FIRST_IMPRESSION = Quality('First Impression', cost=12)
FOCUSED_CONCERNTRATION = Quality('Focused Concerntration', cost=12, levels=3)
GEARHEAD = Quality('Gearhead', cost=10)
GUTS = Quality('Guts', cost=12)
HARDENING = Quality('Hardening', cost=10)
HIGH_PAIN_TOLERANCE = Quality('High Pain Tolerance', cost=7)
HOME_GROUND = Quality('Home Ground', cost=10)
HUMAN_LOOKING = Quality('Human-looking', cost=8)
INDOMITABLE = Quality('Indomitable', cost=12)
JURY_RIGGER = Quality('Jury Rigger', cost=12)
LONG_REACH = Quality('Long Reach', cost=12)
LOW_LIGHT_VISION = Quality('Low-light Vision', cost=6)
MAGIC_RESISTANCE = Quality('Magic Resistance', cost=8)
MENTOR_SPIRIT = Quality('Mentor Spirit', cost=10)
PATHOGEN_RESISTANCE = Quality('Pathogen Resistance', cost=12)
PHOTOGRAPHIC_MEMORY = Quality('Photographic Memory', cost=12)
QUICK_HEALER = Quality('Quick Healer', cost=8)
THERMOGRAPHIC_VISION = Quality('Thermographic Vision', cost=8)
TOUGHNESS = Quality('Toughness', cost=12)
TOXIS_RESISTANCE = Quality('Toxis resistance', cost=12)
WILL_TO_LIVE = Quality('Will to Live', cost=8, levels=3)

class Skill(AbstractBaseClass):
    items = []
    def __init__(self, name, **kwargs):
        Skill.items.append(self)
        self.rank = 1
        super().__init__(name, **kwargs)



ASTRAL = Skill('Astral', unskilled=False, specialisations=['Astral Combat', 'Astral Signatures', 'Emotional States', 'Spirit Types'], attribute='Intuition')
ATHLETICS = Skill('Athletics', unskilled=True, specialisations=['Climbing', 'Flying', 'Gymnastics', 'Sprinting', 'Swimming', 'Throwing'], attribute='Agility')
BIOTECH = Skill('Biotech', unskilled=False, specialisations=['Biotechnology', 'Cybertechnology', 'First Aid', 'Medicine'], attribute='Logic')
CLOSE_COMBAT = Skill('Close Combat', unskilled=True, specialisations=['Blades', 'Clubs', 'Unarmed Combat'], attribute='Agility')
CON = Skill('Con', unskilled=True, specialisations=['Acting', 'Disguise', 'Impersonation', 'Performance'], attribute='Charisma')
CONJURING = Skill('Conjuring', unskilled=False, specialisations=['Banishing', 'Binding', 'Summoning'], attribute='Magic')
CRACKING = Skill('Cracking', unskilled=False, specialisations=['Cybercombat', 'Electronic Warefare', 'Hacking'], attribute='Logic')
ELECTRONICS = Skill('Electronics', unskilled=True, specialisations=['Computer', 'Hardware', 'Software'], attribute='Logic')
ENCHANTING = Skill('Enchanting', unskilled=False, specialisations=['Alchemy', 'Artificing', 'Disenchanting'], attribute='Magic')
ENGINEERING = Skill('Engineering', unskilled=True, specialisations=['Aeronautics Mechanic', 'Automotive Mechanic', 'Demolitions', 'Gunnery', 'Industrial Mechanic', 'Lockpicking', 'Nautical Mechanic'], attribute='Logic')
EXOTIC_WEAPONS = Skill('Exotic Weapons', unskilled=False, specialisations=['N/A'], attribute='Agility')
FIREARMS = Skill('Firearms', unskilled=True, specialisations=['Automatics', 'Longarms', 'Pistols', 'Rifles', 'Shotguns'], attribute='Agility')
INFLUENCE = Skill('Influence', unskilled=True, specialisations=['Etiquette', 'Instruction', 'Intimidation', 'Leadership', 'Negotiation'], attribute='Charisma')
OUTDOORS = Skill('Outdoors', unskilled=True, specialisations=['Navigation', 'Survival', 'Tracking'], attribute='Intuition')
PERCEPTION = Skill('Perception', unskilled=True, specialisations=['Visual', 'Aural', 'Tactile'], attribute='Intuition')
PILOTING = Skill('Piloting', unskilled=True, specialisations=['Ground Craft', 'Aircraft', 'Watercraft'], attribute='Reaction')
SORCERY = Skill('Sorcery', unskilled=False, specialisations=['Counterspelling', 'Ritual Spellcasting', 'Spellcasting'], attribute='Magic')
STEALTH = Skill('Stealth', unskilled=True, specialisations=['Disguise', 'Palming', 'Sneaking'], attribute='Agility')
TASKING = Skill('Tasking', unskilled=False, specialisations=['Compiling', 'Decompiling', 'Registering'], attribute='Resonance')

class Attribute():
    def __init__(self, name, value: int = 0, limit = 6, hidden=False):
        self.name = name
        self.value = int(value)
        self.limit = limit
        if self.value != 0:
            self.hidden = False
        else:
            self.hidden = hidden
    def __repr__(self):
        return f"{self.name}: {self.value}/{self.limit}"
    def __add__(self, x: int, limit_raise=False):
        if limit_raise:
            return Attribute(self.name, self.value, self.limit + x)
        return Attribute(self.name, self.value +  x, self.limit)

class AttributeEdge():
    def __init__(self, name, value = 0):
        self.name = name
        self.value = value
    def __repr__(self):
        return f"{self.name}: {self.value}"
    def __add__(self, x):
        return AttributeEdge(self.name, self.value + x)


BODY = Attribute('Body')
AGILITY = Attribute('Agility')
REACTION = Attribute('Reaction')
STRENGTH = Attribute('Strength')
WILLPOWER = Attribute('Willpower')
LOGIC = Attribute('Logic')
INTUITION = Attribute('Intuition')
CHARISMA = Attribute('Charisma')
EDGE = AttributeEdge('Edge')
MAGIC = Attribute('Magic', hidden=True)
RESONANCE = Attribute('Resonance', hidden=True)


class ComplexForm(AbstractBaseClass):
    items = []
    def __init___(self, name, **kwargs):
        ComplexForm.items.append(self)
        super().__init__(name, **kwargs)


DIFFUSAL_OF_FIREWAL = ComplexForm('DIFFUSAL_OF_FIREWAL')


class Spell(AbstractBaseClass):
    items = []
    def __init__(self, name:str, **kwargs):
        super().__init__(name, **kwargs)
        Spell.items.append(self)
    def __repr__(self):
        return f"[{self.spell_type[0]}] {self.name}"

def SpellList(l: list):
    return str(sorted(l, key=lambda x: x.spell_type))

ACID_STREAM = Spell('Acid Stream', spell_type='Combat')
TOXIC_WAVE = Spell('Toxic Wave', spell_type='Combat')
CLOUT = Spell('Clout', spell_type='Combat')
BLAST = Spell('Blast', spell_type='Combat')
FLAMESTRIKE = Spell('Flamestrike', spell_type='Combat')
FIREBALL = Spell('Fireball', spell_type='Combat')
ICE_SPEAR = Spell('Ice Spear', spell_type='Combat')
ICE_STORM = Spell('Ice Storm', spell_type='Combat')
LIGHTNING_BOLT = Spell('Lightning Bolt', spell_type='Combat')
LIGHTNING_BALL = Spell('Lightning Ball', spell_type='Combat')
MANABOLT = Spell('Manabolt', spell_type='Combat')
MANABALL = Spell('Manaball', spell_type='Combat')
POWERBOLT = Spell('Powerbolt', spell_type='Combat')
POWERBALL = Spell('Powerball', spell_type='Combat')
STUNBOLT = Spell('Stunbolt', spell_type='Combat')
STUNBALL = Spell('Stunball', spell_type='Combat')

ANALYZE_DEVICE = Spell('Analyze Device', spell_type='Detection')
ANALYZE_MAGIC = Spell('Analyze Magic', spell_type='Detection')
ALALYZE_TRUTH = Spell('Analyze Truth', spell_type='Detection')
CLAIRAUDIENCE = Spell('Clairaudience', spell_type='Detection')
CLAIRVOYANCE = Spell('Clairvoyance', spell_type='Detection')
COMBAT_SENSE = Spell('Combat Sense', spell_type='Detection')
DETECT_ENEMIES = Spell('Detect Enemies', spell_type='Detection')
DETECT_LIFE = Spell('Detect Life', spell_type='Detection')
DETECT_MAGIC = Spell('Detect Magic', spell_type='Detection')
MINDLINK = Spell('Mindlink', spell_type='Detection')
MIND_PROBE = Spell('Mind Probe', spell_type='Detection')

ANTIDOTE = Spell('Antidote', spell_type='Heal')
CLEANSING_HEAL = Spell('Cleansing Heal', spell_type='Heal')
COOLING_HEAL = Spell('Cooling Heal', spell_type='Heal')
DECREASE_ATTRIBUTE = Spell('Decrease Attribute', spell_type='Heal')
HEAL = Spell('Heal', spell_type='Heal')
INCREASE_ATTRIBUTE = Spell('Increase Attribute', spell_type='Heal')
INCREASE_REFLEXES = Spell('Increase Reflexes', spell_type='Heal')
RESIST_PAIN = Spell('Resist Pain', spell_type='Heal')
STABILIZE = Spell('Stabilize', spell_type='Heal')
WARMING_HEAL = Spell('Warming Heal', spell_type='Heal')

AGONY = Spell('Agony', spell_type='Illusion')
CONFUSION = Spell('Confusion', spell_type='Illusion')
CHAOS = Spell('Chaos', spell_type='Illusion')
HUSH = Spell('Hush', spell_type='Illusion')
SILENCE = Spell('Silence', spell_type='Illusion')
INVISIBILITY = Spell('Invisibility', spell_type='Illusion')
IMPROVED_INVISIBILITY = Spell('Improved invisibility', spell_type='Illusion')
MASK = Spell('Mask', spell_type='Illusion')
PHYSICAL_MASK = Spell('Physical Mask', spell_type='Illusion')
PHANTASM = Spell('Phantasm', spell_type='Illusion')
TRID_PHANTASM = Spell('Trid Phantasm', spell_type='Illusion')
SENSOR_SNEAK = Spell('Sensor Sneak', spell_type='Illusion')

ARMOR = Spell('Armor', spell_type='Manipulation')
CONTROL_ACTIONS = Spell('Control Actions', spell_type='Manipulation')
CONTROL_THOUGHTS = Spell('Control Thoughts', spell_type='Manipulation')
DARKNESS = Spell('Darkness', spell_type='Manipulation')
LIGHT = Spell('Light', spell_type='Manipulation')
ELEMENTAL_ARMOR = Spell('Elemental Armor', spell_type='Manipulation')
FLING = Spell('Fling', spell_type='Manipulation')
FOCUS_BURST = Spell('Focus Burst', spell_type='Manipulation')
LEVITATE = Spell('Levitate', spell_type='Manipulation')
MANA_BARRIER = Spell('Mana Barrier', spell_type='Manipulation')
MYSTIC_ARMOR = Spell('Mystic Armor', spell_type='Manipulation')
OVERCLOCK = Spell('Overclock', spell_type='Manipulation')
PHYSICAL_BARRIER = Spell('Physical Barrier', spell_type='Manipulation')
SHAPE_METAL = Spell('Shape Metal', spell_type='Manipulation')
SHAPE_PLASTIC = Spell('Shape Plastic', spell_type='Manipulation')
SHAPE_STONE = Spell('Shape Stone', spell_type='Manipulation')
SHAPE_WOOD = Spell('Shape Wood', spell_type='Manipulation')
STRENGTHEN_WALL = Spell('Strengthen Wall', spell_type='Manipulation')
THUNDER = Spell('Thunder', spell_type='Manipulation')
VEHICLE_ARMOR = Spell('Vehicle Armor', spell_type='Manipulation')

SPELLS_COMBAT = [s for s in Spell.items if s.spell_type == 'Combat']
SPELLS_DETECTION = [s for s in Spell.items if s.spell_type == 'Detection']
SPELLS_HEAL = [s for s in Spell.items if s.spell_type == 'Heal']
SPELLS_ILLUSION = [s for s in Spell.items if s.spell_type == 'Illusion']
SPELLS_COMBAT = [s for s in Spell.items if s.spell_type == 'Manipulation']


class Character():
    def __init__(self, name):
        self.name = name
        self.body = BODY
        self.agility = AGILITY
        self.reaction = REACTION
        self.strength = STRENGTH
        self.willpower = WILLPOWER
        self.logic = LOGIC
        self.intuition = INTUITION
        self.charisma = CHARISMA
        self.edge = EDGE
        self.magic = MAGIC
        self.resonance = RESONANCE
        self.attributes = {
            'Physical': [self.body, self.agility, self.reaction, self.strength],
            'Mental': [self.willpower, self.logic, self.intuition, self.charisma],
            'Special': [self.edge, self.magic, self.resonance]
        }
        self.skills = {}
        self.metatype = {}
        self.archetype = {}
        self.gear = {}
        self.spells = []



def pick_qualities(ch: Character):
    karma = 50
    qualities = {}
    while True:
        roll_quality = random.choice(Quality.items)
        if karma - roll_quality.cost > 0:
            karma -= roll_quality.cost
            qualities[roll_quality.name] = roll_quality
            if hasattr(roll_quality, "level"):
                for i in range(roll_quality.level):
                    if karma - roll_quality.cost <= 0:
                        qualities[roll_quality.name]['level'] = i
                        break
                    else:
                        karma -= roll_quality.cost
        else:
            break
    return qualities
                

def get_metatype(metatypes):
    answer = ReturnObj()
    metatype = random.choice(metatypes)
    answer.set("height")
    answer.set("weight")
    answer.set("ears")
    answer.set("racial_qualities")
    answer.set("attributes")
    match metatype:
        case "Dwarf":
            answer.height = 1.2
            answer.weight = 5.4
            answer.ears = "Slightly Pointy"
            answer.racial_qualities = [THERMOGRAPHIC_VISION, TOXIS_RESISTANCE]
            BODY.limit = 7
            REACTION.limit = 5
            STRENGTH.limit = 8
            WILLPOWER.limit = 7
            answer.attributes = [BODY, REACTION, STRENGTH, WILLPOWER]
        case "Elf":
            answer.height = 1.9
            answer.weight = 80
            answer.ears = "Pointy"
            answer.racial_qualities = [LOW_LIGHT_VISION]
            AGILITY.limit = 7
            CHARISMA.limit = 8
            answer.attributes = [AGILITY, CHARISMA]
        case "Human":
            answer.height = 1.75
            answer.weight = 78
            answer.ears = "Rounded"
            answer.racial_qualities = None
            EDGE.limit = 7
            answer.attributes = [EDGE]
        case "Ork":
            answer.height = 1.9
            answer.weight = 128
            answer.ears = "Pointy"
            BUILT_TOUGH.level = 1
            answer.racial_qualities = [LOW_LIGHT_VISION, BUILT_TOUGH]
            BODY.limit = 8
            STRENGTH.limit = 8
            CHARISMA.limit = 5
            answer.attributes = [BODY, STRENGTH, CHARISMA]
        case "Troll":
            answer.height = 2.5
            answer.weight = 300
            answer.ears = "Slightly pointy, often hidden by horns"
            BUILT_TOUGH.level = 2
            answer.racial_qualities = [THERMOGRAPHIC_VISION, BUILT_TOUGH, DERMAL_DEPOSITS]
            BODY.limit = 9
            AGILITY.limit = 5
            STRENGTH.limit = 9
            CHARISMA.limit = 5
            answer.attributes = [BODY, AGILITY, STRENGTH, CHARISMA]
    answer.metatype = metatype
    return answer


def gen_lifestyle():
    lifestyles = ['Street', 'Squatter', 'Low', 'Middle', 'High', 'Luxary']
    lifestyle = random.choice(lifestyles)
    answer = ReturnObj()
    match lifestyle:
        case 'Street':
            answer.monthly_cost = 0
        case 'Squatter':
            answer.monthly_cost = 500
        case 'Low':
            answer.monthly_cost = 2_000
        case 'Middle':
            answer.monthly_cost = 5_000
        case 'High':
            answer.monthly_cost = 10_000
        case 'Luxary':
            answer.monthly_cost = 100_000
    return answer


def get_priority_table(category=False, priority=False):
    answer = ReturnObj()
    if not category and not priority:
        pass
    match category:
        case "Metatype":
            match priority:
                case 'A':
                    answer.metatype_out = get_metatype(['Dwarf', 'Ork', 'Troll'])
                    answer.adjustment_points = 13
                case 'B':
                    answer.metatype_out = get_metatype(['Dwarf', 'Elf', 'Ork', 'Troll'])
                    answer.adjustment_points = 11
                case 'C':
                    answer.metatype_out = get_metatype(['Dwarf', 'Elf', 'Human', 'Ork', 'Troll'])
                    answer.adjustment_points = 9
                case 'D':
                    answer.metatype_out = get_metatype(['Dwarf', 'Elf', 'Human', 'Ork', 'Troll'])
                    answer.adjustment_points = 4
                case 'E':
                    answer.metatype_out = get_metatype(['Dwarf', 'Elf', 'Human', 'Ork', 'Troll'])
                    answer.adjustment_points = 1
        case "Attributes":
            x = {'A': 24, 'B': 16, 'C': 12, 'D': 8, 'E': 2}
            answer.attributes = x[priority]spells
        case "Skills":
            x = {'A': 32, 'B': 24, 'C': 20, 'D': 16, 'E': 10}
            answer.skills = x[priority]
        case "Magic or Resonance":
            match priority:
                case 'A':
                    answer.full = 4
                    answer.aspected = 5
                    answer.mystic_adept = 4
                    answer.adept = 4
                    answer.technomancer = 4
                case 'B':
                    answer.full = 3
                    answer.aspected = 4
                    answer.mystic_adept = 3
                    answer.adept = 3
                    answer.technomancer = 3
                    pass
                case 'C':
                    answer.full = 2
                    answer.aspected = 3
                    answer.mystic_adept = 2
                    answer.adept = 2
                    answer.technomancer = 2
                    pass
                case 'D':
                    answer.full = 1
                    answer.aspected = 2
                    answer.mystic_adept = 1
                    answer.adept = 1
                    answer.technomancer = 2
                    pass
                case 'E':
                    answer.mundane = True
                    pass
        case "Resources":
            match priority:
                case 'A':
                    answer.resources = 450_000
                case 'B':
                    answer.resources = 275_000 
                case 'C':
                    answer.resources = 150_000
                case 'D':
                    answer.resources = 50_000
                case 'E':
                    answer.resources = 8_000
    return answerspells

PRIORITY_PICKS = ['A', 'B', 'C', 'D', 'E']

def get_spells(ch: Character):
    spells = []
    for _ in range(2 * ch.magic):
        while True:
            ROLL_SPELL = random.choice(Spell.items)
            if ROLL_SPELL not in ch.spells:
                spells.append(ROLL_SPELL)
                break
    return spells

def generate_adept(ch: Character):
    MAGIC_TYPE = "Adept"spells
    magic_power = random.choice(['A', 'B', 'C'])
    x = get_priority_table('Magic or Resonance', magic_power)
    ch.magic = ch.magic + x.adept
    PRIORITY_PICKS.pop(PRIORITY_PICKS.index(magic_power))
    y = get_priority_table('Metatype', random.choice(PRIORITY_PICKS))
    ch.adept_powers = {}
    return attrAsDict(y)
def generate_combat_mage(ch: Character):
    MAGIC_TYPE = "Magician / 'Full'"
    magic_power = random.choice(['A', 'B', 'C'])
    x = get_priority_table('Magic or Resonance', magic_power)
    ch.magic = x.full

    ch.spells = SpellList(get_spells(ch))
    print(ch.spells)
    pass
def generate_covert_ops(ch: Character):
    pass
def generate_decker(ch: Character):
    pass
def generate_face(ch: Character):spells
    pass
def generate_rigger(ch: Character):
    pass
def generate_samurai(ch: Character):
    pass
def generate_shaman(ch: Character):
    MAGIC_TYPE = "Mystic Adept"
    magic_power = random.choice(['A', 'B', 'C'])
    x = get_priority_table('Magic or Resonance', magic_power)
    ch.magic = x.mystic
    ch.spells = []
    for _ in range(2 * ch.attributes['Magic']):
        while True:
            ROLL_SPELL = random.choice(Spell.items)
            if ROLL_SPELL in ch.spells:
                continue
            else:
                break
    pass
def generate_technomancer(ch: Character):
    MAGIC_TYPE = "Technomancer"
    resonance_power = random.choice(['A', 'B'])
    x = get_priority_table('Magic / Resonance', resonance_power)
    ch.resonance = x.technomancer

    ch.complex_forms = {}
    pass
def generate_weapon_specs(ch: Character):
    pass

def generate_character(name="Jeff"):
    x = Character(name)

    x.archetype = random.choice(Archetype.items)
    x.qualities = pick_qualities(x)

def get_template_technomancer():
    tm = Character("Technomancer")
    tm.Body = tm.Body + 5
    tm.Agility = tm.Agility + 2
    tm.Reaction = tm.Reaction + 2 
    tm.Strength = tm.Strength + 5
    tm.Willpower = tm.Willpower + 7 
    tm.Logic = tm.Logic + 5
    tm.Intuition = tm.Intuition + 6
    tm.Charisma = tm.Charisma + 5
    tm.Edge = tm.Edge + 3
    tm.Resonance = tm.Resonance + 6
    tm.Essence = tm.Essence + 6

    tm.Initiative = tm.Reaction + tm.Intuition

    tm.ComplexForms = {}




character = Character("Tony Boyce")
y = generate_combat_mage(character)
