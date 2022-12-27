import chargen
from yaml import safe_load

"""
    GOALS

Lets set out some design goals and then have nowhere to formally put them.

    1) Generate Character 
    2) Lil TUI Interface that allows the user to, once a character is fully generated, scroll through menus to look at a weapon in more detail for example.
    2a) I am scrapping this idea immediately after I had it because adding all the different and differing stats for the multitude of pieces of gear is long boring and isn't
            required. A page number reference will suffice.
"""

gear = safe_load(open('./shadowrun_5e_data/gear.yaml', 'rt'))

class Attribute:
    def __init__(self, name, value: int = 0):
        self.name = name
        self.value = value
        self.attribute_limit = 0

    def __add___(self, amount: int):
        self.value += amount
        return Attribute(self.name, self.value)

    def set_attribute_limit(self, value: int):
        self.attribute_limit = value
        return

    def set_attribute_value(self, value: int):
        self.value = value
        return

    def __repr__(self):
        return f"{self.name}: [{self.value}/{self.attribute_limit}]"

    def what_is(self):
        return f"{self.name} is an Attribute"

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

    def set_starting_limit_values(self, data: dict):
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
    def __init__(self, name: str):
        self.name = name
        self.racial_attributes = Attributes()

    def __repr__(self):
        return self.name

    def what_is(self):
        return f"{self.name} is a Metatype"


class Type:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name

    def what_is(self):
        return f"{self.name} is a Character Type"

class DamageType(Type):
    def __init__(self, name: str):
        super().__init__(name)
    
    def what_is(self):
        return f"{self.name} is a Damage Type"



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

    def what_is(self):
        return f"{self.name} is a Quality"

class Skill:
    def __init__(self, name: str, attribute: Attribute, skill_type: str, rating: int = 0, category = None):
        self.name = name
        self.attribute = attribute.name
        self.skill_type = skill_type
        self.rating = rating 
        self.category = None
    
    def __add__(self, amount):
        self.rating += amount
        return Skill(self.attribute, self.skill_type, self.rating)

    def __repr__(self):
        return (self.name, self.value)

    def what_is(self):
        return f"{self.name} is a Skill of '{self.skill_type}' type"

class Skill_Group:
    def __init__(self, name: str, skills: list):
        self.name = name
        self.skills = skills

    def __repr__(self):
        return self.skills

    def what_is(self):
        return f"{self.name} is a Skill Group comprising {', '.join([skill for skill in self.skills])}"

"""
"""

class Gear:
    def __init__(self, name, cost, page_ref, **kwargs):
        self.name = name
        self.cost = cost
        self.page_ref = page_ref
        self.category = None
        self.subtype = None
    
    def what_is(self):
        return f"[{self.category}/{self.subtype}] - {self.name} is a piece of Gear"

    def __repr__(self):
        return self.name



class Firearm(Gear):
    def __init__(self, name, cost, page_ref, avail, subtype, **kwargs):
        super().__init__(name, cost, page_ref)
        self.avail = avail
        self.category = "Firearm"
        self.subtype = subtype
        for key in kwargs.keys():
            match key:
                case "damage":
                    self.damage = kwargs['damage']

class FirearmAcc(Gear):
    def __init__(self, name, cost, page_ref, mount, avail, **kwargs):
        super().__init__(name, cost, page_ref)
        self.category = "Firearm Accessory"
        self.mount = mount
        self.avail = avail
        for key in kwargs.keys():
            pass

class Ammo(Gear):
    def __init__(self, name, cost, page_ref, avail, **kwargs):
        super().__init__(name, cost, page_ref)
        self.category = "Ammunition"
        self.avail = avail
        for key in kwargs.keys():
            pass


class Melee_Weapons:
    def __init__(self, name: str, value: int):
        super().__init__(name, value)
        self.category = "Melee Weapons"

class GearAvailability:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self.name



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
SUMMONING = Skill("Summoning", MAGIC, "Active")
# =============== RESONANCE ==============
COMPILING = Skill("Compiling", RESONANCE, "Active")
DECOMPILING = Skill("Decompiling", RESONANCE, "Active")
REGISTERING = Skill("Registering", RESONANCE, "Active")

