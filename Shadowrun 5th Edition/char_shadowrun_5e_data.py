import random
class Attribute:

    def __init__(self, name, value: int = 0):
        self.name = name
        self.value = value
        self.limit = 6
        if name == "Essence":
            self.limit = None
        self.type = self.get_type(name)

    def __repr__(self):
        return f"{self.name}: [{self.value}/{self.limit}]"

    def get_type(self, name):
        match name:
            case "Body" | "Agility" | "Reaction" | "Strength":
                return "Physical"
            case "Logic" | "Intuition" | "Charisma":
                return "Mental"
            case "Edge" | "Essence" | "Magic" | "Resonance":
                return "Special"
            case _:
                return ValueError("Attribute cannot get type due to bad name")

class Attributes:
    def __init__(self):
        self.Body = Attribute('Body')
        self.Agility = Attribute('Agility')
        self.Reaction = Attribute('Reaction')
        self.Strength = Attribute('Strength')
        self.Charisma = Attribute('Charisma')
        self.Intuition = Attribute('Intuition')
        self.Logic = Attribute('Logic')
        self.Willpower = Attribute('Willpower')
        self.Edge = Attribute('Edge')
        self.Essence = Attribute('Essence')
        self.List = [self.Body, self.Agility, self.Reaction, self.Strength, self.Charisma, self.Intuition, self.Logic, self.Willpower, self.Edge, self.Essence]

    def init_stat_block(self):
        for attribute in self.List:
            if attribute.name != "Essence":
                attribute.value = 1
                attribute.limit = 6
            else:
                attribute.value = 6

    def __repr__(self):
        return str([i.__repr__() for i in self.List])

class Character:
    def __init__(self):
        # Personal Data
        self.Name = None
        self.Concept = None
        self.Metatype = None
        self.Ethnicity = None
        self.Age = None
        self.Sex = None
        self.Height = None
        self.Weight = None
        self.Street_cred = None
        self.Notoriety = None
        self.Public_awareness = None
        self.Karma = None
        self.Total_karma = None
        self.Misc = None
        # Attributes
        self.Body = None
        self.Agility = None 
        self.Reaction = None 
        self.Strength = None 
        self.Willpower = None 
        self.Logic = None 
        self.Intuition = None 
        self.Charisma = None
        self.Essence = None
        self.Edge = None
        self.Magic = None
        self.Resonance = None 
        self.Initiative = None 
        self.Matrix_initiative = None 
        self.Astral_initiative = None 
        self.Composure = None 
        self.Judge_intentions = None 
        self.Memory = None
        self.Lift_carry = None 
        self.Movement = None 
        self.Physical_limit = None 
        self.Mental_limit = None 
        self.Social_limit = None
        self.PhysicalAttributes = [self.Body, self.Agility, self.Reaction, self.Strength]
        self.MentalAttributes = [self.Willpower, self.Logic, self.Intuition, self.Charisma]
        self.SpecialAttributes = [self.Edge, self.Essence, self.Magic, self.Resonance]
        self.CoreAttributes = self.PhysicalAttributes + self.MentalAttributes + self.SpecialAttributes
        # Skills
        self.Skills = {
                'Active': None,
                'Knowledge': None,
                'Language': None
                }
        self.Specialisations = {}
        # IDs/Lifestyle/Currency
        self.Primary_lifestyle = None
        self.Nuyen = None
        self.Licences = None
        self.Other = None
        # Core Combat Info
        self.Physical_armor = None 
        self.Primary_ranged_weapon = None
        self.Primary_melee_weapon = None
        self.Physical_dmg_track = None
        self.Stun_dmg_track = None
        self.Overflow = None
        # Qualities
        self.Qualities = None
        # Contacts
        self.Contacts = None
        # Gear
        self.Ranged_weapons = None
        self.Melee_weapons = None
        self.Armor = None
        self.Cyberdeck = None
        self.Augmentations = None
        self.Vehicle = None
        self.Spells = None
        self.Preparations_rituals = None
        self.Complex_forms = None
        self.Adept_powers = None
        self.Gear = None
        # Other
        self.MagicResoUser = None

    def print_stats(self):
        print(f'{self.Body}\n{self.Agility}\n{self.Reaction}\n{self.Strength}')
        print(f'{self.Logic}\n{self.Willpower}\n{self.Intuition}\n{self.Charisma}')
        print(f'{self.Edge}\n{self.Essence}')

    def redo_attr(self):
        self.PhysicalAttributes = [self.Body, self.Agility, self.Reaction, self.Strength]
        self.MentalAttributes = [self.Willpower, self.Logic, self.Intuition, self.Charisma]
        self.SpecialAttributes = [self.Edge, self.Essence, self.Magic, self.Resonance]
        self.CoreAttributes = self.PhysicalAttributes + self.MentalAttributes + self.SpecialAttributes

    def highest_core_attr(self):
        non_zero_attrs = []
        for attr in self.CoreAttributes:
            if attr is None:
                pass
            if type(attr) == Attribute:
                non_zero_attrs.append(attr)
        highest_attr = None
        for attr in non_zero_attrs:
            if highest_attr is None or attr.value > highest_attr.value:
                highest_attr = attr
        return highest_attr

    def debug_gen_attrs(self, magic=False, techo=False):
        def roll_attr(attr):
            if attr.name == "Essence":
                return
            attr.value = random.randint(1, attr.limit)
        if magic and techo:
            limitation = 1
        elif techo:
            limitation = 2
        elif magic:
            limitation = 3
        else:
            limitation = random.randint(1,3)

        self.Body = Attribute("Body")
        self.Agility = Attribute("Agility")
        self.Reaction = Attribute("Reaction")
        self.Strength = Attribute("Strength")
        self.Willpower = Attribute("Willpower")
        self.Logic = Attribute("Logic")
        self.Intuition = Attribute("Intuition")
        self.Charisma = Attribute("Charisma")
        self.Edge = Attribute("Edge")
        self.Essence = Attribute("Essence")
        self.Magic = Attribute("Magic")
        self.Resonance = Attribute("Resonance")
        self.CoreAttributes = [
                self.Body, self.Agility, self.Reaction, self.Strength, self.Willpower,
                self.Logic, self.Intuition, self.Charisma, self.Edge, self.Essence, 
                self.Magic, self.Resonance
        ]
        for attr in self.CoreAttributes:
            roll_attr(attr)
        match limitation:
            case 1:
                self.Magic = None
                self.Resonance = None
            case 2:
                self.Magic=None
            case 3:
                self.Resonance=None

class Contact:
    def __init__(self, skill_pool, k_skill_pool, uses, meetups):
        self.name = name
        self.attributes = {'Body': 0, 'Agility': 0, 'Reaction': 0, 'Strength': 0,
                           'Logic': 0, 'Willpower': 0, 'Intuition': 0, 'Charisma': 0}
        # Rolling for attribute values
        values = [random.randint(2,5) for _ in range(8)]
        #    Then ensures only one attribute value can be a 5. Chooses randomly
        while values.count(5) > 1:
            values[random.choice([values.index(i) for i in values if i == 5])] -= 1
            
        for idx, attr in enumerate(self.attributes):
            self.attributes[attr] = values[idx]

        self.special_attrs = {'Edge': random.randint(2,3), 'Essence': 6}
        self.skills = self.get_skills(skill_pool)
        self.knowledge_skills = self.get_skills(k_skill_pool)

        self.uses = uses
        self.meetups = meetups

    def get_skills(self, potential_skills):
        skill_dict = {}
        no_of_skills = random.randint(4,9)
        if no_of_skills > len(poential_skills):
            for skill in potential_skills:
                skill_dict[skill] = random.randint(3, 6)
        for _ in range(no_of_skills):
            while True:
                skill = random.choice(potential_skills)
                if skill in skill_dict.keys():
                    continue
                else:
                    skill_dict[skill] = random.randint(3, 6)
                    break
        return skill_dict

    def __repr__(self):
        return self.name



class AbstractBaseClass:
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
        self.attributes = Attributes()
        super().__init__(name, **kwargs)


class Archetype(AbstractBaseClass):
    items = []
    def __init__(self, name, **kwargs):
        Archetype.items.append(self)
        super().__init__(name, **kwargs)


class DamageType(AbstractBaseClass):
    items = []
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)


class ConditionMonitor(AbstractBaseClass):
    def __init__(self, name, physical, stun, overflow, **kwargs):
        super().__init__(name, **kwargs)
        self.physical = physical
        self.stun = stun
        self.overflow = overflow


class Quality(AbstractBaseClass):
    items = []
    def __init__(self, name, **kwargs):
        Quality.items.append(self)
        super().__init__(name, **kwargs)

    def __repr__(self):
        return_string = ""
        cost_string = f"Cost: {self.cost}"
        if hasattr(self, "negative"):
            cost_string = f"Cost: -{self.cost}"
        if hasattr(self, "level"):
            return f"{cost_string} | Level: {self.level}"
        else:
            return f"{cost_string}"


class Skill(AbstractBaseClass):
    items = []
    def __init__(self, name, attribute, skill_type, spec=[], **kwargs):
        super().__init__(name, **kwargs)
        Skill.items.append(self)
        self.attribute = attribute
        self.skill_type = skill_type
        self.rating = 0
        self.group = False
        self.spec = spec

    def __repr__(self):
        if isinstance(self.spec, str):
            if self.group:
                raise ValueError
            return f"{self.name}: {self.rating} (Specialisation: {self.spec})"
        if self.group:
            return f"{self.name}: {self.rating} (Group: {self.group})"
        else:
            return f"{self.name}: {self.rating}"


class SkillGroup(AbstractBaseClass):
    items =[]
    def __init__(self, name, skills, **kwargs):
        super().__init__(name, **kwargs)
        SkillGroup.items.append(self)
        self.skills = skills
        self.idx = 0
    
    def __repr__(self):
        return [skill.name for skill in self.skills]
"""
    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self.skills[self.idx]
        except IndexError:
            raise StopIteration
        self.idx += 1
        return result
"""


class Gear(AbstractBaseClass):
    items = []
    def __init__(self, name, cost, page_ref, **kwargs):
        Gear.items.append(self)
        super().__init__(name, **kwargs)
        self.cost = cost
        self.page_ref = page_ref
        self.category = None
        self.subtype = None

    def __repr__(self):
        if self.subtype is not None:
            return f'[{self.category}/{self.subtype}] {self.name} (p.{self.page_ref})'
        return f'[{self.category}] {self.name} (p. {self.page_ref})'



class MeleeWeapon(Gear):
    items = []
    def __init__(self, name, cost, page_ref, avail, subtype, **kwargs):
        MeleeWeapon.items.append(self)
        super().__init__(name, cost, page_ref, **kwargs)
        self.avail = avail
        self.category = "Melee Weapon"
        self.subtype = subtype


class ProjectileWeapon(Gear):
    items = []
    def __init__(self, name, cost, page_ref, avail, subtype, **kwargs):
        ProjectileWeapon.items.append(self)
        super().__init__(name, cost, page_ref, **kwargs)
        self.avail = avail
        self.category = "ProjectileWeapon"
        self.subtype = subtype


class Firearm(Gear):
    items = []
    def __init__(self, name, cost, page_ref, avail, subtype, **kwargs):
        Firearm.items.append(self)
        super().__init__(name, cost, page_ref, **kwargs)
        self.avail = avail
        self.category = "Firearm"
        self.subtype = subtype


class FirearmAccessory(Gear):
    items = []
    def __init__(self, name, cost, page_ref, avail, **kwargs):
        FirearmAccessory.items.append(self)
        super().__init__(name, cost, page_ref, **kwargs)
        self.avail = avail
        self.category = "Firearm Accessory"


class Ammo(Gear):
    items = []
    def __init__(self, name, cost, page_ref, avail, **kwargs):
        Ammo.items.append(self)
        super().__init__(name, cost, page_ref, **kwargs)
        self.avail = avail
        self.category = "Ammunition"


class Clothing(Gear):
    items = []
    def __init__(self, name, cost, page_ref, **kwargs):
        Clothing.items.append(self)
        super().__init__(name, cost, page_ref, **kwargs)
        self.category = "Clothing"


class Armor(Gear):
    items = []
    def __init__(self, name, cost, page_ref, **kwargs):
        Armor.items.append(self)
        super().__init__(name, cost, page_ref, **kwargs)
        self.category = "Armor"


class ArmorModification(Gear):
    items = []
    def __init__(self, name, cost, page_ref, **kwargs):
        ArmorModification.items.append(self)
        super().__init__(name, cost, page_ref, **kwargs)
        self.category = "Armor Modification"


class Electronics(Gear):
    items = []
    def __init__(self, name, cost, page_ref, **kwargs):
        Electronics.items.append(self)
        super().__init__(name, cost, page_ref, **kwargs)
        self.category = "Electronics"


class Sensor(AbstractBaseClass):
    items = []
    def __init__(self, sensor_type, housing = None, functions = None, **kwargs):
        Sensor.items.append(self)
        self.name = "Sensor"
        super().__init__(self.name, **kwargs)
        self.sensor_type = sensor_type 
        self.housing = housing
        self.functions = functions
        self.rating = 0
        self.cost = 0

    def get_info(self):
        # functions_format = ", ".join([f"{i} (Range: {self.functions[self.functions.index(i)]['Range']})" for i in self.functions])
        print(f"\nSensor Name: {self.name}\n-- Housing: {self.housing}\n-- Type: {self.sensor_type}\n-- Functions: {self.functions}")


"""
    The Item Class. Why now?

heritants of the "Gear" class could all technically classify as "Items", I'm making a distinction
    from the above and generic items by common-sense TTRPG logic, as oxymoronic as that sounds.

If it equips to you, it ain't an item.
If it gets thrust into your storage medium of choice to be used at a later date, it's an item.

Even things like explosvies, who serve the same purpose as weaponary (do the hurty damage), count as items as I'm arbitrarily
    making the call that you wouldn't equip explosives in the same way you would armor or a sword or a gun.
Also I made the Ammo class before I got around to doing this class so fuck you, it stays as is.
"""

class Item(Gear):
    items = []
    def __init__(self, name, cost, page_ref, category="Item", **kwargs):
        Item.items.append(self)
        super().__init__(name, cost, page_ref, **kwargs)
        self.category = category


class Vehicle(Gear):
    items = []
    def __init__(self, name, cost, page_ref, skill_req, category="Vehicle", subtype=None, **kwargs):
        Vehicle.items.append(self)
        super().__init__(name, cost, page_ref, **kwargs)
        self.category = category
        self.subtype = subtype
        self.page_ref = page_ref
        self.skill_req = skill_req



class GearAvailability(AbstractBaseClass):
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)


class Lifestyle(AbstractBaseClass):
    items = []
    def __init__(self, name, **kwargs):
        Lifestyle.items.append(self)
        super().__init__(name, **kwargs)


class ComplexForm(AbstractBaseClass):
    items = []
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        ComplexForm.items.append(self)


class Spell(AbstractBaseClass):
    items = []
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        Spell.items.append(self)


class Augmentation(AbstractBaseClass):
    items = []
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        Augmentation.items.append(self)

class AugmentationGrade(AbstractBaseClass):
    items = []
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        AugmentationGrade.items.append(self)

