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


class Skill(AbstractBaseClass):
    items = []
    def __init__(self, name, attribute, skill_type, **kwargs):
        super().__init__(name, **kwargs)
        Skill.items.append(self)
        self.attribute = attribute
        self.skill_type = skill_type
        self.rating = 0
        self.group = False

    def __repr__(self):
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
ESCAPE_ARTIST = Skill("Escape_artist", AGILITY, "Active", spec=['Cuffs (Restraint)', 'Ropes (Restraint)', 'Zip Ties (Restraint)', 'Contortionism'])
EXOTIC_MELEE_WEAPON = Skill("Exotic_melee_weapon", AGILITY, "Active", specs=None)
EXOTIC_RANGED_WEAPON = Skill("Exotic_ranged_weapon", AGILITY, "Active", specs=None)
GUNNERY = Skill("Gunnery", AGILITY, "Active", spec=['Artillery', 'Ballistic', 'Energy', 'Guided Missile', 'Rocket'])
GYMNASTICS = Skill("Gymnastics", AGILITY, "Active", spec=['Balance', 'Climbing', 'Dance', 'Leaping', 'Parkour', 'Rolling'])
HEAVY_WEAPONS = Skill("Heavy_weapons", AGILITY, "Active", spec=['Assault Cannons', 'Grenade Launchers', 'Guided Missiles', 'Machine Guns', 'Rocket Launchers'])
LOCKSMITH = Skill("Locksmith", AGILITY, "Active", spec=['Combination', 'Keypad', 'Maglock', 'Tumbler', 'Voice Recognition'])
LONGARMS = Skill("Longarms", AGILITY, "Active", spec=['Extended-Range Shots', 'Long-Range Shots', 'Shotguns', 'Sniper Rifles'])
PALMING = Skill("Palming", AGILITY, "Active", spec=['Ledgerdemain', 'Pickpocket', 'Pilfering'])
PISTOLS = Skill("Pistols", AGILITY, "Active", spec=['Holdouts', 'Revolvers', 'Semi-Automatics', 'Tasers'])
SNEAKING = Skill("Sneaking", AGILITY, "Active", spec=['Jungle Stealth', 'Urban Stealth', 'Desert Stealth'])
THROWING_WEAPONS = Skill("Throwing Weapons", AGILITY, "Active", spec=['Aerodynamic', 'Blades', 'Non-Aerodynamic'])
UNARMED_COMBAT = Skill("Unarmed_combat", AGILITY, "Active", spec=['Blocking', 'Cyber Implants', 'Subduing Combat', 'A Martial Art'])
# =============== BODY ===================
DIVING = Skill("Diving", BODY, "Active", spec=['Liquid Breathing Apparatus', 'Mixed Gas Breathing Apparatus', 'Oxygen Extraction Breathing Apparatus', 'SCUBA', 'Artic Diving', 'Cave Diving', 'Commercial Diving', 'Military Diving', 'Controlled Hyperventillation'])
FREE_FALL = Skill("Free_fall", BODY, "Active", spec=['BASE Jumping', 'Break-Fall', 'Bungee', 'HALO', 'Low Altitude', 'Parachute', 'Static Line', 'Wingsuit', 'Zipline'])
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
ANIMAL_HANDLING = Skill("Animal_Handling", CHARISMA, "Active", spec=['Herding', 'Riding', 'Training', 'Cat Handling', 'Bird Handling', 'Hell Hound Handling', 'Horse Handling', 'Dolphin Handling'])
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
ACADEMIC_KNOWLEDGE = Skill("Academic_Knowledge", LOGIC, "Active")
AERONAUTICS_MECHANIC = Skill("Aeronautics_Mechanic", LOGIC, "Active", spec=['Aerospace', 'Fixed Wing', 'LTA (Blimp)', 'Rotary Wing', 'Tilt Wing', 'Vectored Thrust'])
ARCANA = Skill("Arcana", LOGIC, "Active", spec=['Spell Design', 'Focus Design', 'Spirit Formula'])
ARMORER = Skill("Armorer", LOGIC, "Active", spec=['Armor', 'Artillery', 'Explosives', 'Firearms', 'Melee Weapons', 'Heavy Weapons', 'Weapon Accessories'])
AUTOMOTIVE_MECHANIC = Skill("Automotive_Mechanic", LOGIC, "Active", spec=['Walker', 'Hover', 'Tracked', 'Wheeled'])
BIOTECHNOLOGY = Skill("Biotechnology", LOGIC, "Active", spec=['Bioinformatics', 'Bioware', 'Cloning', 'Gene Therapy', 'Vat Maintenance'])
CHEMISTRY = Skill("Chemistry", LOGIC, "Active", spec=['Analytical', 'Biochemestry', 'Inorganic', 'Organic', 'Physical'])
COMPUTER = Skill("Computer", LOGIC, "Active", spec=['File Editing', 'Matrix Perception', 'Matrix Search'])
CYBERCOMBAT = Skill("Cybercombat", LOGIC, "Active", spec=['Devices', 'Grids', 'IC', 'Personas', 'Sprites'])
CYBERTECHNOLOGY = Skill("Cybertechnology", LOGIC, "Active", spec=['Bodyware', 'Cyberlimbs', 'Headware', 'Repair'])
DEMOLITIONS = Skill("Demolitions", LOGIC, "Active", spec=['Commercial Explosives', 'Defusing', 'Improvised Explosives', 'Plastic Explosives'])
ELECTRONIC_WARFARE = Skill("Electronic_Warfare", LOGIC, "Active", spec=['Communications', 'Encryption', 'Jamming', 'Sensor Operations'])
FIRST_AID = Skill("First_Aid", LOGIC, "Active", spec=['Gunshot Wounds', 'Resuscitation', 'Broken Bones', 'Burns'])
FORGERY = Skill("Forgery", LOGIC, "Active", spec=['Counterfeiting', 'Credstick Forgery', 'False ID', 'Image Doctoring', 'Paper Forgery'])
HACKING = Skill("Hacking", LOGIC, "Active", spec=['Devices', 'Files', 'Hosts', 'Personas'])
HARDWARE = Skill("Hardware", LOGIC, "Active", spec=['Commlinks', 'Cyberdecks', 'Smartguns'])
INDUSTRIAL_MECHANIC = Skill("Industrial_Mechanic", LOGIC, "Active", spec=['Electrical Power Systems', 'Hydraulics', 'HVAC', 'Industrial Robotics', 'Structural', 'Welding'])
MEDICINE = Skill("Medicine", LOGIC, "Active", spec=['Cosmetic Surgery', 'Extended Care', 'Implant Surgery', 'Magical Health', 'Organ Culture', 'Trama Surgery'])
NAUTICAL_MECHANIC = Skill("Nautical_Mechanic", LOGIC, "Active", spec=['Motorboat', 'Sailboat', 'Ship', 'Submarine'])
PROFESSIONAL_KNOWLEDGE = Skill("Professional_Knowledge", LOGIC, "Active")
SOFTWARE = Skill("Software", LOGIC, "Active", spec=['Data Bombs', 'Editor Complex Form', 'Resonance Spike Complex Form', 'Tattletale Complex Form'])
# =============== WILLPOWER ==============
ASTRAL_COMBAT = Skill("Astral Combat", WILLPOWER, "Active", spec=['Specific Focus Type', 'Against Magicians', 'Against Spirits', 'Against Mana Barriers'])
SURVIVAL = Skill("Survival", WILLPOWER, "Active", spec=['Desert Survival', 'Forest Survival', 'Jungle Survival', 'Mountain Survival', 'Polar Survival', 'Urban Survival'])
# =============== MAGIC ==================
ALCHEMY = Skill("Alchemy", MAGIC, "Active", spec=['Command Trigger', 'Contact Trigger', 'Time Trigger', 'Combat Spells', 'Detection Spells'])
ARTIFICING = Skill("Artificing", MAGIC, "Active", spec=['Focus Analysis', 'Spell Crafting', 'Spirit Crafting', 'Power Crafting', 'Weapon Crafting', 'Qi Crafting', 'Metamagic Crafting', 'Qi Force Crafting'])
BANISHING = Skill("Banishing", MAGIC, "Active", spec=['Spirits of Air', 'Spirits of Earth', 'Spiriths of Beasts', 'Spirits of Fire', 'Spirits of Main', 'Spirits Water'])
BINDING = Skill("Binding", MAGIC, "Active", spec=['Spiritss of Air', 'Spirits of Earth', 'Spiriths of Beasts', 'Spirits of Fire', 'Spirits of Main', 'Spirits Water'])
COUNTERSPELLING = Skill("Counterspelling", MAGIC, "Active", spec=['Spell Type'])
DISENCHANTING = Skill("Disenchanting", MAGIC, "Active", spec=['Alchemical Preparations', 'Power', 'Foci'])
RITUAL_SPELLCASTING = Skill("Ritual Spellcasting", MAGIC, "Active", spec=['Keyword', 'Anchored', 'Spell'])
SPELLCASTING = Skill("Spellcasting", MAGIC, "Active", spec=['Spell Type'])
SUMMONING = Skill("Summoning", MAGIC, "Active", spec=['Spirit of Air', 'Spirit of Earth', 'Spirith of Beasts', 'Spirit of Fire', 'Spirits of Main', 'Spirits Water'])
# =============== RESONANCE ==============
COMPILING = Skill("Compiling", RESONANCE, "Active", spec=['Sprite Type'])
DECOMPILING = Skill("Decompiling", RESONANCE, "Active", spec=['Sprite Type'])
REGISTERING = Skill("Registering", RESONANCE, "Active", spec=['Sprite Type'])

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
VEHICLE_SKILLS = [GUNNERY, PILOT_AEROSPACE, PILOT_AIRCRAFT, PILOT_GROUND_CRAFT, PILOT_EXOTIC_VEHICLE_SPECIFIC, PILOT_WALKER, PILOT_WATERCRAFT]

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
NATURAL_IMMUNITY = Quality('Natural Immunity', cost=[4, "or", 10], page_ref=76)
PHOTOGRAPHIC_MEMORY = Quality('Photographic Memory', cost=6, page_ref=76)
QUICK_HEALER = Quality('Quick Healer', cost=3, page_ref=77)
RESISTANCE_TO_PATHOGENS_TOXINS = Quality('Resistance to Pathogens/Toxins', cost=[4, "or", 8], page_ref=78)
SPIRIT_AFFINITY = Quality('Spirit Affinity', cost=7, page_ref=78, opts=['Spirits of Air', 'Spirits of Earth', 'Spirits of Beast', 'Spirits of Fire', 'Spirits of Man', 'Spirits of Water'])
TOUGHNESS = Quality('Toughness', cost=9, page_ref=78)
WILL_TO_LIVE = Quality('Will to Live', cost=3, page_ref=78, quantity=4)
# NEGATIVE QUALITIES
ADDICTION = Quality('Addiction', cost=[4, "to", 25], page_ref=77, negative=True, opts={'Types': ['Better than Life Chips', 'Alchemical Preparations', 'Alcohol', 'Street Drugs', 'Foci', 'Augmentations'], 'Severity': {'Mild': 4, 'Moderate': 9, 'Severe': 20, 'Burnout': 25}})
ALLERGY = Quality('Allergy', cost=[5, "to", 25], page_ref=78, negative=True, opts={'Rarity': {'Uncommon': 2, 'Common': 7}, 'Severity': {'Mild': 3, 'Moderate': 8, 'Severe': 13, 'Extreme': 18}})
ASTRAL_BEACON = Quality('Astral Beacon', cost=10, page_ref=78, negative=True)
BAD_LUCK = Quality('Bad Luck', cost=12, page_ref=78, negative=True)
BAD_REP = Quality('Bad Rep', cost=7, page_ref=79, negative=True)
CODE_OF_HONOR = Quality('Code of Honor', cost=15, page_ref=79, negative=True, opts=['Assassin\'s Creed', 'Warriors Code'])
CODEBLOCK = Quality('Codeblock', cost=10, page_ref=80, negative=True)
COMBAT_PARALYSIS = Quality('Combat Paralysis', cost=12, page_ref=80, negative=True)
DEPENDANTS = Quality('Dependants', cost=(3, 6, 9), page_ref=80, negative=True, opts=['Occasional Nuisance', 'Regular Inconvinence', 'Close Family or Life Partner'])
DISTINCTIVE_STYLE = Quality('Distinctive Style', cost=5, page_ref=80, negative=True)
ELF_POSER = Quality('Elf Poser', cost=6, page_ref=81, negative=True)
GREMLINS = Quality('Gremlins', cost=4, page_ref=81, negative=True, quantity=4)
INCOMPETENT = Quality('Incompetent', cost=5, page_ref=81, negative=True)
INSOMNIA = Quality('Insomnia', cost=[10, "or", 15], page_ref=81, negative=True)
LOSS_OF_CONFIDENCE = Quality('Loss of Confidence', cost=10, page_ref=82, negative=True)
LOW_PAIN_TOLERANCE = Quality('Low Pain Tolerance', cost=9, page_ref=82, negative=True)
ORK_POSER = Quality('Ork Poser', cost=6, page_ref=82, negative=True)
PREJUDICED = Quality('Prejudiced', cost=[3, "to", 10], page_ref=82, negative=True, opts={'Rarity': {'Common Target Group': 5, 'Specific Target Group': 3}, 'Severity': {'Biased': 0, 'Outspoken': 2, 'Radical': 5}})
SCORCHED = Quality('Scorched', cost=10, page_ref=83, negative=True)
SENSITIVE_SYSTEM = Quality('Sensitive System', cost=12, page_ref=83, negative=True)
SIMSENSE_VERTIGO = Quality('Simsense Vertigo', cost=5, page_ref=83, negative=True)
SINNER_LAYERED = Quality('SINner (Layered)', cost=[5, "to", 25], page_ref=84, negative=True, opts=['National Sin', 'Criminal Sin', 'Corporate Limited Sin', 'Corporate Sin'])
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
COMBAT_AXE = MeleeWeapon("Combat_Axe", cost=4000, page_ref=421, avail=[12, RESTRICTED], subtype="Blade")
COMBAT_KNIFE = MeleeWeapon("Combat_Knife", cost=300, page_ref=421, avail=4, subtype="Blade")
FOREARM_SNAP_BLADES = MeleeWeapon("Forearm_Snap_Blades", cost=200, page_ref=421, avail=[7, RESTRICTED], subtype="Blade")
KATANA = MeleeWeapon("Katana", cost=1000, page_ref=421, avail=[9, RESTRICTED], subtype="Blade")
KNIFE = MeleeWeapon("Knife", cost=10, page_ref=421, avail="-", subtype="Blade")
POLE_ARM = MeleeWeapon("Pole_Arm", cost=1000, page_ref=421, avail=[6, RESTRICTED], subtype="Blade")
SURVIVAL_KNIFE = MeleeWeapon("Survival_Knife", cost=100, page_ref=421, avail="-", subtype="Blade")
SWORD = MeleeWeapon("Sword", cost=500, page_ref=421, avail=[5, RESTRICTED], subtype="Blade")
# =============== CLUBS =================
CLUB = MeleeWeapon("Club", cost=30, page_ref=421, avail="-", subtype="Club")
EXTENDABLE_BATON = MeleeWeapon("Extendable_Baton", cost=100, page_ref=421, avail=4, subtype="Club")
SAP = MeleeWeapon("Sap", cost=30, page_ref=421, avail=2, subtype="Club")
STAFF = MeleeWeapon("Staff", cost=100, page_ref=421, avail=3, subtype="Club")
STUN_BATON = MeleeWeapon("Stun_Baton", cost=750, page_ref=421, avail=[6, RESTRICTED], subtype="Club")
TELESCOPING_STAFF = MeleeWeapon("Telescoping_Staff", cost=350, page_ref=421, avail=4, subtype="Club")
# =============== OTHER =================
KNUCKS = MeleeWeapon("Knucks", cost=100, page_ref=421, avail=[2, RESTRICTED], subtype="Other")
MONOFILAMENT_WHIP = MeleeWeapon("Monofilament_Whip", cost=10_000, page_ref=421, avail=[12, FORBIDDEN], subtype="Other")
SHOCK_GLOVES = MeleeWeapon("Shock_Gloves", cost=550, page_ref=421, avail=[6, RESTRICTED], subtype="Other")

