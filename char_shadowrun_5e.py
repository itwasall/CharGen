import chargen

class Attribute:
    def __init__(name: str, self, value: int = 0):
        self.name = name
        self.value = value
        self.attribute_limit = 0

    def __add___(amount: int, self):
        self.value += amount
        return Attribute(self.name, self.value)

    def set_attribute_limit(value: int, self):
        self.attribute_limit = value
        return

    def set_attribute_value(value: int, self):
        self.value = value
        return

class Attributes:
    def __init__(self):
        self.Body = Attribute("Body")
        self.Agility = Attribute("Agility")
        self.Reaction = Attribute("Reaction")
        self.Strength = Attribute("Strength")
        self.Charisma = Attribute("Charisma")
        self.Intuition = Attribute("Intuition")
        self.Logic = Attribute("Logic")
        self.Willpower = Attribute("Willpower")
        self.Edge = Attribute("Edge")
        self.Essence = Attribute("Essence")

        self.AttributeList = self.rebuild_attribute_list()

    def rebuild_attribute_list(self):
        return [self.Body, self.Agility, self.Reaction, self.Strength, self.Willpower, self.Logic, self.Intuition, self.Charisma, self.Edge, self.Essence]

    def set_starting_limit_values(data: dict, self):
        for value in data.keys():
            match value:
                case ["Body", "BODY"]:
                    self.Body.set_attribute_value(data[value][0])
                    self.Body.set_attribute_limit(data[value][1])
                case ["Agility", "AGI"]:
                    self.Agility.set_attribute_value(data[value][0])
                    self.Agility.set_attribute_limit(data[value][1])
                case ["Reaction", "REA"]:
                    self.Reaction.set_attribute_value(data[value][0])
                    self.Reaction.set_attribute_limit(data[value][1])
                case ["Strength", "STR"]:
                    self.Strength.set_attribute_value(data[value][0])
                    self.Strength.set_attribute_limit(data[value][1])
                case ["Willpower", "WIL"]:
                    self.Willpower.set_attribute_value(data[value][0])
                    self.Willpower.set_attribute_limit(data[value][1])
                case ["Logic", "LOG"]:
                    self.Logic.set_attribute_value(data[value][0])
                    self.Logic.set_attribute_limit(data[value][1])
                case ["Intuition", "INT"]:
                    self.Intuition.set_attribute_value(data[value][0])
                    self.Intuition.set_attribute_limit(data[value][1])
                case ["Charisma", "CHA"]:
                    self.Charisma.set_attribute_value(data[value][0])
                    self.Charisma.set_attribute_limit(data[value][1])
                case ["Edge", "EDG"]:
                    self.Edge.set_attribute_value(data[value][0])
                    self.Edge.set_attribute_limit(data[value][1])
                case ["Essence", "ESS"]:
                    self.Essence.set_attribute_value(data[value][0])
                    raise ValueError("Essence does not have a limit")
                case _:
                    pass


class Metatype:
    def __init__(name: str, self):
        self.name = name
        self.racial_attributes = Attributes()

    def __repr__(self):
        return self.name


class Type:
    def __init__(name: str, self):
        self.name = name


class ConditionMonitor:
    def __init__(self, overflow: int, physical: int = 0, stun : int = 0):
        self.damagetrack_physical = physical
        self.damagetrack_stun = stun
        self.overflow = overflow

    def __add__(amount: int, _type: str, self):
        if _type.capitalize() == "Physical":
            self.damagetrack_physical += amount
        elif _type.capitalize() == "Stun":
            self.damagetrack_stun += amount
        elif _type.capitalize() == "Overflow":
            self.overflow += amount
        else:
            pass
        return ConditionMonitor(self.overflow, self.damagetrack_physical, self.damagetrack_stun)


class Qualitiy:
    def __init__(name: str, polarity: int, cost, self):
        self.name = name
        # Positive qualities have a polarity of 1, thus making their cost positive.
        # Negative qualities have a polarity of -1, thus making their cost negative (or in essence, adding points)
        self.polarity = polarity
        self.quantity = 1 # The number of times this quality can be taken. Some qualities can be taken multiple times naturally
        self.cost = self.calc_cost(cost)
        if type(self.cost) == bool:
            raise TypeError(f"Cost calculation errored the fuck out. How do you explain this? {self.cost}")

    def calc_cost(cost, self):
        if type(cost) == int:
            return cost
        if type(cost) == list:
            if len(cost) != 3:
                return False
            match cost[1]:
                case "or":
                    return [cost[0], cost[2]]
                case "each":
                    self.quantity = cost[2]
                    return cost[0]
                case "to":
                    return [i for i in range(cost[0], cost[2])]
                case 6: # Catches 'Dependant(s) Quality
                    return cost
                case _:
                    return False
        pass