class KarmaLogger():
    def __init__(self):
        self.logs = []
        self.index = 0

    def __repr__(self):
        return "\n".join(self.logs)

    def append(self, item):
        self.index += 1
        self.logs.append(f'[{self.index}] {item}')

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
ARCHERY = Skill("Archery", AGILITY, "Active", spec=['Bow', 'Crossbow', 'Non-Standard Ammunition', 'Slingshot'])
AUTOMATICS = Skill("Automatics", AGILITY, "Active", spec=['Assault Rifles', 'Cyber-Implant', 'Machine Pistols', 'Submachine Guns'])
BLADES = Skill("Blades", AGILITY, "Active", spec=['Axes', 'Knives', 'Swords', 'Parrying'])
CLUBS = Skill("Clubs", AGILITY, "Active", spec=['Batons', 'Hammers', 'Saps', 'Staves', 'Parrying'])
ESCAPE_ARTIST = Skill("Escape Artist", AGILITY, "Active", spec=['Cuffs (Restraint)', 'Ropes (Restraint)', 'Zip Ties (Restraint)', 'Contortionism'])
EXOTIC_MELEE_WEAPON = Skill("Exotic Melee Weapon", AGILITY, "Active", specs=None)
EXOTIC_RANGED_WEAPON = Skill("Exotic Ranged Weapon", AGILITY, "Active", specs=None)
GUNNERY = Skill("Gunnery", AGILITY, "Active", spec=['Artillery', 'Ballistic', 'Energy', 'Guided Missile', 'Rocket'])
GYMNASTICS = Skill("Gymnastics", AGILITY, "Active", spec=['Balance', 'Climbing', 'Dance', 'Leaping', 'Parkour', 'Rolling'])
HEAVY_WEAPONS = Skill("Heavy Weapons", AGILITY, "Active", spec=['Assault Cannons', 'Grenade Launchers', 'Guided Missiles', 'Machine Guns', 'Rocket Launchers'])
LOCKSMITH = Skill("Locksmith", AGILITY, "Active", spec=['Combination', 'Keypad', 'Maglock', 'Tumbler', 'Voice Recognition'])
LONGARMS = Skill("Longarms", AGILITY, "Active", spec=['Extended-Range Shots', 'Long-Range Shots', 'Shotguns', 'Sniper Rifles'])
PALMING = Skill("Palming", AGILITY, "Active", spec=['Ledgerdemain', 'Pickpocket', 'Pilfering'])
PISTOLS = Skill("Pistols", AGILITY, "Active", spec=['Holdouts', 'Revolvers', 'Semi-Automatics', 'Tasers'])
SNEAKING = Skill("Sneaking", AGILITY, "Active", spec=['Jungle Stealth', 'Urban Stealth', 'Desert Stealth'])
THROWING_WEAPONS = Skill("Throwing Weapons", AGILITY, "Active", spec=['Aerodynamic', 'Blades', 'Non-Aerodynamic'])
UNARMED_COMBAT = Skill("Unarmed Combat", AGILITY, "Active", spec=['Blocking', 'Cyber Implants', 'Subduing Combat', 'A Martial Art'])
# =============== BODY ===================
DIVING = Skill("Diving", BODY, "Active", spec=['Liquid Breathing Apparatus', 'Mixed Gas Breathing Apparatus', 'Oxygen Extraction Breathing Apparatus', 'SCUBA', 'Artic Diving', 'Cave Diving', 'Commercial Diving', 'Military Diving', 'Controlled Hyperventillation'])
FREE_FALL = Skill("Free Fall", BODY, "Active", spec=['BASE Jumping', 'Break-Fall', 'Bungee', 'HALO', 'Low Altitude', 'Parachute', 'Static Line', 'Wingsuit', 'Zipline'])
# =============== REACTION ===============
PILOT_AEROSPACE = Skill("Pilot Aerospace", REACTION, "Active", spec=['Deep Space', 'Launch Craft', 'Remote Operation', 'Semiballistic', 'Suborbital'])
PILOT_AIRCRAFT = Skill("Pilot Aircraft", REACTION, "Active", spec=['Fixed-Wing', 'Lighter-Than-Air', 'Remote Operation', 'Rotary Wing', 'Tilt Wing', 'Vectored Thrust'])
PILOT_EXOTIC_VEHICLE_SPECIFIC = Skill("Pilot Exotic Vehicle Specific", REACTION, "Active", specs=None)
PILOT_GROUND_CRAFT = Skill("Pilot Ground Craft", REACTION, "Active", spec=['Bike', 'Hovercraft', 'Remote Operation', 'Tracked', 'Wheeled'])
PILOT_WALKER = Skill("Pilot Walker", REACTION, "Active", spec=['Biped', 'Multiped', 'Quadruped', 'Remote'])
PILOT_WATERCRAFT = Skill("Pilot Watercraft", REACTION, "Active", spec=['Hydrofoil', 'Motorboat', 'Remote Operation', 'Sail', 'Ship', 'Submarine'])
# =============== STRENGTH ===============
RUNNING = Skill("Running", STRENGTH, "Active", spec=['Distance', 'Sprint', 'Desert Running', 'Urban Running', 'Wilderness Running'])
SWIMMING = Skill("Swimming", STRENGTH, "Active", spec=['Dash', 'Long Distance'])
# =============== CHARISMA ===============
ANIMAL_HANDLING = Skill("Animal Handling", CHARISMA, "Active", spec=['Herding', 'Riding', 'Training', 'Cat Handling', 'Bird Handling', 'Hell Hound Handling', 'Horse Handling', 'Dolphin Handling'])
CON = Skill("Con", CHARISMA, "Active", spec=['Fast Talking', 'Seduction'])
ETIQUETTE = Skill("Etiquette", CHARISMA, "Active", spec=['Corporate Etiquette', 'High Society Etiquette', 'Media Etiquette', 'Mercenary Etiquette', 'Street Etiquette'])
IMPERSONATION = Skill("Impersonation", CHARISMA, "Active", spec=['Dwarf Impersonation', 'Elf Impersonation', 'Human Impersonation', 'Ork Impersonation', 'Troll Impersonation'])
INSTRUCTION = Skill("Instruction", CHARISMA, "Active", spec=['Combat Instruction', 'Language Instruction', 'Magical Instruction', 'Academic Instruction', 'Knowledge Instruction', 'Street Knowledge Instruction'])
INTIMIDATION = Skill("Intimidation", CHARISMA, "Active", spec=['Interrogation', 'Mental Intimidation', 'Physical Intimidation', 'Torture'])
LEADERSHIP = Skill("Leadership", CHARISMA, "Active", spec=['Command', 'Direct', 'Inspire', 'Rally'])
NEGOTIATION = Skill("Negotiation", CHARISMA, "Active", spec=['Bargining', 'Contracts', 'Diplomacy'])
PERFORMANCE = Skill("Performance", CHARISMA, "Active", spec=['Presentation', 'Acting Performance', 'Comedy Performance', 'Musical Performance'])
# =============== INTUITION ==============
ARTISAN = Skill("Artisan", INTUITION, "Active", spec=['Cooking', 'Sculpting', 'Drawing', 'Carpentry'])
ASSENSING = Skill("Assensing", INTUITION, "Active", spec=['Aura Reading', 'Metahuman Astral Signatures','Spirits Astral Signatures', 'Foci Astral Signatures', 'Wards Astral Signatures'])
DISGUISE = Skill("Disguise", INTUITION, "Active", spec=['Camoflage', 'Cosmetic', 'Theatrical', 'Trideo & Video'])
INTERESTS_KNOWLEDGE = Skill("Interests Knowledge", INTUITION, "Active")
LANGUAGE = Skill("Language", INTUITION, "Active", spec=['Read/Write', 'Speak by Dialect', 'Speak by Slang'])
NAVIGATION = Skill("Navigation", INTUITION, "Active", spec=['Augmented Reality Markers', 'Celestial', 'Compass', 'Maps', 'GPS'])
PERCEPTION = Skill("Perception", INTUITION, "Active", spec=['Hearing', 'Scent', 'Searching', 'Taste', 'Touch', 'Visual'])
STREET_KNOWLEDGE = Skill("Street Knowledge", INTUITION, "Active")
TRACKING = Skill("Tracking", INTUITION, "Active", spec=['Desert Tracking', 'Forest Tracking', 'Jungle Tracking', 'Mountain Tracking', 'Polar Tracking', 'Urban Tracking'])
# =============== LOGIC ==================
ACADEMIC_KNOWLEDGE = Skill("Academic Knowledge", LOGIC, "Active")
AERONAUTICS_MECHANIC = Skill("Aeronautics Mechanic", LOGIC, "Active", spec=['Aerospace', 'Fixed Wing', 'LTA (Blimp)', 'Rotary Wing', 'Tilt Wing', 'Vectored Thrust'])
ARCANA = Skill("Arcana", LOGIC, "Active", spec=['Spell Design', 'Focus Design', 'Spirit Formula'])
ARMORER = Skill("Armorer", LOGIC, "Active", spec=['Armor', 'Artillery', 'Explosives', 'Firearms', 'Melee Weapons', 'Heavy Weapons', 'Weapon Accessories'])
AUTOMOTIVE_MECHANIC = Skill("Automotive Mechanic", LOGIC, "Active", spec=['Walker', 'Hover', 'Tracked', 'Wheeled'])
BIOTECHNOLOGY = Skill("Biotechnology", LOGIC, "Active", spec=['Bioinformatics', 'Bioware', 'Cloning', 'Gene Therapy', 'Vat Maintenance'])
CHEMISTRY = Skill("Chemistry", LOGIC, "Active", spec=['Analytical', 'Biochemestry', 'Inorganic', 'Organic', 'Physical'])
COMPUTER = Skill("Computer", LOGIC, "Active", spec=['File Editing', 'Matrix Perception', 'Matrix Search'])
CYBERCOMBAT = Skill("Cybercombat", LOGIC, "Active", spec=['Devices', 'Grids', 'IC', 'Personas', 'Sprites'])
CYBERTECHNOLOGY = Skill("Cybertechnology", LOGIC, "Active", spec=['Bodyware', 'Cyberlimbs', 'Headware', 'Repair'])
DEMOLITIONS = Skill("Demolitions", LOGIC, "Active", spec=['Commercial Explosives', 'Defusing', 'Improvised Explosives', 'Plastic Explosives'])
ELECTRONIC_WARFARE = Skill("Electronic Warfare", LOGIC, "Active", spec=['Communications', 'Encryption', 'Jamming', 'Sensor Operations'])
FIRST_AID = Skill("First Aid", LOGIC, "Active", spec=['Gunshot Wounds', 'Resuscitation', 'Broken Bones', 'Burns'])
FORGERY = Skill("Forgery", LOGIC, "Active", spec=['Counterfeiting', 'Credstick Forgery', 'False ID', 'Image Doctoring', 'Paper Forgery'])
HACKING = Skill("Hacking", LOGIC, "Active", spec=['Devices', 'Files', 'Hosts', 'Personas'])
HARDWARE = Skill("Hardware", LOGIC, "Active", spec=['Commlinks', 'Cyberdecks', 'Smartguns'])
INDUSTRIAL_MECHANIC = Skill("Industrial Mechanic", LOGIC, "Active", spec=['Electrical Power Systems', 'Hydraulics', 'HVAC', 'Industrial Robotics', 'Structural', 'Welding'])
MEDICINE = Skill("Medicine", LOGIC, "Active", spec=['Cosmetic Surgery', 'Extended Care', 'Implant Surgery', 'Magical Health', 'Organ Culture', 'Trama Surgery'])
NAUTICAL_MECHANIC = Skill("Nautical Mechanic", LOGIC, "Active", spec=['Motorboat', 'Sailboat', 'Ship', 'Submarine'])
PROFESSIONAL_KNOWLEDGE = Skill("Professional Knowledge", LOGIC, "Active")
SOFTWARE = Skill("Software", LOGIC, "Active", spec=['Data Bombs', 'Editor Complex Form', 'Resonance Spike Complex Form', 'Tattletale Complex Form'])
# =============== WILLPOWER ==============
ASTRAL_COMBAT = Skill("Astral Combat", WILLPOWER, "Active", spec=['Specific Focus Type', 'Against Magicians', 'Against Spirits', 'Against Mana Barriers'])
SURVIVAL = Skill("Survival", WILLPOWER, "Active", spec=['Desert Survival', 'Forest Survival', 'Jungle Survival', 'Mountain Survival', 'Polar Survival', 'Urban Survival'])
# =============== MAGIC ==================
ALCHEMY = Skill("Alchemy", MAGIC, "Active", spec=['Command Trigger', 'Contact Trigger', 'Time Trigger', 'Combat Spells', 'Detection Spells'])
ARTIFICING = Skill("Artificing", MAGIC, "Active", spec=['Focus Analysis', 'Spell Crafting', 'Spirit Crafting', 'Power Crafting', 'Weapon Crafting', 'Qi Crafting', 'Metamagic Crafting', 'Qi Force Crafting'])
BANISHING = Skill("Banishing", MAGIC, "Active", spec=['Spirits of Air', 'Spirits of Earth', 'Spiriths of Beasts', 'Spirits of Fire', 'Spirits of Man', 'Spirits Water'])
BINDING = Skill("Binding", MAGIC, "Active", spec=['Spiritss of Air', 'Spirits of Earth', 'Spiriths of Beasts', 'Spirits of Fire', 'Spirits of Man', 'Spirits Water'])
COUNTERSPELLING = Skill("Counterspelling", MAGIC, "Active", spec=['Combat Spells', 'Detection Spells', 'Health Spells', 'Illusion Spells', 'Manipulation Spells'])
DISENCHANTING = Skill("Disenchanting", MAGIC, "Active", spec=['Alchemical Preparations', 'Power', 'Foci'])
RITUAL_SPELLCASTING = Skill("Ritual Spellcasting", MAGIC, "Active", spec=['Keyword', 'Anchored', 'Spell'])
SPELLCASTING = Skill("Spellcasting", MAGIC, "Active", spec=['Combat Spells', 'Detection Spells', 'Health Spells', 'Illusion Spells', 'Manipulation Spells'])
SUMMONING = Skill("Summoning", MAGIC, "Active", spec=['Spirit of Air', 'Spirit of Earth', 'Spirith of Beasts', 'Spirit of Fire', 'Spirits of Man', 'Spirits Water'])
# =============== RESONANCE ==============
COMPILING = Skill("Compiling", RESONANCE, "Active", spec=['Courier Sprite', 'Crack Sprite', 'Data Sprite', 'Fault Sprite', 'Machine Sprite'])
DECOMPILING = Skill("Decompiling", RESONANCE, "Active", spec=['Couriter Sprite', 'Crack Sprite', 'Data Sprite', 'Fault Sprite', 'Machine Sprite'])
REGISTERING = Skill("Registering", RESONANCE, "Active", spec=['Couriter Sprite', 'Crack Sprite', 'Data Sprite', 'Fault Sprite', 'Machine Sprite'])

"""
    KNOWLEDGE SKILLS

These are more fluff than the more mechanics-based 'Active' skills
"""
# =============== ACADEMIC ===============
BIOLOGY = Skill("Biology", LOGIC, "Knowledge", category="Academic")
MEDICINE_K = Skill("Medicine", LOGIC, "Knowledge", category="Academic")
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

ACTIVE_SKILLS = [_ for _ in Skill.items if _.skill_type == "Active"]
KNOWLEDGE_SKILLS = [_ for _ in Skill.items if _.skill_type == "Knowledge"]
LANGUAGE_SKILLS = [_ for _ in Skill.items if _.skill_type == "Language"]

"""
    SKILL GROUPS
"""
ACTING = SkillGroup("Acting", [CON, IMPERSONATION, PERFORMANCE])
ATHLETICS = SkillGroup("Athletics", [GYMNASTICS, RUNNING, SWIMMING])
BIOTECH = SkillGroup("Biotech", [CYBERTECHNOLOGY, FIRST_AID, MEDICINE])
CLOSE_COMBAT = SkillGroup("Close_Combat", [BLADES, CLUBS, UNARMED_COMBAT])
CONJURING = SkillGroup("Conjuring", [BANISHING, BINDING, SUMMONING])
CRACKING = SkillGroup("Cracking", [CYBERCOMBAT, ELECTRONIC_WARFARE, HACKING])
ELECTRONICS = SkillGroup("Electronics", [COMPUTER, SOFTWARE, HARDWARE])
ENCHANTING = SkillGroup("Enchanting", [ALCHEMY, ARTIFICING, DISENCHANTING])
FIREARMS = SkillGroup("Firearms", [AUTOMATICS, LONGARMS, PISTOLS])
INFLUENCE = SkillGroup("Influence", [ETIQUETTE, LEADERSHIP, NEGOTIATION])
ENGINEERING = SkillGroup("Engineering", [AERONAUTICS_MECHANIC, AUTOMOTIVE_MECHANIC, INDUSTRIAL_MECHANIC, NAUTICAL_MECHANIC])
OUTDOORS = SkillGroup("Outdoors", [NAVIGATION, SURVIVAL, TRACKING])
SORCERY = SkillGroup("Sorcery", [COUNTERSPELLING, RITUAL_SPELLCASTING, SPELLCASTING])
STEALTH = SkillGroup("Stealth", [DISGUISE, PALMING, SNEAKING])
TASKING = SkillGroup("Tasking", [COMPILING, DECOMPILING, REGISTERING])

SKILL_GROUPS = [group for group in SkillGroup.items]
MAGIC_SKILLS = [ASTRAL_COMBAT, ARCANA, BANISHING, BINDING, SUMMONING, ALCHEMY, ARTIFICING, DISENCHANTING, COUNTERSPELLING, RITUAL_SPELLCASTING, SPELLCASTING]
MAGIC_SKILL_GROUPS = [CONJURING, ENCHANTING, SORCERY]
RESONANCE_SKILLS = [COMPILING, DECOMPILING, REGISTERING]
VEHICLE_SKILLS = [PILOT_AEROSPACE, PILOT_AIRCRAFT, PILOT_GROUND_CRAFT, PILOT_WALKER, PILOT_WATERCRAFT]
COMBAT_ACTIVE_SKILLS = [ARCHERY, AUTOMATICS, BLADES, CLUBS, EXOTIC_RANGED_WEAPON, HEAVY_WEAPONS, LONGARMS, PISTOLS, THROWING_WEAPONS, UNARMED_COMBAT]
PHYSICAL_ACTIVE_SKILLS = [DISGUISE, DIVING, ESCAPE_ARTIST, FREE_FALL, GYMNASTICS, PALMING, PERCEPTION, RUNNING, SNEAKING, SURVIVAL, SWIMMING, TRACKING]
SOCIAL_SKILLS = [CON, ETIQUETTE, IMPERSONATION, INSTRUCTION, INTIMIDATION, LEADERSHIP, NEGOTIATION, PERFORMANCE]
TECHNICAL_SKILLS = [AERONAUTICS_MECHANIC, ANIMAL_HANDLING, ARMORER, ARTISAN, AUTOMOTIVE_MECHANIC, BIOTECHNOLOGY, CHEMISTRY, COMPUTER, CYBERCOMBAT, CYBERTECHNOLOGY, DEMOLITIONS, ELECTRONIC_WARFARE, FIRST_AID, FORGERY, HACKING, HARDWARE,
                    INDUSTRIAL_MECHANIC, LOCKSMITH, MEDICINE, NAUTICAL_MECHANIC, NAVIGATION, SOFTWARE]
DECKER_SKILLS = [CYBERCOMBAT, COMPUTER, CYBERTECHNOLOGY, ELECTRONIC_WARFARE, HACKING]
RIGGER_SKILLS = [PILOT_AEROSPACE, PILOT_AIRCRAFT, PILOT_GROUND_CRAFT, PILOT_WALKER, PILOT_WATERCRAFT]
FACE_SKILLS = [CON, IMPERSONATION, PERFORMANCE, ETIQUETTE, LEADERSHIP, NEGOTIATION]

"""
    METATYPES
"""
HUMAN = Metatype(
        "Human",
        stat_changes={'EDGE': [2, 7]},
        racial_bonus=None)
ELF = Metatype(
        "Elf",
        stat_changes={'AGILITY': [2,7], 'CHARISMA': [3,8]},
        racial_bonus=['Low Light Vision'])
DWARF = Metatype(
        "Dwarf", 
        stat_changes={'BODY': [3, 8], 'REACTION': [1, 5], 'STRENGTH': [3, 8], 'WILLPOWER': [2, 7]}, 
        racial_bonus=['Thermographic Vision', 'Pathogen/Toxin Resistance', '20% increased Lifestyle cost'])
ORK = Metatype(
        "Ork",
        stat_changes={'BODY': [4, 9], 'STRENGTH': [3, 8], 'LOGIC': [1, 5], 'CHARISMA': [1, 5]},
        racial_bonus=['Low Light Vision'])
TROLL = Metatype(
        "Troll",
        stat_changes={'BODY': [5, 10], 'AGILITY': [1, 5], 'STRENGTH': [5, 10], 'LOGIC': [1, 5], 'INTUITION': [1, 5], 'CHARISMA': [1, 4]},
        racial_bonus=['Thermographic Vision', '+1 Reach', '+1 dermal Armor', '100% increased Lifestyle cost'])

"""
    CHARACTER TYPES
"""
STREET_SAMURAI = Archetype('Street Samurai', pref_attrs=['Body', 'Agility' 'Reaction', 'Strength'])
COVERT_OPS_SPECIALIST = Archetype('Covert Ops Specialist', pref_attrs=['Body', 'Agility', 'Strength', 'Intuition'])
OCCULT_INVESTIGATOR = Archetype('Occult Investigator', pref_attrs=['Willpower', 'Intuition'], magic=True)
STREET_SHAMAN = Archetype('Street Shaman', pref_attrs=['Strength', 'Charisma'], magic=True)
COMBAT_MAGE = Archetype('Combat Mage', pref_attrs=['Body', 'Logic'], magic=True)
BRAWLING_ADEPT = Archetype('Brawling Adept', pref_attrs=['Body', 'Agility', 'Reaction', 'Strength'], magic=True)
WEAPONS_SPECIALIST = Archetype('Weapons Specialist', pref_attrs=['Agility'])
FACE = Archetype('Face', pref_attrs=['Charisma'])
TANK = Archetype('Tank', pref_attrs=['Body', 'Strength'])
DECKER = Archetype('Decker', pref_attrs=['Willpower', 'Logic'])
TECHNOMANCER = Archetype('Technomancer', pref_attrs=['Willpower', 'Logic', 'Intuition'], resonance=True)
GUNSLINGER_ADEPT = Archetype('Gunslinger Adept', pref_attrs=['Agility', 'Reaction'], magic=True)
DRONE_RIGGER = Archetype('Drone Rigger', pref_attrs=['Reaction', 'Logic'])
SMUGGLER = Archetype('Smuggler', pref_attrs=['Body', 'Reaction', 'Intuition'])
SPRAWL_GANGSTER = Archetype('Sprawl Gangster', pref_attrs=['Body', 'Strength'])
BOUNTY_HUNTER = Archetype('Bounty Hunter', pref_attrs=['Body', 'Strength'])

