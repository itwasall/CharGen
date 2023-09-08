import random

def roll(dicestring):
    mod = 0
    if len(dicestring.split('+')) > 1:
        dicestring, mod = dicestring.split('+')[0], int(dicestring.split('+')[1])
    throws, sides = [int(i) for i in dicestring.split('d')]
    return sum([mod, sum([random.randint(1, sides) for _ in range(throws)])])

class ABC:
    def __init__(self, name, **kwargs):
        self.name = name
        for k, d in kwargs.items():
            self.__setattr__(k, d)

    def __format__(self):
        return self.name

    def __repr__(self):
        return self.__format__()


class Caste(ABC):
    items = []
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        Caste.items.append(self)


class Attribute:
    items = []
    def __init__(self, name, category=None, value=0):
        self.name = name
        self.category = category
        self.value = value
        Attribute.items.append(self)

    def __add__(self, x):
        return Attribute(self.name, self.category, self.value + x)

    def __iadd__(self, x):
        return self.__add__(x)

    def __format__(self):
        fmt_str = f"{self.name}: {self.value}"
        return fmt_str

    def __repr__(self):
        return self.__format__()

STRENGTH = Attribute('Strength', category='Phys')
DEXTERITY = Attribute('Dexterity', category='Phys')
STAMINA = Attribute('Stamina', category='Phys')
CHARISMA = Attribute('Charisma', category='Social')
MANIPULATION = Attribute('Manipulation', category='Social')
APPEARANCE = Attribute('Appearance', category='Social')
PERCEPTION = Attribute('Perception', category='Mental')
INTELLIGENCE = Attribute('Intelligence', category='Mental')
WITS = Attribute('Wits', category='Mental')

class Ability(ABC):
    items = []
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        Ability.items.append(self)

    def __format__(self):
        return f"{self.name}: {self.value}"

class Merit(ABC):
    items = []
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        Merit.items.append(self)

ALLIES = Merit('Allies', cost=[1, 3, 5], supernatural=False)
AMBIDEXTROUS = Merit('Ambidextrous', cost=[1, 2], supernatural=False)
ARTIFACT = Merit('Artifact', cost=[2, 3, 4, 5], supernatural=False)
BACKING = Merit('Backing', cost=[2, 3, 4], supernatural=False)
BOUNDLESS_ENDURANCE = Merit('Boundless_Endurance', cost=[2], supernatural=False)
COMMAND = Merit('Command', cost=[2,3,4,5], supernatural=False)
CONTACTS = Merit('Contacts', cost=[1,3,5], supernatural=False)
CULT = Merit('Cult', cost=[1,2,3,4,5], supernatural=False)
DANGER_SENSE = Merit('Danger_Sense', cost=[3], supernatural=False)
DEMESNE = Merit('Demesne', cost=[2,4], supernatural=False)
DIRECTION_SENSE = Merit('Direction_Sense', cost=[1], supernatural=False)
EIDETIC_MEMORY = Merit('Eidetic_Memory', cost=[2], supernatural=False)
FAMILIAR = Merit('Familiar', cost=[1,2,3], supernatural=False)
FAST_REFLEXES = Merit('Fast_Reflexes', cost=[3], supernatural=False)
FLEET_OF_FOOT = Merit('Fleet_of_Foot', cost=[4], supernatural=False)
FOLLOWERS = Merit('Followers', cost=[1,2,3], supernatural=False)
GIANT = Merit('Giant', cost=[4], supernatural=False)
HEARTHSTONE = Merit('Hearthstone', cost=[2,4], supernatural=False)
HIDEOUS = Merit('Hideous', cost=[0], supernatural=False)
INFLUENCE = Merit('Influence', cost=[1,2,3,4,5], supernatural=False)
IRON_STOMACH = Merit('Iron_Stomach', cost=[1], supernatural=False)
LANGUAGE = Merit('Language', cost=[1], supernatural=False)
MANSE = Merit('Manse', cost=[3,5], supernatural=False)
MENTOR = Merit('Mentor', cost=[1,2,3], supernatural=False)
MARTIAL_ARTIST = Merit('Martial_Artist', cost=[4], supernatural=False)
MIGHTY_THEW = Merit('Mighty_Thew', cost=[1,2,3], supernatural=False)
NATURAL_IMMUNITY = Merit('Natural_Immunity', cost=[2], supernatural=False)
PAIN_TOLERANCE = Merit('Pain_Tolerance', cost=[4], supernatural=False)
QUICK_DRAW = Merit('Quick_Draw', cost=[1,4], supernatural=False)
RETAINERS = Merit('Retainers', cost=[2,4], supernatural=False)
RESOURCES = Merit('Resources', cost=[1,2,3,4,5], supernatural=False)
SELECTIVE_CONCEPTION = Merit('Selective_Conception', cost=[1], supernatural=False)
STRONG_LUNGS = Merit('Strong_Lungs', cost=[1], supernatural=False)
TEMPERED_BY_THE_ELEMENTS = Merit('Tempered_by_the_Elements', cost=[2], supernatural=False)
TOXIN_RESISTANCE = Merit('Toxin_Resistance', cost=[3], supernatural=False)