"""
    KNOWLEDGE SKILLS

These are more fluff than the more mechanics-based 'Active' skills
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
# =============== INTERESTS ==============
CURRENT_SIMSENSE_MOVIES = Skill("Current_Simsense_movies", INTUITION, "Knowledge", category="Interests")
POPULAR_TRIDEO_SHOWS = Skill("Popular_Trideo_Shows", INTUITION, "Knowledge", category="Interests")
TWENTIETH_CENTURY_TRIVIA = Skill("Twentieth_Century_trivia", INTUITION, "Knowledge", category="Interests")
ELVEN_WINE = Skill("Elven_Wine", INTUITION, "Knowledge", category="Interests")
URBAN_BRAWL = Skill("Urban_Brawl", INTUITION, "Knowledge", category="Interests")
COMBAT_BIKING = Skill("Combat_Biking", INTUITION, "Knowledge", category="Interests")
POP_MUSIC = Skill("Pop_music", INTUITION, "Knowledge", category="Interests")
# =============== PROFESSIONAL ===========
JOURNALISM = Skill("Journalism", LOGIC, "Knowledge", category="Professional")
BUSINESS = Skill("Business", LOGIC, "Knowledge", category="Professional")
LAW = Skill("Law", LOGIC, "Knowledge", category="Professional")
MILITARY_SERVICE = Skill("Military_Service", LOGIC, "Knowledge", category="Professional")
# =============== STREET =================
GANG_IDENTIFICATION = Skill("Gang_Identification", INTUITION, "Knowledge", category="Street")
CRIMINAL_ORGANISATIONS = Skill("Criminal_Organisations", INTUITION, "Knowledge", category="Street")
SMUGGLING_ROUTES = Skill("Smuggling_Routes", INTUITION, "Knowledge", category="Street")
FENCES = Skill("Fences", INTUITION, "Knowledge", category="Street")

"""
    LANGUAGE SKILLS

Sperenthiel - Language of the Elves
OR_ZET -> Or'Zet - Language of the Orks

Category of 'Dialect' refers to how one speaks 
Category of 'Tongue' refers to which language one speaks in
"""
CITYSPEAK = Skill("Cityspeak", INTUITION, "Language", category="Dialect")
CREOLE = Skill("Creole", INTUITION, "Language", category="Dialect")
STREET = Skill("Street", INTUITION, "Language", category="Dialect")
L33TSPEAK = Skill("l33tspeak", INTUITION, "Language", category="Dialect")
MILSPEC = Skill("Milspec", INTUITION, "Language", category="Dialect")
CORP = Skill("Corp", INTUITION, "Language", category="Dialect")
ORBIBAL = Skill("Orbibal", INTUITION, "Language", category="Dialect")
SPERENTHIEL = Skill("Sperenthiel", INTUITION, "Language", category="Tongue")
OR_ZET = Skill("Or'Zet", INTUITION, "Language", category="Tongue") 
ENGLISH = Skill("English", INTUITION, "Language", category="Tongue")
JAPANESE = Skill("Japanese", INTUITION, "Language", category="Tongue")
MANDARIN = Skill("Mandarin", INTUITION, "Language", category="Tongue")
RUSSIAN = Skill("Russian", INTUITION, "Language", category="Tongue")
FRENCH = Skill("French", INTUITION, "Language", category="Tongue")
ITALIAN = Skill("Italian", INTUITION, "Language", category="Tongue")
GERMAN = Skill("German", INTUITION, "Language", category="Tongue")
AZLANDER_SPANISH = Skill("Azlander_Spanish", INTUITION, "Language", category="Tongue")
SPANISH = Skill("Spanish", INTUITION, "Language", category="Tongue")
LAKOTA = Skill("Lakota", INTUITION, "Language", category="Tongue")
DAKOTA = Skill("Dakota", INTUITION, "Language", category="Tongue")
DINE = Skill("Dine", INTUITION, "Language", category="Tongue")

"""
    SKILL GROUPS