"""
    QUALITIES
"""
# POSITIVE QUALITIES
AMBIDEXTROUS = Quality('Ambidextrous', cost=4, page_ref=71)
ANALYTICAL_MIND = Quality('Analytical Mind', cost=5, page_ref=72)
APTITUDE = Quality('Aptitude', cost=14, page_ref=72)
ASTRAL_CHAMELON = Quality('Astral Chamelon', cost=10, page_ref=72)
BILINGUAL = Quality('Bilingual', cost=5, page_ref=72)
BLANDESS = Quality('Blandess', cost=8, page_ref=72)
CATLIKE = Quality('Catlike', cost=7, page_ref=72)
CODESLINGER = Quality('Codeslinger', cost=10, page_ref=72)
DOUBLE_JOINTED = Quality('Double Jointed', cost=6, page_ref=72)
EXCEPTIONAL_ATTRIBUTE = Quality('Exceptional Attribute', cost=14, page_ref=72)
FIRST_IMPRESSION = Quality('First Impression', cost=11, page_ref=74)
FOCUSED_CONCERNTRATION = Quality('Focused Concerntration', cost=4, page_ref=74, quantity=6)
GEARHEAD = Quality('Gearhead', cost=11, page_ref=74)
GUTS = Quality('Guts', cost=10, page_ref=74)
HIGH_PAIN_TOLERANCE = Quality('High Pain Tolerance', cost=7, page_ref=74, quantity=3)
HOME_GROUND = Quality('Home Ground', cost=10, page_ref=74, opts=['Astral Acclimation', 'You Know A Guy', 'Digital Turf', 'The Transporter', 'On the Lam', 'Street Politics'])
HUMAN_LOOKING = Quality('Human Looking', cost=6, page_ref=75)
INDOMITABLE = Quality('Indomitable', cost=8, page_ref=75, quantity=3)
JURYRIGGER = Quality('Juryrigger', cost=10, page_ref=75)
LUCKY = Quality('Lucky', cost=12, page_ref=76)
MAGICAL_RESISTANCE = Quality('Magical Resistance', cost=6, page_ref=76, quantity=4)
MENTOR_SPIRIT = Quality('Mentor Spirit', cost=5, page_ref=76, opts=['Bear', 'Cat', 'Dog', 'Dragonslayer', 'Eagle', 'Fire-Bringer', 'Mountain', 'Rat', 'Raven', 'Sea', 'Seducer', 'Shark', 'Snake', 'Thunderbird', 'Wise Warrior', 'Wolf'])
NATURAL_ATHLETE = Quality('Natural Athlete', cost=7, page_ref=76)
NATURAL_HARDENING = Quality('Natural Hardening', cost=10, page_ref=76)
NATURAL_IMMUNITY_NATURAL = Quality('Natural Immunity (Natural)', cost=4, page_ref=76, group="Natural Immunity")
NATURAL_IMMUNITY_SYNTHETIC = Quality('Natural Immunity (Synthetic)', cost=10, page_ref=76, group="Natural Immunity")
PHOTOGRAPHIC_MEMORY = Quality('Photographic Memory', cost=6, page_ref=76)
QUICK_HEALER = Quality('Quick Healer', cost=3, page_ref=77)
RESISTANCE_TO_PATHOGENS_TOXINS_OR = Quality('Resistance to Pathogens or Toxins', cost=4, page_ref=78, opts=['Pathogens', 'Toxins'], group="Resistance Pathogens Toxins")
RESISTANCE_TO_PATHOGENS_TOXINS_AND = Quality('Resistance to Pathogens and Toxins', cost=10, page_ref=78, group="Resistance Pathogens Toxins")
SPIRIT_AFFINITY = Quality('Spirit Affinity', cost=7, page_ref=78, opts=['Spirits of Air', 'Spirits of Earth', 'Spirits of Beast', 'Spirits of Fire', 'Spirits of Man', 'Spirits of Water'])
TOUGHNESS = Quality('Toughness', cost=9, page_ref=78)
WILL_TO_LIVE = Quality('Will to Live', cost=3, page_ref=78, quantity=4)
# NEGATIVE QUALITIES
ADDICTION_MILD = Quality('Addiction (Mild)', cost=4, page_ref=77, negative=True, opts=['Better than Life Chips', 'Alchemical Preparations', 'Alcohol', 'Street Drugs', 'Foci', 'Augmentations'], group='Addiction')
ADDICTION_MODERATE = Quality('Addiction (Moderate)', cost=9, page_ref=77, negative=True, opts=['Better than Life Chips', 'Alchemical Preparations', 'Alcohol', 'Street Drugs', 'Foci', 'Augmentations'], group='Addiction')
ADDICTION_SEVERE = Quality('Addiction (Severe)', cost=20, page_ref=77, negative=True, opts=['Better than Life Chips', 'Alchemical Preparations', 'Alcohol', 'Street Drugs', 'Foci', 'Augmentations'], group='Addiction')
ADDICTION_BURNOUT = Quality('Addiction (Burnout)', cost=25, page_ref=77, negative=True, opts=['Better than Life Chips', 'Alchemical Preparations', 'Alcohol', 'Street Drugs', 'Foci', 'Augmentations'], group='Addiction')
ALLERGY_COMMON_MILD = Quality('Common Allergy (Mild)', cost=5, page_ref=78, negative=True, group='Allergy')
ALLERGY_COMMON_MODERATE = Quality('Common Allergy (Moderate)', cost=10, page_ref=78, negative=True, group='Allergy')
ALLERGY_COMMON_SEVERE = Quality('Common Allergy (Severe)', cost=15, page_ref=78, negative=True, group='Allergy')
ALLERGY_COMMON_EXTREME = Quality('Common Allergy (Extreme)', cost=20, page_ref=78, negative=True, group='Allergy')
ALLERGY_UNCOMMON_MILD = Quality('Uncommon Allergy (Mild)', cost=10, page_ref=78, negative=True, group='Allergy')
ALLERGY_UNCOMMON_MODERATE = Quality('Uncommon Allergy (Moderate)', cost=15, page_ref=78, negative=True, group='Allergy')
ALLERGY_UNCOMMON_SEVERE = Quality('Uncommon Allergy (Severe)', cost=20, page_ref=78, negative=True, group='Allergy')
ALLERGY_UNCOMMON_EXTREME = Quality('Uncommon Allergy (Extreme)', cost=25, page_ref=78, negative=True, group='Allergy')
ASTRAL_BEACON = Quality('Astral Beacon', cost=10, page_ref=78, negative=True)
BAD_LUCK = Quality('Bad Luck', cost=12, page_ref=78, negative=True)
BAD_REP = Quality('Bad Rep', cost=7, page_ref=79, negative=True)
CODE_OF_HONOR = Quality('Code of Honor', cost=15, page_ref=79, negative=True, opts=['Assassin\'s Creed', 'Warriors Code'])
CODEBLOCK = Quality('Codeblock', cost=10, page_ref=80, negative=True)
COMBAT_PARALYSIS = Quality('Combat Paralysis', cost=12, page_ref=80, negative=True)
DEPENDANTS_OCCASIONAL = Quality('Dependants (Occasional)', cost=3, page_ref=80, negative=True, group='Dependants')
DEPENDANTS_REGULAR = Quality('Dependants (Regular)', cost=6, page_ref=80, negative=True, group='Dependants')
DEPENDANTS_CLOSE = Quality('Dependants (Close)', cost=9, page_ref=80, negative=True, group='Dependants')
DISTINCTIVE_STYLE = Quality('Distinctive Style', cost=5, page_ref=80, negative=True)
ELF_POSER = Quality('Elf Poser', cost=6, page_ref=81, negative=True)
GREMLINS = Quality('Gremlins', cost=4, page_ref=81, negative=True, quantity=4)
INCOMPETENT = Quality('Incompetent', cost=5, page_ref=81, negative=True)
INSOMNIA = Quality('Insomnia', cost=10, page_ref=81, negative=True, group='Insomnia')
INSOMNIA_BAD = Quality('Bad Insomnia', cost=15, page_ref=81, negative=True, group='Insomnia')
LOSS_OF_CONFIDENCE = Quality('Loss of Confidence', cost=10, page_ref=82, negative=True)
LOW_PAIN_TOLERANCE = Quality('Low Pain Tolerance', cost=9, page_ref=82, negative=True)
ORK_POSER = Quality('Ork Poser', cost=6, page_ref=82, negative=True)
PREJUDICED_COMMON_BIAS = Quality('Bias Prejudiced (Common)', cost=5, page_ref=82, negative=True, group='Prejudiced')
PREJUDICED_COMMON_OUTSPOKEN = Quality('Outspoken Prejudcied (Common)', cost=7, page_ref=82, negative=True, group='Prejudiced')
PREJUDICED_COMMON_RADICAL = Quality('Radical Prejudiced (Common)', cost=10, page_ref=82, negative=True, group='Prejudiced')
PREJUDICED_SPECIFIC_BIAS = Quality('Bias Prejudiced (Specific)', cost=3, page_ref=82, negative=True, group='Prejudiced')
PREJUDICED_SPECIFIC_OUTSPOKEN = Quality('Outspoken Prejudiced (Specific)', cost=5, page_ref=82, negative=True, group='Prejudiced')
PREJUDICED_SPECIFIC_RADICAL = Quality('Radical Prejudiced (Specific)', cost=8, page_ref=82, negative=True, group='Prejudiced')
SCORCHED = Quality('Scorched', cost=10, page_ref=83, negative=True)
SENSITIVE_SYSTEM = Quality('Sensitive System', cost=12, page_ref=83, negative=True)
SIMSENSE_VERTIGO = Quality('Simsense Vertigo', cost=5, page_ref=83, negative=True)
SINNER_NATIONAL = Quality('SINner (National)', cost=5, page_ref=84, negative=True, group='SINner')
SINNER_CRIMINAL = Quality('SINner (Criminal)', cost=10, page_ref=84, negative=True, group='SINner')
SINNER_CORPORATE_LIMITED = Quality('SINner (Corporate Limited)', cost=15, page_ref=84, negative=True, group='SINner')
SINNER_CORPORATE = Quality('SINner (Corporate)', cost=25, page_ref=84, negative=True, group='SINner')
SOCIAL_STRESS = Quality('Social Stress', cost=8, page_ref=85, negative=True)
SPIRIT_BANE = Quality('Spirit Bane', cost=7, page_ref=85, negative=True)
UNCOUTH = Quality('Uncouth', cost=14, page_ref=85, negative=True)
UNEDUCATED = Quality('Uneducated', cost=8, page_ref=87, negative=True)
UNSTEADY_HANDS = Quality('Unsteady Hands', cost=7, page_ref=87, negative=True)
WEAK_IMMUNE_SYSTEM = Quality('Weak Immune System', cost=10, page_ref=87, negative=True)

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
# =============== BLADES =================
COMBAT_AXE = MeleeWeapon("Combat Axe", cost=4000, page_ref=421, avail=12, legality=RESTRICTED, subtype="Blade")
COMBAT_KNIFE = MeleeWeapon("Combat Knife", cost=300, page_ref=421, avail=4, subtype="Blade")
FOREARM_SNAP_BLADES = MeleeWeapon("Forearm Snap Blades", cost=200, page_ref=421, avail=7, legality=RESTRICTED, subtype="Blade")
KATANA = MeleeWeapon("Katana", cost=1000, page_ref=421, avail=9, legality=RESTRICTED, subtype="Blade")
KNIFE = MeleeWeapon("Knife", cost=10, page_ref=421, avail=0, subtype="Blade")
POLE_ARM = MeleeWeapon("Pole Arm", cost=1000, page_ref=421, avail=6, legality=RESTRICTED, subtype="Blade")
SURVIVAL_KNIFE = MeleeWeapon("Survival Knife", cost=100, page_ref=421, avail=0, subtype="Blade")
SWORD = MeleeWeapon("Sword", cost=500, page_ref=421, avail=5, legality=RESTRICTED, subtype="Blade")
# =============== CLUBS =================
CLUB = MeleeWeapon("Club", cost=30, page_ref=421, avail=0, subtype="Club")
EXTENDABLE_BATON = MeleeWeapon("Extendable Baton", cost=100, page_ref=421, avail=4, subtype="Club")
SAP = MeleeWeapon("Sap", cost=30, page_ref=421, avail=2, subtype="Club")
STAFF = MeleeWeapon("Staff", cost=100, page_ref=421, avail=3, subtype="Club")
STUN_BATON = MeleeWeapon("Stun Baton", cost=750, page_ref=421, avail=6, legality=RESTRICTED, subtype="Club")
TELESCOPING_STAFF = MeleeWeapon("Telescoping Staff", cost=350, page_ref=421, avail=4, subtype="Club")
# =============== OTHER =================
KNUCKS = MeleeWeapon("Knucks", cost=100, page_ref=421, avail=2, legality=RESTRICTED, subtype="Other Melee Weapon")
MONOFILAMENT_WHIP = MeleeWeapon("Monofilament Whip", cost=10_000, page_ref=421, avail=12, legality=FORBIDDEN, subtype="Exotic Melee Weapon")
SHOCK_GLOVES = MeleeWeapon("Shock Gloves", cost=550, page_ref=421, avail=6, legality=RESTRICTED, subtype="Other Melee Weapon")
MONOFILAMENT_CHAINSAW = MeleeWeapon("Monofilament Chainsaw", cost=500, page_ref=448, rating="-", avail=8, subtype="Exotic Melee Weapon")

"""
    PROJECTILE GEAR
"""
# =============== BOWS ==================
BOW = ProjectileWeapon("Bow", cost=["Rating", "*", 100], page_ref=421, avail="Rating", rating=[1, "to", 6], subtype="Bows")
ARROW = ProjectileWeapon("Arrow", cost=["Rating", "*", 2], page_ref=421, avail="Rating", rating=[1, "to", 6], subtype="Bows", requires=BOW)
INJECTION_ARROW = ProjectileWeapon("Injection Arrow", cost=["Rating", "*", 20], page_ref=421, avail=["Rating", "*", 2], legality=RESTRICTED, rating=[1, "to", 6], subtype="Bows", requires=BOW)
# =============== CROSSBOWS =============
LIGHT_CROSSBOW = ProjectileWeapon("Light Crossbow", cost=300, page_ref=421, avail=2, subtype="Crossbow")
MEDIUM_CROSSBOW = ProjectileWeapon("Medium Crossbow", cost=300, page_ref=421, avail=2, subtype="Crossbow")
HEAVY_CROSSBOW = ProjectileWeapon("Heavy Crossbow", cost=300, page_ref=421, avail=2, subtype="Crossbow")
CROSSBOW_BOLT = ProjectileWeapon("Crossbow Bolt", cost=5, page_ref=421, avail=2, subtype="Crossbow", requires=(LIGHT_CROSSBOW, MEDIUM_CROSSBOW, HEAVY_CROSSBOW))
INJECTION_BOLT = ProjectileWeapon("Injection Bolt", cost=50, page_ref=421, avail=8, legality=RESTRICTED, subtype="Crossbow", requires=(LIGHT_CROSSBOW, MEDIUM_CROSSBOW, HEAVY_CROSSBOW))
# =============== THROWING ==============
THROWING_KNIFE = ProjectileWeapon("Throwing Knife", cost=25, page_ref=424, avail=4, subtype="Throwing Weapons")

"""
    FIREARM GEAR
arg order is:
    name, cost, page_ref, avail, subtype, kwargs
"""
# =============== TASERS =================
DEFINANCE_EX_SHOCKER = Firearm("Definance EX Shocker", cost=250, page_ref=424, avail=0, subtype="Taser", damage=[9, STUN, ELECTRICAL], mods=None)
YAMAHA_PULSAR = Firearm("Yamaha Pulsar", cost=180, page_ref=424, avail=0, subtype="Taser", mods=None)
# =============== HOLD-OUTS ==============
FINCHETTI_TIFFANI_NEEDLER = Firearm("Finchetti Tiffani Needler", cost=1000, page_ref=425, avail=5, legality=RESTRICTED, subtype="Hold-Out", mods=None)
STREETLINE_SPECIAL = Firearm("Streetline Special", cost=120, page_ref=425, avail=4, legality=RESTRICTED, subtype="Hold-Out", mods=None)
WALTHER_PALM_PISTOL = Firearm("Walther Palm Pistol", cost=180, page_ref=425, avail=4, legality=RESTRICTED, subtype="Hold-Out", mods=None)
# =============== LIGHT PISTOLS ==========
ARES_LIGHT_FIRE_75 = Firearm("Ares_Light Fire 75", cost=1250, page_ref=425, avail=6, legality=RESTRICTED, subtype="Light Pistol", mods=None)
ARES_LIGHT_FIRE_70 = Firearm("Ares Light Fire 70", cost=200, page_ref=425, avail=3, legality=RESTRICTED, subtype="Light Pistol", mods=None)
BERETTA_201T = Firearm("Beretta 201T", cost=210, page_ref=425, avail=7, legality=RESTRICTED, subtype="Light Pistol", mods=None)
COLT_AMERICA_L36 = Firearm("Colt America L36", cost=320, page_ref=425, avail=4, legality=RESTRICTED, subtype="Light Pistol", mods=None)
FICHETTI_SECURITY_600 = Firearm("Fichetti Security 600", cost=350, page_ref=426, avail=6, legality=RESTRICTED, subtype="Light Pistol", mods=None)
TAURUS_OMNI_6 = Firearm("Taurus Omni 6", cost=300, page_ref=426, avail=3, legality=RESTRICTED, subtype="Light Pistol", mods=None)
# =============== HEAVY PISTOLS ==========
ARES_PREDATOR_V = Firearm("Ares Predator V", cost=725, page_ref=426, avail=5, legality=RESTRICTED, subtype="Heavy Pistol", mods=None)
ARES_VIPER_SHOTGUN = Firearm("Ares Viper Shotgun", cost=380, page_ref=426, avail=8, legality=RESTRICTED, subtype="Heavy Pistol", mods=None)
BROWNING_ULTRA_POWER = Firearm("Browning Ultra Power", cost=640, page_ref=426, avail=4, legality=RESTRICTED, subtype="Heavy Pistol", mods=None)
COLT_GOVERNMENT_2066 = Firearm("Colt Government 2066", cost=425, page_ref=426, avail=7, legality=RESTRICTED, subtype="Heavy Pistol", mods=None)
REMINGTON_ROOMSWEEPER = Firearm("Remington Roomsweeper", cost=250, page_ref=426, avail=6, legality=RESTRICTED, subtype="Heavy Pistol", mods=None)
REMINGTON_ROOMSWEEPER_FLECHETTES = Firearm("Remington Roomsweeper Flechettes", cost=REMINGTON_ROOMSWEEPER.cost, page_ref=426, avail=REMINGTON_ROOMSWEEPER.avail, subtype="Heavy Pistol" , requires=REMINGTON_ROOMSWEEPER, mods=None)
RUGER_SUPER_WARHAWK = Firearm("Ruger Super Warhawk", cost=400, page_ref=427, avail=4, legality=RESTRICTED, subtype="Heavy Pistol", mods=None)
# =============== MACHINE PISTOLS ========
ARES_CRUSADER_II = Firearm("Ares Crusader II", cost=830, page_ref=427, avail=9, legality=RESTRICTED, subtype="Machine Pistol", mods=None)
CESKA_BLACK_SCORPIAN = Firearm("Ceska Black Scorpian", cost=270, page_ref=427, avail=6, legality=RESTRICTED, subtype="Machine Pistol", mods=None)
STEYR_TMP = Firearm("Steyr TMP", cost=350, page_ref=427, avail=8, legality=RESTRICTED, subtype="Machine Pistol", mods=None)
# =============== SMGS ===================
COLT_COBRA_TZ_120  = Firearm("Colt Cobra TZ-120", cost=660, page_ref=427, avail=5, legality=RESTRICTED, subtype="Submachine Gun", mods=None)
FN_P93_PRAETOR = Firearm("FN-P93 Praetor", cost=900, page_ref=427, avail=11, legality=RESTRICTED, subtype="Submachine Gun", mods=None)
HK_227 = Firearm("HK-227", cost=730, page_ref=427, avail=8, legality=RESTRICTED, subtype="Submachine Gun", mods=None)
INGRAM_SMARTGUN_X = Firearm("Ingram Smartgun X", cost=800, page_ref=427, avail=6, legality=RESTRICTED, subtype="Submachine Gun", mods=None)
SCK_MODEL_100 = Firearm("SCK Model 100", cost=875, page_ref=428, avail=6, legality=RESTRICTED, subtype="Submachine Gun", mods=None)
UZI_IV = Firearm("Uzi IV", cost=450, page_ref=428, avail=4, legality=RESTRICTED, subtype="Submachine Gun", mods=None)
# =============== ASSAULT RIFLE ==========
AK_97 = Firearm("AK 97", cost=950, page_ref=428, avail=4 ,legality=RESTRICTED, subtype="Assault Rifle", mods=None)
ARES_ALPHA = Firearm("Ares Alpha", cost=2650, page_ref=428, avail=11, legality=FORBIDDEN, subtype="Assault Rifle", mods=None)
ARES_ALPHA_GRENADE_LAUNCHER = Firearm("Ares Alpha Grenade Launcher", cost=0, page_ref=428, avail=11, legality=FORBIDDEN, subtype="Assault Rifle", requires=ARES_ALPHA, mods=None)
COLT_M23 = Firearm("Colt-M23", cost=550, page_ref=428, avail=4, legality=RESTRICTED, subtype="Assault Rifle", mods=None)
FN_HAR = Firearm("FN HAR", cost=1500, page_ref=428, avail=8, legality=RESTRICTED, subtype="Assault Rifle", mods=None)
YAMAHA_RAIDEN = Firearm("Yamaha Raiden", cost=2600, page_ref=428, avail=14, legality=FORBIDDEN, subtype="Assault Rifle", mods=None)
# =============== SNIPERS ================
ARES_DESERT_STRIKE = Firearm("Ares Desert Strike", cost=17_500, page_ref=28, avail=10, legality=FORBIDDEN, subtype="Sniper Rifle", mods=None)
CAVALIER_ARMS_CROCKETT_EBR = Firearm("Cavalier Arms Crockett EBR", cost=10_300, page_ref=28, avail=12, legality=FORBIDDEN, subtype="Sniper Rifle", mods=None)
RANGER_ARMS_SM_5 = Firearm("Ranger Arms SM-5", cost=28_000, page_ref=29, avail=16, legality=FORBIDDEN, subtype="Sniper Rifle", mods=None)
REMINGTON_950 = Firearm("Remington 950", cost=2100, page_ref=29, avail=4, legality=RESTRICTED, subtype="Sniper Rifle", mods=None)
RUGER_100 = Firearm("Ruger 100", cost=1300, page_ref=29, avail=4, legality=RESTRICTED, subtype="Sniper Rifle", mods=None)
# =============== SHOTGUNS ===============
DEFIANCE_T_250 = Firearm("Defiance T-250", cost=450, page_ref=429, avail=4, legality=RESTRICTED, subtype="Shotgun", mods=None)
ENFIELD_AS_7 = Firearm("Enfield AS-7", cost=1100, page_ref=429, avail=12, legality=FORBIDDEN, subtype="Shotgun", mods=None)
PJSS_MODEL_55  = Firearm("PJSS Model 55", cost=1000, page_ref=429, avail=0, legality=RESTRICTED, subtype="Shotgun", mods=None)
# =============== SPECiAL ================
ARES_S_III_SUPER_SQUIRT = Firearm("Ares S-III Super Squirt", cost=950, page_ref=429, avail=0, legality=RESTRICTED, subtype="Special", damage="Chemical", mods=None)
FICHETTI_PAIN_INDUCER = Firearm("Fichetti Pain Inducer", cost=5000, page_ref=430, avail=11, legality=FORBIDDEN, subtype="Special", damage="Special", mods=None)
PARASHIELD_DART_PISTOL = Firearm("Parashield Dart Pistol", cost=600, page_ref=430, avail=4, legality=FORBIDDEN, subtype="Special", damage="As Drug/Toxin", mods=None)
PARASHIELD_DART_RIFLE = Firearm("Parashield Dart Rifle", cost=1200, page_ref=430, avail=6, legality=FORBIDDEN, subtype="Special", damage="As Drug/Toxin", mods=None)
# =============== MACHINE ================
INGRAM_VALIANT = Firearm("Ingram Valiant", cost=5800, page_ref=430, avail=12, legality=FORBIDDEN, subtype="Machine Gun", mods=None)
STONER_ARES_M202 = Firearm("Stoner-Ares M202", cost=7000, page_ref=430, avail=12, legality=FORBIDDEN, subtype="Machine Gun", mods=None)
RPK_HMG = Firearm("RPK HMG", cost=16_300, page_ref=430, avail=16, legality=FORBIDDEN, subtype="Machine Gun", mods=None)
# =============== LAUNCHER ===============
ARES_ANTIOCH_2 = Firearm("Ares Antioch-2", cost=3200, page_ref=431, avail=8, legality=FORBIDDEN, subtype="Cannon/Launcher", mods=None)
ARMTECH_MGL_12 = Firearm("ArmTech MGL-12", cost=5000, page_ref=431, avail=10, legality=FORBIDDEN, subtype="Cannon/Launcher", mods=None)
AZTECHNOLOGY_STRIKER = Firearm("Aztechnology Striker", cost=1200, page_ref=431, avail=10, legality=FORBIDDEN, subtype="Cannon/Launcher", mods=None)
KRIME_CANNON = Firearm("Krime Cannon", cost=21_000, page_ref=431, avail=20, legality=FORBIDDEN, subtype="Cannon/Launcher", mods=None)
ONOTARI_INTERCEPTOR = Firearm("Onotari Interceptor", cost=14_000, page_ref=431, avail=18, legality=FORBIDDEN, subtype="Cannon/Launcher", mods=None)
PANTHER_XXL = Firearm("Panther XXL", cost=43_000, page_ref=431, avail=20, legality=FORBIDDEN, subtype="Cannon/Launcher", mods=None)

"""
    FIREARM ACCESSORIES
    arg order: name, cost, page_ref, mount, avail, **kwargs
"""
AIRBURST_LINK = FirearmAccessory("Airburst Link", cost=600, page_ref=432, mount="", avail=6, legality=RESTRICTED, requires=["Category", "Firearm"])
BIPOD = FirearmAccessory("Bipod", cost=200, page_ref=432, mount="", avail=2, requires=["Category", "Firearm"])
CONCEALABLE_HOLSTER = FirearmAccessory("Concealable Holster", cost=150, page_ref=432, mount="", avail=2, requires=["Category", "Firearm"])
GAS_VENT_SYSTEM = FirearmAccessory("Gas Vent System", cost=["Rating", "*", 200], page_ref=432, mount="", avail=["Rating", "*", 3], legality=RESTRICTED, requires=["Category", "Firearm"])
GYRO_MOUNT = FirearmAccessory("Gyro Mount", cost=1400, page_ref=432, mount="", avail=7, requires=["Category", "Firearm"])
HIDDEN_ARM_SLIDE = FirearmAccessory("Hidden Arm Slide", cost=350, page_ref=432, mount="", avail=4,legality=RESTRICTED, requires=["Category", "Firearm"])
IMAGING_SCOPE = FirearmAccessory("Imaging Scope", cost=300, page_ref=432, mount="", avail=2, requires=["Category", "Firearm"])
LASER_SIGHT = FirearmAccessory("Laser Sight", cost=125, page_ref=432, mount="", avail=2, requires=["Category", "Firearm"])
PERISCOPE = FirearmAccessory("Periscope", cost=70, page_ref=432, mount="", avail=3, requires=["Category", "Firearm"])
QUICK_DRAW_HOLSTER = FirearmAccessory("Quick Draw Holster", cost=175, page_ref=432, mount="", avail=4, requires=["Category", "Firearm"])
SHOCK_PAD = FirearmAccessory("Shock Pad", cost=50, page_ref=432, mount="", avail=2, requires=["Category", "Firearm"])
SILENCER_SUPPRESSOR = FirearmAccessory("Silencer Suppressor", cost=500, page_ref=432, mount="", avail=9, legality=FORBIDDEN, requires=["Category", "Firearm"])
SMART_FIRING_PLATFORM = FirearmAccessory("Smart Firing Platform", cost=2_500, page_ref=432, mount="", avail=12, legality=FORBIDDEN, requires=["Category", "Firearm"])
SMARTGUN_SYSTEM_INTERNAL = FirearmAccessory("Smartgun System Internal", cost=["WeaponCost", "*", 2], page_ref=432, mount="", avail=2, legality=RESTRICTED, requires=["Category", "Firearm"])
SMARTGUN_SYSTEM_EXTERNAL = FirearmAccessory("Smartgun System External", cost=200, page_ref=432, mount="", avail=4, legality=RESTRICTED, requires=["Category", "Firearm"])
SPARE_CLIP = FirearmAccessory("Spare Clip", cost=5, page_ref=432, mount="", avail=4, requires=["Category", "Firearm"])
SPEED_LOADER = FirearmAccessory("Speed Loader", cost=25, page_ref=432, mount="", avail=2, requires=["Category", "Firearm"])
TRIPOD = FirearmAccessory("Tripod", cost=500, page_ref=432, mount="", avail=4, requires=["Category", "Firearm"])

