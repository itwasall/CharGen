from dataclasses import dataclass, field
import random

@dataclass
class Attribute:
    name: str
    value: int

@dataclass
class Skill:
    name: str
    value: int
    category: str
    specialties: str = field(repr=False)
    specialty: list[str]

# Physical Skills
ATHLETICS = Skill('Athletics', 0, 'Physical', "Acrobatics, Climbing, Endurance, Jumping, Parkour, Swimming, Throwing", [])
BRAWL = Skill('Brawl', 0, 'Physical', "Animals, Armed Humans, Bar Fights, Ceremonial Combat, Grappling, Unarmed Humans", [])
CRAFT = Skill('Craft', 0, 'Physical', "Carpentry, Caern Rites, Design, Painting, Sculpting, Sewing, Weaponsmithing", [])
DRIVING = Skill('Driving', 0, 'Physical', "All-Terrain Vehicles, Construction Equipment, Evasion, Motorcycles, Street Racing, Stunts, Tailing, Trucks, Vintage Models", [])
FIREARMS = Skill('Firearms', 0, 'Physical', "Crossbows, Gun Dealing, Gunsmithing, Handloading Ammunition, Quick Draw, Sniper, Trick Shooting", [])
LARCENY = Skill('Larceny', 0, 'Physical', "Alarms, Forgery, Grand Theft Auto, Housebreaking, Lockpicking, Pickpocketing, Safecracking, Security Analysis", [])
MELEE = Skill('Melee', 0, 'Physical', "Axes, Chains, Clubs, Foils, Disarming Blows, Garrotes, Improvised Weapons, Knives, Stakes, Swords", [])
STEALTH = Skill('Stealth', 0, 'Physical', "Ambushes, Crowds, Disguise, Hiding, Shadowing, Urban, Wilderness", [])
SURVIVAL = Skill('Survival', 0, 'Physical', "Desert, Hunting, Jungle, Tracking, Traps, Shelters, Urban, Woodlands", [])
# Social Skills
ANIMAL_KEN = Skill('Animal_Ken', 0, 'Social', "Attack Training, Cats, Dogs, Falconry, Horses, Pacification, Rats, Snakes, Wolves", [])
ETIQUETTE = Skill('Etiquette', 0, 'Social', "Celebrities, Corporate, Garou, One-Percenter, Spirits, Secret Society", [])
INSIGHT = Skill('Insight', 0, 'Social', "Discerning Lies, Empathy, Interrogation, Motives, Phobias, Spirits, Vices", [])
INTIMIDATION = Skill('Intimidation', 0, 'Social', "Extortion, Insults, Interrogation, Physical Coercion, Stare Downs, Veiled Threats", [])
LEADERSHIP = Skill('Leadership', 0, 'Social', "Command, Down But Not Out, Inspiration, Oratory, Team Dynamics, War Pack", [])
PERFORMANCE = Skill('Performance', 0, 'Social', "Comedy, Dance, Drama, Drums, Guitar, Moot-Songs, Poetry, Rites, Rap, Singing, Violin, Wind Instruments", [])
PERSUASION = Skill('Persuasion', 0, 'Social', "Bargaining, Fast Talk, Interrogation, Legal Argument, Negotiation, Nonstop Bullshit, Rhetoric", [])
STREETWISE = Skill('Streetwise', 0, 'Social', "Arms Dealing, Black Market, Bribery, Drugs, Fence Stolen Goods, Gangs, Graffiti, Sex Trade, The Best Parties", [])
SUBTERFUGE = Skill('Subterfuge', 0, 'Social', "Bluff, Corporate Double-Talk, Impeccable Lies, Innocence, The Long Con, Seduction", [])
# Mental Skills
ACADEMICS = Skill('Academics', 0, 'Mental', "African Literature, Architecture, History of Art, History (specific Field or Period), Migration Practices of Predatory Animals, Journalism, Philosophy, Research, Teaching, Theology", [])
AWARENESS = Skill('Awareness', 0, 'Mental', "Ambushes, Camouflage, Concealed Objects, Hearing, Instincts, Smell, Sight, Traps, Wilderness", [])
FINANCE = Skill('Finance', 0, 'Mental', "Appraisal, Banking, Black Markets, Corporate Finance, Currency Manipulation, Emerging Markets, Forensic Accounting, Meme Stock Speculation, Money Laundering", [])
INVESTIGATION = Skill('Investigation', 0, 'Mental', "Criminology, Deduction, Forensics, Missing Persons, Murder, Racketeering, Traffic Analysis", [])
MEDICINE = Skill('Medicine', 0, 'Mental', "First Aid, Hematology, Pathology, Pharmacy, Phlebotomy, Surgery, Trauma Care, Veterinary", [])
OCCULT = Skill('Occult', 0, 'Mental', "Alchemy, Faeries, Ghosts, Goetia, Grimoires, Metaphysics, Parapsychology, Spirits, Umbra", [])
POLITICS = Skill('Politics', 0, 'Mental', "City Government, Diplomacy, Media, National Politics, Pack Territories, State or Provincial Politics", [])
SCIENCE = Skill('Science', 0, 'Mental', "Astronomy, Biology, Chemistry, Demolitions, Engineering, Genetics, Geology, Mathematics, Physics", [])
TECHNOLOGY = Skill('Technology', 0, 'Mental', "Artillery, Coding, Computer Construction, Data Mining, Energy Systems, Hacking, Networks, Phones, Surveillance Systems", [])