"""
ACTING = Skill_Group("Acting", [CON, IMPERSONATION, PERFORMANCE])
ATHLETICS = Skill_Group("Athletics", [GYMNASTICS, RUNNING, SWIMMING])
BIOTECH = Skill_Group("Biotech", [CYBERTECHNOLOGY, FIRST_AID, MEDICINE])
CLOSE_COMBAT = Skill_Group("Close_Combat", [BLADES, CLUBS, UNARMED_COMBAT])
CONJURING = Skill_Group("Conjuring", [BANISHING, BINDING, SUMMONING])
CRACKING = Skill_Group("Cracking", [CYBERCOMBAT, ELECTRONIC_WARFARE, HACKING])
ELECTRONICS = Skill_Group("Electronics", [COMPUTER, SOFTWARE, HARDWARE])
ENCHANTING = Skill_Group("Enchanting", [ALCHEMY, ARTIFICING, DISENCHANTING])
FIREARMS = Skill_Group("Firearms", [AUTOMATICS, LONGARMS, PISTOLS])
INFLUENCE = Skill_Group("Influence", [ETIQUETTE, LEADERSHIP, NEGOTIATION])
ENGINEERING = Skill_Group("Engineering", [AERONAUTICS_MECHANIC, AUTOMOTIVE_MECHANIC, INDUSTRIAL_MECHANIC, NAUTICAL_MECHANIC])
OUTDOORS = Skill_Group("Outdoors", [NAVIGATION, SURVIVAL, TRACKING])
SORCERY = Skill_Group("Sorcery", [COUNTERSPELLING, RITUAL_SPELLCASTING, SPELLCASTING])
STEALTH = Skill_Group("Stealth", [DISGUISE, PALMING, SNEAKING])
TASKING = Skill_Group("Tasking", [COMPILING, DECOMPILING, REGISTERING])

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
    DAMAGE TYPES
"""
PHYSICAL = DamageType("Physical")
STUN = DamageType("Stun")
ELECTRICAL = DamageType("Electrical")
FLECH = DamageType("Flechette")
"""
    GEAR AVAILABILITY
"""
LEGAL = GearAvailability("Legal")
RESTRICTED = GearAvailability("Restricted")
FORBIDDEN = GearAvailability("Forbidden")
"""
    GEAR

And now, a breakdown on the weird pnemonics the corebook uses to denote certain parameters for pieces of gear.

ACC: Accuracy
AMMO: Ammuition
        (b): Break-Action
        (c): Clip
        (d): Drum
        (m): Internal Magazine
        (ml): Muzzle Loader
        (cy): Cylinder
        (belt): Belt fed
AP: Armor Penetration
AVAIL: Availability
        "-": Easily Accessible & Legal
        R: Restricted
        F: Forbidden
        [no letter]: Legal
DV: Damage Value
        P: Physical
        S: Stun
        (e): Electrical
        (f): Flechette
MODE: Firing Mode
        SS: Single-Shot
        SA: Semi-Automatic
        BF: Burst Fire
        FA: Full Auto
RC: Recoil Compensation
"""
"""
    MELEE GEAR
"""
# COMBAT_AXE = Melee_Weapons()
"""
    FIREARM GEAR
arg order is:
    name, cost, page_ref, avail, subtype, kwargs
"""
# =============== TASERS =================
DEFINANCE_EX_SHOCKER = Firearm("Definance EX Shocker", 250, "p.424", avail="-", subtype="Taser", damage=[9, STUN, ELECTRICAL])
YAMAHA_PULSAR = Firearm("Yamaha Pulsar", 180, 'p. 424', "-", "Taser")
# =============== HOLD-OUTS ==============
FINCHETTI_TIFFANI_NEEDLER = Firearm("Finchetti Tiffani Needler", 1000, 'p. 425', [5, RESTRICTED], "Hold-Outs")
STREETLINE_SPECIAL = Firearm("Streetline Special", 120, 'p. 425', [4, RESTRICTED], "Hold-Outs")
WALTHER_PALM_PISTOL = Firearm("Walther Palm Pistol", 180, 'p425', [4, RESTRICTED], "Hold-Out")
# =============== LIGHT PISTOLS ==========
ARES_LIGHT_FIRE_75 = Firearm("Ares_Light Fire 75", 1250, 'p.425', [6, RESTRICTED], "Light Pistol")
ARES_LIGHT_FIRE_70 = Firearm("Ares Light Fire 70", 200, 'p.425', [3, RESTRICTED], "Light Pistol")
BERETTA_201T = Firearm("Beretta 201T", 210, 'p.425', [7, RESTRICTED], "Light Pistol")
COLT_AMERICA_L36 = Firearm("Colt America L36", 320, 'p.425', [4, RESTRICTED], "Light Pistol")
FICHETTI_SECURITY_600 = Firearm("Fichetti Security 600", 350, 'p.426', [6, RESTRICTED], "Light Pistol")
TAURUS_OMNI_6 = Firearm("Taurus Omni 6", 300, 'p.426', [3, RESTRICTED], "Light Pistol")
# =============== HEAVY PISTOLS ==========
ARES_PREDATOR_V = Firearm("Ares Predator V", 725, 'p.426', [5, RESTRICTED], "Heavy Pistol")
ARES_VIPER_SHOTGUN = Firearm("Ares Viper Shotgun", 380, 'p.426', [8, RESTRICTED], "Heavy Pistol")
BROWNING_ULTRA_POWER = Firearm("Browning Ultra Power", 640, 'p.426', [4, RESTRICTED], "Heavy Pistol")
COLT_GOVERNMENT_2066 = Firearm("Colt Government 2066", 425, 'p.426', [7, RESTRICTED], "Heavy Pistol")
REMINGTON_ROOMSWEEPER = Firearm("Remington Roomsweeper", 250, 'p.426', [6, RESTRICTED], "Heavy Pistol")
RUGER_SUPER_WARHAWK = Firearm("Ruger Super Warhawk", 400, 'p.427', [4, RESTRICTED], "Heavy Pistol")
# =============== MACHINE PISTOLS ========
ARES_CRUSADER_II = Firearm("Ares Crusader II", 830, 'p.427', [9, RESTRICTED], "Machine Pistol")
CESKA_BLACK_SCORPIAN = Firearm("Ceska Black Scorpian", cost=270, page_ref='p.427', avail=[6, RESTRICTED], subtype="Machine Pistol")
STEYR_TMP = Firearm("Steyr TMP", cost=350, page_ref='p.427', avail=[8, RESTRICTED], subtype="Machine Pistol")
# =============== SMGS ===================
COLT_COBRA_TZ_120  = Firearm("Colt Cobra TZ-120", cost=660, page_ref='p.427', avail=[5, RESTRICTED], subtype="Submachine Gun")
FN_P93_PRAETOR = Firearm("FN-P93 Praetor", cost=900, page_ref='p.427', avail=[11, RESTRICTED], subtype="Submachine Gun")
HK_227 = Firearm("HK-227", cost=730, page_ref='p.427', avail=[8, RESTRICTED], subtype="Submachine Gun")
INGRAM_SMARTGUN_X = Firearm("Ingram Smartgun X", cost=800, page_ref='p.427', avail=[6, RESTRICTED], subtype="Submachine Gun")
SCK_MODEL_100 = Firearm("SCK Model 100", cost=875, page_ref='p.428', avail=[6, RESTRICTED], subtype="Submachine Gun")
UZI_IV = Firearm("Uzi IV", cost=450, page_ref='p.428', avail=[4, RESTRICTED], subtype="Submachine Gun")
# =============== ASSAULT RIFLE ==========
AK_97 = Firearm("AK 97", cost=950, page_ref='p.428', avail=[4 ,RESTRICTED], subtype="Assault Rifle")
ARES_ALPHA = Firearm("Ares Alpha", cost=2650, page_ref='p.428', avail=[11, FORBIDDEN], subtype="Assault Rifle")
COLT_M23 = Firearm("Colt-M23", cost=550, page_ref='p.428', avail=[4, RESTRICTED], subtype="Assault Rifle")
FN_HAR = Firearm("FN HAR", cost=1500, page_ref='p.428', avail=[8, RESTRICTED], subtype="Assault Rifle")
YAMAHA_RAIDEN = Firearm("Yamaha Raiden", cost=2600, page_ref='p.428', avail=[14, FORBIDDEN], subtype="Assault Rifle")
# =============== SNIPERS ================
ARES_DESERT_STRIKE = Firearm("Ares Desert Strike", cost=17_500, page_ref='p428', avail=[10, FORBIDDEN], subtype="Sniper Rifle")
CAVALIER_ARMS_CROCKETT_EBR = Firearm("Cavalier Arms Crockett EBR", cost=10_300, page_ref='p428', avail=[12, FORBIDDEN], subtype="Sniper Rifle")
RANGER_ARMS_SM_5 = Firearm("Ranger Arms SM-5", cost=28_000, page_ref='p429', avail=[16, FORBIDDEN], subtype="Sniper Rifle")
REMINGTON_950 = Firearm("Remington 950", cost=2100, page_ref='p429', avail=[4, RESTRICTED], subtype="Sniper Rifle")
RUGER_100 = Firearm("Ruger 100", cost=1300, page_ref='p429', avail=[4, RESTRICTED], subtype="Sniper Rifle")
# =============== SHOTGUNS ===============
DEFIANCE_T_250 = Firearm("Defiance T-250", cost=450, page_ref='p.429', avail=[4, RESTRICTED], subtype="Shotgun")
ENFIELD_AS_7 = Firearm("Enfield AS-7", cost=1100, page_ref='p.429', avail=[12, FORBIDDEN], subtype="Shotgun")
PJSS_MODEL_55  = Firearm("PJSS Model 55", cost=1000, page_ref='p.429', avail=[0, RESTRICTED], subtype="Shotgun")
# =============== SPECiAL ================
ARES_S_III_SUPER_SQUIRT = Firearm("Ares S-III Super Squirt", cost=950, page_ref='p.429', avail=[0, RESTRICTED], subtype="Special", damage="Chemical")
FICHETTI_PAIN_INDUCER = Firearm("Fichetti Pain Inducer", cost=5000, page_ref='p430', avail=[11, FORBIDDEN], subtype="Special", damage="Special")
PARASHIELD_DART_PISTOL = Firearm("Parashield Dart Pistol", cost=600, page_ref='p430', avail=[4, FORBIDDEN], subtype="Special", damage="As Drug/Toxin")
PARASHIELD_DART_RIFLE = Firearm("Parashield Dart Rifle", cost=1200, page_ref='p430', avail=[6, FORBIDDEN], subtype="Special", damage="As Drug/Toxin")
# =============== MACHINE ================
INGRAM_VALIANT = Firearm("Ingram Valiant", cost=5800, page_ref='p430', avail=[12, FORBIDDEN], subtype="Machine Gun")
STONER_ARES_M202 = Firearm("Stoner-Ares M202", cost=7000, page_ref='p430', avail=[12, FORBIDDEN], subtype="Machine Gun")
RPK_HMG = Firearm("RPK HMG", cost=16_300, page_ref='p430', avail=[16, FORBIDDEN], subtype="Machine Gun")
# =============== LAUNCHER ===============
ARES_ANTIOCH_2 = Firearm("Ares Antioch-2", cost=3200, page_ref='p42', avail=[8, FORBIDDEN], subtype="Cannon/Launcher")
ARMTECH_MGL_12 = Firearm("ArmTech MGL-12", cost=5000, page_ref='p42', avail=[10, FORBIDDEN], subtype="Cannon/Launcher")
AZTECHNOLOGY_STRIKER = Firearm("Aztechnology Striker", cost=1200, page_ref='p42', avail=[10, FORBIDDEN], subtype="Cannon/Launcher")
KRIME_CANNON = Firearm("Krime Cannon", cost=21_000, page_ref='p42', avail=[20, FORBIDDEN], subtype="Cannon/Launcher")
ONOTARI_INTERCEPTOR = Firearm("Onotari Interceptor", cost=14_000, page_ref='p42', avail=[18, FORBIDDEN], subtype="Cannon/Launcher")
PANTHER_XXL = Firearm("Panther XXL", cost=43_000, page_ref='p42', avail=[20, FORBIDDEN], subtype="Cannon/Launcher")