"""
    INDUSTRIAL CHEMICALS
    No I don't know why this gets its own chapter in the book either
"""
GLUE_SOLVENT = Item("Glue Solvent", cost=90, page_ref=448, avail=2, category="Industrial Chemicals")
GLUE_SPRAYER= Item("Glue Sprayer", cost=150, page_ref=448, avail=2, category="Industrial Chemicals")
THERMITE_BURNING_BAR = Item("Thermite Burning Bar", cost=500, page_ref=448, avail=16, legality=RESTRICTED, category="Industrial Chemicals")

"""
    AMMO TYPES
"""
# =============== STANDARD ===============
APFS = Ammo("APFS", cost=120, page_ref=433, avail=12, legality=FORBIDDEN)
ASSAULT_CANNON = Ammo("Assault Cannon", cost=400, page_ref=433, avail=12, legality=FORBIDDEN)
EXPLOSIVE_ROUNDS = Ammo("Explosive Rounds", cost=80, page_ref=433, avail=9, legality=FORBIDDEN)
FLECHETTE_ROUNDS = Ammo("Flechette Rounds", cost=65, page_ref=433, avail=6, legality=RESTRICTED)
GEL_ROUNDS = Ammo("Gel Rounds", cost=25, page_ref=433, avail=2, legality=RESTRICTED)
HOLLOW_POINTS = Ammo("Hollow Points", cost=70, page_ref=433, avail=4, legality=FORBIDDEN)
INJECTION_DARTS = Ammo("Injection Darts", cost=75, page_ref=433, avail=4, legality=RESTRICTED)
REGULAR_AMMO = Ammo("Regular Ammo", cost=20, page_ref=433, avail=2, legality=RESTRICTED)
STICK_N_SHOCK = Ammo("Stick-n-Shock", cost=80, page_ref=433, avail=6, legality=RESTRICTED)
TRACER = Ammo("Tracer", cost=60, page_ref=433, avail=6, legality=RESTRICTED)
TASER_DART = Ammo("Taser Dart", cost=50, page_ref=433, avail=3)
# =============== GRENADES ===============
FLASH_BANG = Ammo("Flash Bang", cost=100, page_ref=434, avail=6, legality=RESTRICTED, subtype="Grenade")
FLASH_PAK = Ammo("Flash Pak", cost=125, page_ref=434, avail=4, subtype="Grenade")
FRAGMENTATION = Ammo("Fragmentation", cost=100, page_ref=434, avail=11, legality=FORBIDDEN, subtype="Grenade")
HIGH_EXPLOSIVE = Ammo("High Explosive", cost=100, page_ref=434, avail=11, legality=FORBIDDEN, subtype="Grenade")
GAS_GRENADE = Ammo("Gas Grenade", cost=["WeaponCost", "+", 40], page_ref=434, avail=["Chemical Availability", "", 2], legality=RESTRICTED, subtype="Grenade", requires=["Category", "Industrial Chemicals"])
SMOKE_GRENADE = Ammo("Smoke", cost=40, page_ref=434, avail=4, legality=RESTRICTED, subtype="Grenade")
THERMAL_SMOKE = Ammo("Thermal Smoke", cost=60, page_ref=434, avail=6, legality=RESTRICTED, subtype="Grenade")
# =============== MISSILES ==============
ANTI_VEHICLE = Ammo("Anti Vehicle", cost=2800, page_ref=435, avail=18, legality=FORBIDDEN, subtype="Missile")
FRAGMENTATION_MISSLE = Ammo("Fragmentation Missle", cost=2000, page_ref=435, avail=12, legality=FORBIDDEN, subtype="Missile")
HIGH_EXPLOSIVE_MISSLE = Ammo("High Explosive Missle", cost=2100, page_ref=435, avail=18, legality=FORBIDDEN, subtype="Missile")
# =============== ROCKETS ==============
# ANTI_VEHICLE_ROCKET = Ammo("Anti_Vehicle_Rocket", cost=[2800, "+", ("Sensor Rating", 500)], page_ref=435, avail=18, legality=FORBIDDEN, subtype="Rocket", requires=ANTI_VEHICLE)
# FRAGMENTATION_ROCKET = Ammo("Fragmentation_Rocket", cost=[2000, "+", ("Sensor Rating", 500)], page_ref=435, avail=12, legality=FORBIDDEN, subtype="Rocket", requires=FRAGMENTATION_MISSLE)
# HIGH_EXPLOSIVE_ROCKET = Ammo("High_Explosive_Rocket", cost=[2100, "+", ("Sensor Rating", 500)], page_ref=435, avail=18, legality=FORBIDDEN, subtype="Rocket", requires=HIGH_EXPLOSIVE_MISSLE)

"""
    EXPLOSIVES
"""
COMMERCIAL_EXPLOSIVES = Item("Commercial Explosives", cost=100, page_ref=436, rating=5, avail=8, legality=RESTRICTED, category="Explosives")
FOAM_EXPLOSIVES = Item("Foam Explosives", cost=["Rating", "*", 100], page_ref=436, rating=[6, "to", 25], avail=12, legality=FORBIDDEN, category="Explosives")
PLASTIC_EXPLOSIVES = Item("Plastic Explosives", cost=["Rating", "*", 100], page_ref=436, rating=[6, "to", 25], avail=16, legality=FORBIDDEN, category="Explosives")
DETONATOR_CAP = Item("Detonator Cap", cost=75, page_ref=436, rating="-", avail=8, legality=RESTRICTED, category="Explosives")

"""
    CLOTHING/ARMOR
"""
# =============== CLOTHING ==============
CLOTHING = Clothing("Clothing", cost=["Range", 20, 100_000], page_ref=436, avail=0, armor_rating=0)
ELECTROCHROMATIC_MODIFICATION = Clothing("Electrochromatic Modification", cost=500, page_ref=436, avail=2, requires=CLOTHING)
FEEDBACK_CLOTHING = Clothing("Feedback Clothing", cost=500, page_ref=436, avail=8, requires=CLOTHING)
SYNTH_LEATHER = Clothing("Synth Leather", cost=200, page_ref=436, avail=0, requires=CLOTHING)
# =============== ARMOR =================
ACTIONEER_BUSINESS_CLOTHING = Armor("Actioneer Business Clothing", cost=1500, page_ref=436, avail=8, armor_rating=8, mods=None)
ARMOR_CLOTHING = Armor("Armor Clothing", cost=450, page_ref=436, avail=2, armor_rating=6, mods=None)
ARMOR_JACKET = Armor("Armor Jacket", cost=1000, page_ref=436, avail=2, armor_rating=12, mods=None)
ARMOR_VEST = Armor("Armor Vest", cost=500, page_ref=436, avail=4, armor_rating=9, mods=None)
CHAMELEON_SUIT = Armor("Chameleon Suit", cost=1700, page_ref=436, avail=10, legality=RESTRICTED, armor_rating=9, mods=None)
FULL_BODY_ARMOR = Armor("Full Body Armor", cost=2000, page_ref=436, avail=14, legality=RESTRICTED, armor_rating=15, mods=None)
FULL_HELMET = Armor("Full Helmet", cost=500, page_ref=436, avail=14, legality=RESTRICTED, requires=FULL_BODY_ARMOR, armor_rating=3, mods=None)
# FULL_BODY_ARMOR_CHEMICAL_SEAL = ArmorModification("Chemical Seal", cost=6000, page_ref=436, avail=[FULL_BODY_ARMOR.avail[0] +6, legality=RESTRICTED, requires=FULL_BODY_ARMOR, armor_rating="-")
# FULL_BODY_ARMOR_ENVIRONMENTAL_ADAPTATION = ArmorModification("Environmental Adaptation", 1000, page_ref=436, avail=[FULL_BODY_ARMOR.avail[0] +3, legality=RESTRICTED, requires=FULL_BODY_ARMOR, armor_rating="-")
LINED_COAT = Armor("Lined Coat", cost=900, page_ref=436, avail=4, armor_rating=9, mods=None)
URBAN_EXPLORER_JUMPSUIT = Armor("Urban Explorer Jumpsuit", cost=650, page_ref=436, avail=8, armor_rating=9, mods=None)
URBAN_EXPLORER_JUMPSUIT_HELMET = Armor("Urban Explorer Jumpsuit Helmet", cost=100, page_ref=436, avail=URBAN_EXPLORER_JUMPSUIT.avail, requires=URBAN_EXPLORER_JUMPSUIT, armor_rating=2, mods=None)
# =============== SUBTYPES ==============
HELMET = Armor("Helmet", cost=100, page_ref=438, avail=2, armor_rating=2, subtype="Helmet", mods=None)
BALLISTIC_SHIELD = Armor("Ballistic Shield", cost=1200, page_ref=438, avail=12, legality=RESTRICTED, armor_rating=6, subtype="Shield", mods=None)
RIOT_SHIELD = Armor("Riot Shield", cost=1500, page_ref=438, avail=10, legality=RESTRICTED, armor_rating=6, subtype="Shield", mods=None)
BALLISTIC_SHIELD_WEA = MeleeWeapon("Ballistic Shield", cost=BALLISTIC_SHIELD.cost, page_ref=BALLISTIC_SHIELD.page_ref, avail=BALLISTIC_SHIELD.avail, subtype="Exotic Melee Weapon")
RIOT_SHIELD = MeleeWeapon("Riot Shield", cost=RIOT_SHIELD.cost, page_ref=RIOT_SHIELD.page_ref, avail=RIOT_SHIELD.avail, subtype="Exotic Melee Weapon")
# =============== ARMOR MODS ============
CHEMICAL_PROTECTION = ArmorModification("Chemical Protection", cost=["ArmorRating", "*", 250], page_ref=438, avail=6, capacity="ArmorRating", requires=["Category", "Armor"])
CHEMICAL_SEAL = ArmorModification("Chemical Seal", cost=3000, page_ref=438, avail=12, legality=RESTRICTED, capacity=6, requires=["Category", "Armor"])
FIRE_RESISTANCE = ArmorModification("Fire Resistance", cost=["ArmorRating", "*", 250], page_ref=438, avail=6, capacity="ArmorRating", requires=["Category", "Armor"])
INSULATION = ArmorModification("Insulation", cost=["ArmorRating", "*", 250], page_ref=438, avail=6, capacity="ArmorRating", requires=["Category", "Armor"])
NONCONDUCTIVITY = ArmorModification("Nonconductivity", cost=["ArmorRating", "*", 250], page_ref=438, avail=6, capacity="ArmorRating", requires=["Category", "Armor"])
SHOCK_FRILLS = ArmorModification("Shock Frills", cost=250, page_ref=438, avail=6, legality=RESTRICTED, capacity=2, requires=["Category", "Armor"])
THERMAL_DAMPING = ArmorModification("Thermal Damping", cost=["ArmorRating", "*", 500], page_ref=438, avail=10, legality=RESTRICTED, capacity="ArmorRating", requires=["Category", "Armor"])

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
SIM_MODULE = Electronics("Sim Module", cost=100, page_ref=439, rating="-", avail=0, subtype="Commlink_", requires=["Subtype", "Commlink"])
SIM_MODULE_HOT_SIM = Electronics("Sim Module Hot Sim", cost=250, page_ref=439, rating="-", avail=0, subtype="Commlink", requires=SIM_MODULE)
# =============== CYBERDECKS ===========
ERIKA_MCD_1 = Electronics("Erika MCD-1", cost=49_500, page_ref=439, rating=1, avail=3, legality=RESTRICTED, attribute_array=[4,3,2,1], programs=1, subtype="Cyberdeck")
MICRODECK_SUMMIT = Electronics("Microdeck Summit", cost=58_000, page_ref=439, rating=1, avail=3, legality=RESTRICTED, attribute_array=[4,3,3,1], programs=1, subtype="Cyberdeck")
MIROTRONICA_AZTECA_200 = Electronics("Mirotronica Azteca 200", cost=110_250, page_ref=439, rating=2, avail=6, legality=RESTRICTED, attribute_array=[5,4,3,2], programs=2, subtype="Cyberdeck")
HERMES_CHARIOT = Electronics("Hermes Chariot", cost=123_000, page_ref=439, rating=2, avail=6, legality=RESTRICTED, attribute_array=[5,4,4,2], programs=2, subtype="Cyberdeck")
NOVATECH_NAVIGATOR = Electronics("Novatech Navigator", cost=205_750, page_ref=439, rating=3, avail=9, legality=RESTRICTED, attribute_array=[6,5,4,3], programs=3, subtype="Cyberdeck")
RENRAKU_TSURUGI = Electronics("Renraku Tsurugi", cost=214_125, page_ref=439, rating=3, avail=9, legality=RESTRICTED, attribute_array=[6,5,5,3], programs=3, subtype="Cyberdeck")
SONY_CIY_720 = Electronics("Sony CIY-720", cost=345_000, page_ref=439, rating=4, avail=12, legality=RESTRICTED, attribute_array=[7,6,5,4], programs=4, subtype="Cyberdeck")
SHIAWASE_CYBER_5 = Electronics("Shiawase Cyber-5", cost=549_375, page_ref=439, rating=5, avail=15, legality=RESTRICTED, attribute_array=[8,7,6,5], programs=5, subtype="Cyberdeck")
FAIRLIGHT_EXCALIBUR = Electronics("Fairlight Excalibur", cost=823_250, page_ref=439, rating=6, avail=18, legality=RESTRICTED, attribute_array=[9,8,7,6], programs=6, subtype="Cyberdeck")
# =============== ACCESSORIES =========
AR_GLOVES = Electronics("AR Gloves", cost=150, page_ref=440, rating=3, avail=0, subtype="Accessories")
BIOMETRIC_READER = Electronics("Biometric Reader", cost=200, page_ref=440, rating=3, avail=4, subtype="Accessories")
ELECTRONIC_PAPER = Electronics("Electronic Paper", cost=5, page_ref=440, rating=1, avail=0, subtype="Accessories")
PRINTER = Electronics("Printer", cost=25, page_ref=440, rating=3, avail=0, subtype="Accessories")
SATELLITE_LINK = Electronics("Satellite Link", cost=500, page_ref=440, rating=4, avail=6, subtype="Accessories")
SIMRIG = Electronics("Simrig", cost=1000, page_ref=440, rating=3, avail=12, subtype="Accessories")
SUBVOCAL_MIC = Electronics("Subvocal Mic", cost=50, page_ref=440, rating=3, avail=4, subtype="Accessories")
TRID_PROJECTOR = Electronics("Trid Projector", cost=200, page_ref=440, rating=3, avail=0, subtype="Accessories")
TRODES = Electronics("Trodes", cost=70, page_ref=440, rating=3, avail=0, subtype="Accessories")
# =============== RFID TAG ===========
STANDARD_RFID = Electronics("Standard RFID", cost=1, page_ref=440, rating=1, avail=0, subtype="RFID Tags")
DATACHIP = Electronics("Datachip", cost=5, page_ref=440, rating=1, avail=0, subtype="RFID Tags")
SECURITY_RFID = Electronics("Security RFID", cost=5, page_ref=440, rating=3, avail=3, subtype="RFID Tags")
SENSOR_RFID = Electronics("Sensor RFID", cost=40, page_ref=440, rating=2, avail=5, subtype="RFID Tags")
STEALTH_RFID = Electronics("Stealth RFID", cost=10, page_ref=440, rating=3, avail=7, legality=RESTRICTED, subtype="RFID Tags")
# =============== COMMUNICATIONS =====
BUG_SCANNER = Electronics("Bug Scanner", cost=["Rating", "*", 100], page_ref=441, rating=[1, "to", 6], avail=["Rating"], legality=RESTRICTED, subtype="Communications")
DATA_TAP = Electronics("Data Tap", cost=300, page_ref=441, rating="-", avail=6, legality=RESTRICTED, subtype="Communications")
HEADJAMMER = Electronics("Headjammer", cost=["Rating", "*", 150], page_ref=441, rating=[1, "to", 6], avail=["Rating"], legality=RESTRICTED, subtype="Communications")
JAMMER_AREA = Electronics("Jammer Area", cost=["Rating", "*", 200], page_ref=441, rating=[1, "to", 6], avail=["Rating", "*", 3], legality=RESTRICTED, subtype="Communications")
JAMMER_DIRECTIONAL = Electronics("Jammer Directional", cost=["Rating", "*", 200], page_ref=441, rating=[1, "to", 6], avail=["Rating", "*", 2], legality=RESTRICTED, subtype="Communications")
MICRO_TRANSRECEIVER = Electronics("Micro Transreceiver", cost=100, page_ref=441, rating="-", avail=2, subtype="Communications")
TAG_ERASER = Electronics("Tag Eraser", cost=450, page_ref=441, rating="-", avail=6, legality=RESTRICTED, subtype="Communications")
WHITE_NOISE_GENERATOR = Electronics("White Noise Generator", cost=["Rating", "*", 50], page_ref=441, rating=[1, "to", 6], avail="Rating", subtype="Communications")
# =============== SOFTWARE ===========
AGENT_1_3 = Electronics("Agent (Rating 1-3)", cost=["Rating", "*", 1_000], page_ref=442, rating=[1, "to", 3], avail=["Rating", "*", 3], subtype="Software")
AGENT_4_6 = Electronics("Agent (Rating 4-6)", cost=["Rating", "*", 2_000], page_ref=442, rating=[4, "to", 6], avail=["Rating", "*", 3], subtype="Software")
CYBERPROGRAM_COMMON = Electronics("Cyberprogram Common", cost=80, page_ref=442, rating="-", avail=0, subtype="Software")
CYBERPROGRAM_HACKING = Electronics("Cyberprogram Hacking", cost=250, page_ref=442, rating="-", avail=6, legality=RESTRICTED, subtype="Software")
DATASOFT = Electronics("Datasoft", cost=120, page_ref=442, rating="-", avail=0, subtype="Software")
MAPSOFT = Electronics("Mapsoft", cost=100, page_ref=442, rating="-", avail=0, subtype="Software")
SHOPSOFT = Electronics("Shopsoft", cost=150, page_ref=442, rating="-", avail=0, subtype="Software")
TUTORSOFT = Electronics("Tutorsoft", cost=["Rating", "*", 400], page_ref=442, rating=[1, "to", 6], avail="Rating", subtype="Software")
# =============== SKILLSOFTS =========
ACTIVESOFTS = Electronics("Activesofts", cost=["Rating", "*", 5000], page_ref=442, rating=[1, "to", 6], avail=8, subtype="Skillsofts")
KNOWSOFTS = Electronics("Knowsofts", cost=["Rating", "*", 2000], page_ref=442, rating=[1, "to", 6], avail=8, subtype="Skillsofts")
LINGUASOFTS = Electronics("Linguasofts", cost=["Rating", "*", 1000], page_ref=442, rating=[1, "to", 6], avail=8, subtype="Skillsofts")
# =============== CREDSTICKS =========
STANDARD = Electronics("Standard Credstick", cost=5, page_ref=443, rating="-", avail=0, max_value=5000, subtype="Credsticks")
SILVER = Electronics("Silver Credstick", cost=20, page_ref=443, rating="-", avail=0, max_value=20_000, subtype="Credsticks")
GOLD = Electronics("Gold Credstick", cost=100, page_ref=443, rating="-", avail=5, max_value=100_000, subtype="Credsticks")
PLATINUM = Electronics("Platinum Credstick", cost=500, page_ref=443, rating="-", avail=10, max_value=500_000, subtype="Credsticks")
EBONY = Electronics("Ebony Credstick", cost=1000, page_ref=443, rating="-", avail=20, max_value=1_000_000, subtype="Credsticks")
# =============== IDENTIFICATION =====
FAKE_SIN = Electronics("Fake SIN", cost=["Rating", "*", 2500], page_ref=443, rating=[1, "to", 6], avail=["Rating", "*", 3], legality=FORBIDDEN, subtype="Identification")
FAKE_LICENCE = Electronics("Fake Licence", cost=["Rating", "*", 200], page_ref=443, rating=[1, "to", 6], avail=["Rating", "*", 3], legality=FORBIDDEN, subtype="Identification")
# =============== TOOLS ==============
TOOL_KIT = Electronics("Tool Kit", cost=500, page_ref=443, rating="-", avail=0, subtype="Tools")
TOOL_SHOP = Electronics("Tool Shop", cost=5000, page_ref=443, rating="-", avail=8, subtype="Tools")
TOOL_FACILITY = Electronics("Tool Facility", cost=50000, page_ref=443, rating="-", avail=12, subtype="Tools")
# ========== OPTICAL / IMAGING DEVICES
BINOCULARS = Electronics(f"Binoculars", cost=["Capacity", "*", 50], page_ref=444, rating="-", avail=0, capacity=[1, "to", 3], subtype="Optical/Imaging Devices")
OPTICAL_BINOCULARS = Electronics("Optical Binoculars", cost=50, page_ref=444, rating="-", avail=0, subtype="Optical/Imaging Devices")
CAMERA = Electronics("Camera", cost=["Capacity", "*", 100], page_ref=444, rating="-", avail=0,capacity=[1, "to", 6], subtype="Optical/Imaging Devices")
MICRO_CAMERA = Electronics("Micro Camera", cost=100, page_ref=444, rating="-", avail=0, capacity=1, subtype="Optical/Imaging Devices")
EYE_CONTACTS = Electronics(f"Eye Contacts", cost=["Capacity", "*", 200], page_ref=444, rating="-", avail=0, capacity=[1, "to", 3], subtype="Optical/Imaging Devices")
GLASSES = Electronics("Glasses", cost=["Capacity", "*", 100], page_ref=444, rating="-", avail=0, capacity=[1, "to", 4], subtype="Optical/Imaging Devices")
GOGGLES = Electronics("Goggles", cost=["Capacity", "*", 50], page_ref=444, rating="-", avail=0, capacity=[1, "to", 6], subtype="Optical/Imaging Devices")
ENDOSCOPE = Electronics("Endoscope", cost=250, page_ref=444, rating="-", avail=8, subtype="Optical/Imaging Devices")
MAGE_SIGHT_GOGGLES = Electronics("Mage Sight Goggles", cost=3000, page_ref=444, rating="-", avail=12, legality=RESTRICTED, subtype="Optical/Imaging Devices")
MONOCLE = Electronics("Monocle", cost=3000, page_ref=444, rating="-", avail=12, legality=RESTRICTED, capacity=[1, "to", 3], subtype="Optical/Imaging Devices")
# =============== VISION ENCHANCEMENTS 
LOW_LIGHT_VISION = Electronics("Low-Light Vision", cost=500, page_ref=444, rating="-", avail=4, capacity=1, subtype="Vision Enhancement", requires=["Subtype", "Optical/Imaging Devices"])
FLARE_COMPENSATION = Electronics("Flare Compensation", cost=250, page_ref=444, rating="-", avail=1, capacity=1, subtype="Vision Enhancement", requires=["Subtype", "Optical/Imaging Devices"])
IMAGE_LINK = Electronics("Image Link", cost=25, page_ref=444, rating="-", avail=0, capacity=1, subtype="Vision Enhancement", requires=["Subtype", "Optical/Imaging Devices"])
SMARTLINK = Electronics("Smartlink", cost=2000, page_ref=444, rating="-", avail=4, legality=RESTRICTED, capacity=1, subtype="Vision Enhancement", requires=["Subtype", "Optical/Imaging Devices"])
THERMOGRAPHIC_VISION = Electronics("Thermographic Vision", cost=500, page_ref=444, rating="-", avail=6, capacity=1, subtype="Vision Enhancement", requires=["Subtype", "Optical/Imaging Devices"])
VISION_ENHANCEMENT = Electronics("Vision Enhancement", cost=["Rating", "*", 500], page_ref=444, rating="-", avail=["Rating", "*", 2], capacity="Rating", subtype="Vision Enhancement", requires=["Subtype", "Optical/Imaging Devices"])
VISION_MAGNIFICATION = Electronics("Vision Magnification", cost=250, page_ref=444, rating="-", avail=2, capacity=1, subtype="Vision Enhancement", requires=["Subtype", "Optical/Imaging Devices"])
# =============== AUDIO DEVICES=======
DIRECTIONAL_MIC = Electronics("Directional Mic", cost=["Capacity", "*", 50], page_ref=445, rating="-", avail=4, capacity=[1, "to", 6], subtype="Audio Device")
EAR_BUDS = Electronics("Ear Buds", cost=["Capacity", "*", 50], page_ref=445, rating="-", avail=0, capacity=[1, "to", 3], subtype="Audio Device")
HEADPHONES = Electronics("Headphones", cost=["Capacity", "*", 50], page_ref=445, rating="-", avail=0, capacity=[1, "to", 6], subtype="Audio Device")
LASER_MIC = Electronics("Laser Mic", cost=["Capacity", "*", 100], page_ref=445, rating="-", avail=6, legality=RESTRICTED, capacity=[1, "to", 6], subtype="Audio Device")
OMNI_DIRECTIONAL_MIC = Electronics("Omni-Directional Mic", cost=["Capacity", "*", 50], page_ref=445, rating="-", avail=0, capacity=[1, "to", 6], subtype="Audio Device")
# =============== AUDIO ENHANCEMENTS==
AUDIO_ENHANCEMENT = Electronics("Audio Enhancement", cost=["Rating", "*", 500], page_ref=445, rating=[1, "to", 3], avail=["Rating", "*", 2], capacity="Rating", subtype="Audio Enhancement")
SELECT_SOUND_FILTER = Electronics("Select Sound Filter", cost=["Rating", "*", 250], page_ref=445, rating=[1, "to", 3], avail=["Rating", "*", 3], capacity="Rating", subtype="Audio Enhancement")
SPACIAL_REGONISER = Electronics("Spacial Regoniser", cost=1000, page_ref=445, rating="-", avail=4, capacity=2, subtype="Audio Enhancement")
# =============== SENSORS ============
"""
I'm like 100 lines into electronics alone, probably a few hundred if you include everything in this data dump section.
    So far everything has been predictable. Sure there's been some edge cases and oddities, but that's to be expected, 
    a game would be boring if everything was boxed into the same formula, sharing the same restrictions.
I say this because the sensor section can go fuck itself. For now. I'll figure out something in the future, probably
    a shitty band-aid solution because I really do not want to reengineer how I've been storing data up to this point.
Fuck that.

Edit from months later: Just gonna bodge the sensor functions as their own dict, with the sensor function as the key and it's range as the value.
    Then gonna add a custom arg to randomly pull one of those sensor functions from whatever kind of sensor/sensor housing gets rolled
"""
# Sensor Function: Range (in feet)
SENSOR_FUNCTIONS = {
    "Atmosphere Sensor": 0, "Camera": 0, "Cyberware Scanner": 15, "Directional Microphone": 0, "Geiger Counter": 0, 'Laser Microphone': 100, 'Laser Range Finder': 1000, 'MAD Scanner': 5,
    'Motion Sensor': 25, 'Oilfactory Sensor': 0, 'Omni-directional Microphone': 0, 'Radio Signal Scanner': 20, 'Ultrasound': 50
}
SENSOR_HOUSINGS = { # 'Sensor Package': Max Sensor Rating
    'RFID': 2,
    'Audio Device': 2,
    'Visual Device': 2,
    'Headware': 2,
    'Handheld Device': 3,
    'Small Drone': 3,
    'Wall-mounted Device': 4,
    'Medium Drone': 4,
    'Large Drone': 5,
    'Cyberlimb': 5,
    'Motorcycle': 6,
    'Vehicle': 7,
    'Building': 8,
    'Airport': 8
}
# HANDHELD_HOUSING = Electronics("Handheld Housing", cost=["Capacity", "*", 100], page_ref=445, rating=[1, "to", 3], avail=0, capacity=[1, "to", 3], housing=[{k:d} for k, d in SENSOR_HOUSINGS.items() if d <= 3], sensor_function=SENSOR_FUNCTIONS, subtype="Sensor Housing")
HANDHELD_HOUSING = Electronics("Handheld Housing", cost=["Capacity", "*", 100], page_ref=445, rating=[1, "to", 3], avail=0, capacity=[1, "to", 3], subtype="Sensor Housing")
# WALL_MOUNTED_HOUSING = Electronics("Wall-Mounted Housing", cost=["Capacity", "*", 250], page_ref=445, rating=[1, "to", 4], avail=0, capacity=[1, "to", 6], housing=[{k:d} for k, d in SENSOR_HOUSINGS.items() if d <= 4], sensor_function=SENSOR_FUNCTIONS, subtype="Sensor Housing")
WALL_MOUNTED_HOUSING = Electronics("Wall-Mounted Housing", cost=["Capacity", "*", 250], page_ref=445, rating=[1, "to", 4], avail=0, capacity=[1, "to", 6], subtype="Sensor Housing")
# SENSOR_ARRAY = Electronics("Sensor Array", cost=["Rating", "*", 1000], page_ref=445, rating=[2, "to", 8], avail=0, capacity=6, housing=SENSOR_HOUSINGS, sensor_function=SENSOR_FUNCTIONS, subtype="Sensor Housing")
SENSOR_ARRAY = Electronics("Sensor Array", cost=["Rating", "*", 1000], page_ref=445, rating=[2, "to", 8], avail=0, capacity=6, subtype="Sensor Type")
# SINGLE_SENSOR = Electronics("Single Sensor", cost=["Rating", "*", 100], page_ref=445, rating=[2, "to", 8], avail=0, capacity=1, housing=SENSOR_HOUSINGS, sensor_function=SENSOR_FUNCTIONS, subtype="Sensor Housing")
SENSOR_SINGLE = Electronics("Single Sensor", cost=["Rating", "*", 100], page_ref=445, rating=[2, "to", 8], avail=0, capacity=1, subtype="Sensor Type")
# =============== SECURITY DEVICES====
KEY_COMBINATION_LOCK = Electronics("Key Combination Lock", cost=["Rating", "*", 10], page_ref=447, rating=[1, "to", 6], avail="Rating", subtype="Security Device")
MAGLOCK = Electronics("Maglock", cost=["Rating", "*", 100], page_ref=447, rating=[1, "to", 6], avail="Rating", subtype="Security Device")
KEYPAD_CARD_READER = Electronics("Keypad Card Reader", cost=50, page_ref=447, rating="-", avail=0, subtype="Security Device")
ANTI_TAMPER_CIRCUITS = Electronics("Anti Tamper Circuits", cost=["Rating", "*", 250], page_ref=447, rating=[1, "to", 4], avail="Rating", subtype="Security Device")
# ============== RESTRAINT ===========
METAL_RESTRAINT = Electronics("Metal Restraint", cost=20, page_ref=447, rating="-", avail=0, subtype="Restraint")
PLATEEL_RESTRAINT = Electronics("Plateel Restraint", cost=50, page_ref=447, rating="-", avail=6, legality=RESTRICTED, subtype="Restraint")
PLASTIC_RESTRAINT_PER_10 = Electronics("Plastic Restraint (Per 10)", cost=5, page_ref=447, rating="-", avail=0, subtype="Restraint")
CONTAINMENT_MANACLES = Electronics("Containment Manacles", cost=250, page_ref=447, rating="-", avail=6, legality=RESTRICTED, subtype="Restraint")
# ============== BREAKING AND ENTERING
AUTOPICKER = Electronics("Autopicker", cost=["Rating", "*", 500], page_ref=448, rating=[1, "to", 6], avail=8, legality=RESTRICTED, subtype="B&E Gear")
CELLUAR_GLOVE_MOLDER = Electronics("Celluar Glove Molder", cost=["Rating", "*", 500], page_ref=448, rating=[1, "to", 4], avail=12, legality=FORBIDDEN, subtype="B&E Gear")
CHISEL_CROWBAR = Electronics("Chisel Crowbar", cost=20, page_ref=448, rating="-", avail=0, subtype="B&E Gear")
KEYCARD_COPIER = Electronics("Keycard Copier", cost=["Rating", "*", 600], page_ref=448, rating=[1, "to", 6], avail=8, legality=FORBIDDEN, subtype="B&E Gear")
LOCKPICK_SET = Electronics("Lockpick Set", cost=250, page_ref=448, rating="-", avail=4, legality=RESTRICTED, subtype="B&E Gear")
MAGLOCK_PASSKEY = Electronics("Maglock Passkey", cost=["Rating", "*", 2000], page_ref=448, rating=[1, "to", 4], avail=["Rating", "*", 3], legality=FORBIDDEN, subtype="B&E Gear")
MINIWELDER = Electronics("Miniwelder", cost=250, page_ref=448, rating="-", avail=2, subtype="B&E Gear")
MINIWELDER_FUEL_CANISTER = Electronics("Miniwelder Fuel Canister", cost=80, page_ref=448, rating="-", avail=2, subtype="B&E Gear")
SEQUENCER = Electronics("Sequencer", cost=["Rating", "*", 250], page_ref=448, rating=[1, "to", 6], avail=["Rating", "*", 3], legality=RESTRICTED, subtype="B&E Gear")