class Skill:
    def __init__(name: str, attribute: Attribute, skill_type: str, self, rating: int = 0, category = None):
        self.name = name
        self.attribute = attribute.name
        self.skill_type = skill_type
        self.rating = rating 
        self.category = None
    
    def __add__(amount, self):
        self.rating += amount
        return Skill(self.attribute, self.skill_type, self.rating)

    def __repr__(self):
        return (self.name, self.value)

class Skill_Group:
    def __init__(name: str, skills: list, self):
        self.name = name
        self.skills = skills

    def __repr__(self):
        return self.skills

"""
    ATTRIBUTES
"""
BODY = Attribute("Body")
AGILITY = Attribute("Agility")
REACTION = Attribute("Reaction")
STRENGTH = Attribute("Strength")
CHARISMA = Attribute("Charisma")
INTUITION = Attribute("Intuition")
LOGIC = Attribute("Logic")
WILLPOWER = Attribute("Willpower")
EDGE = Attribute("Edge")
ESSENCE = Attribute("Essence")
MAGIC = Attribute("Magic")
RESONANCE = Attribute("Resonance")
        
"""
    ACTIVE SKILLS
"""
# =============== AGILITY ================
ARCHERY = Skill("Archery", AGILITY, "Active")
AUTOMATICS = Skill("Automatics", AGILITY, "Active")
BLADES = Skill("Blades", AGILITY, "Active")
CLUBS = Skill("Clubs", AGILITY, "Active")
ESCAPE_ARTIST = Skill("Escape_artist", AGILITY, "Active")
EXOTIC_MELEE_WEAPON = Skill("Exotic_melee_weapon", AGILITY, "Active")
EXOTIC_RANGED_WEAPON = Skill("Exotic_ranged_weapon", AGILITY, "Active")
GUNNERY = Skill("Gunnery", AGILITY, "Active")
GYMNASTICS = Skill("Gymnastics", AGILITY, "Active")
HEAVY_WEAPONS = Skill("Heavy_weapons", AGILITY, "Active")
LOCKSMITH = Skill("Locksmith", AGILITY, "Active")
LONGARMS = Skill("Longarms", AGILITY, "Active")
PALMING = Skill("Palming", AGILITY, "Active")
PISTOLS = Skill("Pistols", AGILITY, "Active")
SNEAKING = Skill("Sneaking", AGILITY, "Active")
THROWING = Skill("Throwing", AGILITY, "Active")
WEAPONS = Skill("Weapons", AGILITY, "Active")
UNARMED_COMBAT = Skill("Unarmed_combat", AGILITY, "Active")
# =============== BODY ===================
DIVING = Skill("Diving", BODY, "Active")
FREE_FALL = Skill("Free_fall", BODY, "Active")
# =============== REACTION ===============
PILOT_AEROSPACE = Skill("Pilot Aerospace", REACTION, "Active")
PILOT_AIRCRAFT = Skill("Pilot Aircraft", REACTION, "Active")
PILOT_EXOTIC_VEHICLE_SPECIFIC = Skill("Pilot Exotic Vehicle Specific", REACTION, "Active")
PILOT_GROUND_CRAFT = Skill("Pilot Ground Craft", REACTION, "Active")
PILOT_WALKER = Skill("Pilot Walker", REACTION, "Active")
PILOT_WATERCRAFT = Skill("Pilot Watercraft", REACTION, "Active")
# =============== STRENGTH ===============
RUNNING = Skill("Running", STRENGTH, "Active")
SWIMMING = Skill("Swimming", STRENGTH, "Active")
# =============== CHARISMA ===============
ANIMAL_HANDLING = Skill("Animal_Handling", CHARISMA, "Active")
CON = Skill("Con", CHARISMA, "Active")
ETIQUETTE = Skill("Etiquette", CHARISMA, "Active")
IMPERSONATION = Skill("Impersonation", CHARISMA, "Active")
INSTRUCTION = Skill("Instruction", CHARISMA, "Active")
INTIMIDATION = Skill("Intimidation", CHARISMA, "Active")
LEADERSHIP = Skill("Leadership", CHARISMA, "Active")
NEGOTIATION = Skill("Negotiation", CHARISMA, "Active")
PERFORMANCE = Skill("Performance", CHARISMA, "Active")
# =============== INTUITION ==============
ARTISAN = Skill("Artisan", INTUITION, "Active")
ASSENSING = Skill("Assensing", INTUITION, "Active")
DISGUISE = Skill("Disguise", INTUITION, "Active")
INTERESTS_KNOWLEDGE = Skill("Interests Knowledge", INTUITION, "Active")
LANGUAGE = Skill("Language", INTUITION, "Active")
NAVIGATION = Skill("Navigation", INTUITION, "Active")
PERCEPTION = Skill("Perception", INTUITION, "Active")
STREET_KNOWLEDGE = Skill("Street Knowledge", INTUITION, "Active")
TRACKING = Skill("Tracking", INTUITION, "Active")
# =============== LOGIC ==================
ACADEMIC_KNOWLEDGE = Skill("Academic_Knowledge", LOGIC, "Active")
AERONAUTICS_MECHANIC = Skill("Aeronautics_Mechanic", LOGIC, "Active")
ARCANA = Skill("Arcana", LOGIC, "Active")
ARMORER = Skill("Armorer", LOGIC, "Active")
AUTOMOTIVE_MECHANIC = Skill("Automotive_Mechanic", LOGIC, "Active")
BIOTECHNOLOGY = Skill("Biotechnology", LOGIC, "Active")
CHEMISTRY = Skill("Chemistry", LOGIC, "Active")
COMPUTER = Skill("Computer", LOGIC, "Active")
CYBERTECHNOLOGY = Skill("Cybertechnology", LOGIC, "Active")
CYBERCOMBAT = Skill("Cybercombat", LOGIC, "Active")
DEMOLITIONS = Skill("Demolitions", LOGIC, "Active")
ELECTRONIC_WARFARE = Skill("Electronic_Warfare", LOGIC, "Active")
FIRST_AID = Skill("First_Aid", LOGIC, "Active")
FORGERY = Skill("Forgery", LOGIC, "Active")
INDUSTRIAL_MECHANIC = Skill("Industrial_Mechanic", LOGIC, "Active")
HACKING = Skill("Hacking", LOGIC, "Active")
HARDWARE = Skill("Hardware", LOGIC, "Active")
MEDICINE = Skill("Medicine", LOGIC, "Active")
NAUTICAL_MECHANIC = Skill("Nautical_Mechanic", LOGIC, "Active")
PROFESSIONAL_KNOWLEDGE = Skill("Professional_Knowledge", LOGIC, "Active")
SOFTWARE = Skill("Software", LOGIC, "Active")
# =============== WILLPOWER ==============
ASTRAL_COMBAT = Skill("Astral Combat", WILLPOWER, "Active")
SURVIVAL = Skill("Survival", WILLPOWER, "Active")
# =============== MAGIC ==================
ALCHEMY = Skill("Alchemy", MAGIC, "Active")
ARTIFICING = Skill("Artificing", MAGIC, "Active")
BANISHING = Skill("Banishing", MAGIC, "Active")
BINDING = Skill("Binding", MAGIC, "Active")
COUNTERSPELLING = Skill("Counterspelling", MAGIC, "Active")
DISENCHANTING = Skill("Disenchanting", MAGIC, "Active")
RITUAL_SPELLCASTING = Skill("Ritual Spellcasting", MAGIC, "Active")
SPELLCASTING = Skill("Spellcasting", MAGIC, "Active")
sUMMONING = Skill("Summoning", MAGIC, "Active")
# =============== RESONANCE ==============
COMPILING = Skill("Compiling", RESONANCE, "Active")
DECOMPILING = Skill("Decompiling", RESONANCE, "Active")
REGISTERING = Skill("Registering", RESONANCE, "Active")