Chameleon
Claws_Fangs_Hooves_Horns



ARCHERY = Ability('Archery', value=0)
ATHLETICS = Ability('Athletics', value=0)
AWARENESS = Ability('Awareness', value=0)
BRAWL = Ability('Brawl', value=0)
BUEREAUCRACY = Ability('Buereaucracy', value=0)
CRAFT = Ability('Craft', value=0)
DODGE = Ability('Dodge', value=0)
INTEGRITY = Ability('Integrity', value=0)
INVESTIGATION = Ability('Investigation', value=0)
LARCENY = Ability('Larceny', value=0)
LINGUISTICS = Ability('Linguistics', value=0)
LORE = Ability('Lore', value=0)
MARTIAL_ARTS = Ability('Martial_Arts', value=0)
MEDICINE = Ability('Medicine', value=0)
MELEE = Ability('Melee', value=0)
OCCULT = Ability('Occult', value=0)
PERFORMANCE = Ability('Performance', value=0)
PRESENCE = Ability('Presence', value=0)
RESISTANCE = Ability('Resistance', value=0)
RIDE = Ability('Ride', value=0)
SAIL = Ability('Sail', value=0)
SOCIALISE = Ability('Socialise', value=0)
STEALTH = Ability('Stealth', value=0)
SURVIVAL = Ability('Survival', value=0)
THROWN = Ability('Thrown', value=0)
WAR = Ability('War', value=0)

DAWN = Caste('Dawn', abls=[ARCHERY, AWARENESS, BRAWL, MARTIAL_ARTS, DODGE, MELEE, RESISTANCE, THROWN, WAR])
ZENITH = Caste('Zenith', abls=[ATHLETICS, INTEGRITY, PERFORMANCE, LORE, PRESENCE, RESISTANCE, SURVIVAL, WAR])
TWILIGHT = Caste('Twilight', abls=[BUEREAUCRACY, CRAFT, INTEGRITY, INVESTIGATION, LINGUISTICS, LORE, RIDE, STEALTH, SOCIALISE])
NIGHT = Caste('Night', abls=[ATHLETICS, AWARENESS, DODGE, INVESTIGATION, LARCENY, RIDE, STEALTH, SOCIALISE])
ECLIPSE = Caste('Eclipse', abls=[BUEREAUCRACY, LARCENY, LINGUISTICS, OCCULT, PRESENCE, RIDE, SAIL, SOCIALISE])

def gen_character():
    # Get caste
    player_caste = random.choice(Caste.items)
    print(player_caste)
    # Sort attributes
    player_attributes = {
            'Physical': [i for i in Attribute.items if i.category=='Phys'],
            'Social': [i for i in Attribute.items if i.category=='Social'],
            'Mental': [i for i in Attribute.items if i.category=='Mental'],
            }
    print(player_attributes)
    primary_attr_dots = 8
    secondary_attr_dots = 6
    tertiary_attr_dots = 4
    # Abilities
    player_skills = [i for i in Ability.items]
    relevant_caste_abls = player_caste.abls
    print([i.name for i in relevant_caste_abls])
    favoured_abls = [None for _ in range(5) if _ not in relevant_caste_abls]
    supernal_abl = random.choice(relevant_caste_abls)
    ability_dots = 28
    for skill in player_skills:
        if not isinstance(skill, Ability):
            pass
        elif skill.value > 3:
            skill.value = 3
            ability_dots += 1
        elif skill in relevant_caste_abls and skill.value < 1:
            skill.value += 1
            ability_dots -= 1
        print(skill)
    player_specialties = [None for _ in range(4)]
    # Merits
    player_merits = [] 
    merit_dots = 10
    while merit_dots > 0:
        roll_merit = random.choice([i for i in Merit.items if not i.supernatural])
        roll_cost = random.choice(roll_merit.cost)
        if roll_cost < merit_dots:
            player_merits.append((roll_merit,roll_cost))
            Merit.items.pop(Merit.items.index(roll_merit))
            merit_dots -= roll_cost
        # Increasing liklihood of stopping, beginning at 4pts and becoming more likely the fewer points remaining
        if ((merit_dots == 4 and random.randint(1,100) < 50) or (2 <= merit_dots <= 3 and random.randint(1,100) < 70) or (merit_dots == 1 and random.randint(1,100) < 90)):
            merit_dots = 0
    print(player_merits)


    # Charms
    player_charms = None
    max_charms = 15
    # Intimacies & Triggers
    defining_inti = None
    major_inti = None
    positive_inti = None
    negative_inti = None
    player_intimacies = [defining_inti, major_inti, positive_inti, negative_inti]
    # Bonus points
    bonus_points = 15



gen_character()