"""
   MISC ITEMS 
"""
# SURVIVAL GEAR
CHEMSUIT = Item("Chemsuit", cost=["Rating", "*", 150], page_ref=449, rating=[1, "to", 6], avail=["Rating", "*", 2], category="Survival Gear")
CLIMBING_GEAR = Item("Climbing Gear", cost=200, page_ref=449, rating="-", avail=0, category="Survival Gear")
DIVING_GEAR = Item("Diving Gear", cost=2000, page_ref=449, rating="-", avail=6, category="Survival Gear")
FLASHLIGHT = Item("Flashlight", cost=25, page_ref=449, rating="-", avail=0, category="Survival Gear")
GAS_MASK = Item("Gas Mask", cost=200, page_ref=449, rating="-", avail=0, category="Survival Gear")
GECKO_TAPE_GLOVES = Item("Gecko Tape Gloves", cost=250, page_ref=449, rating="-", avail=12, category="Survival Gear")
HAZMAT_SUIT = Item("Hazmat Suit", cost=3000, page_ref=449, rating="-", avail=8, category="Survival Gear")
LIGHT_STICK = Item("Light Stick", cost=25, page_ref=449, rating="-", avail=0, category="Survival Gear")
MAGNESIUM_TORCH = Item("Magnesium Torch", cost=5, page_ref=449, rating="-", avail=0, category="Survival Gear")
MICRO_FLARE_LAUNCHER = Item("Micro Flare Launcher", cost=175, page_ref=449, rating="-", avail=0, category="Survival Gear")
MICRO_FLARES = Item("Micro Flares", cost=25, page_ref=449, rating="-", avail=0, category="Survival Gear")
RAPPELLING_GLOVES = Item("Rappelling Gloves", cost=50, page_ref=449, rating="-", avail=0, category="Survival Gear")
RESPIRATOR = Item("Respirator", cost=["Rating", "*", 50], page_ref=449, rating=[1, "to", 6], avail=0, category="Survival Gear")
SURVIVAL_KIT = Item("Survival Kit", cost=200, page_ref=449, rating="-", avail=4, category="Survival Gear")
# GRAPPLE GUN
GRAPPLE_GUN = Item("Grapple Gun", cost=500, page_ref=450, rating="-", avail=8, legality=RESTRICTED, category="Grapple Gun")
CATALYST_STICK = Item("Catalyst Stick", cost=120, page_ref=450, rating="-", avail=8, legality=FORBIDDEN, category="Grapple Gun")
MICROWIRE = Item("Microwire (100m)", cost=50, page_ref=450, rating="-", avail=4, category="Grapple Gun")
MYOMERIC_ROPE = Item("Myomeric Rope (10m)", cost=200, page_ref=450, rating="-", avail=10, category="Grapple Gun")
STANDARD_ROPE = Item("Standard Rope (100m)", cost=50, page_ref=450, rating="-", avail=0, category="Grapple Gun")
STEALTH_ROPE = Item("Stealth Rope (100m)", cost=85, page_ref=450, rating="-", avail=8, legality=FORBIDDEN, category="Grapple Gun")
# BIOTECH
BIOMONITOR = Item("BIOMONITOR", cost=300, page_ref=450, rating="-", avail=3, category="Biotech")
DISPOSABLE_SYRINGE = Item("DISPOSABLE_SYRINGE", cost=10, page_ref=450, rating="-", avail=3, category="Biotech")
MEDKIT_1_6 = Item("MEDKIT_1_6", cost=["Rating", "*", 250], page_ref=450, rating="-", avail="Rating", category="Biotech")
MEDKIT_SUPPLIES = Item("MEDKIT_SUPPLIES", cost=300, page_ref=450, rating="-", avail=0, category="Biotech")
# SLAP PATCHES
ANTIDOTE_PATCH_1_6 = Item("ANTIDOTE_PATCH_1_6", cost=["Rating", "*", 50], page_ref=451, rating="-", avail="Rating", category="Slap Patches")
CHEM_PATCH = Item("Chem Patch", cost=200, page_ref=451, rating="-", avail=6, category="Slap Patches")
STIM_PATCH_1_6 = Item("Stim Patch (Rating 1-6)", cost=["Rating", "*", 25], page_ref=451, rating="-", avail=["Rating", "*", 2], category="Slap Patches")
TRANQ_PATCH_1_10 = Item("Tranq Patch (Rating 1-6)", cost=["Rating", "*", 50], page_ref=451, rating="-", avail=["Rating", "*", 2], category="Slap Patches")
TRAUMA_PATCH = Item("Trama Patch", cost=500, page_ref=451, rating="-", avail=6, category="Slap Patches")
# DOCWAGON CONTRACT
DOCWAGON_BASIC = Item("DOCWAGON_BASIC", cost=5000, page_ref=450, rating="-", avail=0, category="Doc Wagon")
DOCWAGON_GOLD = Item("DOCWAGON_GOLD", cost=25000, page_ref=450, rating="-", avail=0, category="Doc Wagon")
DOCWAGON_PLATINUM = Item("DOCWAGON_PLATINUM", cost=50000, page_ref=450, rating="-", avail=0, category="Doc Wagon")
DOCWAGON_PLATINUM_PLUS = Item("DOCWAGON_PLATINUM_PLUS", cost=100000, page_ref=450, rating="-", avail=0, category="Doc Wagon")

"""
    VEHICLES
"""
# BIKES
DODGE_SCOUT = Vehicle('Dodge Scout', cost=3000, avail="-", page_ref=462, subtype="Bike", skill_req=PILOT_GROUND_CRAFT)
HARLEY_DAVIDSON_SCORPION = Vehicle('Harley-Davidson Scorpion', cost=12000, avail="-", page_ref=462, subtype="Bike", skill_req=PILOT_GROUND_CRAFT)
YAMAHA_GROWLER = Vehicle('Yamaha Growler', cost=5000, avail="-", page_ref=462, subtype="Bike", skill_req=PILOT_GROUND_CRAFT)
SUZUKI_MIRAGE = Vehicle('Suzuki Mirage', cost=8500, avail="-", page_ref=462, subtype="Bike", skill_req=PILOT_GROUND_CRAFT)
# CARS
CN_JACKRABBIT = Vehicle('Chrysler-Nissan Jackrabbit', cost=10000, avail="-", page_ref=462, subtype="Car", skill_req=PILOT_GROUND_CRAFT)
HONDA_SPIRIT = Vehicle('Honda Spirit', cost=12000, avail="-", page_ref=463, subtype="Car", skill_req=PILOT_GROUND_CRAFT)
HYUNDAI_SHIN_HYUNG = Vehicle('Hyundai Shin-Hyung', cost=28500, avail="-", page_ref=463, subtype="Car", skill_req=PILOT_GROUND_CRAFT)
EUROCAR_WESTWIND_3000 = Vehicle('Eurocar Westwind 3000', cost=110_000, avail=13, page_ref=463, subtype="Car", skill_req=PILOT_GROUND_CRAFT)
FORD_AMERICAR = Vehicle('Ford Americar', cost=16000, avail="-", page_ref=463, subtype="Car", skill_req=PILOT_GROUND_CRAFT)
SK_BENTLY_CONCORDAT = Vehicle('Saeder-Krupp-Bently Concordat', cost=65000, avail=10, page_ref=463, subtype="Car", skill_req=PILOT_GROUND_CRAFT)
MITSUBISHI_NIGHTSKY = Vehicle('Mitsubishi Nightsky', cost=320_000, avail=16, page_ref=463, subtype="Car", skill_req=PILOT_GROUND_CRAFT)
# TRUCKS / VANS
TOYOTA_GOPHER = Vehicle('Toyota Gopher', cost=25000, avail="-", page_ref=463, subtype="Truck", skill_req=PILOT_GROUND_CRAFT)
GMC_BULLDOG = Vehicle('GMC Bulldog Step-Van', cost=35000, avail="-", page_ref=463, subtype="Truck", skill_req=PILOT_GROUND_CRAFT)
ROVER_MODEL_2072 = Vehicle('Rover Model 2072', cost=68000, avail=10, page_ref=464, subtype="Truck", skill_req=PILOT_GROUND_CRAFT)
ARES_ROADMASTER = Vehicle('Ares Roadmaster', cost=52000, avail=8, page_ref=464, subtype="Truck", skill_req=PILOT_GROUND_CRAFT)
# BOATS
SAMUVANI_CRISCRAFT_OTTER = Vehicle('Samuvani Criscraft Otter', cost=21000, avail="-", page_ref=464, subtype="Boat", skill_req=PILOT_WATERCRAFT)
YONGKANG_GALA_TRINITY = Vehicle('Yongkang Gala Trinity', cost=37000, avail=7, page_ref=464, subtype="Boat", skill_req=PILOT_WATERCRAFT)
MORGAN_CUTLASS = Vehicle('Morgan Cutlass', cost=96000, avail=14, legality=RESTRICTED, page_ref=464, subtype="Boat", skill_req=PILOT_WATERCRAFT)
# SUBMARINES
PROTEUS_LAMPREY = Vehicle('Proteus Lamprey', cost=14000, avail="-", page_ref=464, subtype="Submarine", skill_req=PILOT_WATERCRAFT)
VULKAN_ELECTRONAUT = Vehicle('Vulkan Electronaut', cost=108_000, avail=10, page_ref=464, subtype="Submarine", skill_req=PILOT_WATERCRAFT)
# FIXED-WING AIRCRAFT
ARTEMIS_INDUSTRIES_NIGHTWING = Vehicle('Artemis Industries Nightwing', cost=20000, avail=8, page_ref=464, subtype='Fixed-Wing', skill_req=PILOT_AIRCRAFT)
CESSNA_C750 = Vehicle('Cessna C750', cost=146_000, avail=8, page_ref=464, subtype='Fixed-Wing', skill_req=PILOT_AIRCRAFT)
RF_FOKKER_TUNDRA_9 = Vehicle('Renaut-Fiat Fokker Tundra 9', cost=300_000, avail=12, page_ref=464, subtype='Fixed-Wing', skill_req=PILOT_AIRCRAFT)
# ROTORCRAFT
ARES_DRAGON = Vehicle('Ares Dragon', cost=355_000, avail=12, page_ref=464, subtype='Rotocraft', skill_req=PILOT_AIRCRAFT)
NISSAN_HOUND = Vehicle('Nissan Hound', cost=425_000, avail=13, legality=RESTRICTED, page_ref=464, subtype='Rotocraft', skill_req=PILOT_AIRCRAFT)
NORTHRUP_WASP = Vehicle('Northrup Wasp', cost=86_000, avail=12, legality=RESTRICTED, page_ref=465, subtype='Rotocraft', skill_req=PILOT_AIRCRAFT)
# VTOL
ARES_VENTURE = Vehicle('Ares Venture', cost=400_000, avail=12, legality=FORBIDDEN, page_ref=465, subtype='VTOL', skill_req=PILOT_AIRCRAFT)
GMC_BANSHEE = Vehicle('GMC Banshee', cost=2_500_000, avail=24, legality=FORBIDDEN, page_ref=465, subtype='VTOL', skill_req=PILOT_AIRCRAFT)
FEDERATED_BOEING_COMMUTER = Vehicle('Federated Boeing Commuter', cost=350_000, avail=10, page_ref=465, subtype='VTOL', skill_req=PILOT_AIRCRAFT)
# MICRODRONES 
SHIAWASE_KANMUSHI = Vehicle('Shiawase Kanmushi', cost=1000, avail=8, page_ref=465, subtype='Microdrone', skill_req=PILOT_WALKER)
SIKORSKY_BELL_MICROSKIMMER = Vehicle('Sikorsky-Bell Microskimmer', cost=1000, avail=6, page_ref=465, subtype='Microdrone', skill_req=PILOT_GROUND_CRAFT)
# MINIDRONES 
HORIZON_FLYING_EYE = Vehicle('Horizon Flying Eye', cost=2000, avail=8, page_ref=465, subtype='Minidrone', skill_req=PILOT_AIRCRAFT)
MCT_FLY_SPY = Vehicle('MCT Fly Spy', cost=2000, avail=8, page_ref=466, subtype='Minidrone', skill_req=PILOT_AIRCRAFT)
# SMALL DRONES 
AZTECHNOLOGY_CRAWLER = Vehicle('Aztechnology Crawler', cost=4000, avail=4, page_ref=466, subtype='Small Drone', skill_req=PILOT_WALKER)
LOCKHEED_OPTIC_X2 = Vehicle('Lockheed Optic-X2', cost=21000, avail=10, page_ref=466, subtype='Small Drone', skill_req=PILOT_AIRCRAFT)
# MEDIUM DRONES 
ARES_DUELIST = Vehicle('Ares Duelist', cost=4500, avail=5, legality=RESTRICTED, page_ref=466, subtype='Medium Drone', skill_req=PILOT_WALKER)
GM_NISSAN_DOBERMAN = Vehicle('GM-Nissan Doberman', cost=5000, avail=4, legality=RESTRICTED, page_ref=466, subtype='Medium Drone', skill_req=PILOT_GROUND_CRAFT)
MCT_NISSAN_ROTO_DRONE = Vehicle('MCT-Nissan Roto-Drone', cost=5000, avail=6, page_ref=466, subtype='Medium Drone', skill_req=PILOT_AIRCRAFT)
# LARGE DRONES 
CYBERSPACE_DESIGNS_DALMATION = Vehicle('Cyberspace Designs Dalmation', cost=10000, avail=6, legality=RESTRICTED, page_ref=466, subtype='Large Drone', skill_req=PILOT_AIRCRAFT)
STEEL_LYNX_COMBAT_DRONE = Vehicle('Steel Lynx Combat Drone', cost=25000, avail=10, legality=RESTRICTED, page_ref=466, subtype='Large Drone', skill_req=PILOT_GROUND_CRAFT)