"""
    PROJECTILE GEAR
"""
# =============== BOWS ==================
BOW = ProjectileWeapon("Bow", cost=["Rating", "*", 100], page_ref=421, avail="Rating", rating=[1, "to", 6], subtype="Bows")
ARROW = ProjectileWeapon("Arrow", cost=["Rating", "*", 2], page_ref=421, avail="Rating", rating=[1, "to", 6], subtype="Bows", requires=BOW)
INJECTION_ARROW = ProjectileWeapon("Injection_Arrow", cost=["Rating", "*", 20], page_ref=421, avail=[["Rating", "+", 2], RESTRICTED], rating=[1, "to", 6], subtype="Bows", requires=BOW)
# =============== CROSSBOWS =============
LIGHT_CROSSBOW = ProjectileWeapon("Light_Crossbow", cost=300, page_ref=421, avail=2, subtype="Crossbow")
MEDIUM_CROSSBOW = ProjectileWeapon("Medium_Crossbow", cost=300, page_ref=421, avail=2, subtype="Crossbow")
HEAVY_CROSSBOW = ProjectileWeapon("Heavy_Crossbow", cost=300, page_ref=421, avail=2, subtype="Crossbow")
CROSSBOW_BOLT = ProjectileWeapon("Crossbow_Bolt", cost=5, page_ref=421, avail=2, subtype="Crossbow", requires=(LIGHT_CROSSBOW, MEDIUM_CROSSBOW, HEAVY_CROSSBOW))
INJECTION_BOLT = ProjectileWeapon("Injection_Bolt", cost=50, page_ref=421, avail=[8, RESTRICTED], subtype="Crossbow", requires=(LIGHT_CROSSBOW, MEDIUM_CROSSBOW, HEAVY_CROSSBOW))
# =============== THROWING ==============
THROWING_KNIFE = ProjectileWeapon("Throwing Knife", cost=25, page_ref=424, avail=4, subtype="Throwing Weapons")

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
AIRBURST_LINK = FirearmAccessory("Airburst_Link", cost=600, page_ref=432, mount="", avail=[6, RESTRICTED], requires=["Category", "Firearm"])
BIPOD = FirearmAccessory("Bipod", cost=200, page_ref=432, mount="", avail=2, requires=["Category", "Firearm"])
CONCEALABLE_HOLSTER = FirearmAccessory("Concealable_Holster", cost=150, page_ref=432, mount="", avail=2, requires=["Category", "Firearm"])
GAS_VENT_SYSTEM = FirearmAccessory("Gas_Vent_System", cost=["Rating", "*", 200], page_ref=432, mount="", avail=[(3, "Rating"), RESTRICTED], requires=["Category", "Firearm"])
GYRO_MOUNT = FirearmAccessory("Gyro_Mount", cost=1400, page_ref=432, mount="", avail=7, requires=["Category", "Firearm"])
HIDDEN_ARM_SLIDE = FirearmAccessory("Hidden_Arm_Slide", cost=350, page_ref=432, mount="", avail=[4,RESTRICTED], requires=["Category", "Firearm"])
IMAGING_SCOPE = FirearmAccessory("Imaging_Scope", cost=300, page_ref=432, mount="", avail=2, requires=["Category", "Firearm"])
LASER_SIGHT = FirearmAccessory("Laser_Sight", cost=125, page_ref=432, mount="", avail=2, requires=["Category", "Firearm"])
PERISCOPE = FirearmAccessory("Periscope", cost=70, page_ref=432, mount="", avail=3, requires=["Category", "Firearm"])
QUICK_DRAW_HOLSTER = FirearmAccessory("Quick_Draw_Holster", cost=175, page_ref=432, mount="", avail=4, requires=["Category", "Firearm"])
SHOCK_PAD = FirearmAccessory("Shock_Pad", cost=50, page_ref=432, mount="", avail=2, requires=["Category", "Firearm"])
SILENCER_SUPPRESSOR = FirearmAccessory("Silencer_Suppressor", cost=500, page_ref=432, mount="", avail=[9, FORBIDDEN], requires=["Category", "Firearm"])
SMART_FIRING_PLATFORM = FirearmAccessory("Smart_Firing_Platform", cost=2_500, page_ref=432, mount="", avail=[12, FORBIDDEN], requires=["Category", "Firearm"])
SMARTGUN_SYSTEM_INTERNAL = FirearmAccessory("Smartgun_System_Internal", cost=["WeaponCost", "*", 2], page_ref=432, mount="", avail=[2, RESTRICTED], requires=["Category", "Firearm"])
SMARTGUN_SYSTEM_EXTERNAL = FirearmAccessory("Smartgun_System_External", cost=200, page_ref=432, mount="", avail=[4, RESTRICTED], requires=["Category", "Firearm"])
SPARE_CLIP = FirearmAccessory("Spare_Clip", cost=5, page_ref=432, mount="", avail=4, requires=["Category", "Firearm"])
SPEED_LOADER = FirearmAccessory("Speed_Loader", cost=25, page_ref=432, mount="", avail=2, requires=["Category", "Firearm"])
TRIPOD = FirearmAccessory("Tripod", cost=500, page_ref=432, mount="", avail=4, requires=["Category", "Firearm"])