"""
    FIREARM ACCESSORIES
    arg order: name, cost, page_ref, mount, avail, **kwargs
"""
AIRBURST_LINK = FirearmAcc("Airburst_Link", cost=600, page_ref='p.432', mount="", avail=[6, RESTRICTED])
BIPOD = FirearmAcc("Bipod", cost=200, page_ref='p.432', mount="", avail=2)
CONCEALABLE_HOLSTER = FirearmAcc("Concealable_Holster", cost=150, page_ref='p.432', mount="", avail=2)
GAS_VENT_SYSTEM = FirearmAcc("Gas_Vent_System", cost=[200 x "Rating"], page_ref='p.432', mount="", avail=[(3, "Rating"), RESTRICTED])
GYRO_MOUNT = FirearmAcc("Gyro_Mount", cost=1400, page_ref='p.432', mount="", avail=7)
HIDDEN_ARM_SLIDE = FirearmAcc("Hidden_Arm_Slide", cost=350, page_ref='p.432', mount="", avail=[4,RESTRICTED])
IMAGING_SCOPE = FirearmAcc("Imaging_Scope", cost=300, page_ref='p.432', mount="", avail=2)
LASER_SIGHT = FirearmAcc("Laser_Sight", cost=125, page_ref='p.432', mount="", avail=2)
PERISCOPE = FirearmAcc("Periscope", cost=70, page_ref='p.432', mount="", avail=3)
QUICK_DRAW_HOLSTER = FirearmAcc("Quick_Draw_Holster", cost=175, page_ref='p.432', mount="", avail=4)
SHOCK_PAD = FirearmAcc("Shock_Pad", cost=50, page_ref='p.432', mount="", avail=2)
SILENCER_SUPPRESSOR = FirearmAcc("Silencer_Suppressor", cost=500, page_ref='p.432', mount="", avail=[9, FORBIDDEN])
SMART_FIRING_PLATFORM = FirearmAcc("Smart_Firing_Platform", cost=2_500, page_ref='p.432', mount="", avail=[12, FORBIDDEN])
SMARTGUN_SYSTEM_INTERNAL = FirearmAcc("Smartgun_System_Internal", cost=[2 * "WeaponCost"], page_ref='p.432', mount="", avail=[2, RESTRICTED])
SMARTGUN_SYSTEM_EXTERNAL = FirearmAcc("Smartgun_System_External", cost=200, page_ref='p.432', mount="", avail=[4, RESTRICTED])
SPARE_CLIP = FirearmAcc("Spare_Clip", cost=5, page_ref='p.432', mount="", avail=4)
SPEED_LOADER = FirearmAcc("Speed_Loader", cost=25, page_ref='p.432', mount="", avail=2)
TRIPOD = FirearmAcc("Tripod", cost=500, page_ref='p.432', mount="", avail=4)