ROAD_VEHICLES = [i for i in Vehicle.items if i.subtype in ['Bike', 'Car', 'Truck']]
AIR_VEHICLES = [i for i in Vehicle.items if i.subtype in ['Fixed-Wing', 'Rotocraft', 'VTOL']]
WATER_VEHICLES = [i for i in Vehicle.items if i.subtype in ['Boat', 'Submarine']]
DRONE_VEHICLES = [i for i in Vehicle.items if i.subtype in ['Microdrone', 'Minidrone', 'Small Drone', 'Medium Drone', 'Large Drone']]
        
"""
    LIFESTYLE
"""
STREET_LIFESTYLE = Lifestyle("Street Lifestyle", dicestring="1d6", base_amount=20, cost=0)
SQUATTER_LIFESTYLE = Lifestyle("Squatter Lifestyle", dicestring="2d6", base_amount=40, cost=500)
LOW_LIFESTYLE = Lifestyle("Low Lifestyle", dicestring="3d6", base_amount=60, cost=2000)
MIDDLE_LIFESTYLE = Lifestyle("Middle Lifestyle", dicestring="4d6", base_amount=100, cost=5000)
HIGH_LIFESTYLE = Lifestyle("High Lifestyle", dicestring="5d6", base_amount=500, cost=10_000)
LUXURY_LIFESTYLE = Lifestyle("Luxury Lifestyle", dicestring="6d6", base_amount=1000, cost=100_000)

"""
    COMPLEX FORMS

    duration:
        Perm -> Permanent
        Sustain -> Sustained
        Imm -> Immediate

    fading_value:
        level + fading_value

"""
CLEANER = ComplexForm("Cleaner", target='Persona', duration='Permerm', fading_value=1)
DIFFUSE_OF_ATTACK = ComplexForm("Diffuse of attack", target='Device', duration='Sustainustain', fading_value=1)
DIFFUSE_OF_SLEAZE = ComplexForm("Diffuse of sleaze", target='Device', duration='Sustainustain', fading_value=1)
DIFFUSE_OF_DATA_PROCESSING = ComplexForm("Diffuse of data processing", target='Device', duration='Sustainustain', fading_value=1)
DIFFUSE_OF_FIREWALL = ComplexForm("Diffuse of firewall", target='Device', duration='Sustainustain', fading_value=1)
EDITOR = ComplexForm("Editor", target='File', duration='Permerm', fading_value=2)
INFUSION_OF_ATTACK = ComplexForm("Infusion of attack", target='Device', duration='Sustainustain', fading_value=1)
INFUSION_OF_SLEAZE = ComplexForm("Infusion of sleaze", target='Device', duration='Sustainustain', fading_value=1)
INFUSION_OF_DATA_PROCESSING = ComplexForm("Infusion of data processing", target='Device', duration='Sustainustain', fading_value=1)
INFUSION_OF_FIREWALL = ComplexForm("Infusion of firewall", target='Device', duration='Sustainustain', fading_value=1)
STATIC_VEIL = ComplexForm("Static veil", target='Persona', duration='Sustainustain', fading_value=-1)
PULSE_STORM = ComplexForm("Pulse storm", target='Persona', duration='Imm', fading_value=0)
PUPPETEER = ComplexForm("Puppeteer", target='Device', duration='Imm', fading_value=4)
RESONANCE_CHANNEL = ComplexForm("Resonance channel", target='Device', duration='Sustainustain', fading_value=-1)
RESONANCE_SPIKE = ComplexForm("Resonance spike", target='Device', duration='Imme', fading_value=0)
RESONANCE_VEIL = ComplexForm("Resonance veil", target='Device', duration='Sustainustain', fading_value=-1)
STATIC_BOMB = ComplexForm("Static bomb", target='Self', duration='Imme', fading_value=2)
STITCHES = ComplexForm("Stitches", target='Sprite', duration='Permerm', fading_value=-2)
TRANSCENDENT_GRID = ComplexForm("Transcendent grid", target='Self', duration='Imme', fading_value=-3)
TATTLETALE = ComplexForm("Tattletale", target='Persona', duration='Permerm', fading_value=-2)

"""
    SPELLS
"""
# COMBAT SPELLS
ACID_STREAM = Spell("Acid Stream", direct=False, elemental=True, type='Physical', range='Line of Sight', damage='Physical', duration='Instantaneous', drain=-6, category='Combat')
TOXIC_WAVE = Spell('Toxic Wave', direct=False, elemental=True, type='Physical', range='Line of Sight (Area)', damage='Physical', duration='Instantaneous', drain=-1, category='Combat')
PUNCH = Spell('Punch', direct=False, elemental=False, type='Physical', range='Touch', damage='Stun', duration='Instantaneous', drain=-6, category='Combat')
CLOUT = Spell('Clout', direct=False, elemental=False, type='Physical', range='Line of Sight', damage='Stun', duration='Instantaneous', drain=-3, category='Combat')
BLAST = Spell('Blast', direct=False, elemental=False, type='Physical', range='Line of Sight (Area)', damage='Stun', duration='Instantaneous', drain=0, category='Combat')
DEATH_TOUCH = Spell('Death Touch', direct=True, elemental=False, type='Mana', range='Touch', damage='Physical', duration='Instantaneous', drain=-6, category='Combat')
MANABOLT = Spell('Manabolt', direct=True, elemental=False, type='Mana', range='Line of Sight', damage='Physical', duration='Instantaneous', drain=-3, category='Combat')
MANABALL = Spell('Manaball', direct=True, elemental=False, type='Mana', range='Line of Sight (Area)', damage='Physical', duration='Instantaneous', drain=0, category='Combat')
FLAMETHROWER = Spell('Flamethrower', direct=False, elemental=True, type='Physical', range='Line of Sight', damage='Physical', duration='Instantaneous', drain=-3, category='Combat')
FIREBALL = Spell('Fireball', direct=False, elemental=True, type='Physical', range='Los (Area)', damage='Physical', duration='Instantaneous', drain=-1, category='Combat')
LIGHTNING_BOLT = Spell('Lightning Bolt', direct=False, elemental=True, type='Physical', range='Line of Sight', damage='Physical', duration='Instantaneous', drain=-3, category='Combat')
BALL_LIGHTNING = Spell('Ball Lightning', direct=False, elemental=True, type='Physical', range='Line of Sight (Area)', damage='Physical', duration='Instantaneous', drain=-1, category='Combat')
SHATTER = Spell('Shatter', direct=True, elemental=False, type='Physical', range='Touch', damage='Physical', duration='Instantaneous', drain=-6, category='Combat')
POWERBOLT = Spell('Powerbolt', direct=True, elemental=False, type='Physical', range='Line of Sight', damage='Physical', duration='Instantaneous', drain=-3, category='Combat')
POWERBALL = Spell('Powerball', direct=True, elemental=False, type='Physical', range='Line of Sight (Area)', damage='Physical', duration='Instantaneous', drain=0, category='Combat')
KNOCKOUT = Spell('Knockout', direct=True, elemental=False, type='Mana', range='Touch', damage='Stun', duration='Instantaneous', drain=-6, category='Combat')
STUNBOLT = Spell('Stunbolt', direct=True, elemental=False, type='Mana', range='Line of Sight', damage='Stun', duration='Instantaneous', drain=-3, category='Combat')
STUNBALL = Spell('Stunball', direct=True, elemental=False, type='Mana', range='Line of Sight (Area)', damage='Stun', duration='Instantaneous', drain=0, category='Combat')
# DETECTION SPELLS
ANALYZE_DEVICE = Spell('Analyze Device', active=True, detect_type='Directional', type='Physical', range='Touch', duration='Sustainustain', drain=-3, category='Detection')
ANALYZE_MAGIC = Spell('Analyze Magic', active=True, detect_type='Directional', type='Physical', range='Touch', duration='Sustainustain', drain=-3, category='Detection')
ANALYZE_TRUTH = Spell('Analyze Truth', active=True, detect_type='Directional', type='Mana', range='Touch', duration='Sustainustain', drain=-2, category='Detection')
CLAIRAUDIENCE = Spell('Clairaudience', active=False, detect_type='Directional', type='Mana', range='Touch', duration='Sustainustain', drain=-3, category='Detection')
CLAIRVOYANCE = Spell('Clairvoyance', active=False, detect_type='Directional', type='Mana', range='Touch', duration='Sustainustain', drain=-3, category='Detection')
COMBAT_SENSE = Spell('Combat Sense', active=True, detect_type='Psychic', type='Mana', range='Touch', duration='Sustainustain', drain=0, category='Detection')
DETECT_ENEMIES = Spell('Detect Enemies', active=True, detect_type='Area', type='Mana', range='Touch', duration='Sustainustain', drain=-2, category='Detection')
DETECT_ENEMIES_EXTENDED = Spell('Detect Enemies (Extended)', active=True, detect_type='Extended Area', type='Mana', range='Touch', duration='Sustainustain', drain=0, category='Detection')
DETECT_INDIVIDUAL = Spell('Detect individual', active=True, detect_type='Area', type='Mana', range='Touch', duration='Sustainustain', drain=-3, category='Detection')
DETECT_LIFE = Spell('Detect life', active=True, detect_type='Area', type='Mana', range='Touch', duration='Sustainustain', drain=-3, category='Detection')
DETECT_LIFE_EXTENDED = Spell('Detect Life (Extended)', active=True, detect_type='Extended Area', type='Mana', range='Touch', duration='Sustainustain', drain=-1, category='Detection')
DETECT_LIFE_FORM = Spell('Detect Life-form', active=True, detect_type='Area', type='Mana', range='Touch', duration='Sustainustain', drain=-2, category='Detection')
DETECT_LIFE_FORM_EXTENDED = Spell('Detect Life-form (Extended)', active=True, detect_type='Extended Area', type='Mana', range='Touch', duration='Sustainustain', drain=0, category='Detection')
DETECT_MAGIC = Spell('Detect Magic', active=True, detect_type='Area', type='Mana', range='Touch', duration='Sustainustain', drain=-2, category='Detection')
DETECT_MAGIC_EXTENDED = Spell('Detect Magic (Extended)', active=True, detect_type='Extended Area', type='Mana', range='Touch', duration='Sustainustain', drain=0, category='Detection')
DETECT_OBJECT = Spell('Detect Object', active=True, detect_type='Area', type='Physical', range='Touch', duration='Sustainustain', drain=-2, category='Detection')
MIND_LINK = Spell('Mind Link', active=True, detect_type='Psychic', type='Mana', range='Touch', duration='Sustainustain', drain=-1, category='Detection')
MIND_PROBE = Spell('Mind Probe', active=True, detect_type='Directional', type='Mana', range='Touch', duration='Sustainustain', drain=0, category='Detection')
# HEALTH SPELLS
ANTIDOTE = Spell('Antidote', essence=False, type='Mana', range='Touch', duration='Permerm', drain=-3, category='Health')
CURE_DISEASE = Spell('Cure Disease', essence=True, type='Mana', range='Touch', duration='Permerm', drain=-4, category='Health')
DECREASE_BODY = Spell('Decrease Body', essence=True, type='Physical', range='Touch', duration='Sustainustain', drain=-2, category='Health')
DECREASE_AGILITY = Spell('Decrease Agility', essence=True, type='Physical', range='Touch', duration='Sustainustain', drain=-2, category='Health')
DECREASE_REACTION = Spell('Decrease Reaction', essence=True, type='Physical', range='Touch', duration='Sustainustain', drain=-2, category='Health')
DECREASE_STRENGTH = Spell('Decrease Strength', essence=True, type='Physical', range='Touch', duration='Sustainustain', drain=-2, category='Health')
DECREASE_WILLPOWER = Spell('Decrease Willpower', essence=True, type='Physical', range='Touch', duration='Sustainustain', drain=-2, category='Health')
DECREASE_LOGIC = Spell('Decrease Logic', essence=True, type='Physical', range='Touch', duration='Sustainustain', drain=-2, category='Health')
DECREASE_INTUITION = Spell('Decrease Intuition', essence=True, type='Physical', range='Touch', duration='Sustainustain', drain=-2, category='Health')
DECREASE_CHARISMA = Spell('Decrease Charisma', essence=True, type='Physical', range='Touch', duration='Sustainustain', drain=-2, category='Health')
DETOX = Spell('Detox', essence=False, type='Physical', range='Touch', duration='Permerm', drain=-6, category='Health')
HEAL = Spell('Heal', essence=False, type='Physical', range='Touch', duration='Permerm', drain=-4, category='Health')
INCREASE_BODY = Spell('Increase Body', essence=True, type='Physical', range='Touch', duration='Sustainustain', drain=-3, category='Health')
INCREASE_AGILITY = Spell('Increase Agility', essence=True, type='Physical', range='Touch', duration='Sustainustain', drain=-3, category='Health')
INCREASE_REACTION = Spell('Increase Reaction', essence=True, type='Physical', range='Touch', duration='Sustainustain', drain=-3, category='Health')
INCREASE_STRENGTH = Spell('Increase Strength', essence=True, type='Physical', range='Touch', duration='Sustainustain', drain=-3, category='Health')
INCREASE_WILLPOWER = Spell('Increase Willpower', essence=True, type='Physical', range='Touch', duration='Sustainustain', drain=-3, category='Health')
INCREASE_LOGIC = Spell('Increase Logic', essence=True, type='Physical', range='Touch', duration='Sustainustain', drain=-3, category='Health')
INCREASE_INTUITION = Spell('Increase Intuition', essence=True, type='Physical', range='Touch', duration='Sustainustain', drain=-3, category='Health')
INCREASE_CHARISMA = Spell('Increase Charisma', essence=True, type='Physical', range='Touch', duration='Sustainustain', drain=-3, category='Health')
INCREASE_REFLEXES = Spell('Increase Reflexes', essence=True, type='Physical', range='Touch', duration='Sustainustain', drain=0, category='Health')
OXYGENATE = Spell('Oxygenate', essence=False, type='Physical', range='Touch', duration='Sustainustain', drain=-5, category='Health')
PROPHYLAXIS = Spell('Prophylaxis', essence=False, type='Mana', range='Touch', duration='Sustainustain', drain=-4, category='Health')
RESIST_PAIN = Spell('Resist Pain', essence=False, type='Mana', range='Touch', duration='Permerm', drain=-4, category='Health')
STABALISE = Spell('Stabalise', essence=False, type='Mana', range='Touch', duration='Permerm', drain=-4, category='Health')
# ILLUSION SPELLS
AGONY = Spell('Agony', realistic=True, sense='Single', type='Mana', range='Line of Sight', duration='Sustain', drain=-4, category='Illusion')
MASS_AGONY = Spell('Mass Agony', realistic=True, sense='Single', type='Mana', range='Line of Sight (Area)', duration='Sustain', drain=-2, category='Illusion')
BUGS = Spell('Bugs', realistic=True, sense='Multi', type='Mana', range='Line of Sight', duration='Sustain', drain=-3, category='Illusion')
SWARM = Spell('Swarm', realistic=True, sense='Multi', type='Mana', range='Line of Sight (Area)', duration='Sustain', drain=-1, category='Illusion')
CONFUSION = Spell('Confusion', realistic=True, sense='Multi', type='Mana', range='Line of Sight', duration='Sustain', drain=-3, category='Illusion')
MASS_CONFUSION = Spell('Mass Confusion', realistic=True, sense='Multi', type='Mana', range='Line of Sight (Area)', duration='Sustain', drain=-1, category='Illusion')
CHAOS = Spell('Chaos', realistic=True, sense='Multi', type='Physical', range='Line of Sight', duration='Sustain', drain=-2, category='Illusion')
CHAOTIC_WORLD = Spell('Chaotic World', realistic=True, sense='Multi', type='Physical', range='Line of Sight (Area)', duration='Sustain', drain=0, category='Illusion')
ENTERTAINMENT = Spell('Entertainment', realistic=True, sense='Multi', type='Mana', range='Line of Sight (Area)', duration='Sustain', drain=-3, category='Illusion')
TRID_ENTERTAINMENT = Spell('Trid Entertainment', realistic=True, sense='Multi', type='Physical', range='Line of Sight (Area)', duration='Sustain', drain=-2, category='Illusion')
INVISIBILITY = Spell('Invisibility', realistic=True, sense='Single', type='Mana', range='Line of Sight', duration='Sustain', drain=-2, category='Illusion')
IMPROVED_INVISIBILITY = Spell('Improved Invisibility', realistic=True, sense='Single', type='Physical', range='Line of Sight', duration='Sustain', drain=-1, category='Illusion')
MASK = Spell('Mask', realistic=True, sense='Multi', type='Mana', range='Touch', duration='Sustain', drain=-2, category='Illusion')
PHYSICAL_MASK = Spell('Physical', realistic=True, sense='Multi', type='Physical', range='Touch', duration='Sustain', drain=-1, category='Illusion')
PHANTASM = Spell('Phantasm', realistic=True, sense='Multi', type='Mana', range='Line of Sight (Area)', duration='Sustain', drain=-1, category='Illusion')
TRID_PHANTASM = Spell('Trid Phantasm', realistic=True, sense='Multi', type='Physical', range='Line of Sight (Area)', duration='Sustain', drain=0, category='Illusion')
HUSH = Spell('Hush', realistic=True, sense='Single', type='Mana', range='Line of Sight (Area)', duration='Sustain', drain=-2, category='Illusion')
SILENCE = Spell('Silence', realistic=True, sense='Single', type='Physical', range='Line of Sight (Area)', duration='Sustain', drain=-1, category='Illusion')
STEALTH = Spell('Stealth', realistic=True, sense='Single', type='Physical', range='Line of Sight', duration='Sustain', drain=-2, category='Illusion')
# MANIPULATION SPELLS
ANIMATE = Spell('Animate', damaging=False, targeting='Physical', type='Physical', range='Line of Sight', duration='Sustain', drain=-1, category='Manipulation')
MASS_ANIMATE = Spell('Mass Animate', damaging=False, targeting='Physical', type='Physical', range='Line of Sight (Area)', duration='Sustain', drain=1, category='Manipulation')
ARMOR = Spell('Armor', damaging=False, targeting='Physical', type='Physical', range='Line of Sight', duration='Sustain', drain=-2, category='Manipulation')
CONTROL_ACTIONS = Spell('Control Actions', damaging=False, targeting='Mental', type='Mana', range='Line of Sight', duration='Sustain', drain=-1, category='Manipulation')
MOB_CONTROL = Spell('Mob Control', damaging=False, targeting='Mental', type='Mana', range='Line of Sight (Area)', duration='Sustain', drain=1, category='Manipulation')
CONTROL_THOUGHTS = Spell('Control Thoughts', damaging=False, targeting='Mental', type='Mana', range='Line of Sight', duration='Sustain', drain=-1, category='Manipulation')
MOB_MIND = Spell('Mob Mind', damaging=False, targeting='Mental', type='Mana', range='Line of Sight', duration='Sustain', drain=1, category='Manipulation')
FLING = Spell('Fling', damaging=True, targeting='Physical', type='Physical', range='Line of Sight', duration='Instantaneous', drain=-2, category='Manipulation')
ICE_SHEET = Spell('Ice Sheet', damaging=False, targeting='Environmental', type='Physical', range='Line of Sight (Area)', duration='Instantaneous', drain=0, category='Manipulation')
IGNITE = Spell('Ignite', damaging=False, targeting='Physical', type='Physical', range='Line of Sight', duration='Perm', drain=-1, category='Manipulation')
INFLUENCE = Spell('Influence', damaging=False, targeting='Physical', type='Mana', range='Line of Sight', duration='Perm', drain=-1, category='Manipulation')
LEVITATE = Spell('Levitate', damaging=False, targeting='Physical', type='Physical', range='Line of Sight', duration='Sustain', drain=-2, category='Manipulation')
LIGHT = Spell('Light', damaging=False, targeting='Environmental', type='Physical', range='Line of Sight (Area)', duration='Sustain', drain=-4, category='Manipulation')
MAGIC_FINGERS = Spell('Magic Fingers', damaging=False, targeting='Physical', type='Physical', range='Line of Sight', duration='Sustain', drain=-2, category='Manipulation')
MANA_BARRIER = Spell('Mana Barrier', damaging=False, targeting='Environmental', type='Mana', range='Line of Sight (Area)', duration='Sustain', drain=-2, category='Manipulation')
PHYSICAL_BARRIER = Spell('Physical Barrier', damaging=False, targeting='Environmental', type='Physical', range='Line of Sight (Area)', duration='Sustain', drain=-1, category='Manipulation')
POLTERGEIST = Spell('Poltergeist', damaging=False, targeting='Environmental', type='Physical', range='Line of Sight (Area)', duration='Sustain', drain=-2, category='Manipulation')
SHADOW = Spell('Shadow', damaging=False, targeting='Environmental', type='Physical', range='Line of Sight (Area)', duration='Sustain', drain=-3, category='Manipulation')