ALL_SKILLS = [ATHLETICS, BRAWL, CRAFT, DRIVING, FIREARMS, LARCENY, MELEE, STEALTH, SURVIVAL, ANIMAL_KEN, ETIQUETTE, INSIGHT, INTIMIDATION, LEADERSHIP, PERFORMANCE, PERSUASION, STREETWISE, SUBTERFUGE, ACADEMICS, AWARENESS, FINANCE, INVESTIGATION, MEDICINE, OCCULT, POLITICS, SCIENCE, TECHNOLOGY]
PHYSICAL_SKILLS = [ATHLETICS, BRAWL, CRAFT, DRIVING, FIREARMS, LARCENY, MELEE, STEALTH, SURVIVAL]
SOCIAL_SKILLS = [ANIMAL_KEN, ETIQUETTE, INSIGHT, INTIMIDATION, LEADERSHIP, PERFORMANCE, PERSUASION, STREETWISE, SUBTERFUGE]
MENTAL_SKILLS = [ACADEMICS, AWARENESS, FINANCE, INVESTIGATION, MEDICINE, OCCULT, POLITICS, SCIENCE, TECHNOLOGY]


@dataclass
class Merit:
    name: str
    value: int
    group: str

@dataclass
class Flaw(Merit):
    name: str
    value: int
    group: str


CAERN_ACCESS = Merit("Caern Access", 1, "Caern")
AWAKENED_CAERN = Merit("Awakened Caern", 5, "Caern")
CAERN_PARIAH = Flaw("Caern Pariah", -2, "Caern")

DAY_JOB = Merit("Day Job", 1, "DayJob")
CORROBORATED_DAY_JOB = Merit("Corroborated Day Job", 2, "DayJob")

ILLITERATE = Flaw("Illiterate", -2, "Linguistics")

CLEMENT_LUPUS = Merit("Clement Lupus", 1, "Looks")
BEAUTIFUL = Merit("Beautiful", 2, "Looks")
STUNNING = Merit("Stunning", 4, "Looks")
REPULSIVE = Flaw("Repulsive", -2, "Looks")
UGLY = Flaw("Ugly", -1, "Looks")

OBSCURE_SAFE_HOUSE = Merit("Obscure Safe House", 2, "SafeHouse")
SECURE_SAFE_HOUSE = Merit("Secure Safe House", 2, "SafeHouse")

ADDICTION = Flaw("Addiction", -1, "SubstanceAbuse")
HOPELESS_ADDICTION = Flaw("Hopeless Addiction", -2, "SubstanceAbuse")

MOON_QUICKENED = Merit("Moon-Quickened", 1, "SupernaturalSituations")
MOON_RILED = Merit("Moon-Riled", 3, "SupernaturalSituations")
FOLKLORIC_BLOCK = Flaw("Folkloric Block", -1, "SupernaturalSituations")
FOLKLORIC_TELL = Flaw("Folkloric Tell", -1, "SupernaturalSituations")
CRONES_CURSE = Flaw("Crone's Curse", -2, "SupernaturalSituations")
MOON_THRALL = Flaw("Moon-Thrall", -2, "SupernaturalSituations")


