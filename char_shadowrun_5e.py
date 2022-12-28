import chargen
import random
from yaml import safe_load

"""
    GOALS

Lets set out some design goals and then have nowhere to formally put them.

    1) Generate Character 
    2) Lil TUI Interface that allows the user to, once a character is fully generated, scroll through menus to look at a weapon in more detail for example.
    2a) I am scrapping this idea immediately after I had it because adding all the different and differing stats for the multitude of pieces of gear is long boring and isn't
            required. A page number reference will suffice.
"""

"""
    USAGE
    dice("2d6")
"""
def dice(dice_string):
    sides, throws = dice_string.split("d")
    return sum([random.randint(1, int(sides)) for _ in range(int(throws))])


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
    def __init__(self, name, cost, page_ref):
        self.name = name
        self.cost = cost
        self.page_ref = page_ref
        self.category = None
        self.subtype = None
    
    def what_is(self):
        return f"[{self.category}/{self.subtype}] - {self.name} is a piece of Gear"

    def __repr__(self):
        return self.name

class Melee_Weapons(Gear):
    def __init__(self, name, cost, page_ref, avail, subtype, **kwargs):
        super().__init__(name, cost, page_ref)
        self.avail = avail
        self.category = "Melee Weapon"
        self.subtype = subtype
        for k, d in kwargs.items():
            self.__setattr__(k, d)

class Firearm(Gear):
    def __init__(self, name, cost, page_ref, avail, subtype, **kwargs):
        super().__init__(name, cost, page_ref)
        self.avail = avail
        self.category = "Firearm"
        self.subtype = subtype
        for k, d in kwargs.items():
            self.__setattr__(k, d)

class FirearmAcc(Gear):
    def __init__(self, name, cost, page_ref, mount, avail, **kwargs):
        super().__init__(name, cost, page_ref)
        self.category = "Firearm Accessory"
        self.mount = mount
        self.avail = avail
        for k, d in kwargs.items():
            self.__setattr__(k, d)

class Ammo(Gear):
    def __init__(self, name, cost, page_ref, avail, **kwargs):
        super().__init__(name, cost, page_ref)
        self.category = "Ammunition"
        self.avail = avail
        for k, d in kwargs.items():
            self.__setattr__(k, d)

class Clothing(Gear):
    def __init__(self, name, cost, page_ref, **kwargs):
        super().__init__(name, cost, page_ref)
        self.category = "Clothing"
        for k, d in kwargs.items():
            self.__setattr__(k, d)

class Armor(Gear):
    def __init__(self, name, cost, page_ref, **kwargs):
        super().__init__(name, cost, page_ref)
        self.category = "Armor"
        for k, d in kwargs.items():
            self.__setattr__(k, d)

class ArmorModification(Gear):
    def __init__(self, name, cost, page_ref, avail, capacity, **kwargs):
        super().__init__(name, cost, page_ref)
        self.category = "Armor"
        self.subtype = "Modification"
        self.avail = avail
        self.capacity = capacity
        for k, d in kwargs.items():
            self.__setattr__(k, d)

class Electronics(Gear):
    def __init__(self, name, cost, page_ref, rating, avail, subtype, **kwargs):
        super().__init__(name, cost, page_ref)
        self.category = "Electronics"
        self.rating = rating
        self.avail = avail
        self.subtype = subtype
        for k, d in kwargs.items():
            self.__setattr__(k, d)

"""
    The Item Class. Why now?

So while the previous inheritants of the "Gear" class could all technically classify as "Items", I'm making a distinction
    from the above and generic items by common-sense TTRPG logic, as oxymoronic as that sounds.

If it equips to you, it ain't an item.
If it gets thrust into your storage medium of choice to be used at a later date, it's an item.

Even things like explosvies, who serve the same purpose as weaponary (do the hurty damage), count as items as I'm arbitrarily
    making the call that you wouldn't equip explosives in the same way you would armor or a sword or a gun.
Also I made the Ammo class before I got around to doing this class so fuck you, it stays as is.
"""

class Item(Gear):
    def __init__(self, name, cost, page_ref, rating=0, category="Item", subtype=None, **kwargs):
        super().__init__(name, cost, page_ref)
        self.category = category
        self.subtype = subtype
        self.rating = rating
        for k, d in kwargs.items():
            self.__setattr__(k, d)


class GearAvailability:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self.name