COMBAT_SPELLS = [spell for spell in Spell.items if spell.category=='Combat']
DETECTION_SPELLS = [spell for spell in Spell.items if spell.category=='Detection']
HEALTH_SPELLS = [spell for spell in Spell.items if spell.category=='Health']
ILLUSION_SPELLS = [spell for spell in Spell.items if spell.category=='Illusion']
MANIPULATION_SPELLS = [spell for spell in Spell.items if spell.category=='Manipulation']

"""
    AUGMENTATIONS
"""
# HEADWARE
COMMLINK = Augmentation("Commlink (Aug)", page_ref=453, cost=["CommlinkCost", "+", 2000], essence=0.2, capacity=2, avail=0, cyberlimbs=True, subtype="Headware", requires=["Subtype", "Commlink"], )
CONTROL_RIG_1 = Augmentation("Control Rig (Rating 1)", page_ref=453, cost=43_000, rating=1, essence=1, capacity="-", avail=5, legality=RESTRICTED, subtype="Headware", base=True)
CONTROL_RIG_2 = Augmentation("Control Rig (Rating 2)", page_ref=453, cost=97_000, rating=2, essence=2, capacity="-", avail=10, legality=RESTRICTED, subtype="Headware", base=True)
CONTROL_RIG_3 = Augmentation("Control Rig (Rating 3)", page_ref=453, cost=208_000, rating=3, essence=3, capacity="-", avail=15, legality=RESTRICTED, subtype="Headware", base=True)
CORTEX_BOMB_KINK = Augmentation("Cortex Bomb (Kink)", page_ref=453, cost=10_000, essence=0, capacity=1, avail=12, legality=FORBIDDEN, cyberlimbs=True, subtype="Headware", )
CORTEX_BOMB_MICROBOMB = Augmentation("Cortex Bomb (Microbomb)", page_ref=453, cost=25_000, essence=0, capacity=2, avail=16, legality=FORBIDDEN, cyberlimbs=True, subtype="Headware", )
CORTEX_BOMB_AREA = Augmentation("Cortex Bomb (Area)", page_ref=453, cost=40_000, essence=0, capacity=3, avail=20, legality=FORBIDDEN, cyberlimbs=True, subtype="Headware", )
CYBERDECK_AUG = Augmentation("Cyberdeck", page_ref=453, cost=["DeckCost", "+", 5000], essence=0.4, capacity=4, avail=5, legality=RESTRICTED, cyberlimbs=True, subtype="Headware", requires=["Subtype", "Cyberdeck"], )
DATAJACK = Augmentation("Datajack", page_ref=453, cost=1000, essence=0.1, capacity="-", avail=2, subtype="Headware", )
DATA_LOCK_1_12 = Augmentation("Data Lock", page_ref=453, cost=["Rating", "*", 1000], rating=[1, "to", 12], essence=0.1, capacity="-", avail=["Rating", "*", 2], subtype="Headware", )
OLFACTORY_BOOSTER_1_6 = Augmentation("Olfactory Booster", page_ref=453, cost=["Rating", "*", 4000], rating=[1, "to", 6], essence=0.2, capacity="-", avail=["Rating", "*", 3], subtype="Headware", )
SIMRIG = Augmentation("Simrig", cost=4000, essence=0.2, capacity="-", avail=12, legality=RESTRICTED, subtype="Headware", )
SKILLJACK_1_6 = Augmentation("Skilljack", page_ref=453, cost=["Rating", "*", 20000], rating=[1, "to", 6], essence=["Rating", "*", 0.1], capacity="-", avail=["Rating", "*", 2], subtype="Headware", )
TASTE_BOOSTER = Augmentation("Taste Booster", page_ref=453, cost=["Rating", "*", 3000], rating=[1, "to", 3], essence=0.2, capacity="-", avail=["Rating", "*", 3], subtype="Headware", )
TOOTH_COMPARTMENT = Augmentation("Tooth Compartment", page_ref=453, cost=800, essence="-", capacity="-", avail=8, subtype="Headware", )
ULTRASOUND_SENSOR_1_6 = Augmentation("Ultrasound Sensor", page_ref=453, cost=["Rating", "*", 12_000], rating=[1, "to", 6], essence=0.25, capacity=2, avail=10, cyberlimbs=True, subtype="Headware", )
VOICE_MODULATOR_1_6 = Augmentation("Voice Modulator", page_ref=453, cost=["Rating", "*", 5000], rating=[1, "to", 6], essence=0.2, capacity="-", avail=["Rating", "*", 3], legality=FORBIDDEN, subtype="Headware", )
# EYEWARE
CYBEREYES_1 = Augmentation("Cybereyes (Rating 1)", page_ref=454, cost=4000, rating=1, essence=0.2, capacity=4, avail=3, cyberlimbs=False, subtype='Eyeware', base=True)
CYBEREYES_2 = Augmentation("Cybereyes (Rating 2)", page_ref=454, cost=6000, rating=2, essence=0.3, capacity=8, avail=6, cyberlimbs=False, subtype='Eyeware', base=True)
CYBEREYES_3 = Augmentation("Cybereyes (Rating 3)", page_ref=454, cost=10000, rating=3, essence=0.4, capacity=12, avail=9, cyberlimbs=False, subtype='Eyeware', base=True)
CYBEREYES_4 = Augmentation("Cybereyes (Rating 4)", page_ref=454, cost=14000, rating=4, essence=0.5, capacity=16, avail=12, cyberlimbs=False, subtype='Eyeware', base=True)
FLARE_COMPENSATION_AUG = Augmentation("Flare Compensation (Aug)", page_ref=454, cost=1000, essence=0.1, capacity=1, avail=4, cyberlimbs=True, subtype='Eyeware', )
IMAGE_LINK_AUG = Augmentation("Image Link (Aug)", page_ref=454, cost=1000, essence=0.1, capacity="-", avail=4, as_standard=True, subtype='Eyeware', )
LOW_LIGHT_VISION_AUG = Augmentation("Low Light Vision (Aug)", page_ref=454, cost=1500, essence=0.1, capacity=2, avail=4, cyberlimbs=True, subtype='Eyeware', )
OCULAR_DRONE = Augmentation("Ocular Drone", page_ref=454, cost=6000, essence="-", capacity=6, avail=6, cyberlimbs=True, subtype='Eyeware', )
RETINAL_DUPLICATION_1_6 = Augmentation("Retinal Duplication", page_ref=454, cost=["Rating", "*", 20_000], rating=[1, "to", 6], essence=0.1, capacity=1, avail=16, legality=FORBIDDEN, cyberlimbs=True, subtype='Eyeware', )
SMARTLINK_AUG = Augmentation("Smartlink (Aug)", page_ref=454, cost=4000, essence=0.2, capacity=3, avail=8, legality=RESTRICTED, cyberlimbs=True, subtype='Eyeware', )
THERMOGRAPHIC_VISION_AUG = Augmentation("Thermographic Vision (Aug)", page_ref=454, cost=1500, essence=0.1, capacity=2, avail=4, cyberlimbs=True, subtype='Eyeware', )
VISION_ENHANCEMENT_AUG = Augmentation("Vision Enhancement (Aug)", page_ref=454, cost=["Rating", "*", 4000], rating=[1, "to", 3], essence=0.1, capacity=["Rating"], avail=["Rating", "*", 3], cyberlimbs=True, subtype='Eyeware', )
VISION_MAGNIFICATION_AUG = Augmentation("Vision Magnification (Aug)", page_ref=454, cost=2000, essence=0.1, capacity=2, avail=4, cyberlimbs=True, subtype='Eyeware', )
# EARWARE
CYBEREARS_1 = Augmentation("Cyberears (Rating 1)", page_ref=454, cost=3000, rating=1, essence=0.2, capacity=4, avail=3, cyberlimbs=False, subtype='Earware', location="Ears", base=True)
CYBEREARS_2 = Augmentation("Cyberears (Rating 2)", page_ref=454, cost=4500, rating=2, essence=0.3, capacity=8, avail=6, cyberlimbs=False, subtype='Earware', location="Ears", base=True)
CYBEREARS_3 = Augmentation("Cyberears (Rating 3)", page_ref=454, cost=7500, rating=3, essence=0.4, capacity=12, avail=9, cyberlimbs=False, subtype='Earware', location="Ears", base=True)
CYBEREARS_4 = Augmentation("Cyberears (Rating 4)", page_ref=454, cost=11000, rating=4, essence=0.5, capacity=16, avail=12, cyberlimbs=False, subtype='Earware', location="Ears", base=True)
AUDIO_ENHANCEMENT_AUG_1_3 = Augmentation("Audio Enhancement (Aug)", page_ref=454, cost=["Rating", "*", 4000], rating=[1, "to", 3], essence=0.1, capacity=["Rating"], avail=["Rating", "*", 3], cyberlimbs=True, subtype='Earware', location="Ears")
BALANCE_AUGMENTER = Augmentation("Balance Augmenter", page_ref=454, cost=8000, essence=0.1, capacity=4, avail=8, cyberlimbs=True, subtype='Earware', location="Ears")
DAMPER = Augmentation("Damper", page_ref=454, cost=2250, essence=0.1, capacity=1, avail=6, cyberlimbs=True, subtype='Earware', location="Ears")
SELECT_SOUND_FILTER_AUG_1_6 = Augmentation("Select Sound Filter (Aug)", page_ref=454, cost=["Rating", "*", 3500], rating=[1, "to", 6], essence=0.1, capacity=["Rating"], avail=["Rating", "*", 3], cyberlimbs=True, subtype='Earware', location="Ears")
SOUND_LINK = Augmentation("Sound Link", page_ref=454, cost=1000, essence=0.1, capacity="-", avail=4, cyberlimbs=False, as_standard=True, subtype='Earware', location="Ears")
SPATIAL_RECOGNIZER = Augmentation("Spatial Recognizer", page_ref=454, cost=4000, essence=0.1, capacity=2, avail=8, cyberlimbs=True, subtype='Earware', location="Ears")
# BODYWARE
BONE_LACING_PLASTIC = Augmentation("Bone Lacing (Plastic)", page_ref=456, cost=8000, essence=0.5, capacity="-", avail=8, legality=RESTRICTED, cyberlimbs=False, subtype='Bodyware', location="Body")
BONE_LACING_ALUMINUM = Augmentation("Bone Lacing (Aluminum)", page_ref=456, cost=18000, essence=1, capacity="-", avail=12, legality=RESTRICTED, cyberlimbs=False, subtype='Bodyware', location="Body")
BONE_LACING_TITANIUM = Augmentation("Bone Lacing (Titanium)", page_ref=456, cost=30000, essence=1.5, capacity="-", avail=16, legality=RESTRICTED, cyberlimbs=False, subtype='Bodyware', location="Body")
DERMAL_PLANTING_1_6 = Augmentation("Dermal Planting", page_ref=456, cost=["Rating", "*", 3000], rating=[1, "to", 6], essence=["Rating", "*", 0.5], capacity="-", avail=["Rating", "*", 4], legality=RESTRICTED, cyberlimbs=False, subtype='Bodyware', location="Body")
FINGERTIP_COMPARTMENT = Augmentation("Fingertip Compartment", page_ref=456, cost=3000, essence=0.1, capacity=1, avail=4, cyberlimbs=True, subtype='Bodyware', location="Body")
GRAPPLE_GUN_AUG = Augmentation("Grapple Gun (Aug)", page_ref=456, cost=5000, essence=0.5, capacity=4, avail=8, cyberlimbs=True, subtype='Bodyware', location="Body")
INTERNAL_AIR_TANK_1_3 = Augmentation("Internal Air Tank", page_ref=456, cost=["Rating", "*", 8000], rating=[1, "to", 3], essence=0.25, capacity=3, avail=["Rating"], cyberlimbs=True, subtype='Bodyware', location="Body")
MUSCLE_REPLACEMENT_1_3 = Augmentation("Muscle Replacement", page_ref=456, cost=["Rating", "*", 25000], rating=[1, "to", 4], essence=["Rating", "*", 1], capacity="-", avail=["Rating", "*", 5], legality=RESTRICTED, cyberlimbs=False, subtype='Bodyware', location="Body")
REACTION_ENHANCERS_1_3 = Augmentation("Reaction Enhancers", page_ref=456, cost=["Rating", "*", 13000], rating=[1, "to", 3], essence=["Rating", "*", 0.3], capacity="-", avail=["Rating", "*", 5], legality=RESTRICTED, cyberlimbs=False, subtype='Bodyware', location="Body")
SKILLWIRES_1_6 = Augmentation("Skillwires", page_ref=456, cost=["Rating", "*", 20000], rating=[1, "to", 6], essence=["Rating", "*", 0.1], capacity="-", avail=["Rating", "*", 4], cyberlimbs=False, subtype='Bodyware', location="Body")
SMUGGLING_COMPARTMENT = Augmentation("Smuggling Compartment", page_ref=456, cost=7500, essence=0.2, capacity=2, avail=6, cyberlimbs=True, subtype='Bodyware', location="Body")
WIRED_REFLEXES_1 = Augmentation("Wired Reflexes (Rating 1)", page_ref=456, cost=39000, essence=2, capacity="-", avail=8, legality=RESTRICTED, cyberlimbs=False, subtype='Bodyware', location="Body")
WIRED_REFLEXES_2 = Augmentation("Wired Reflexes (Rating 2)", page_ref=456, cost=149000, essence=3, capacity="-", avail=12, legality=RESTRICTED, cyberlimbs=False, subtype='Bodyware', location="Body")
WIRED_REFLEXES_3 = Augmentation("Wired Reflexes (Rating 3)", page_ref=456, cost=217000, essence=5, capacity="-", avail=20, legality=RESTRICTED, cyberlimbs=False, subtype='Bodyware', location="Body")
# CYBERLIMBS
FULL_ARM_OBV = Augmentation("Cyberlimb - Full Arm (Obvious)", page_ref=457, cost=15000, essence=1, capacity=15, avail=4, subtype='Cyberlimbs', location="Full Arm", base=True)
FULL_LEG_OBV = Augmentation("Cyberlimb - Full Leg (Obvious)", page_ref=457, cost=15000, essence=1, capacity=20, avail=4, subtype='Cyberlimbs', location="Full Leg", base=True)
HAND_OBV = Augmentation("Cyberlimb - Hand (Obvious)", page_ref=457, cost=5000, essence=0.25, capacity=4, avail=2, subtype='Cyberlimbs', location="Hand", base=True)
FOOT_OBV = Augmentation("Cyberlimb - Foot (Obvious)", page_ref=457, cost=5000, essence=0.25, capacity=4, avail=2, subtype='Cyberlimbs', location="Foot", base=True)
LOWER_ARM_OBV = Augmentation("Cyberlimb - Lower Arm (Obvious)", page_ref=457, cost=10000, essence=0.45, capacity=10, avail=4, subtype='Cyberlimbs', location="Lower Arm", base=True)
LOWER_LEG_OBV = Augmentation("Cyberlimb - Lower Leg (Obvious)", page_ref=457, cost=10000, essence=0.45, capacity=12, avail=4, subtype='Cyberlimbs', location="Lower Leg", base=True)
TORSO_OBV = Augmentation("Cyberlimb - Torso (Obvious)", page_ref=457, cost=20000, essence=1.5, capacity=10, avail=12, subtype='Cyberlimbs', location="Torso", base=True)
SKULL_OBV = Augmentation("Cyberlimb - Skull (Obvious)", page_ref=457, cost=10000, essence=0.75, capacity=4, avail=16, subtype='Cyberlimbs', location="Skull", base=True)
FULL_ARM_SYNTH = Augmentation("Cyberlimb - Full Arm (Synthetic)", page_ref=457, cost=20000, essence=1, capacity=8, avail=4, subtype='Cyberlimbs', location="Full Arm", base=True)
FULL_LEG_SYNTH = Augmentation("Cyberlimb - Full Leg (Synthetic)", page_ref=457, cost=20000, essence=1, capacity=10, avail=4, subtype='Cyberlimbs', location="Full Leg", base=True)
HAND_SYNTH = Augmentation("Cyberlimb - Hand (Synthetic)", page_ref=457, cost=6000, essence=0.25, capacity=2, avail=2, subtype='Cyberlimbs', location="Hand", base=True)
FOOT_SYNTH = Augmentation("Cyberlimb - Foot (Synthetic)", page_ref=457, cost=6000, essence=0.25, capacity=2, avail=2, subtype='Cyberlimbs', location="Foot", base=True)
LOWER_ARM_SYNTH = Augmentation("Cyberlimb - Lower Arm (Synthetic)", page_ref=457, cost=12000, essence=0.45, capacity=5, avail=4, subtype='Cyberlimbs', location="Lower Arm", base=True)
LOWER_LEG_SYNTH = Augmentation("Cyberlimb - Lower Leg (Synthetic)", page_ref=457, cost=12000, essence=0.45, capacity=6, avail=4, subtype='Cyberlimbs', location="Lower Leg", base=True)
TORSO_SYNTH = Augmentation("Cyberlimb - Torso (Synthetic)", page_ref=457, cost=25000, essence=1.5, capacity=5, avail=12, subtype='Cyberlimbs', location="Torso", base=True)
SKULL_SYNTH = Augmentation("Cyberlimb - Skull (Synthetic)", page_ref=457, cost=15000, essence=0.75, capacity=2, avail=16, subtype='Cyberlimbs', location="Skull", base=True)
# CYBERLIMB ENHANCEMENTS
CYBERLIMB_EN_AGILITY = Augmentation("Cyberlimb Enhancement - Agility", page_ref=457, cost=["Rating", "*", 6500], rating=[1, "to", 3], essence="-", capacity=["Rating"], avail=["Rating", "*", 3], legality=RESTRICTED, subtype='Cyberlimbs Enhancement')
CYBERLIMB_EN_ARMOR = Augmentation("Cyberlimb Enchancement - Armor", page_ref=457, cost=["Rating", "*", 3000], rating=[1, "to", 3], essence="-", capacity=["Rating"], avail=["Rating", "*", 5], subtype='Cyberlimbs Enhancement')
CYBERLIMB_EN_STRENGTH = Augmentation("Cyberlimb Enhancement - Strenght", page_ref=457, cost=["Rating", "*", 6500], rating=[1, "to", 3], essence="-", capacity=["Rating"], avail=["Rating", "*", 3], legality=RESTRICTED, subtype='Cyberlimbs Enhancement')
# CYBERLIMB ACCESSORIES
CYBERARM_GYROMOUNT = Augmentation("Cyberarm Gyromount", page_ref=457, cost=6000, essence="-", capacity=8, avail=12, legality=FORBIDDEN, cymberlimbs=True, subtype='Cyberlimb Accessory', )
CYBERARM_SLIDE = Augmentation("Cyberarm Slide", page_ref=457, cost=3000, essence="-", capacity=3, avail=12, legality=RESTRICTED, cymberlimbs=True, subtype='Cyberlimb Accessory', )
CYBER_HOLSTER = Augmentation("Cyber Holster", page_ref=457, cost=2000, essence="-", capacity=5, avail=8, legality=RESTRICTED, cymberlimbs=True, subtype='Cyberlimb Accessory', )
HYDRAULIC_JACKS_1_6 = Augmentation("Hydraulic Jacks", page_ref=457, cost=["Rating", "*", 2500], rating=[1, "to", 6], essence="-", capacity=["Rating"], avail=9, cymberlimbs=True, subtype='Cyberlimb Accessory', )
LARGE_SMUGGLING_COMPARMENT = Augmentation("Large Smuggling Comparment", page_ref=457, cost=8000, essence="-", capacity=5, avail=6, cymberlimbs=True, subtype='Cyberlimb Accessory', )
# CYBER IMPLANT WEAPONS - AUGMENTATION ENTRY
CYBER_HOLD_OUT_PISTOL = Augmentation("Hold Out Pistol (Cyber Implant)", page_ref=458, cost=2000, essence=0.1, capacity=2, avail=8, legality=RESTRICTED, cyberlimbs=True, subtype="Cyber Implant Weapons", )
CYBER_LIGHT_PISTOL = Augmentation("Light Pistol (Cymber Implant)", page_ref=458, cost=3900, essence=0.25, capacity=4, avail=10, legality=RESTRICTED, cyberlimbs=True, subtype="Cyber Implant Weapons", )
CYBER_MACHINE_PISTOL = Augmentation("Machine Pistol (Cyber Implant)", page_ref=458, cost=3500, essence=0.5, capacity=6, avail=12, legality=RESTRICTED, cyberlimbs=True, subtype="Cyber Implant Weapons", )
CYBER_HEAVY_PISTOL = Augmentation("Heavy Pistol (Cyber Implant)", page_ref=458, cost=4300, essence=0.5, capacity=6, avail=12, legality=RESTRICTED, cyberlimbs=True, subtype="Cyber Implant Weapons", )
CYBER_SUBMACHINE_GUN = Augmentation("Submachine Gun (Cyber Implant)", page_ref=458, cost=4800, essence=1, capacity=8, avail=12, legality=RESTRICTED, cyberlimbs=True, subtype="Cyber Implant Weapons", )
CYBER_SHOTGUN = Augmentation("Shotgun (Cyber Implant)", page_ref=458, cost=8500, essence=1.25, capacity=10, avail=12, legality=RESTRICTED, cyberlimbs=True, subtype="Cyber Implant Weapons", )
CYBER_MICROGRENADE_LAUNCHER = Augmentation("Micro-Grenade Launcher (Cyber Implant)", page_ref=458, cost=30000, essence=1.5, capacity=15, avail=20, legality=FORBIDDEN, cyberlimbs=True, subtype="Cyber Implant Weapons", )
CYBER_HAND_BLADE = Augmentation("Hand Blade (Cyber Implant)", page_ref=458, cost=2500, essence=0.25, capacity=2, avail=10, legality=FORBIDDEN, cyberlimbs=True, subtype="Cyber Implant Weapons", )
CYBER_HAND_RAZOR = Augmentation("Hand Razor (Cyber Implant)", page_ref=458, cost=1250, essence=0.2, capacity=2, avail=8, legality=FORBIDDEN, cyberlimbs=True, subtype="Cyber Implant Weapons", )
CYBER_SPURS = Augmentation("Spurs (Cyber Implant)", page_ref=458, cost=5000, essence=0.3, capacity=3, avail=12, legality=FORBIDDEN, cyberlimbs=True, subtype="Cyber Implant Weapons", )
CYBER_SHOCK_HAND = Augmentation("Shock Hand (Cyber Implant)", page_ref=458, cost=5000, essence=0.25, capacity=4, avail=8, legality=RESTRICTED, cyberlimbs=True, subtype="Cyber Implant Weapons", )
# CYBER IMPLANT WEAPONS - FIREARM/MELEE WEAPON ENTRY
HOLD_OUT_PISTOL_CYBER = Firearm("Hold Out Pistol (Cyber Implant) [W]", cost=CYBER_HOLD_OUT_PISTOL.cost, page_ref=CYBER_HOLD_OUT_PISTOL.page_ref, avail=CYBER_HOLD_OUT_PISTOL.avail, subtype="Cyber Implant Weapons")
LIGHT_PISTOL_CYBER = Firearm("Light Pistol (Cymber Implant) [W]", cost=CYBER_LIGHT_PISTOL.cost, page_ref=CYBER_LIGHT_PISTOL.page_ref, avail=CYBER_LIGHT_PISTOL.avail, subtype="Cyber Implant Weapons")
MACHINE_PISTOL_CYBER = Firearm("Machine Pistol (Cyber Implant) [W]", cost=CYBER_MACHINE_PISTOL.cost, page_ref=CYBER_MACHINE_PISTOL.page_ref, avail=CYBER_MACHINE_PISTOL.avail, subtype="Cyber Implant Weapons")
HEAVY_PISTOL_CYBER = Firearm("Heavy Pistol (Cyber Implant) [W]", cost=CYBER_HEAVY_PISTOL.cost, page_ref=CYBER_HEAVY_PISTOL.page_ref, avail=CYBER_HEAVY_PISTOL.avail, subtype="Cyber Implant Weapons")
SUBMACHINE_GUN_CYBER = Firearm("Submachine Gun (Cyber Implant) [W]", cost=CYBER_SUBMACHINE_GUN.cost, page_ref=CYBER_SUBMACHINE_GUN.page_ref, avail=CYBER_SUBMACHINE_GUN.avail, subtype="Cyber Implant Weapons")
SHOTGUN_CYBER = Firearm("Shotgun (Cyber Implant) [W]", cost=CYBER_SHOTGUN.cost, page_ref=CYBER_SHOTGUN.page_ref, avail=CYBER_SHOTGUN.avail, subtype="Cyber Implant Weapons")
MICROGRENADE_LAUNCHER_CYBER = Firearm("Micro-Grenade Launcher (Cyber Implant) [W]", cost=CYBER_MICROGRENADE_LAUNCHER.cost, page_ref=CYBER_MICROGRENADE_LAUNCHER.page_ref, avail=CYBER_MICROGRENADE_LAUNCHER.avail, subtype="Cyber Implant Weapons")
HAND_BLADE_CYBER = MeleeWeapon("Hand Blade (Cyber Implant) [W]", cost=CYBER_HAND_BLADE.cost, page_ref=CYBER_HAND_BLADE.page_ref, avail=CYBER_HAND_BLADE.avail, subtype="Cyber Implant Weapons")
HAND_RAZOR_CYBER = MeleeWeapon("Hand Razor (Cyber Implant) [W]", cost=CYBER_HAND_RAZOR.cost, page_ref=CYBER_HAND_RAZOR.page_ref, avail=CYBER_HAND_RAZOR.avail, subtype="Cyber Implant Weapons")
SPURS_CYBER = MeleeWeapon("Spurs (Cyber Implant) [W]", cost=CYBER_SPURS.cost, page_ref=CYBER_SPURS.page_ref, avail=CYBER_SPURS.avail, subtype="Cyber Implant Weapons")
SHOCK_HAND_CYBER = MeleeWeapon("Shock Hand (Cyber Implant) [W]", cost=CYBER_SHOCK_HAND.cost, page_ref=CYBER_SHOCK_HAND.page_ref, avail=CYBER_SHOCK_HAND.avail, subtype="Cyber Implant Weapons")
# BIOWARE
ADRENALINE_PUMP_1_3 = Augmentation("ADRENALINE_PUMP_1_3", page_ref=460, cost=["Rating", "*", 55000], rating=[1, "to", 3], essence=["Rating", "*", 0.75], avail=["Rating", "*", 6], legality=FORBIDDEN, subtype="Bioware", )
BONE_DENSITY_AUGMENTATION_1_4 = Augmentation("BONE_DENSITY_AUGMENTATION_1_4", page_ref=460, cost=["Rating", "*", 5000], rating=[1, "to", 4], essence=["Rating", "*", 0.3], avail=["Rating", "*", 4], subtype="Bioware", )
CATS_EYE = Augmentation("CATS_EYE", page_ref=460, cost=4000, essence=0.1, avail=4, subtype="Bioware", )
ENHANCED_ARTICULATION = Augmentation("ENHANCED_ARTICULATION", page_ref=460, cost=24000, essence=0.3, avail=12, subtype="Bioware", )
MUSCLE_AUGMENTATION_1_4 = Augmentation("MUSCLE_AUGMENTATION_1_4", page_ref=460, cost=["Rating", "*", 31000], rating=[1, "to", 4], essence=["Rating", "*", 0.2], avail=["Rating", "*", 5], legality=RESTRICTED, subtype="Bioware", )
MUSCLE_TONER_1_4 = Augmentation("MUSCLE_TONER_1_4", page_ref=460, cost=["Rating", "*", 32000], rating=[1, "to", 4], essence=["Rating", "*", 0.2], avail=["Rating", "*", 5], legality=RESTRICTED, subtype="Bioware", )
ORTHOSKIN_1_4 = Augmentation("ORTHOSKIN_1_4", page_ref=460, cost=["Rating", "*", 6000], rating=[1, "to", 4], essence=["Rating", "*", 0.25], avail=["Rating", "*", 5], legality=RESTRICTED, subtype="Bioware", )
PATHOGENIC_DEFENSE_1_6 = Augmentation("PATHOGENIC_DEFENSE_1_6", page_ref=460, cost=["Rating", "*", 4500], rating=[1, "to", 6], essence=["Rating", "*", 0.1], avail=["Rating", "*", 2], subtype="Bioware", )
PLATELET_FACTORIES = Augmentation("PLATELET_FACTORIES", page_ref=460, cost=17000, essence=0.2, avail=12, subtype="Bioware", )
SKIN_POCKET = Augmentation("SKIN_POCKET", page_ref=460, cost=12000, essence=0.1, avail=4, subtype="Bioware", )
SUPRATHYROID_GLAND = Augmentation("SUPRATHYROID_GLAND", page_ref=460, cost=140_000, essence=0.7, avail=20, legality=RESTRICTED, subtype="Bioware", )
SYMBIOTES_1_4 = Augmentation("SYMBIOTES_1_4", page_ref=460, cost=["Rating", "*", 3500], rating=[1, "to", 4], essence=["Rating", "*", 0.2], avail=["Rating", "*", 5], subtype="Bioware", )
SYNTHCARDIUM_1_3 = Augmentation("SYNTHCARDIUM_1_3", page_ref=460, cost=["Rating", "*", 30000], rating=[1, "to", 3], essence=["Rating", "*", 0.1], avail=["Rating", "*", 4], subtype="Bioware", )
TAILORED_PHEROMONES_1_3 = Augmentation("TAILORED_PHEROMONES_1_3", page_ref=460, cost=["Rating", "*", 31000], rating=[1, "to", 3], essence=["Rating", "*", 0.2], avail=["Rating", "*", 4], legality=RESTRICTED, subtype="Bioware", )
TOXIN_EXTRACTOR_1_6 = Augmentation("TOXIN_EXTRACTOR_1_6", page_ref=460, cost=["Rating", "*", 4800], rating=[1, "to", 6], essence=["Rating", "*", 0.2], avail=["Rating", "*", 3], subtype="Bioware", )
TRACHEAL_FILTER_1_6 = Augmentation("TRACHEAL_FILTER_1_6", page_ref=460, cost=["Rating", "*", 4500], rating=[1, "to", 6], essence=["Rating", "*", 0.1], avail=["Rating", "*", 3], subtype="Bioware", )
# CULTURED BIOWARE
CEREBRAL_BOOSTER_1_3 = Augmentation("CEREBRAL_BOOSTER_1_3", page_ref=461, cost=["Rating", "*", 31500], rating=[1, "to", 3], essence=["Rating", "*", 0.2], avail=["Rating", "*", 6], subtype="Cultured Bioware", )
DAMAGE_COMPENSATORS_1_12 = Augmentation("DAMAGE_COMPENSATORS_1_12", page_ref=461, cost=["Rating", "*", 2000], rating=[1, "to", 12], essence=["Rating", "*", 0.1], avail=["Rating", "*", 3], legality=FORBIDDEN, subtype="Cultured Bioware", )
MNEMONIC_ENCHANCER_1_3 = Augmentation("MNEMONIC_ENCHANCER_1_3", page_ref=461, cost=["Rating", "*", 9000], rating=[1, "to", 3], essence=["Rating", "*", 0.1], avail=["Rating", "*", 5], subtype="Cultured Bioware", )
PAIN_EDITOR = Augmentation("PAIN_EDITOR", page_ref=461, cost=48000, essence=0.3, avail=18, legality=FORBIDDEN, subtype="Cultured Bioware", )
REFLEX_RECORDER = Augmentation("REFLEX_RECORDER", page_ref=461, cost=14000, essence=0.1, avail=10, subtype="Cultured Bioware", )
SLEEP_REGULATOR = Augmentation("SLEEP_REGULATOR", page_ref=461, cost=12000, essence=0.1, avail=6, subtype="Cultured Bioware", )
SYNAPTIC_BOOSTER_1_3 = Augmentation("SYNAPTIC_BOOSTER_1_3", page_ref=461, cost=["Rating", "*", 95000], rating=[1, "to", 3], essence=["Rating", "*", 0.5], avail=["Rating", "*", 6], legality=RESTRICTED, subtype="Cultured Bioware", )