"""
    INDUSTRIAL CHEMICALS
    No I don't know why this gets its own chapter in the book either
"""
GLUE_SOLVENT = Item("Glue_Solvent", cost=90, page_ref=448, avail=2, category="Industrial Chemicals")
GLUE_SPRAYER= Item("Glue_Sprayer", cost=150, page_ref=448, avail=2, category="Industrial Chemicals")
THERMITE_BURNING_BAR = Item("Thermite_Burning_Bar", cost=500, page_ref=448, avail=[16, RESTRICTED], category="Industrial Chemicals")

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
GAS_GRENADE = Ammo("Gas Grenade", cost=["WeaponCost", "+", 40], page_ref=434, avail=[[2, "Chemical Availability"], RESTRICTED], subtype="Grenade", requires=["Category", "Industrial Chemicals"])
SMOKE_GRENADE = Ammo("Smoke", cost=40, page_ref=434, avail=[4, RESTRICTED], subtype="Grenade")
THERMAL_SMOKE = Ammo("Thermal Smoke", cost=60, page_ref=434, avail=[6, RESTRICTED], subtype="Grenade")
# =============== MISSILES ==============
ANTI_VEHICLE = Ammo("Anti_Vehicle", cost=2800, page_ref=435, avail=[18, FORBIDDEN], subtype="Missile")
FRAGMENTATION_MISSLE = Ammo("Fragmentation_Missle", cost=2000, page_ref=435, avail=[12, FORBIDDEN], subtype="Missile")
HIGH_EXPLOSIVE_MISSLE = Ammo("High_Explosive_Missle", cost=2100, page_ref=435, avail=[18, FORBIDDEN], subtype="Missile")
# =============== ROCKETS ==============
# ANTI_VEHICLE_ROCKET = Ammo("Anti_Vehicle_Rocket", cost=[2800, "+", ("Sensor Rating", 500)], page_ref=435, avail=[18, FORBIDDEN], subtype="Rocket", requires=ANTI_VEHICLE)
# FRAGMENTATION_ROCKET = Ammo("Fragmentation_Rocket", cost=[2000, "+", ("Sensor Rating", 500)], page_ref=435, avail=[12, FORBIDDEN], subtype="Rocket", requires=FRAGMENTATION_MISSLE)
# HIGH_EXPLOSIVE_ROCKET = Ammo("High_Explosive_Rocket", cost=[2100, "+", ("Sensor Rating", 500)], page_ref=435, avail=[18, FORBIDDEN], subtype="Rocket", requires=HIGH_EXPLOSIVE_MISSLE)