"""
    AMMO TYPES
"""
APFS = Ammo("APFS", cost=120, page_ref='p.433', avail=[12, FORBIDDEN])
ASSAULT_CANNON = Ammo("Assault Cannon", cost=400, page_ref='p.433', avail=[12, FORBIDDEN])
EXPLOSIVE_ROUNDS = Ammo("Explosive Rounds", cost=80, page_ref='p.433', avail=[9, FORBIDDEN])
FLECHETTE_ROUNDS = Ammo("Flechette Rounds", cost=65, page_ref='p.433', avail=[6, RESTRICTED])
GEL_ROUNDS = Ammo("Gel Rounds", cost=25, page_ref='p.433', avail=[2, RESTRICTED])
HOLLOW_POINTS = Ammo("Hollow Points", cost=70, page_ref='p.433', avail=[4, FORBIDDEN])
INJECTION_DARTS = Ammo("Injection Darts", cost=75, page_ref='p.433', avail=[4, RESTRICTED])
REGULAR_AMMO = Ammo("Regular Ammo", cost=20, page_ref='p.433', avail=[2, RESTRICTED])
STICK_N_SHOCK = Ammo("Stick-n-Shock", cost=80, page_ref='p.433', avail=[6, RESTRICTED])
TRACER = Ammo("Tracer", cost=60, page_ref='p.433', avail=[6, RESTRICTED])
TASER_DART = Ammo("Taser Dart", cost=50, page_ref='p.433', avail=3)
Flash_Bang
Flash_Pak
Fragmentation
High_Explosive
Gas