class BackgroundAlly():
    items = []

    def __init__(self, name = 'Ally', effectiveness=0, reliability=0, is_stalker=False):
        self.name = name
        self.effectiveness = effectiveness
        self.reliability = reliability
        self.is_stalker = is_stalker
        BackgroundAlly.items.append(self)

    def __repr__(self):
        if not self.is_stalker:
            return f'Ally: [Effectiveness: {self.effectiveness}, Reliability: {self.reliability}]'
        else:
            return f'Stalker: [Effectiveness: {self.effectiveness}, Reliability: {self.reliability}]'


ALLY_TEMPLATE_WEAK = BackgroundAlly('Weak Individual', 2, 1, False)
ALLY_TEMPLATE_AVERAGE = BackgroundAlly('Average Individual', 3, 2, False)
ALLY_TEMPLATE_GIFTED = BackgroundAlly('Gifted Individual', 4, 2, False)
ALLY_TEMPLATE_SUPERLATIVE = BackgroundAlly('Superlative Individual', 5, 3, False)


class BackgroundContact:
    items = []

    def __init__(self, name = 'Contact', useful=0):
        self.name = name
        self.useful = useful

    def __repr__(self):
        return f'Contact: {self.useful}'

CONTACT_TEMPLATE_COMMON = BackgroundContact('Common Knowledge Informant', 1)
CONTACT_TEMPLATE_UNCOMMON = BackgroundContact('Uncommon/Privileged Knowledge Informant', 2)
CONTACT_TEMPLATE_CRITICAL = BackgroundContact('Critical/Government Classified Knowledge Informant', 3)


def get_background():
    background_types = ['Ally', 'Contact', 'Fame', 'Loresheet', 'Mask', 'Mentor', 'Resources', 'Spirit Pact', 'Talisman']
    new_background = random.choice(background_types)

    match new_background:
        case 'Ally':
            return random.choice(BackgroundAlly.items)
        case 'Contact':
            return random.choice(BackgroundContact.items)




class Tribe:
    items = []

    def __init__(self, name, **kwargs):
        Tribe.items.append(self)
        self.name = name
        for k, d in kwargs.items():
            self.__setattr__(k, d)

    def __repr__(self):
        return self.name

BLACK_FURIES = Tribe('Black Furies', patron='Gorgon', archetype=['Most Wanted', 'EMT', 'Musician', 'Outrider'])
BONE_GNAWERS = Tribe('Bone Gnawers', patron='Rat', archetype=['Zine Racounteur', 'Sound Tech', 'Friend of Ours', 'Gig Wheelman'])
CHILDREN_OF_GAIA = Tribe('Children of Gaia', patron='Unicorn', archetype=['Sawbones', 'Dealer', 'Wayfarer', 'Miner'])
GALESTALKERS = Tribe('Galestalkers', patron='North Wind', archetype=['Drifter', 'Spiritwalker', 'Gaucho', 'Leechtalker'])
GHOST_COUNCIL = Tribe('Ghost Council', patron='Horned Serpent', archetype=['Contemplative', 'Saboteur', 'Witch', 'Shepherd'])
GLASS_WALKERS = Tribe('Glass Walkers', patron='Spider', archetype=['Urban Planner', 'Car Liberator', 'Detective', 'Tattoo Artist'])
HART_WARDENS = Tribe('Hart Wardens', patron='Stag', archetype=['Huntsman', 'Digital Caern Strategist', 'Emcee', 'Local Legend'])
RED_TALONS = Tribe('Red Talons', patron='Griffin', archetype=['Bounty Hunter', 'Maneater', 'Prepper', 'Plague Dog'])
SHADOW_LORDS = Tribe('Shadow Lords', patron='Thunder', archetype=['Boyar', 'Hacktivist', 'Midnight Terror', 'Assassin'])
SILENT_STRIDERS = Tribe('Silent Striders', patron='Owl', archetype=['Kinseeker', 'Ambassador', 'Revivalist', 'Long-Haul Trucker'])
SILVER_FANGS = Tribe('Silver Fangs', patron='Falcon', archetype=['Local Celebrity', 'Hetman', 'Glory-Days QB', 'Nobile-in-Exile'])

AUSPICES = ['RAGABASH', 'THEURGE', 'PHILDOX', 'GALLIAD', 'AHROUN']

class Character():
    def __init__(self, **kwargs):
        for k, d in kwargs:
            self.__setattr__(k, d)
    