"""
    KNOWLEDGE SKILLS
"""
# =============== ACADEMIC ===============
BIOLOGY = Skill("Biology", LOGIC, "Knowledge", category="Academic")
MEDICINE = Skill("Medicine", LOGIC, "Knowledge", category="Academic")
MAGIC_THEORY = Skill("Magic_Theory",LOGIC, "Knowledge", category="Academic")
POLITICS = Skill("Politics", LOGIC, "Knowledge", category="Academic")
PHILOSOPHY = Skill("Philosophy", LOGIC, "Knowledge", category="Academic")
LITERATURE = Skill("Literature", LOGIC, "Knowledge", category="Academic")
HISTORY = Skill("History", LOGIC, "Knowledge", category="Academic")
MUSIC = Skill("Music", LOGIC, "Knowledge", category="Academic")
PARABOTANY = Skill("Parabotany", LOGIC, "Knowledge", category="Academic")
PARAZOOLOGY = Skill("Parazoology", LOGIC, "Knowledge", category="Academic")


"""
    METATYPES
"""
HUMAN = Metatype("Human")
HUMAN.racial_attributes.set_starting_limit_values({'BODY': [1,6], 'AGI': [1, 6], 'REA': [1, 6], 'STR': [1, 6], 'WIL': [1, 6], 'LOG': [1, 6], 'INT': [1, 6], 'CHA': [1, 6], 'EDG': [2, 7], 'ESS': [6]})
ELF = Metatype("Elf")
ELF.racial_attributes.set_starting_limit_values({'BODY': [1,6], 'AGI': [2, 7], 'REA': [1, 6], 'STR': [1, 6], 'WIL': [1, 6], 'LOG': [1, 6], 'INT': [1, 6], 'CHA': [3, 8], 'EDG': [1, 6], 'ESS': [6]})
DWARF = Metatype("Dwarf")
DWARF.racial_attributes.set_starting_limit_values({'BODY': [3,8], 'AGI': [1, 6], 'REA': [1, 5], 'STR': [3, 8], 'WIL': [2, 7], 'LOG': [1, 6], 'INT': [1, 6], 'CHA': [1, 6], 'EDG': [1, 6], 'ESS': [6]})
ORK = Metatype("Ork")
ORK.racial_attributes.set_starting_limit_values({'BODY': [1,6], 'AGI': [1, 6], 'REA': [1, 6], 'STR': [1, 6], 'WIL': [1, 6], 'LOG': [1, 6], 'INT': [1, 6], 'CHA': [1, 6], 'EDG': [1, 6], 'ESS': [6]})
TROLL = Metatype("Troll")
TROLL.racial_attributes.set_starting_limit_values({'BODY': [1,6], 'AGI': [1, 6], 'REA': [1, 6], 'STR': [1, 6], 'WIL': [1, 6], 'LOG': [1, 6], 'INT': [1, 6], 'CHA': [1, 6], 'EDG': [1, 6], 'ESS': [6]})