"""
    Starting Nuyen is calculated from two parts
    First is the Nuyen multipler, or 'base_amount', then a dice roll is made to see how the total 
        amount of starting Nuyen. This is *not* the same as the Nuyen amount chosen at the priorities
        table, that's just cash for buying equipment, weapons & the like. This determines your starting
        money
"""
class Lifestyle:
    def __init__(self, name, dice_string, base_amount, cost):
        self.name = name
        self.dice_string = dice_string
        self.base_amount = base_amount 
        self.nuyen = 0
        self.cost = cost

    def roll(self):
        self.nuyen = dice(self.dice_string) * self.base_amount
        return self.nuyen

    def __repr__(self):
        return self.nuyen



    



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
DEFINANCE_EX_SHOCKER = Firearm("Definance EX Shocker", cost=250, page_ref=424, avail="-", subtype="Taser", damage=[9, STUN, ELECTRICAL])
YAMAHA_PULSAR = Firearm("Yamaha Pulsar", cost=180, page_ref=424, avail="-", subtype="Taser")
# =============== HOLD-OUTS ==============
FINCHETTI_TIFFANI_NEEDLER = Firearm("Finchetti Tiffani Needler", cost=1000, page_ref=425, avail=[5, RESTRICTED], subtype="Hold-Outs")
STREETLINE_SPECIAL = Firearm("Streetline Special", cost=120, page_ref=425, avail=[4, RESTRICTED], subtype="Hold-Outs")
WALTHER_PALM_PISTOL = Firearm("Walther Palm Pistol", cost=180, page_ref=425, avail=[4, RESTRICTED], subtype="Hold-Out")
# =============== LIGHT PISTOLS ==========
ARES_LIGHT_FIRE_75 = Firearm("Ares_Light Fire 75", cost=1250, page_ref=425, avail=[6, RESTRICTED], subtype="Light Pistol")
ARES_LIGHT_FIRE_70 = Firearm("Ares Light Fire 70", cost=200, page_ref=425, avail=[3, RESTRICTED], subtype="Light Pistol")
BERETTA_201T = Firearm("Beretta 201T", cost=210, page_ref=425, avail=[7, RESTRICTED], subtype="Light Pistol")
COLT_AMERICA_L36 = Firearm("Colt America L36", cost=320, page_ref=425, avail=[4, RESTRICTED], subtype="Light Pistol")
FICHETTI_SECURITY_600 = Firearm("Fichetti Security 600", cost=350, page_ref=426, avail=[6, RESTRICTED], subtype="Light Pistol")
TAURUS_OMNI_6 = Firearm("Taurus Omni 6", cost=300, page_ref=426, avail=[3, RESTRICTED], subtype="Light Pistol")
# =============== HEAVY PISTOLS ==========
ARES_PREDATOR_V = Firearm("Ares Predator V", cost=725, page_ref=426, avail=[5, RESTRICTED], subtype="Heavy Pistol")
ARES_VIPER_SHOTGUN = Firearm("Ares Viper Shotgun", cost=380, page_ref=426, avail=[8, RESTRICTED], subtype="Heavy Pistol")
BROWNING_ULTRA_POWER = Firearm("Browning Ultra Power", cost=640, page_ref=426, avail=[4, RESTRICTED], subtype="Heavy Pistol")
COLT_GOVERNMENT_2066 = Firearm("Colt Government 2066", cost=425, page_ref=426, avail=[7, RESTRICTED], subtype="Heavy Pistol")
REMINGTON_ROOMSWEEPER = Firearm("Remington Roomsweeper", cost=250, page_ref=426, avail=[6, RESTRICTED], subtype="Heavy Pistol")
REMINGTON_ROOMSWEEPER_FLECHETTES = Firearm("Remington_Roomsweeper_Flechettes", cost=REMINGTON_ROOMSWEEPER.cost, page_ref=426, avail=REMINGTON_ROOMSWEEPER.avail, subtype="Heavy Pistol" , requires=REMINGTON_ROOMSWEEPER)
RUGER_SUPER_WARHAWK = Firearm("Ruger Super Warhawk", cost=400, page_ref=427, avail=[4, RESTRICTED], subtype="Heavy Pistol")
# =============== MACHINE PISTOLS ========
ARES_CRUSADER_II = Firearm("Ares Crusader II", cost=830, page_ref=427, avail=[9, RESTRICTED], subtype="Machine Pistol")
CESKA_BLACK_SCORPIAN = Firearm("Ceska Black Scorpian", cost=270, page_ref=427, avail=[6, RESTRICTED], subtype="Machine Pistol")
STEYR_TMP = Firearm("Steyr TMP", cost=350, page_ref=427, avail=[8, RESTRICTED], subtype="Machine Pistol")
# =============== SMGS ===================
COLT_COBRA_TZ_120  = Firearm("Colt Cobra TZ-120", cost=660, page_ref=427, avail=[5, RESTRICTED], subtype="Submachine Gun")
FN_P93_PRAETOR = Firearm("FN-P93 Praetor", cost=900, page_ref=427, avail=[11, RESTRICTED], subtype="Submachine Gun")
HK_227 = Firearm("HK-227", cost=730, page_ref=427, avail=[8, RESTRICTED], subtype="Submachine Gun")
INGRAM_SMARTGUN_X = Firearm("Ingram Smartgun X", cost=800, page_ref=427, avail=[6, RESTRICTED], subtype="Submachine Gun")
SCK_MODEL_100 = Firearm("SCK Model 100", cost=875, page_ref=428, avail=[6, RESTRICTED], subtype="Submachine Gun")
UZI_IV = Firearm("Uzi IV", cost=450, page_ref=428, avail=[4, RESTRICTED], subtype="Submachine Gun")
# =============== ASSAULT RIFLE ==========
AK_97 = Firearm("AK 97", cost=950, page_ref=428, avail=[4 ,RESTRICTED], subtype="Assault Rifle")
ARES_ALPHA = Firearm("Ares Alpha", cost=2650, page_ref=428, avail=[11, FORBIDDEN], subtype="Assault Rifle")
ARES_ALPHA_GRENADE_LAUNCHER = Firearm("Ares Alpha Grenade Launcher", cost=0, page_ref=428, avail=[11, FORBIDDEN], subtype="Assault Rifle", requires=ARES_ALPHA)
COLT_M23 = Firearm("Colt-M23", cost=550, page_ref=428, avail=[4, RESTRICTED], subtype="Assault Rifle")
FN_HAR = Firearm("FN HAR", cost=1500, page_ref=428, avail=[8, RESTRICTED], subtype="Assault Rifle")
YAMAHA_RAIDEN = Firearm("Yamaha Raiden", cost=2600, page_ref=428, avail=[14, FORBIDDEN], subtype="Assault Rifle")
# =============== SNIPERS ================
ARES_DESERT_STRIKE = Firearm("Ares Desert Strike", cost=17_500, page_ref=28, avail=[10, FORBIDDEN], subtype="Sniper Rifle")
CAVALIER_ARMS_CROCKETT_EBR = Firearm("Cavalier Arms Crockett EBR", cost=10_300, page_ref=28, avail=[12, FORBIDDEN], subtype="Sniper Rifle")
RANGER_ARMS_SM_5 = Firearm("Ranger Arms SM-5", cost=28_000, page_ref=29, avail=[16, FORBIDDEN], subtype="Sniper Rifle")
REMINGTON_950 = Firearm("Remington 950", cost=2100, page_ref=29, avail=[4, RESTRICTED], subtype="Sniper Rifle")
RUGER_100 = Firearm("Ruger 100", cost=1300, page_ref=29, avail=[4, RESTRICTED], subtype="Sniper Rifle")
# =============== SHOTGUNS ===============
DEFIANCE_T_250 = Firearm("Defiance T-250", cost=450, page_ref=429, avail=[4, RESTRICTED], subtype="Shotgun")
ENFIELD_AS_7 = Firearm("Enfield AS-7", cost=1100, page_ref=429, avail=[12, FORBIDDEN], subtype="Shotgun")
PJSS_MODEL_55  = Firearm("PJSS Model 55", cost=1000, page_ref=429, avail=[0, RESTRICTED], subtype="Shotgun")
# =============== SPECiAL ================
ARES_S_III_SUPER_SQUIRT = Firearm("Ares S-III Super Squirt", cost=950, page_ref=429, avail=[0, RESTRICTED], subtype="Special", damage="Chemical")
FICHETTI_PAIN_INDUCER = Firearm("Fichetti Pain Inducer", cost=5000, page_ref=430, avail=[11, FORBIDDEN], subtype="Special", damage="Special")
PARASHIELD_DART_PISTOL = Firearm("Parashield Dart Pistol", cost=600, page_ref=430, avail=[4, FORBIDDEN], subtype="Special", damage="As Drug/Toxin")
PARASHIELD_DART_RIFLE = Firearm("Parashield Dart Rifle", cost=1200, page_ref=430, avail=[6, FORBIDDEN], subtype="Special", damage="As Drug/Toxin")
# =============== MACHINE ================
INGRAM_VALIANT = Firearm("Ingram Valiant", cost=5800, page_ref=430, avail=[12, FORBIDDEN], subtype="Machine Gun")
STONER_ARES_M202 = Firearm("Stoner-Ares M202", cost=7000, page_ref=430, avail=[12, FORBIDDEN], subtype="Machine Gun")
RPK_HMG = Firearm("RPK HMG", cost=16_300, page_ref=430, avail=[16, FORBIDDEN], subtype="Machine Gun")
# =============== LAUNCHER ===============
ARES_ANTIOCH_2 = Firearm("Ares Antioch-2", cost=3200, page_ref=431, avail=[8, FORBIDDEN], subtype="Cannon/Launcher")
ARMTECH_MGL_12 = Firearm("ArmTech MGL-12", cost=5000, page_ref=431, avail=[10, FORBIDDEN], subtype="Cannon/Launcher")
AZTECHNOLOGY_STRIKER = Firearm("Aztechnology Striker", cost=1200, page_ref=431, avail=[10, FORBIDDEN], subtype="Cannon/Launcher")
KRIME_CANNON = Firearm("Krime Cannon", cost=21_000, page_ref=431, avail=[20, FORBIDDEN], subtype="Cannon/Launcher")
ONOTARI_INTERCEPTOR = Firearm("Onotari Interceptor", cost=14_000, page_ref=431, avail=[18, FORBIDDEN], subtype="Cannon/Launcher")
PANTHER_XXL = Firearm("Panther XXL", cost=43_000, page_ref=431, avail=[20, FORBIDDEN], subtype="Cannon/Launcher")