def get_attribute(ch: Character, attr_name, value):
    match attr_name:
        case 'Strength':
            ch.Strength = Attribute('Strength', value)
        case 'Dexterity':
            ch.Dexterity = Attribute('Dexterity', value)
        case 'Stamina':
            ch.Stamina = Attribute('Stamina', value)
        case 'Charisma':
            ch.Charisma = Attribute('Charisma', value)
        case 'Manipulation':
            ch.Manipulation = Attribute('Manipulation', value)
        case 'Composure':
            ch.Composure = Attribute('Composure', value)
        case 'Intelligence':
            ch.Intelligence = Attribute('Intelligence', value)
        case 'Wits':
            ch.Wits = Attribute('Wits', value)
        case 'Resolve':
            ch.Resolve = Attribute('Resolve', value)


def get_attributes(ch: Character):
    attributes = ['Strength', 'Dexterity', 'Stamina', 'Charisma', 'Manipulation', 'Composure', 'Intelligence', 'Wits', 'Resolve']
    new_attribute = random.choice(attributes)
    attributes.pop(attributes.index(new_attribute))
    get_attribute(ch, new_attribute, 4)

    for _ in range(3):
        new_attribute = random.choice(attributes)
        attributes.pop(attributes.index(new_attribute))
        get_attribute(ch, new_attribute, 3)
    
    for _ in range(4):
        new_attribute = random.choice(attributes)
        attributes.pop(attributes.index(new_attribute))
        get_attribute(ch, new_attribute, 2)

    get_attribute(ch, attributes[0], 1)
    attributes.pop(0)

    ch.Physical_Attributes = [ch.Strength, ch.Dexterity, ch.Stamina]
    ch.Social_Attributes = [ch.Charisma, ch.Manipulation, ch.Composure]
    ch.Mental_Attributes = [ch.Intelligence, ch.Wits, ch.Resolve]
    ch.Attributes = ch.Physical_Attributes + ch.Social_Attributes + ch.Mental_Attributes


def get_health_willpower(ch: Character):
    ch.Health = ch.Stamina.value + 3
    ch.Willpower = ch.Resolve.value + ch.Composure.value


def get_skills(ch: Character):
    ch.Skills = []
    all_skills = list(ALL_SKILLS)
    for skill in all_skills:
        ch.__setattr__(skill.name, skill)
        ch.Skills.append(ch.__getattribute__(skill.name))

    skill_spreads = ['Jack', 'Balanced', 'Specialist']
    skill_spread = random.choice(skill_spreads)
    skills_values = {}
    match skill_spread:
        case 'Jack':
            skills_values[3] = 1
            skills_values[2] = 8
            skills_values[1] = 10
        case 'Balanced':
            skills_values[3] = 3
            skills_values[2] = 5
            skills_values[1] = 7
        case 'Specialist':
            skills_values[4] = 1
            skills_values[3] = 3
            skills_values[2] = 3
            skills_values[1] = 3

    for k, d in skills_values.items():
        for _ in range(d):
            new_skill = random.choice(all_skills)
            all_skills.pop(all_skills.index(new_skill))
            ch.__getattribute__(new_skill.name).value = k

    if hasattr(ch, "Academics"):
        ch.Academics.specialty.append(random.choice(ch.Academics.specialties.split(", ")))
    if hasattr(ch, "Craft"):
        ch.Craft.specialty.append(random.choice(ch.Craft.specialties.split(", ")))
    if hasattr(ch, "Performance"):
        ch.Performance.specialty.append(random.choice(ch.Performance.specialties.split(", ")))
    if hasattr(ch, "Science"):
        ch.Science.specialty.append(random.choice(ch.Science.specialties.split(", ")))

    char_gen_speciality_skill = random.choice([skill for skill in ch.Skills if skill.value > len(skill.specialty) and 
                                               skill.name not in ["Academics", "Craft", "Performance", "Science"]])
    char_gen_specialty = random.choice(char_gen_speciality_skill.specialties.split(", "))
    ch.__getattribute__(char_gen_speciality_skill.name).specialty.append(char_gen_specialty)
    return ch


def generate_character():
    character = Character()
    get_attributes(character)
    get_health_willpower(character)
    get_skills(character)
    for attribute in character.Attributes:
        print(attribute)
    for skill in character.Skills:
        print(skill)


if __name__ == "__main__":
    generate_character()