"""
    EXPLOSIVES
"""
COMMERCIAL_EXPLOSIVES = Item("Commercial_Explosives", cost=100, page_ref=436, rating=5, avail=[8, RESTRICTED], category="Explosives")
FOAM_EXPLOSIVES = Item("Foam_Explosives", cost=["Rating", "*", 100], page_ref=436, rating=[6, "to", 25], avail=[12, FORBIDDEN], category="Explosives")
PLASTIC_EXPLOSIVES = Item("Plastic_Explosives", cost=["Rating", "*", 100], page_ref=436, rating=[6, "to", 25], avail=[16, FORBIDDEN], category="Explosives")
DETONATOR_CAP = Item("Detonator Cap", cost=75, page_ref=436, rating="-", avail=[8, RESTRICTED], category="Explosives")

"""
    CLOTHING/ARMOR
"""
# =============== CLOTHING ==============
CLOTHING = Clothing("Clothing", cost=["Range", 20, 100_000], page_ref=436, avail="-", armor_rating=0)
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
CHEMICAL_PROTECTION = ArmorModification("Chemical Protection", cost=["Rating", "*", 250], page_ref=438, avail=6, capacity="Rating", requires=["Category", "Armor"])
CHEMICAL_SEAL = ArmorModification("Chemical Seal", cost=3000, page_ref=438, avail=[12, RESTRICTED], capacity=6, requires=["Category", "Armor"])
FIRE_RESISTANCE = ArmorModification("Fire Resistance", cost=["Rating", "*", 250], page_ref=438, avail=6, capacity="Rating", requires=["Category", "Armor"])
INSULATION = ArmorModification("Insulation", cost=["Rating", "*", 250], page_ref=438, avail=6, capacity="Rating", requires=["Category", "Armor"])
NONCONDUCTIVITY = ArmorModification("Nonconductivity", cost=["Rating", "*", 250], page_ref=438, avail=6, capacity="Rating", requires=["Category", "Armor"])
SHOCK_FRILLS = ArmorModification("Shock Frills", cost=250, page_ref=438, avail=[6, RESTRICTED], capacity=2, requires=["Category", "Armor"])
THERMAL_DAMPING = ArmorModification("Thermal Damping", cost=["Rating", "*", 500], page_ref=438, avail=[10, RESTRICTED], capacity="Rating", requires=["Category", "Armor"])

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
SIM_MODULE = Electronics("Sim Module", cost=100, page_ref=439, rating="-", avail="-", subtype="Commlink_", requires=["Subtype", "Commlink"])
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
LOW_LIGHT_VISION = Electronics("Low_Light_Vision", cost=500, page_ref=444, rating="-", avail=4, capacity=1, subtype="Vision Enhancement", requires=Electronics)
FLARE_COMPENSATION = Electronics("Flare_Compensation", cost=250, page_ref=444, rating="-", avail=1, capacity=1, subtype="Vision Enhancement", requires=Electronics)
IMAGE_LINK = Electronics("Image_Link", cost=25, page_ref=444, rating="-", avail="-", capacity=1, subtype="Vision Enhancement", requires=Electronics)
SMARTLINK = Electronics("Smartlink", cost=2000, page_ref=444, rating="-", avail=[4, RESTRICTED], capacity=1, subtype="Vision Enhancement", requires=Electronics)
THERMOGRAPHIC_VISION = Electronics("Thermographic_Vision", cost=500, page_ref=444, rating="-", avail=6, capacity=1, subtype="Vision Enhancement", requires=Electronics)
VISION_ENHANCEMENT = Electronics("Vision_Enhancement", cost=["Rating", "*", 500], page_ref=444, rating="-", avail=[["Rating", "*", 2], 0], capacity="Rating", subtype="Vision Enhancement", requires=Electronics)
VISION_MAGNIFICATION = Electronics("Vision_Magnification", cost=250, page_ref=444, rating="-", avail=2, capacity=1, subtype="Vision Enhancement", requires=Electronics)
# =============== AUDIO DEVICES=======
DIRECTIONAL_MIC = Electronics("Directional_Mic", cost=["Capacity", "*", 50], page_ref=445, rating="-", avail=4, capacity=[1, "to", 6], subtype="Audio Device")
EAR_BUDS = Electronics("Ear_Buds", cost=["Capacity", "*", 50], page_ref=445, rating="-", avail="-", capacity=[1, "to", 3], subtype="Audio Device")
HEADPHONES = Electronics("Headphones", cost=["Capacity", "*", 50], page_ref=445, rating="-", avail="-", capacity=[1, "to", 6], subtype="Audio Device")
LASER_MIC = Electronics("Laser_Mic", cost=["Capacity", "*", 100], page_ref=445, rating="-", avail=[6, RESTRICTED], capacity=[1, "to", 6], subtype="Audio Device")
OMNI_DIRECTIONAL_MIC = Electronics("Omni_Directional_Mic", cost=["Capacity", "*", 50], page_ref=445, rating="-", avail="-", capacity=[1, "to", 6], subtype="Audio Device")
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