"""
    FIREARM ACCESSORIES
    arg order: name, cost, page_ref, mount, avail, **kwargs
"""
AIRBURST_LINK = FirearmAcc("Airburst_Link", cost=600, page_ref=432, mount="", avail=[6, RESTRICTED])
BIPOD = FirearmAcc("Bipod", cost=200, page_ref=432, mount="", avail=2)
CONCEALABLE_HOLSTER = FirearmAcc("Concealable_Holster", cost=150, page_ref=432, mount="", avail=2)
GAS_VENT_SYSTEM = FirearmAcc("Gas_Vent_System", cost=(200, "Rating"), page_ref=432, mount="", avail=[(3, "Rating"), RESTRICTED])
GYRO_MOUNT = FirearmAcc("Gyro_Mount", cost=1400, page_ref=432, mount="", avail=7)
HIDDEN_ARM_SLIDE = FirearmAcc("Hidden_Arm_Slide", cost=350, page_ref=432, mount="", avail=[4,RESTRICTED])
IMAGING_SCOPE = FirearmAcc("Imaging_Scope", cost=300, page_ref=432, mount="", avail=2)
LASER_SIGHT = FirearmAcc("Laser_Sight", cost=125, page_ref=432, mount="", avail=2)
PERISCOPE = FirearmAcc("Periscope", cost=70, page_ref=432, mount="", avail=3)
QUICK_DRAW_HOLSTER = FirearmAcc("Quick_Draw_Holster", cost=175, page_ref=432, mount="", avail=4)
SHOCK_PAD = FirearmAcc("Shock_Pad", cost=50, page_ref=432, mount="", avail=2)
SILENCER_SUPPRESSOR = FirearmAcc("Silencer_Suppressor", cost=500, page_ref=432, mount="", avail=[9, FORBIDDEN])
SMART_FIRING_PLATFORM = FirearmAcc("Smart_Firing_Platform", cost=2_500, page_ref=432, mount="", avail=[12, FORBIDDEN])
SMARTGUN_SYSTEM_INTERNAL = FirearmAcc("Smartgun_System_Internal", cost=[2 * "WeaponCost"], page_ref=432, mount="", avail=[2, RESTRICTED])
SMARTGUN_SYSTEM_EXTERNAL = FirearmAcc("Smartgun_System_External", cost=200, page_ref=432, mount="", avail=[4, RESTRICTED])
SPARE_CLIP = FirearmAcc("Spare_Clip", cost=5, page_ref=432, mount="", avail=4)
SPEED_LOADER = FirearmAcc("Speed_Loader", cost=25, page_ref=432, mount="", avail=2)
TRIPOD = FirearmAcc("Tripod", cost=500, page_ref=432, mount="", avail=4)