"""
    PRIORITY TABLE
"""
PRIORITY_TABLE = {
    'A': {
        'Metatype': [(HUMAN, 9), (ELF, 8), (DWARF, 7), (ORK, 7), (TROLL, 5)],
        'Attributes': 24,
        'MagicResonance': {
            'Magician or Mystic Adept': { 'Magic': 6, 'Skills': {'Type': 'Magic', 'Rating': 5, 'Quantity': 2 }, 'Spells': 10 },
            'Technomancer': { 'Resonance': 6, 'Skills': {'Type': 'Resonance', 'Rating': 5, 'Quantity': 2 }, 'Complex Forms': 5 }
        },
        'Skills': [46, 10],
        'Money': 450_000
    },
    'B': {
        'Metatype': [(HUMAN, 7), (ELF, 6), (DWARF, 4), (ORK, 4), (TROLL, 0)],
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
        'Metatype': [(HUMAN, 5), (ELF, 3), (DWARF, 1), (ORK, 0)],
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
        'Metatype': [(HUMAN, 3), (ELF, 0)],
        'Attributes': 14,
        'MagicResonance': {
            'Adept': {'Magic': 2},
            'Aspected Magician': {'Magic': 2}
        },
        'Skills': [22, 0],
        'Money': 50_000
    },
    'E': {
        'Metatype': [(HUMAN, 1)],
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

print(STRENGTH.what_is())
print(BIOTECHNOLOGY.what_is())
print(THROWING.what_is())
print(ELF.what_is())
print(STREETSAMURAI.what_is())
print(DEFINANCE_EX_SHOCKER.what_is())
print(DEFINANCE_EX_SHOCKER.damage)