"""
    AUGMENTATION GRADES
"""
AUG_GRADE_STANDARD = AugmentationGrade('Standard', cost=1, avail=0, essence=1, default=True)
AUG_GRADE_ALPHAWARE = AugmentationGrade('Alphaware', cost=1.2, avail=2, essence=0.8, default=True)
AUG_GRADE_BETAWARE = AugmentationGrade('Betaware', cost=1.5, avail=4, essence=0.7)
AUG_GRADE_DELTAWARE = AugmentationGrade('Deltaware', cost=2.5, avail=8, essence=0.5)
AUG_GRADE_USED = AugmentationGrade('Used', cost=0.75, avail=-4, essence=1.25)

AUG_GRADES = [i for i in AugmentationGrade.items]
"""
    PRIORITY TABLE
"""
PRIORITY_TABLE = { 
    'A': { 'Metatype': [(HUMAN, 9), (ELF, 8), (DWARF, 7), (ORK, 7), (TROLL, 5)], 'Attributes': 24, 'MagicResonance': { 'Magician or Mystic Adept': { 'Magic': 6, 'Skills': {'Type': 'Magic', 'Rating': 5, 'Quantity': 2 }, 'Spells': 10 }, 'Technomancer': { 'Resonance': 6, 'Skills': {'Type': 'Resonance', 'Rating': 5, 'Quantity': 2 }, 'Complex Forms': 5 } }, 'Skills': [46, 10], 'Money': 450_000 },
    'B': { 'Metatype': [(HUMAN, 7), (ELF, 6), (DWARF, 4), (ORK, 4), (TROLL, 0)], 'Attributes': 20, 'MagicResonance':{ 'Magician or Mystic Adept': { 'Magic': 6, 'Skills': {'Type': 'Magic', 'Rating': 4, 'Quantity': 2}, 'Spells': 7 }, 'Technomancer': { 'Resonance': 4, 'Skills': {'Type': 'Resonance', 'Rating': 4, 'Quantity': 2}, 'Complex Forms': 2 }, 'Adept': { 'Magic': 6, 'Skills': {'Type': 'Active', 'Rating': 4, 'Quantity': 1}}, 'Aspected Magician': { 'Magic': 5, 'Skills': {'Type': 'Magic Group', 'Rating': 4, 'Quantity': 1}} }, 'Skills': [36, 5], 'Money': 275_000 },
    'C': { 'Metatype': [(HUMAN, 5), (ELF, 3), (DWARF, 1), (ORK, 0)], 'Attributes': 16, 'MagicResonance': { 'Magician or Mystic Adept': { 'Magic': 3, 'Spells': 5}, 'Technomancer': { 'Resonance': 3, 'Complex Forms': 1}, 'Adept': { 'Magic': 4, 'Skills': {'Type': 'Active', 'Rating': 2, 'Quantity': 1}}, 'Aspected Magician': { 'Magic': 3, 'Skills': {'Type': 'Magic Group', 'Rating': 2, 'Quantity': 1}} }, 'Skills': [28,2], 'Money': 140_000 },
    'D': { 'Metatype': [(HUMAN, 3), (ELF, 0)], 'Attributes': 14, 'MagicResonance': { 'Adept': {'Magic': 2}, 'Aspected Magician': {'Magic': 2} }, 'Skills': [22, 0], 'Money': 50_000 },
    'E': { 'Metatype': [(HUMAN, 1)], 'Attributes': 12, 'Skills': [18, 0], 'Money': 6_000 }
}
PRIORITY_TABLE_FLIPPED = {
    'Metatype': {
        'A': [(HUMAN, 9), (ELF, 8), (DWARF, 7), (ORK, 7), (TROLL, 5)],
        'B': [(HUMAN, 7), (ELF, 6), (DWARF, 4), (ORK, 4), (TROLL, 0)],
        'C': [(HUMAN, 5), (ELF, 3), (DWARF, 1), (ORK, 0)],
        'D': [(HUMAN, 3), (ELF, 0)],
        'E': [(HUMAN, 1)]
    },
    'Attributes': { 'A': 24, 'B': 20, 'C': 16, 'D': 14, 'E': 12 },
    'MagicResonance': {
        'A': {
            'Magician' : { 'Magic': 6, 'Skills': {'Type': 'Magic', 'Rating': 5, 'Quantity': 2 }, 'Spells': 10 },
            'Mystic Adept': { 'Magic': 6, 'Skills': {'Type': 'Magic', 'Rating': 5, 'Quantity': 2 }, 'Spells': 10 },
            'Technomancer': { 'Resonance': 6, 'Skills': {'Type': 'Resonance', 'Rating': 5, 'Quantity': 2 }, 'Complex Forms': 5 } 
        },
        'B': {
            'Magician': { 'Magic': 6, 'Skills': {'Type': 'Magic', 'Rating': 4, 'Quantity': 2}, 'Spells': 7 },
            'Mystic Adept': { 'Magic': 6, 'Skills': {'Type': 'Magic', 'Rating': 4, 'Quantity': 2}, 'Spells': 7 },
            'Technomancer': { 'Resonance': 4, 'Skills': {'Type': 'Resonance', 'Rating': 4, 'Quantity': 2}, 'Complex Forms': 2 },
            'Adept': { 'Magic': 6, 'Skills': {'Type': 'Active', 'Rating': 4, 'Quantity': 1}},
            'Aspected Magician': { 'Magic': 5, 'Skills': {'Type': 'Magic Group', 'Rating': 4, 'Quantity': 1}}
        },
        'C': {
            'Magician':{ 'Magic': 3, 'Spells': 5},
            'Mystic Adept': { 'Magic': 3, 'Spells': 5},
            'Technomancer': { 'Resonance': 3, 'Complex Forms': 1},
            'Adept': { 'Magic': 4, 'Skills': {'Type': 'Active', 'Rating': 2, 'Quantity': 1}},
            'Aspected Magician': { 'Magic': 3, 'Skills': {'Type': 'Magic Group', 'Rating': 2, 'Quantity': 1}}
        },
        'D': {
            'Adept': {'Magic': 2},
            'Aspected Magician': {'Magic': 2}
        },
        'E': None
    },
    'Skills': {
        'A': [46, 10],
        'B': [36, 5],
        'C': [28, 2],
        'D': [22, 0],
        'E': [18, 0]
    },
    'Resources': {
        'A': 450_000,
        'B': 275_000,
        'C': 140_000,
        'D': 50_000,
        'E': 6_000
    }
}

def refresh_priority_table():
    PRIORITY_TABLE_FLIPPED['Metatype'] = {
        'A': [(HUMAN, 9), (ELF, 8), (DWARF, 7), (ORK, 7), (TROLL, 5)],
        'B': [(HUMAN, 7), (ELF, 6), (DWARF, 4), (ORK, 4), (TROLL, 0)],
        'C': [(HUMAN, 5), (ELF, 3), (DWARF, 1), (ORK, 0)],
        'D': [(HUMAN, 3), (ELF, 0)],
        'E': [(HUMAN, 1)]
    }
    PRIORITY_TABLE_FLIPPED['Attributes'] = { 'A': 24, 'B': 20, 'C': 16, 'D': 14, 'E': 12 }
    PRIORITY_TABLE_FLIPPED['MagicResonance'] = {
        'A': {
            'Magician': {
                'Magic': 6,
                'Skills': {'Type': 'Magic', 'Rating': 5, 'Quantity': 2 },
                'Spells': 10 },
            'Mystic Adept': {
                'Magic': 6,
                'Skills': {'Type': 'Magic', 'Rating': 5, 'Quantity': 2 },
                'Spells': 10 },
            'Technomancer': {
                'Resonance': 6,
                'Skills': {'Type': 'Resonance', 'Rating': 5, 'Quantity': 2 },
                'Complex Forms': 5 } 
        },
        'B': {
            'Magician': {
                'Magic': 6,
                'Skills': {'Type': 'Magic', 'Rating': 4, 'Quantity': 2},
                'Spells': 7 },
            'Mystic Adept': {
                'Magic': 6,
                'Skills': {'Type': 'Magic', 'Rating': 4, 'Quantity': 2},
                'Spells': 7 },
            'Technomancer': {
                'Resonance': 4,
                'Skills': {'Type': 'Resonance', 'Rating': 4, 'Quantity': 2},
                'Complex Forms': 2 },
            'Adept': {
                'Magic': 6,
                'Skills': {'Type': 'Active', 'Rating': 4, 'Quantity': 1}},
            'Aspected Magician': {
                'Magic': 5,
                'Skills': {'Type': 'Magic Group', 'Rating': 4, 'Quantity': 1}}
        },
        'C': {
            'Magician': { 'Magic': 3, 'Spells': 5},
            'Mystic Adept': { 'Magic': 3, 'Spells': 5},
            'Technomancer': { 'Resonance': 3, 'Complex Forms': 1},
            'Adept': { 'Magic': 4, 'Skills': {'Type': 'Active', 'Rating': 2, 'Quantity': 1}},
            'Aspected Magician': { 'Magic': 3, 'Skills': {'Type': 'Magic Group', 'Rating': 2, 'Quantity': 1}}
        },
        'D': {
            'Adept': {'Magic': 2},
            'Aspected Magician': {'Magic': 2}
        },
        'E': None
    }
    PRIORITY_TABLE_FLIPPED['Skills'] = {
        'A': [46, 10],
        'B': [36, 5],
        'C': [28, 2],
        'D': [22, 0],
        'E': [18, 0]
    }
    PRIORITY_TABLE_FLIPPED['Resources'] = {
        'A': 450_000,
        'B': 275_000,
        'C': 140_000,
        'D': 50_000,
        'E': 6_000
    }