"""
    AMMO TYPES
"""
# =============== STANDARD ===============
APFS = Ammo("APFS", cost=120, page_ref=433, avail=[12, FORBIDDEN])
ASSAULT_CANNON = Ammo("Assault Cannon", cost=400, page_ref=433, avail=[12, FORBIDDEN])
EXPLOSIVE_ROUNDS = Ammo("Explosive Rounds", cost=80, page_ref=433, avail=[9, FORBIDDEN])
FLECHETTE_ROUNDS = Ammo("Flechette Rounds", cost=65, page_ref=433, avail=[6, RESTRICTED])
GEL_ROUNDS = Ammo("Gel Rounds", cost=25, page_ref=433, avail=[2, RESTRICTED])
HOLLOW_POINTS = Ammo("Hollow Points", cost=70, page_ref=433, avail=[4, FORBIDDEN])
INJECTION_DARTS = Ammo("Injection Darts", cost=75, page_ref=433, avail=[4, RESTRICTED])
REGULAR_AMMO = Ammo("Regular Ammo", cost=20, page_ref=433, avail=[2, RESTRICTED])
STICK_N_SHOCK = Ammo("Stick-n-Shock", cost=80, page_ref=433, avail=[6, RESTRICTED])
TRACER = Ammo("Tracer", cost=60, page_ref=433, avail=[6, RESTRICTED])
TASER_DART = Ammo("Taser Dart", cost=50, page_ref=433, avail=3)
# =============== GRENADES ===============
FLASH_BANG = Ammo("Flash Bang", cost=100, page_ref=434, avail=[6, RESTRICTED], subtype="Grenade")
FLASH_PAK = Ammo("Flash Pak", cost=125, page_ref=434, avail=4, subtype="Grenade")
FRAGMENTATION = Ammo("Fragmentation", cost=100, page_ref=434, avail=[11, FORBIDDEN], subtype="Grenade")
HIGH_EXPLOSIVE = Ammo("High Explosive", cost=100, page_ref=434, avail=[11, FORBIDDEN], subtype="Grenade")
GAS = Ammo("Gas", cost=[40, "Chemical Cost"], page_ref=434, avail=[[2, "Chemical Availability"], RESTRICTED], subtype="Grenade")
SMOKE = Ammo("Smoke", cost=40, page_ref=434, avail=[4, RESTRICTED], subtype="Grenade")
THERMAL_SMOKE = Ammo("Thermal Smoke", cost=60, page_ref=434, avail=[6, RESTRICTED], subtype="Grenade")
# =============== MISSILES ==============
ANTI_VEHICLE = Ammo("Anti_Vehicle", cost=2800, page_ref=435, avail=[18, FORBIDDEN], subtype="Missile")
FRAGMENTATION_MISSLE = Ammo("Fragmentation_Missle", cost=2000, page_ref=435, avail=[12, FORBIDDEN], subtype="Missile")
HIGH_EXPLOSIVE_MISSLE = Ammo("High_Explosive_Missle", cost=2100, page_ref=435, avail=[18, FORBIDDEN], subtype="Missile")
# =============== ROCKETS ==============
ANTI_VEHICLE_ROCKET = Ammo("Anti_Vehicle_Rocket", cost=[ANTI_VEHICLE.cost, "+", ("Sensor Rating", 500)], page_ref=ANTI_VEHICLE.page_ref, avail=ANTI_VEHICLE.avail, subtype="Rocket", requires=ANTI_VEHICLE)
FRAGMENTATION_ROCKET = Ammo("Fragmentation_Rocket", cost=[FRAGMENTATION_MISSLE.cost, "+", ("Sensor Rating", 500)], page_ref=FRAGMENTATION_MISSLE.page_ref, avail=FRAGMENTATION_MISSLE.avail, subtype="Rocket", requires=FRAGMENTATION_MISSLE)
HIGH_EXPLOSIVE_ROCKET = Ammo("High_Explosive_Rocket", cost=[HIGH_EXPLOSIVE_MISSLE.cost, "+", ("Sensor Rating", 500)], page_ref=HIGH_EXPLOSIVE_MISSLE.page_ref, avail=HIGH_EXPLOSIVE_MISSLE.avail, subtype="Rocket", requires=HIGH_EXPLOSIVE_MISSLE)

"""
    EXPLOSIVES
"""
COMMERCIAL_EXPLOSIVES = Item("Commercial_Explosives", cost=100, page_ref=436, rating=5, avail=[8, RESTRICTED], category="Explosives")
FOAM_EXPLOSIVES = Item("Foam_Explosives", cost=0, page_ref=436, rating=[6, "range", 25], avail=[12, FORBIDDEN], category="Explosives")
FOAM_EXPLOSIVES.cost = (100, FOAM_EXPLOSIVES.rating)
PLASTIC_EXPLOSIVES = Item("Plastic_Explosives", cost=0, page_ref=436, rating=[6, "range", 25], avail=[16, FORBIDDEN], category="Explosives")
PLASTIC_EXPLOSIVES.cost = (100, PLASTIC_EXPLOSIVES.rating)
DETONATOR_CAP = Item("Detonator Cap", cost=75, page_ref=436, rating="-", avail=[8, RESTRICTED], category="Explosives")

"""
    CLOTHING/ARMOR
"""
# =============== CLOTHING ==============
CLOTHING = Clothing("Clothing", cost=[20, "Range", 100_000], page_ref=436, avail="-", armor_rating=0)
ELECTROCHROMATIC_MODIFICATION = Clothing("Electrochromatic Modification", cost=500, page_ref=436, avail=2, requires=CLOTHING)
FEEDBACK_CLOTHING = Clothing("Feedback Clothing", cost=500, page_ref=436, avail=8, requires=CLOTHING)
SYNTH_LEATHER = Clothing("Synth Leather", cost=200, page_ref=436, avail="-", requires=CLOTHING)
# =============== ARMOR =================
ACTIONEER_BUSINESS_CLOTHING = Armor("Actioneer Business Clothing", cost=1500, page_ref=436, avail=8, armor_rating=8)
ARMOR_CLOTHING = Armor("Armor Clothing", cost=450, page_ref=436, avail=2, armor_rating=6)
ARMOR_JACKET = Armor("Armor Jacket", cost=1000, page_ref=436, avail=2, armor_rating=12)
ARMOR_VEST = Armor("Armor Vest", cost=500, page_ref=436, avail=4, armor_rating=9)
CHAMELEON_SUIT = Armor("Chameleon Suit", cost=1700, page_ref=436, avail=[10, RESTRICTED], armor_rating=9)
FULL_BODY_ARMOR = Armor("Full Body Armor", cost=2000, page_ref=436, avail=[14, RESTRICTED], armor_rating=15)
FULL_HELMET = Armor("Full Helmet", cost=500, page_ref=436, avail=[14, RESTRICTED], requires=FULL_BODY_ARMOR, armor_rating=3)
FULL_BODY_ARMOR_CHEMICAL_SEAL = Armor("Chemical Seal", cost=6000, page_ref=436, avail=[FULL_BODY_ARMOR.avail[0] + 6, RESTRICTED], requires=FULL_BODY_ARMOR, armor_rating="-")
FULL_BODY_ARMOR_ENVIRONMENTAL_ADAPTATION = Armor("Environmental Adaptation", 1000, page_ref=436, avail=[FULL_BODY_ARMOR.avail[0] + 3, RESTRICTED], requires=FULL_BODY_ARMOR, armor_rating="-")
LINED_COAT = Armor("Lined Coat", cost=900, page_ref=436, avail=4, armor_rating=9)
URBAN_EXPLORER_JUMPSUIT = Armor("Urban Explorer Jumpsuit", cost=650, page_ref=436, avail=8, armor_rating=9)
URBAN_EXPLORER_JUMPSUIT_HELMET = Armor("Urban Explorer Jumpsuit Helmet", cost=100, page_ref=436, avail=URBAN_EXPLORER_JUMPSUIT.avail, requires=URBAN_EXPLORER_JUMPSUIT, armor_rating=2)
# =============== SUBTYPES ==============
HELMET = Armor("Helmet", cost=100, page_ref=438, avail=2, armor_rating=2, subtype="Helmet")
BALLISTIC_SHIELD = Armor("Ballistic Shield", cost=1200, page_ref=438, avail=[12, RESTRICTED], armor_rating=6, subtype="Shield")
RIOT_SHIELD = Armor("Riot Shield", cost=1500, page_ref=438, avail=[10, RESTRICTED], armor_rating=6, subtype="Shield")
# =============== ARMOR MODS ============
CHEMICAL_PROTECTION = ArmorModification("Chemical Protection", cost=[250, "*", "Rating"], page_ref=438, avail=6, capacity="Rating")
CHEMICAL_SEAL = ArmorModification("Chemical Seal", cost=3000, page_ref=438, avail=[12, RESTRICTED], capacity=6)
FIRE_RESISTANCE = ArmorModification("Fire Resistance", cost=[250, "*", "Rating"], page_ref=438, avail=6, capacity="Rating")
INSULATION = ArmorModification("Insulation", cost=[250, "*", "Rating"], page_ref=438, avail=6, capacity="Rating")
NONCONDUCTIVITY = ArmorModification("Nonconductivity", cost=[250, "*", "Rating"], page_ref=438, avail=6, capacity="Rating")
SHOCK_FRILLS = ArmorModification("Shock Frills", cost=250, page_ref=438, avail=[6, RESTRICTED], capacity=2)
THERMAL_DAMPING = ArmorModification("Thermal Damping", cost=[500, "*", "Rating"], page_ref=438, avail=[10, RESTRICTED], capacity="Rating")

