import random

class AbstractBaseClass():
    def __init__(self, name, **kwargs):
        self.name = name
        for k, d in kwargs.items():
            self.__setattr__(k, d)

    def __repr__(self):
        return self.name

class Metatype(AbstractBaseClass):
    items = []
    def __init__(self, name, **kwargs):
        Metatype.items.append(self)
        super().__init__(self, name, **kwargs)

class Archetype(AbstractBaseClass):
    items = []
    def __init__(self, name, **kwargs):
        Archetype.items.append(self)
        super().__init__(self, name, **kwargs)

class ReturnObj(AbstractBaseClass):
    def __init__(self, name, **kwargs):
        super().__init__(self, name, **kwargs)

class Quality(AbstractBaseClass):
    items = []
    def __init__(self, name, **kwargs):
        Quality.items.append(self)
        super().__init__(self, name, **kwargs)

class Skill(AbstractBaseClass):
    items = []
    def __init__(self, name, **kwargs):
        Skill.items.append(self)
        self.rank = 1
        super().__init__(self, name, **kwargs)


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
    def __init__(self, name, value = 1, limit = 6):
        self.name = name
        self.value = value
        self.limit = limit
    def __repr__(self):
        return f"{self.name}: {self.value}/{self.limit}"
    def __add__(self, x, limit_raise=False):
        if limit_raise:
            return Attribute(self.name, self.value, self.limit + x)
        return Attribute(self.name, self.value + x, self.limit)


BODY = Attribute('Body')
AGILITY = Attribute('Agility')
REACTION = Attribute('Reaction')
STRENGTH = Attribute('Strength')
WILLPOWER = Attribute('Willpower')
LOGIC = Attribute('Logic')
INTUITION = Attribute('Intuition')
CHARISMA = Attribute('Charisma')
EDGE = Attribute('Edge')
MAGIC = Attribute('Magic', value = 0)
RESONANCE = Attribute('Resonance', value = 0)



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


# ARCHETYPE
ADEPT = Archetype('Adept')
FACE = Archetype('Face')
RIGGER = Archetype('Rigger')
STREET_SAMURAI = Archetype('Street Samurai')
STREET_SHAMAN = Archetype('Street Shaman')
TECHNOMANCER = Archetype('Technomancer')
WEAPONS_SPECIALIST = Archetype('Weapons Specialist')

# QUALITIES
# POSITIVE
AMBIDEXTROUS = Quality('Ambidextrous', cost=4)
ANALYTICAL_MIND = Quality('Analytical_mind', cost=3)
APTITUDE = Quality('Aptitude', cost=12)
ASTRAL_CHAMELEON = Quality('Astral_chameleon', cost=9)
BLANDNESS = Quality('Blandness', cost=8)
BUILT_TOUGH = Quality('Built_tough', cost=4, levels=4)
CAT_LIKE = Quality('Cat_like', cost=12)
DERMAL_DEPOSITS = Quality('Dermal_deposits', cost=7)
DOUBLE_JOINTED = Quality('Double_jointed', cost=12)
FIRST_IMPRESSION = Quality('First_impression', cost=12)
FOCUSED_CONCERNTRATION = Quality('Focused_concerntration', cost=12, levels=3)
GEARHEAD = Quality('Gearhead', cost=10)
GUTS = Quality('Guts', cost=12)
HARDENING = Quality('Hardening', cost=10)
HIGH_PAIN_TOLERANCE = Quality('High_pain_tolerance', cost=7)
HOME_GROUND = Quality('Home_ground', cost=10)
HUMAN_LOOKING = Quality('Human_looking', cost=8)
INDOMITABLE = Quality('Indomitable', cost=12)
JURY_RIGGER = Quality('Jury_rigger', cost=12)
LONG_REACH = Quality('Long_reach', cost=12)
LOW_LIGHT_VISION = Quality('Low_light_vision', cost=6)
MAGIC_RESISTANCE = Quality('Magic_resistance', cost=8)
MENTOR_SPIRIT = Quality('Mentor_spirit', cost=10)
PATHOGEN_RESISTANCE = Quality('Pathogen_resistance', cost=12)
PHOTOGRAPHIC_MEMORY = Quality('Photographic_memory', cost=12)
QUICK_HEALER = Quality('Quick_healer', cost=8)
THERMOGRAPHIC_VISION = Quality('Thermographic_vision', cost=8)
TOUGHNESS = Quality('Toughness', cost=12)
TOXIS_RESISTANCE = Quality('Toxis_resistance', cost=12)
WILL_TO_LIVE = Quality('Will_to_live', cost=8, levels=3)

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
                

def generate_metatype(metatypes):
    answer = ReturnObj()
    metatype = random.choice(metatypes)
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
        case 'Squatter'
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
                    answer.metatypes = ['Dwarf', 'Ork', 'Troll'] 
                    answer.adjustment_points = 13
                case 'B':
                    answer.metatypes = ['Dwarf', 'Elf', 'Ork', 'Troll'] 
                    answer.adjustment_points = 11
                case 'C':
                    answer.metatypes = ['Dwarf', 'Elf', 'Human', 'Ork', 'Troll'] 
                    answer.adjustment_points = 9
                case 'D':
                    answer.metatypes = ['Dwarf', 'Elf', 'Human', 'Ork', 'Troll'] 
                    answer.adjustment_points = 4
                case 'E':
                    answer.metatypes = ['Dwarf', 'Elf', 'Human', 'Ork', 'Troll'] 
                    answer.adjustment_points = 1
        case "Attributes":
            x = {'A': 24, 'B': 16, 'C': 12, 'D': 8, 'E': 2}
            answer.attributes = x[priority]
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
    return answer

PRIORITY_PICKS = ['A', 'B', 'C', 'D', 'E']

def generate_adept(ch: Character):
    MAGIC_TYPE = "Adept"
    magic_power = random.choice(['A', 'B', 'C'])
    x = get_priority_table('Magic / Resonance', magic_power)
    PRIORITY_PICKS.pop(PRIORITY_PICKS.index(magic_power))
    ch.adept_powers = {}
    pass
def generate_combat_mage(ch: Character):
    MAGIC_TYPE = "Magician / 'Full'"
    magic_power = random.choice(['A', 'B', 'C'])
    x = get_priority_table('Magic / Resonance', magic_power)
    ch.attributes['Magic'] = x.full
    ch.spells = 2 * ch.attributes['Magic']
    pass
def generate_covert_ops(ch: Character):
    pass
def generate_decker(ch: Character):
    pass
def generate_face(ch: Character):
    pass
def generate_rigger(ch: Character):
    pass
def generate_samurai(ch: Character):
    pass
def generate_shaman(ch: Character):
    MAGIC_TYPE = "Mystic Adept"
    magic_power = random.choice(['A', 'B', 'C'])
    x = get_priority_table('Magic / Resonance', magic_power)
    ch.spells = {}
    pass
def generate_technomancer(ch: Character):
    MAGIC_TYPE = "Technomancer"
    resonance_power = random.choice(['A', 'B'])
    x = get_priority_table('Magic / Resonance', resonance_power)
    ch.attributes['Resonance'] = x.technomancer

    ch.complex_forms = {}
    pass
def generate_weapon_specs(ch: Character):
    pass

def generate_character(name="Jeff"):
    x = Character(name)

    x.archetype = random.choice(Archetype.items)
    x.qualities = pick_qualities(x)