"""
    CHARACTER TYPES
"""
FACE = Type('Face')
SPELLCASTER = Type('Spellcaster')
DECKER = Type('Decker')
TECHNOMANCER = Type('Technomancer')
RIGGER = Type('Rigger')
STREETSAMURAI = Type('Street Samurai')

"""
    PRIORITY TABLE
"""
PRIORITY_TABLE = {
    'A': {
        'Metatype': [(Human, 9), (Elf, 8), (Dwarf, 7), (Ork, 7), (Troll, 5)],
        'Attributes': 24,
        'MagicResonance': {
            'Magician or Mystic Adept': { 'Magic': 6, 'Skills': {'Type': 'Magic', 'Rating': 5, 'Quantity': 2 }, 'Spells': 10 },
            'Technomancer': { 'Resonance': 6, 'Skills': {'Type': 'Resonance', 'Rating': 5, 'Quantity': 2 }, 'Complex Forms': 5 }
        },
        'Skills': [46, 10],
        'Money': 450_000
    },
    'B': {
        'Metatype': [(Human, 7), (Elf, 6), (Dwarf, 4), (Ork, 4), (Troll, 0)],
        'Attributes': 20,
        'MagicResonance':{
            'Magician or Mystic Adept': { 'Magic': 6, 'Skills': {'Type': 'Magic', 'Rating': 4, 'Quantity': 2}, 'Spells': 7 },
            'Technomancer': { 'Resonance': 4, 'Skills': {'Type': 'Resonance', 'Rating': 4, 'Quantity': 2}, 'Complex Forms': 2 },
            'Adept': { 'Magic': 6, 'Skills': {'Type': 'Active', 'Rating': 4, 'Quantity': 1}},
            'Aspected Magician': { 'Magic': 5, 'Skills': {'Type': 'Magic Group', 'Rating': 4, 'Quantity': 1}}
        },
        'Skills': [36, 5],
        'Money': 275_000
    },
    'C': {
        'Metatype': [(Human, 5), (Elf, 3), (Dwarf, 1), (Ork, 0)],
        'Attributes': 16,
        'MagicResonance': {
            'Magician or Mystic Adept': { 'Magic': 3, 'Spells': 5},
            'Technomancer': { 'Resonance': 3, 'Complex Forms': 1},
            'Adept': { 'Magic': 4, 'Skills': {'Type': 'Active', 'Rating': 2, 'Quantity': 1}},
            'Aspected Magician': { 'Magic': 3, 'Skills': {'Type': 'Magic Group', 'Rating': 2, 'Quantity': 1}}
        },
        'Skills': [28,2],
        'Money': 140_000
    },
    'D': {
        'Metatype': [(Human, 3), (Elf, 0)],
        'Attributes': 14,
        'MagicResonance': {
            'Adept': {'Magic': 2},
            'Aspected Magician': {'Magic': 2}
        },
        'Skills': [22, 0],
        'Money': 50_000
    },
    'E': {
        'Metatype': [(Human, 1)],
        'Attributes': 12,
        'Skills': [18, 0],
        'Money': 6_000
    }
}

character = {
    'Name': "",
    'Metatype': Metatype
}

def generate_character():
    # PHASE 1: CONCEPT

    # PHASE 2: PR
    pass