"""
    ELECTRONICS
"""
# =============== COMMLINKS ============
META_LINK = Electronics("Meta Link", cost=100, page_ref=439, rating=1, avail=2, subtype="Commlink")
SONY_EMPORER = Electronics("Sony Emporer", cost=700, page_ref=439, rating=2, avail=4, subtype="Commlink")
RENRAKU_SENSEI = Electronics("Renraku Sensei", cost=1000, page_ref=439, rating=3, avail=6, subtype="Commlink")
ERIKA_ELITE = Electronics("Erika Elite", cost=2500, page_ref=439, rating=4, avail=8, subtype="Commlink")
HERMES_IKON = Electronics("Hermes Ikon", cost=3000, page_ref=439, rating=5, avail=10, subtype="Commlink")
TRANSYS_AVALON = Electronics("Transys Avalon", cost=5000, page_ref=439, rating=6, avail=12, subtype="Commlink")
FAIRLIGHT_CALIBAN = Electronics("Fairlight Caliban", cost=8000, page_ref=439, rating=7, avail=14, subtype="Commlink")
SIM_MODULE = Electronics("Sim Module", cost=100, page_ref=439, rating="-", avail="-", subtype="Commlink", requires=["Commlink"])
SIM_MODULE_HOT_SIM = Electronics("Sim Module Hot Sim", cost=250, page_ref=439, rating="-", avail="-", subtype="Commlink", requires=SIM_MODULE)
# =============== CYBERDECKS ===========
ERIKA_MCD_1 = Electronics("Erika MCD-1", cost=49_500, page_ref=439, rating=1, avail=[3, RESTRICTED], attribute_array=[4,3,2,1], programs=1, subtype="Cyberdeck")
MICRODECK_SUMMIT = Electronics("Microdeck Summit", cost=58_000, page_ref=439, rating=1, avail=[3, RESTRICTED], attribute_array=[4,3,3,1], programs=1, subtype="Cyberdeck")
MIROTRONICA_AZTECA_200 = Electronics("Mirotronica Azteca 200", cost=110_250, page_ref=439, rating=2, avail=[6, RESTRICTED], attribute_array=[5,4,3,2], programs=2, subtype="Cyberdeck")
HERMES_CHARIOT = Electronics("Hermes Chariot", cost=123_000, page_ref=439, rating=2, avail=[6, RESTRICTED], attribute_array=[5,4,4,2], programs=2, subtype="Cyberdeck")
NOVATECH_NAVIGATOR = Electronics("Novatech Navigator", cost=205_750, page_ref=439, rating=3, avail=[9, RESTRICTED], attribute_array=[6,5,4,3], programs=3, subtype="Cyberdeck")
RENRAKU_TSURUGI = Electronics("Renraku Tsurugi", cost=214_125, page_ref=439, rating=3, avail=[9, RESTRICTED], attribute_array=[6,5,5,3], programs=3, subtype="Cyberdeck")
SONY_CIY_720 = Electronics("Sony CIY-720", cost=345_000, page_ref=439, rating=4, avail=[12, RESTRICTED], attribute_array=[7,6,5,4], programs=4, subtype="Cyberdeck")
SHIAWASE_CYBER_5 = Electronics("Shiawase Cyber-5", cost=549_375, page_ref=439, rating=5, avail=[15, RESTRICTED], attribute_array=[8,7,6,5], programs=5, subtype="Cyberdeck")
FAIRLIGHT_EXCALIBUR = Electronics("Fairlight Excalibur", cost=823_250, page_ref=439, rating=6, avail=[18, RESTRICTED], attribute_array=[9,8,7,6], programs=6, subtype="Cyberdeck")
# =============== ACCESSORIES =========
AR_GLOVES = Electronics("AR Gloves", cost=150, page_ref=440, rating=3, avail="-", subtype="Accessories")
BIOMETRIC_READER = Electronics("Biometric Reader", cost=200, page_ref=440, rating=3, avail=4, subtype="Accessories")
ELECTRONIC_PAPER = Electronics("Electronic Paper", cost=5, page_ref=440, rating=1, avail="-", subtype="Accessories")
PRINTER = Electronics("Printer", cost=25, page_ref=440, rating=3, avail="-", subtype="Accessories")
SATELLITE_LINK = Electronics("Satellite Link", cost=500, page_ref=440, rating=4, avail=6, subtype="Accessories")
SIMRIG = Electronics("Simrig", cost=1000, page_ref=440, rating=3, avail=12, subtype="Accessories")
SUBVOCAL_MIC = Electronics("Subvocal Mic", cost=50, page_ref=440, rating=3, avail=4, subtype="Accessories")
TRID_PROJECTOR = Electronics("Trid Projector", cost=200, page_ref=440, rating=3, avail="-", subtype="Accessories")
TRODES = Electronics("Trodes", cost=70, page_ref=440, rating=3, avail="-", subtype="Accessories")
# =============== RFID TAG ===========
STANDARD_RFID = Electronics("Standard RFID", cost=1, page_ref=440, rating=1, avail="-", subtype="RFID Tags")
DATACHIP = Electronics("Datachip", cost=5, page_ref=440, rating=1, avail="-", subtype="RFID Tags")
SECURITY_RFID = Electronics("Security RFID", cost=5, page_ref=440, rating=3, avail=3, subtype="RFID Tags")
SENSOR_RFID = Electronics("Sensor RFID", cost=40, page_ref=440, rating=2, avail=5, subtype="RFID Tags")
STEALTH_RFID = Electronics("Stealth RFID", cost=10, page_ref=440, rating=3, avail=[7, RESTRICTED], subtype="RFID Tags")
# =============== COMMUNICATIONS =====
BUG_SCANNER = Electronics("Bug Scanner", cost=["Rating", "*", 100], page_ref=441, rating=[1, "to", 6], avail=["Rating", RESTRICTED], subtype="Communications")
DATA_TAP = Electronics("Data Tap", cost=300, page_ref=441, rating="-", avail=[6, RESTRICTED], subtype="Communications")
HEADJAMMER = Electronics("Headjammer", cost=["Rating", "*", 150], page_ref=441, rating=[1, "to", 6], avail=["Rating", RESTRICTED], subtype="Communications")
JAMMER_AREA = Electronics("Jammer Area", cost=["Rating", "*", 200], page_ref=441, rating=[1, "to", 6], avail=[["Rating", "*", 3], RESTRICTED], subtype="Communications")
JAMMER_DIRECTIONAL = Electronics("Jammer Directional", cost=["Rating", "*", 200], page_ref=441, rating=[1, "to", 6], avail=[["Rating", "*", 2], RESTRICTED], subtype="Communications")
MICRO_TRANSRECEIVER = Electronics("Micro Transreceiver", cost=100, page_ref=441, rating="-", avail=2, subtype="Communications")
TAG_ERASER = Electronics("Tag Eraser", cost=450, page_ref=441, rating="-", avail=[6, RESTRICTED], subtype="Communications")
WHITE_NOISE_GENERATOR = Electronics("White Noise Generator", cost=["Rating", "*", 50], page_ref=441, rating=[1, "to", 6], avail="Rating", subtype="Communications")
# =============== SOFTWARE ===========
AGENT_1_3 = Electronics("Agent (Rating 1-3)", cost=["Rating", "*", 1_000], page_ref=442, rating=[1, "to", 3], avail=["Rating", "*", 3], subtype="Software")
AGENT_4_6 = Electronics("Agent (Rating 4-6)", cost=["Rating", "*", 2_000], page_ref=442, rating=[4, "to", 6], avail=["Rating", "*", 3], subtype="Software")
AUTOSOFT = Electronics("Autosoft", cost=["Rating", "*", 500], page_ref=442, rating="-", avail=["Rating", "*", 2], subtype="Software")
CYBERPROGRAM_COMMON = Electronics("Cyberprogram Common", cost=80, page_ref=442, rating="-", avail="-", subtype="Software")
CYBERPROGRAM_HACKING = Electronics("Cyberprogram Hacking", cost=250, page_ref=442, rating="-", avail=[6, RESTRICTED], subtype="Software")
DATASOFT = Electronics("Datasoft", cost=120, page_ref=442, rating="-", avail="-", subtype="Software")
MAPSOFT = Electronics("Mapsoft", cost=100, page_ref=442, rating="-", avail="-", subtype="Software")
SHOPSOFT = Electronics("Shopsoft", cost=150, page_ref=442, rating="-", avail="-", subtype="Software")
TUTORSOFT = Electronics("Tutorsoft", cost=["Rating", "*", 400], page_ref=442, rating=[1, "to", 6], avail="Rating", subtype="Software")
# =============== SKILLSOFTS =========
ACTIVESOFTS = Electronics("Activesofts", cost=["Rating", "*", 5000], page_ref=442, rating=[1, "to", 6], avail=8, subtype="Skillsofts")
KNOWSOFTS = Electronics("Knowsofts", cost=["Rating", "*", 2000], page_ref=442, rating=[1, "to", 6], avail=8, subtype="Skillsofts")
LINGUASOFTS = Electronics("Linguasofts", cost=["Rating", "*", 1000], page_ref=442, rating=[1, "to", 6], avail=8, subtype="Skillsofts")
# =============== CREDSTICKS =========
STANDARD = Electronics("Standard Credstick", cost=5, page_ref=443, rating="-", avail="-", max_value=5000, subtype="Credsticks")
SILVER = Electronics("Silver Credstick", cost=20, page_ref=443, rating="-", avail="-", max_value=20_000, subtype="Credsticks")
GOLD = Electronics("Gold Credstick", cost=100, page_ref=443, rating="-", avail=5, max_value=100_000, subtype="Credsticks")
PLATINUM = Electronics("Platinum Credstick", cost=500, page_ref=443, rating="-", avail=10, max_value=500_000, subtype="Credsticks")
EBONY = Electronics("Ebony Credstick", cost=1000, page_ref=443, rating="-", avail=20, max_value=1_000_000, subtype="Credsticks")
# =============== IDENTIFICATION =====
FAKE_SIN = Electronics("Fake_SIN", cost=["Rating", "*", 2500], page_ref=443, rating=[1, "to", 6], avail=[["Rating", "*", 3], FORBIDDEN], subtype="Identification")
FAKE_LICENCE = Electronics("Fake_Licence", cost=["Rating", "*", 200], page_ref=443, rating=[1, "to", 6], avail=[["Rating", "*", 3], FORBIDDEN], subtype="Identification")
# =============== TOOLS ==============
TOOL_KIT = Electronics("Tool_Kit", cost=500, page_ref=443, rating="-", avail="-", subtype="Tools")
TOOL_SHOP = Electronics("Tool_Shop", cost=5000, page_ref=443, rating="-", avail=8, subtype="Tools")
TOOL_FACILITY = Electronics("Tool_Facility", cost=50000, page_ref=443, rating="-", avail=12, subtype="Tools")
# ========== OPTICAL / IMAGING DEVICES
BINOCULARS = Electronics("Binoculars", cost=["Capacity", "*", 50], page_ref=444, rating="-", avail="-", capacity=[1, "to", 3], subtype="Optical/Imaging Devices")
OPTICAL_BINOCULARS = Electronics("Optical_Binoculars", cost=50, page_ref=444, rating="-", avail="-", subtype="Optical/Imaging Devices")
CAMERA = Electronics("Camera", cost=["Capacity", "*", 100], page_ref=444, rating="-", avail="-",capacity=[1, "to", 6], subtype="Optical/Imaging Devices")
MICRO_CAMERA = Electronics("Micro_Camera", cost=100, page_ref=444, rating="-", avail="-", capacity=1, subtype="Optical/Imaging Devices")
EYE_CONTACTS = Electronics("Eye_Contacts", cost=["Capacity", "*", 200], page_ref=444, rating="-", avail="-", capacity=[1, "to", 3], subtype="Optical/Imaging Devices")
GLASSES = Electronics("Glasses", cost=["Capacity", "*", 100], page_ref=444, rating="-", avail="-", capacity=[1, "to", 4], subtype="Optical/Imaging Devices")
GOGGLES = Electronics("Goggles", cost=["Capacity", "*", 50], page_ref=444, rating="-", avail="-", capacity=[1, "to", 6], subtype="Optical/Imaging Devices")
ENDOSCOPE = Electronics("Endoscope", cost=250, page_ref=444, rating="-", avail=8, subtype="Optical/Imaging Devices")
MAGE_SIGHT_GOGGLES = Electronics("Mage_Sight_Goggles", cost=3000, page_ref=444, rating="-", avail=[12, RESTRICTED], subtype="Optical/Imaging Devices")
MONOCLE = Electronics("Monocle", cost=3000, page_ref=444, rating="-", avail=[12, RESTRICTED], capacity=[1, "to", 3], subtype="Optical/Imaging Devices")
# =============== VISION ENCHANCEMENTS 
LOW_LIGHT_VISION = Electronics("Low_Light_Vision", cost=500, page_ref=444, rating="-", avail=4, capacity=1, subtype="Vision Enhancement")
FLARE_COMPENSATION = Electronics("Flare_Compensation", cost=250, page_ref=444, rating="-", avail=1, capacity=1, subtype="Vision Enhancement")
IMAGE_LINK = Electronics("Image_Link", cost=25, page_ref=444, rating="-", avail="-", capacity=1, subtype="Vision Enhancement")
SMARTLINK = Electronics("Smartlink", cost=2000, page_ref=444, rating="-", avail=[4, RESTRICTED], capacity=1, subtype="Vision Enhancement")
THERMOGRAPHIC_VISION = Electronics("Thermographic_Vision", cost=500, page_ref=444, rating="-", avail=6, capacity=1, subtype="Vision Enhancement")
VISION_ENHANCEMENT = Electronics("Vision_Enhancement", cost=["Rating", "*", 500], page_ref=444, rating="-", avail=[["Rating", "*", 2], 0], capacity="Rating", subtype="Vision Enhancement")
VISION_MAGNIFICATION = Electronics("Vision_Magnification", cost=250, page_ref=444, rating="-", avail=2, capacity=1, subtype="Vision Enhancement")
# =============== AUDIO DEVICES=======
DIRECTIONAL_MIC = Electronics("Directional_Mic", cost=["Capactiy", "*", 50], page_ref=445, rating="-", avail=4, capacity=[1, "to", 6], subtype="Audio Device")
EAR_BUDS = Electronics("Ear_Buds", cost=["Capactiy", "*", 50], page_ref=445, rating="-", avail="-", capacity=[1, "to", 3], subtype="Audio Device")
HEADPHONES = Electronics("Headphones", cost=["Capactiy", "*", 50], page_ref=445, rating="-", avail="-", capacity=[1, "to", 6], subtype="Audio Device")
LASER_MIC = Electronics("Laser_Mic", cost=["Capactiy", "*", 100], page_ref=445, rating="-", avail=[6, RESTRICTED], capacity=[1, "to", 6], subtype="Audio Device")
OMNI_DIRECTIONAL_MIC = Electronics("Omni_Directional_Mic", cost=["Capactiy", "*", 50], page_ref=445, rating="-", avail="-", capacity=[1, "to", 6], subtype="Audio Device")
# =============== AUDIO ENHANCEMENTS==
AUDIO_ENHANCEMENT = Electronics("Audio_Enhancement", cost=["Rating", "*", 500], page_ref=445, rating=[1, "to", 3], avail=[["Rating", "*", 2], 0], capacity="Rating", subtype="Audio Enhancement")
SELECT_SOUND_FILTER = Electronics("Select_Sound_Filter", cost=["Rating", "*", 250], page_ref=445, rating=[1, "to", 3], avail=[["Rating", "*", 3], 0], capacity="Rating", subtype="Audio Enhancement")
SPACIAL_REGONISER = Electronics("Spacial_Regoniser", cost=1000, page_ref=445, rating="-", avail=4, capacity=2, subtype="Audio Enhancement")
# =============== SENSORS ============
"""
I'm like 100 lines into electronics alone, probably a few hundred if you include everything in this data dump section.
    So far everything has been predictable. Sure there's been some edge cases and oddities, but that's to be expected, 
    a game would be boring if everything was boxed into the same formula, sharing the same restrictions.
I say this because the sensor section can go fuck itself. For now. I'll figure out something in the future, probably
    a shitty band-aid solution because I really do not want to reengineer how I've been storing data up to this point.
Fuck that.
"""
# =============== SECURITY DEVICES====
KEY_COMBINATION_LOCK = Electronics("Key_Combination_Lock", cost=["Rating", "*", 10], page_ref=447, rating=[1, "to", 6], avail="Rating", subtype="Security Device")
MAGLOCK = Electronics("Maglock", cost=["Rating", "*", 100], page_ref=447, rating="-", avail="Rating", subtype="Security Device")
KEYPAD_CARD_READER = Electronics("Keypad_Card_Reader", cost=50, page_ref=447, rating="-", avail="-", subtype="Security Device")
ANTI_TAMPER_CIRCUITS = Electronics("Anti_Tamper_Circuits", cost=["Rating", "*", 250], page_ref=447, rating=[1, "to", 4], avail="Rating", subtype="Security Device")
# ============== RESTRAINT ===========
METAL_RESTRAINT = Electronics("Metal_Restraint", cost=20, page_ref=447, rating="-", avail="-", subtype="Restraint")
PLATEEL_RESTRAINT = Electronics("Plateel_Restraint", cost=50, page_ref=447, rating="-", avail=[6, RESTRICTED], subtype="Restraint")
PLASTIC_RESTRAINT_PER_10 = Electronics("Plastic_Restraint_Per_10", cost=5, page_ref=447, rating="-", avail="-", subtype="Restraint")
CONTAINMENT_MANACLES = Electronics("Containment_Manacles", cost=250, page_ref=447, rating="-", avail=[6, RESTRICTED], subtype="Restraint")
# ============== BREAKING AND ENTERING
AUTOPICKER = Electronics("Autopicker", cost=["Rating", "*", 500], page_ref=448, rating=[1, "to", 6], avail=[8, RESTRICTED], subtype="B&E Gear")
CELLUAR_GLOVE_MOLDER = Electronics("Celluar_Glove_Molder", cost=["Rating", "*", 500], page_ref=448, rating=[1, "to", 4], avail=[12, FORBIDDEN], subtype="B&E Gear")
CHISEL_CROWBAR = Electronics("Chisel_Crowbar", cost=20, page_ref=448, rating="-", avail="-", subtype="B&E Gear")
KEYCARD_COPIER = Electronics("Keycard_Copier", cost=["Rating", "*", 600], page_ref=448, rating=[1, "to", 6], avail=[8, FORBIDDEN], subtype="B&E Gear")
LOCKPICK_SET = Electronics("Lockpick_Set", cost=250, page_ref=448, rating="-", avail=[4, RESTRICTED], subtype="B&E Gear")
MAGLOCK_PASSKEY = Electronics("Maglock_Passkey", cost=["Rating", "*", 2000], page_ref=448, rating=[1, "to", 4], avail=[["Rating", "*", 3], FORBIDDEN], subtype="B&E Gear")
MINIWELDER = Electronics("Miniwelder", cost=250, page_ref=448, rating="-", avail=2, subtype="B&E Gear")
MINIWELDER_FUEL_CANISTER = Electronics("Miniwelder_Fuel_Canister", cost=80, page_ref=448, rating="-", avail=2, subtype="B&E Gear")
MONOFILAMENT_CHAINSAW = Electronics("Monofilament_Chainsaw", cost=500, page_ref=448, rating="-", avail=8, subtype="B&E Gear")
SEQUENCER = Electronics("Sequencer", cost=["Rating", "*", 250], page_ref=448, rating=[1, "to", 6], avail=[["Rating", "*", 3], RESTRICTED], subtype="B&E Gear")