Edit from months later: Just gonna bodge the sensor functions as their own dict, with the sensor function as the key and it's range as the value.
    Then gonna add a custom arg to randomly pull one of those sensor functions from whatever kind of sensor/sensor housing gets rolled
"""
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
HANDHELD_HOUSING = Electronics("Handheld Housing", cost=["Capacity", "*", 100], page_ref=445, rating=[1, "to", 3], avail="-", capacity=[1, "to", 3], housing=[{k:d} for k, d in SENSOR_HOUSINGS.items() if d <= 3], sensor_function=SENSOR_FUNCTIONS, subtype="Sensors")
WALL_MOUNTED_HOUSING = Electronics("Wall-Mounted Housing", cost=["Capacity", "*", 250], page_ref=445, rating=[1, "to", 4], avail="-", capacity=[1, "to", 6], housing=[{k:d} for k, d in SENSOR_HOUSINGS.items() if d <= 4], sensor_function=SENSOR_FUNCTIONS, subtype="Sensors")
SENSOR_ARRAY = Electronics("Sensor Array", cost=["Rating", "*", 1000], page_ref=445, rating=[2, "to", 8], avail="-", capacity=6, housing=SENSOR_HOUSINGS, sensor_function=SENSOR_FUNCTIONS, subtype="Sensors")
SINGLE_SENSOR = Electronics("Single Sensor", cost=["Rating", "*", 100], page_ref=445, rating=[2, "to", 8], avail="-", capacity=1, housing=SENSOR_HOUSINGS, sensor_function=SENSOR_FUNCTIONS, subtype="Sensors")
# =============== SECURITY DEVICES====
KEY_COMBINATION_LOCK = Electronics("Key_Combination_Lock", cost=["Rating", "*", 10], page_ref=447, rating=[1, "to", 6], avail="Rating", subtype="Security Device")
MAGLOCK = Electronics("Maglock", cost=["Rating", "*", 100], page_ref=447, rating=[1, "to", 6], avail="Rating", subtype="Security Device")
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
STREET_LIFESTYLE = Lifestyle("Street_Lifestyle", dicestring="1d6", base_amount=20, cost=0)
SQUATTER_LIFESTYLE = Lifestyle("Squatter_Lifestyle", dicestring="2d6", base_amount=40, cost=500)
LOW_LIFESTYLE = Lifestyle("Low_Lifestyle", dicestring="3d6", base_amount=60, cost=2000)
MIDDLE_LIFESTYLE = Lifestyle("Middle_Lifestyle", dicestring="4d6", base_amount=100, cost=5000)
HIGH_LIFESTYLE = Lifestyle("High_Lifestyle", dicestring="5d6", base_amount=500, cost=10_000)
LUXURY_LIFESTYLE = Lifestyle("Luxury_Lifestyle", dicestring="6d6", base_amount=1000, cost=100_000)

"""
    COMPLEX FORMS

    duration:
        Perm -> Permanent
        Sustain -> Sustained
        Imm -> Immediate

    fading_value:
        level + fading_value