"""
    INDUSTRIAL CHEMICALS
    No I don't know why this gets its own chapter in the book either
"""
GLUE_SOLVENT = Item("Glue_Solvent", cost=90, page_ref=448, avail=2, category="Industrial Chemicals")
GLUE_SPRAYER= Item("Glue_Sprayer", cost=150, page_ref=448, avail=2, category="Industrial Chemicals")
THERMITE_BURNING_BAR = Item("Thermite_Burning_Bar", cost=500, page_ref=448, avail=[16, RESTRICTED], category="Industrial Chemicals")

"""
    SURVIVAL GEAR
"""
CHEMSUIT = Item("Chemsuit", cost=["Rating", "*", 150], page_ref=449, rating=[1, "to", 6], avail=[["Rating", "*", 2],0], category="Survival Gear")
CLIMBING_GEAR = Item("Climbing_Gear", cost=200, page_ref=449, rating="-", avail="-", category="Survival Gear")
DIVING_GEAR = Item("Diving_Gear", cost=2000, page_ref=449, rating="-", avail=6, category="Survival Gear")
FLASHLIGHT = Item("Flashlight", cost=25, page_ref=449, rating="-", avail="-", category="Survival Gear")
GAS_MASK = Item("Gas_Mask", cost=200, page_ref=449, rating="-", avail="-", category="Survival Gear")
GECKO_TAPE_GLOVES = Item("Gecko_Tape_Gloves", cost=250, page_ref=449, rating="-", avail=12, category="Survival Gear")
HAZMAT_SUIT = Item("Hazmat_Suit", cost=3000, page_ref=449, rating="-", avail=8, category="Survival Gear")
LIGHT_STICK = Item("Light_Stick", cost=25, page_ref=449, rating="-", avail="-", category="Survival Gear")
MAGNESIUM_TORCH = Item("Magnesium_Torch", cost=5, page_ref=449, rating="-", avail="-", category="Survival Gear")
MICRO_FLARE_LAUNCHER = Item("Micro_Flare_Launcher", cost=175, page_ref=449, rating="-", avail="-", category="Survival Gear")
MICRO_FLARES = Item("Micro_Flares", cost=25, page_ref=449, rating="-", avail="-", category="Survival Gear")
RAPPELLING_GLOVES = Item("Rappelling_Gloves", cost=50, page_ref=449, rating="-", avail="-", category="Survival Gear")
RESPIRATOR = Item("Respirator", cost=["Rating", "*", 50], page_ref=449, rating=[1, "to", 6], avail="-", category="Survival Gear")
SURVIVAL_KIT = Item("Survival_Kit", cost=200, page_ref=449, rating="-", avail=4, category="Survival Gear")
"""
    LIFESTYLE
"""
STREET_LIFESTYLE = Lifestyle("Street_Lifestyle", "1d6", 20, 0)
SQUATTER_LIFESTYLE = Lifestyle("Squatter_Lifestyle", "2d6", 40, 500)
LOW_LIFESTYLE = Lifestyle("Low_Lifestyle", "3d6", 60, 2000)
MIDDLE_LIFESTYLE = Lifestyle("Middle_Lifestyle", "4d6", 100, 5000)
HIGH_LIFESTYLE = Lifestyle("High_Lifestyle", "5d6", 500, 10_000)
LUXURY_LIFESTYLE = Lifestyle("Luxury_Lifestyle", "6d6", 1000, 100_000)

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
print(SENSOR_RFID.category)