"""
CLEANER = ComplexForm("Cleaner", target='Persona', duration='Perm', fading_value=1)
DIFFUSE_OF_ATTACK = ComplexForm("Diffuse_of_attack", target='Device', duration='Sustain', fading_value=1)
DIFFUSE_OF_SLEAZE = ComplexForm("Diffuse_of_sleaze", target='Device', duration='Sustain', fading_value=1)
DIFFUSE_OF_DATA_PROCESSING = ComplexForm("Diffuse_of_data_processing", target='Device', duration='Sustain', fading_value=1)
DIFFUSE_OF_FIREWALL = ComplexForm("Diffuse_of_firewall", target='Device', duration='Sustain', fading_value=1)
EDITOR = ComplexForm("Editor", target='File', duration='Perm', fading_value=2)
INFUSION_OF_ATTACK = ComplexForm("Infusion_of_attack", target='Device', duration='Sustain', fading_value=1)
INFUSION_OF_SLEAZE = ComplexForm("Infusion_of_sleaze", target='Device', duration='Sustain', fading_value=1)
INFUSION_OF_DATA_PROCESSING = ComplexForm("Infusion_of_data_processing", target='Device', duration='Sustain', fading_value=1)
INFUSION_OF_FIREWALL = ComplexForm("Infusion_of_firewall", target='Device', duration='Sustain', fading_value=1)
STATIC_VEIL = ComplexForm("Static_veil", target='Persona', duration='Sustain', fading_value=-1)
PULSE_STORM = ComplexForm("Pulse_storm", target='Persona', duration='Imm', fading_value=0)
PUPPETEER = ComplexForm("Puppeteer", target='Device', duration='Imm', fading_value=4)
RESONANCE_CHANNEL = ComplexForm("Resonance_channel", target='Device', duration='Sustain', fading_value=-1)
RESONANCE_SPIKE = ComplexForm("Resonance_spike", target='Device', duration='Imme', fading_value=0)
RESONANCE_VEIL = ComplexForm("Resonance_veil", target='Device', duration='Sustain', fading_value=-1)
STATIC_BOMB = ComplexForm("Static_bomb", target='Self', duration='Imme', fading_value=2)
STITCHES = ComplexForm("Stitches", target='Sprite', duration='Perm', fading_value=-2)
TRANSCENDENT_GRID = ComplexForm("Transcendent_grid", target='Self', duration='Imme', fading_value=-3)
TATTLETALE = ComplexForm("Tattletale", target='Persona', duration='Perm', fading_value=-2)



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


