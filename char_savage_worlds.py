import random

def dice(dicestring):
    mod = 0
    if len(dicestring.split('+')) > 1:
        dicestring, mod = dicestring.split('+')
    throws, sides = dicestring.split('d')
    return sum([mod, sum([random.randint(1, int(sides)) for _ in range(int(throws))])])

DICE_RANK = {1: '1d4', 2: '1d6', 3: '1d8', 4: '1d10', 5: '1d12'}

def find_dice_rank(rank):
    if rank <= 5:
        return DICE_RANK[rank]
    else:
        return f'{DICE_RANK[5]}+{rank-5}'

class ABC:
    def __init__(self, name, **kwargs):
        self.name = name
        for k, d in kwargs.items():
            self.__setattr__(k, d)

    def _dict(self):
        return self.__dict__

    def __format__(self):
        return self.name

    def __repr__(self):
        return self.__format__()

class Race(ABC):
    items = []
    def __init__(self, name, **kwargs):
        super().__init__(name, kwargs)
        Race.items.append(self)

class Attribute:
    items = []
    def __init__(self, name, rank):
        Attribute.items.append(self)
        self.rank = rank 
        self.name = name
        self.value = find_dice_rank(self.rank)

    def __add__(self, x):
        self.rank += x
        return Attribute(self.name, self.rank)

    def __iadd__(self, x):
        return self.__add__(x)

    def __repr__(self):
        return f'{self.name}: {self.value}'

AGILITY = Attribute('Agility', 1)
SMARTS = Attribute('Smarts', 1)
SPIRIT = Attribute('Spirit', 1)
STRENGTH = Attribute('Strength', 1)
VIGOR = Attribute('Vigor', 1)

class Skill(ABC):
    items = []
    def __init__(self, name, attribute, rank=1, core=False, **kwargs):
        super().__init__(name, kwargs)
        Skill.items.append(self)
        self.attribute = attribute
        self.is_core = core
        self.rank = rank
        self.value = find_dice_rank(self.rank)

    def __add__(self, x):
        self.rank += x
        self.value = find_dice_rank(self.rank)
    
    def __iadd__(self, x):
        return self.__add__(x)


ATHLETICS = Skill('Athletics', attribute=AGILITY, core=True)
COMMON_KNOWLEDGE = Skill('Common Knowledge', attribute=SMARTS, core=True)
NOTICE = Skill('Notice', attribute=SMARTS, core=True)
PERSUASION = Skill('Persuasion', attribute=SPIRIT, core=True)
STEALTH = Skill('Stealth', attribute=AGILITY, core=True)
ACADEMICS = Skill('Academics', attribute=SMARTS)
BATTLE = Skill('Battle', attribute=SMARTS)
BOATING = Skill('Boating', attribute=AGILITY)
DRIVING = Skill('Driving', attribute=AGILITY)
ELECTRONICS = Skill('Electronics', attribute=SMARTS)
FAITH = Skill('Faith', attribute=SPIRIT)
FIGHTING = Skill('Fighting', attribute=AGILITY)
FOCUS = Skill('Focus', attribute=SPIRIT)
GAMBLING = Skill('Gambling', attribute=SMARTS)
HACKING = Skill('Hacking', attribute=SMARTS)
HEALING = Skill('Healing', attribute=SMARTS)
INTIMIDATION = Skill('Intimidation', attribute=SPIRIT)
LANGUAGE = Skill('Language', attribute=SMARTS)
OCCULT = Skill('Occult', attribute=SMARTS)
PERFORMANCE = Skill('Performance', attribute=SPIRIT)
PILOTING = Skill('Piloting', attribute=AGILITY)
PSIONICS = Skill('Psionics', attribute=SMARTS)
REPAIR = Skill('Repair', attribute=SMARTS)
RESEARCH = Skill('Research', attribute=SMARTS)
RIDING = Skill('Riding', attribute=AGILITY)
SCIENCE = Skill('Science', attribute=SMARTS)
SHOOTING = Skill('Shooting', attribute=AGILITY)
SPELLCASTING = Skill('Spellcasting', attribute=SMARTS)
SURVIVAL = Skill('Survival', attribute=SMARTS)
TAUNT = Skill('Taunt', attribute=SMARTS)
THIEVERY = Skill('Thievery', attribute=AGILITY)
WEIRD_SCIENCE = Skill('Weird Science', attribute=SMARTS)


class Hinderance(ABC):
    items = []
    def __init__(self, name, _type=None, **kwargs):
        super().__init__(name, kwargs)
        Hinderance.items.append(self)
        self.type = _type
        self.cost = 0
        if self.type == 'Minor':
            self.cost = 1
        elif self.type == 'Major':
            self.cost = 2

def penalty_resolve(penalty):
    resolutions = []
    for idx, item in enumerate(penalty):
        if not isinstance(item, str) and isinstance(penalty[idx+1], str):
            if item == None:
                item = 'Automatic Failure'
            key = penalty[idx+1]
            if len(key.split(' & ')) > 1:
                item_resolution = (item, [i for i in key.split(' & ')])
                resolutions.append(item_resolution)
            elif len(key.split(' -> ')) > 1:
                item_resolution = (item, f"{key.split(' -> ')[0]} dependant on {key.split(' -> ')[1]}")
                resolutions.append(item_resolution)
            else:
                resolutions.append(item, key)
    return resolutions

"""
    penalty syntax
    penalty = [-2, 'Knowledge & Notice]
        -2 on all knowledge rolls and -2 on all notice rolls
    penalty = [-1, 'Trait Rolls -> Vision]
        -1 on all trait rolls that require vision
    penalty = [1, 'Size', -1, 'Pace', 0, 'Run Dice Rank']
        +1 to Size
        -1 to Pace
        0 is the Dice Rank for Running (1d4)
"""
ALL_THUMBS = Hinderance('All Thumbs', _type='Minor', penalty=[-2, 'Mechanical Devices & Electrical Devices'])
ANEMIC = Hinderance('Anemic', _type='Minor', penalty=[-2, 'Vigor -> Resist Fatigue'])
ARROGANT = Hinderance('Arrogant', _type='Minor', desc="Likes to dominate opponent. Challenges the most powerful fow in combat")
BAD_EYES = Hinderance('Bad Eyes', _type='Minor', penalty=[-1, 'Trait Rolls -> Vision'], negate='Eyewear')
BAD_EYES_M = Hinderance('Bad Eyes', _type='Major', penalty=[-2, 'Trait Rolls -> Vision'], negate='Eyewear')
BAD_LUCK = Hinderance('Bad Luck', _type='Major', penalty=[-1, 'Benny'])
BIG_MOUTH = Hinderance('Big Mouth', _type='Minor', desc='Unable to keep secrets and constantly gives away private information')
BLIND = Hinderance('Blind', _type='Major', penalty=[-6, 'All Tasks -> Vision'], buff=[1, 'Edge'])
BLOODTHIRSTY = Hinderance('Bloodthirsty', _type='Major', desc='Never takes prisoners')
CANT_SWIM = Hinderance('Cant Swim', _type='Minor', penalty=[-2, 'All Agility Tasks -> Swimming', 3, 'Pace Cost -> Movement in Water'])
CAUTIOUS = Hinderance('Cautious', _type='Minor', desc='The character plans extensively and/or is overly careful')
CLUELESS = Hinderance('Clueless', _type='Minor', penalty=[-1, 'Knowledge & Notice'])
CLUMSY = Hinderance('Clumsy', _type='Major', penalty=[-2, 'Athletics & Stealth'])
CODE_OF_HONOR = Hinderance('Code of Honor', _type='Major', desc='The character keeps their word and acts honorably')
CURIOUS = Hinderance('Curious', _type='Major', desc='The character wants to know about everything')
DEATH_WISH = Hinderance('Death Wish', _type='Minor', desc='The hero wants to die after or while completing some epic task')
DELUSIONAL = Hinderance('Delusional', _type='Minor', desc='The individual believes something strange causes them occasional trouble')
DELUSIONAL_M = Hinderance('Delusional', _type='Major', desc='The individual believes something strange causes them frequent trouble')
DOUBTING_THOMAS = Hinderance('Doubting Thomas', _type='Minor', desc='The character doesn\'t believe in the supernatural, often exposing them to unnecessary risks')
DRIVEN = Hinderance('Driven', _type='Minor', desc='The hero\'s actions are driven by some important goal or belief')
DRIVEN_M = Hinderance('Driven', _type='Major', desc='The hero\'s actions are driven by some important goal or belief')
ELDERLY = Hinderance('Elderly', _type='Major', penalty=[-1, 'Pace & Running & Agility & Strength & Vigor'], buff=[5, 'Skill points'])
ENEMY = Hinderance('Enemy', _type='Minor', desc='The character has a recurring nemesis')
ENEMY_M = Hinderance('Enemy', _type='Major', desc='The character has a recurring nemesis')
GREEDY = Hinderance('Greedy', _type='Minor', desc='The individual is obsessed with wealth and material possesions')
GREEDY_M = Hinderance('Greedy', _type='Major', desc='The individual is obsessed with wealth and material possesions')
HABIT = Hinderance('Habit', _type='Minor', desc='Addicted to something, suffers fatigue if deprived')
HABIT_M = Hinderance('Habit', _type='Major', desc='Addicted to something, suffers fatigue if deprived')
HARD_OF_HEARING = Hinderance('Hard of Hearing', _type='Minor', penalty=[-4, 'Sound -> Notice'])
HARD_OF_HEARING_M = Hinderance('Hard of Hearing', _type='Major', penalty=[None, 'Sound -> Notice'])
HEROIC = Hinderance('Heroic', _type='Major', desc='The character always helps those in need')
HESITANT = Hinderance('Hesitant', _type='Major', desc='Draw two action cards and take the lowest (excluding Jokers, which can be kept')
ILLITERATE = Hinderance('Illiterate', _type='Minor', desc='The character cannont read or write')
IMPULSIVE = Hinderance('Impulsive', _type='Major', desc='The hero leaps before they look')
JEALOUS = Hinderance('Jealous', _type='Minor', desc='The individual covets what others have')
JEALOUS_M = Hinderance('Jealous', _type='Major', desc='The individual covets what others have')
LOYAL = Hinderance('Loyal', _type='Minor', desc='The hero is loyal to his friends & allies')
MEAN = Hinderance('Mean', _type='Minor', penalty=[-1, 'Persuasion'])
MILD_MANNERED = Hinderance('Mild Mannered', _type='Minor', penalty=[-2, 'Intimidation'])
MUTE = Hinderance('Mute', _type='Major', desc='The hero cannot speak')
OBESE = Hinderance('Obese', _type='Minor', penalty=[1, 'Size', -1, 'Pace', 0, 'Run Dice Rank'])
OBLIGATION = Hinderance('Obligation', _type='Minor', desc='The character has a weekly obligation of 20 hours')
OBLIGATION_M = Hinderance('Obligation', _type='Major', desc='The character has a weekly obligation of 40 hours')
ONE_ARM = Hinderance('One Arm', _type='Major', penalty=[-4, 'All Tasks -> Two-Handed'])
ONE_EYE = Hinderance('One Eye', _type='Major', penalty=[-2, 'All Actions -> 5+ Feet Away'])
OUTSIDER = Hinderance('Outsider', _type='Minor', penalty=[-2, 'Persuasion'])
OUTSIDER_M = Hinderance('Outsider', _type='Major', penalty=[-2, 'Persuasion'], desc='The character has no legal rights or other serious consequences')
OVERCONFIDENT = Hinderance('Overconfident', _type='Major', desc='The hero believes they can do anything')
PACIFIST = Hinderance('Pacifist', _type='Minor', desc='The individual only fights in self defense')
PACIFIST_M = Hinderance('Pacifist', _type='Major', desc='The individual never fights, ever')
PHOBIA = Hinderance('Phobia', _type='Minor', penalty=[-1, 'Trait Rolls -> In Presence of Fear'])
PHOBIA_M = Hinderance('Phobia', _type='Major', penalty=[-2, 'Trait Rolls -> In Presence of Fear'])
POVERTY = Hinderance('Poverty', _type='Minor', desc='Half starting funds and the character is always broke')
QUIRK = Hinderance('Quirk', _type='Minor', desc='The character has some minor but persistant foible that often annoys others')
RUTHLESS = Hinderance('Ruthless', _type='Minor', desc='The character does what it takes to get their way')
RUTHLESS_M = Hinderance('Ruthless', _type='Major', desc='The character does what it takes to get their way')
SECRET = Hinderance('Secret', _type='Minor', desc='The hero has a dark secret of some kind')
SECRET_M = Hinderance('Secret', _type='Major', desc='The hero has a dark secret of some kind')
SHAMED = Hinderance('Shamed', _type='Minor', desc='The individual is haunted by some tragic event in their past')
SHAMED_M = Hinderance('Shamed', _type='Major', desc='The individual is haunted by some tragic event in their past')
SLOW = Hinderance('Slow', _type='Minor', penalty=[-1, 'Pace'])
SLOW_M = Hinderance('Slow', _type='Major', penalty=[-2, 'Pace & Athletics'])
SMALL = Hinderance('Small', _type='Minor', penalty=[-1, 'Size & Toughness'])
STUBBORN = Hinderance('Stubborn', _type='Minor', desc='The character whats their way and rarely admits mistakes')
SUSPICIOUS = Hinderance('Suspicious', _type='Minor', desc='The individual is paranoid')
SUSPICIOUS_M = Hinderance('Suspicious', _type='Major', penalty=[-2, 'All Ally Rolls -> Supporting Character'], desc='The individual is paranoid')
THIN_SKINNED = Hinderance('Thin Skinned', _type='Minor', penalty=[-2, 'Resist Taunt'])
THIN_SKINNED_M = Hinderance('Thin Skinned', _type='Major', penalty=[-4, 'Resist Taunt'])
TONGUE_TIED = Hinderance('Tongue Tied', _type='Major', penalty=[-1, 'Intimidation & Persuasion & Taunt'])
UGLY = Hinderance('Ugly', _type='Minor', penalty=[-1, 'Persuasion'])
UGLY_M = Hinderance('Ugly', _type='Major', penalty=[-2, 'Persuasion'])
VENGEFUL = Hinderance('Vengeful', _type='Minor', desc='The adventurer seeks payback for slights against them')
VENGEFUL_M = Hinderance('Vengeful', _type='Major', desc='The adventurer seeks payback for slights against them. They\'ll cause physical harm to get it')
VOW = Hinderance('Vow', _type='Minor', desc='The individual has pledged themself to some cause')
VOW_M = Hinderance('Vow', _type='Major', desc='The individual has pledged themself to some cause')
WANTED = Hinderance('Wanted', _type='Minor', desc='The character is wanted by the authorities')
WANTED_M = Hinderance('Wanted', _type='Major', desc='The character is wanted by the authorities')
YELLOW = Hinderance('Yellow', _type='Major', penalty=[-2, 'Fear & Resist Intimidation'])
YOUNG = Hinderance('Young', _type='Minor', penalty=[4, 'Attribute Points', 10, 'Skill Points'], buff=[1, 'Benny'])
YOUNG_M = Hinderance('Young', _type='Major', penalty=[3, 'Attribute Points', 10, 'Skill Points'], buff=[2, 'Benny'])


class Trait(ABC):
    items = []
    def __init__(self, name, **kwargs):
        super().__init__(name, kwargs)
        Trait.items.append(self)


class Edge(ABC):
    items = []
    def __init__(self, name, category, **kwargs):
        super().__init__(name, kwargs)
        self.category = category
        Edge.items.append(self)

class EdgeType:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

NOVICE = EdgeType('Novice')
SEASONED = EdgeType('Seasoned')
VETERAN = EdgeType('Veteran')
WILDCARD = EdgeType('Wild Card')
HEROIC = EdgeType('Heroic')
LEGENDARY = EdgeType('Legendary')

"""
    EDGES
"""
# BACKGROUND EDGES
ALERTNESS = Edge('Alertness', category='Background')
AMBIDEXTROUS = Edge('Ambidextrous', category='Background', requirements={AGILITY: 3})
ARCANE_BACKGROUND = Edge('Arcane Background', category='Background')
ARCANE_RESISTANCE = Edge('Arcane Resistance', category='Background', requirements={SPIRIT: 3})
IMPROVED_ARCANE_RESISTANCE = Edge('Improved Arcane Resistance', category='Background', requirements={ARCANE_RESISTANCE: True})
ARISTOCRAT = Edge('Aristocrat', category='Background')
ATTRACTIVE = Edge('Attractive', category='Background', requirements={VIGOR: 2})
VERY_ATTRACTIVE = Edge('Very Attractive', category='Background', requirements={'Edge': ATTRACTIVE})
BESERK = Edge('Beserk', category='Background')
BRAVE = Edge('Brave', category='Background', requirements={SPIRIT: 2})
BRAWNY = Edge('Brawny', category='Background', requirements={STRENGTH: 2, VIGOR: 2})
BRUTE = Edge('Brute', category='Background', requirements={STRENGTH: 2, VIGOR: 2})
CHARISMATIC = Edge('Charismatic', category='Background', requirements={SPIRIT: 3})
ELAN = Edge('Elan', category='Background', requirements={SPIRIT: 3})
FAME = Edge('Fame', category='Background')
FAMOUS = Edge('Famous', category='Background', requirements={SEASONED: True, FAME: True})
FAST_HEALER = Edge('Fast Healer', category='Background', requirements={VIGOR: 3})
FLEET_FOOTED = Edge('Fleet-Footed', category='Background', requirements={AGILITY: 2})
LINGUIST = Edge('Linguist', category='Background', requirements={SMARTS: 2})
LUCK = Edge('Luck', category='Background')
GREAT_LUCK = Edge('Great Luck', category='Background', requirements={LUCK: True})
QUICK = Edge('Quick', category='Background', requirements={AGILITY: 3})
RICH = Edge('Rich', category='Background')
FILTHY_RICH = Edge('Filthy Rich', category='Background', requirements={RICH: True})
# COMBAT EDGES
BLOCK = Edge('Block', category='Combat', requirements={SEASONED: True, FIGHTING: 3})
IMPROVED_BLOCK = Edge('Improved Block', category='Combat', requirements={VETERAN: True, BLOCK: True})
BRAWLER = Edge('Brawler', category='Combat', requirements={STRENGTH: 3, VIGOR: 3})
BRUISER = Edge('Bruiser', category='Combat', requirements={SEASONED: True})
CALCULATING = Edge('Calculating', category='Combat', requirements={SMARTS: 3})
COMBAT_REFLEXES = Edge('Combat Reflexes', category='Combat', requirements={SEASONED: True})
COUNTERATTACK = Edge('Counterattack', category='Combat', requirements={SEASONED: True, FIGHTING: 3})
IMPROVED_COUNTERATTACK = Edge('Improved Counterattack', category='Combat', requirements={VETERAN: True, COUNTERATTACK: True})
DEAD_SHOT = Edge('Dead Shot', category='Combat', requirements={WILDCARD: True, 'Or': ([ATHLETICS, SHOOTING], 3)})
DODGE = Edge('Dodge', category='Combat', requirements={SEASONED: True, AGILITY: 3})
IMPROVED_DODGE = Edge('Improved Dodge', category='Combat', requirements={SEASONED: True, DODGE: True})
DOUBLE_TAP = Edge('Double Tap', category='Combat', requirements={SEASONED: True, SHOOTING: 2})
EXTRACTION = Edge('Extraction', category='Combat', requirements={AGILITY: 3})
IMPROVED_EXTRACTION = Edge('Improved Extraction', category='Combat', requirements={SEASONED: True, EXTRACTION: True})
FEINT = Edge('Feint', category='Combat', requirements={FIGHTING: 3})
FIRST_STRIKE = Edge('First Strike', category='Combat', requirements={AGILITY: 3})
IMPROVED_FIRST_STRIKE = Edge('Improved First Strike', category='Combat', requirements={HEROIC, FIRST_STRIKE})
FREE_RUNNER = Edge('Free Runner', category='Combat', requirements={AGILITY: 3, ATHLETICS: 2})
FRENZY = Edge('Frenzy', category='Combat', requirements={SEASONED: True, FIGHTING: 3})
IMPROVED_FRENZY = Edge('Improved Frenzy', category='Combat', requirements={VETERAN: True, FRENZY: True})
GIANT_KILLER = Edge('Giant Killer', category='Combat', requirements={VETERAN: True})
HARD_TO_KILL = Edge('Hard to Kill', category='Combat', requirements={SPIRIT: 3})
HARDER_TO_KILL = Edge('Harder to Kill', category='Combat', requirements={VETERAN: True, HARD_TO_KILL: True})
IMPROVISATIONAL_FIGHTER = Edge('Improvisational Fighter', category='Combat', requirements={SEASONED: True, SMARTS: 2})
IRON_JAW = Edge('Iron Jaw', category='Combat', requirements={VIGOR: 3})
KILLER_INSTINCT = Edge('Killer Instinct', category='Combat', requirements={SEASONED: True})
LEVEL_HEADED = Edge('Level Headed', category='Combat', requirements={SEASONED: True, SMARTS: 3})
IMPROVED_LEVEL_HEADED = Edge('Improved Level Headed', category='Combat', requirements={SEASONED: True, LEVEL_HEADED: True})
MARKSMAN = Edge('Marksman', category='Combat', requirements={SEASONED: True, 'Or': ([ATHLETICS, SHOOTING], 3)})
MARTIAL_ARTIST = Edge('Martial Artist', category='Combat', requirements={FIGHTING: 2})
MARTIAL_WARRIOR = Edge('Martial Warrior', category='Combat', requirements={SEASONED: True, MARTIAL_ARTIST: True})
MIGHTY_BLOW = Edge('Mighty Blow', category='Combat', requirements={WILDCARD: True, FIGHTING: 3})
NERVES_OF_STEEL = Edge('Nerves of Steel', category='Combat', requirements={VIGOR: 3})
IMPROVED_NERVES_OF_STEEL = Edge('Improved Nerves of Steel', category='Combat', requirements={NERVES_OF_STEEL})
NO_MERCY = Edge('No Mercy', category='Combat', requirements={SEASONED: True})
RAPID_FIRE = Edge('Rapid Fire', category='Combat', requirements={SEASONED: True, SHOOTING: 2})
IMPROVED_RAPID_FIRE = Edge('Improved Rapid Fire', category='Combat', requirements={VETERAN: True, RAPID_FIRE: True})
ROCK_AND_ROLL = Edge('Rock and Roll', category='Combat', requirements={SEASONED: True, SHOOTING: 3})
STEADY_HANDS = Edge('Steady Hands', category='Combat', requirements={AGILITY: 3})
SWEEP = Edge('Sweep', category='Combat', requirements={STRENGTH: 3, FIGHTING: 3})
IMPROVED_SWEEP = Edge('Improved Sweep', category='Combat', requirements={VETERAN: True, SWEEP: True})
TRADEMARK_WEAPON = Edge('Trademark Weapon', category='Combat', requirements={'Weapon Skill': 3})
IMPROVED_TRADEMARK_WEAPON = Edge('Improved Trademark Weapon', category='Combat', requirements={SEASONED: True, TRADEMARK_WEAPON: True})
TWO_FISTED = Edge('Two Fisted', category='Combat', requirements={AGILITY: 3})
TWO_GUN_KID = Edge('Two-Gun Kid', category='Combat', requirements={AGILITY: 3})
# LEADERSHIP EDGES
COMMAND = Edge('Command', category='Leadership', requirements={SMARTS: 2})
COMMAND_PSYCHE = Edge('Command Psyche', category='Leadership', requirements={SEASONED: True, COMMAND: True})
FERVOR = Edge('Fervor', category='Leadership', requirements={VETERAN: True, SPIRIT: 3, COMMAND: True})
HOLD_THE_LINE = Edge('Hold the Line', category='Leadership', requirements={SEASONED: True, SMARTS: 3, COMMAND: True})
INSPIRE = Edge('Inspire', category='Leadership', requirements={SEASONED: True, COMMAND: True})
NATRUAL_LEADER = Edge('Natrual Leader', category='Leadership', requirements={SEASONED: True, SPIRIT: 3, COMMAND: True})
TACTICIAN = Edge('Tactician', category='Leadership', requirements={SEASONED: True, SMARTS: 3, COMMAND: True, BATTLE: 2})
MASTER_TACTICIAN = Edge('Master Tactician', category='Leadership', requirements={VETERAN: True, TACTICIAN: True})
# POWER EDGES
ARTIFICER = Edge('Artificer', category='Power', requirements={SEASONED: True, ARCANE_BACKGROUND: True})
CHANNELING = Edge('Channeling', category='Power', requirements={SEASONED: True, ARCANE_BACKGROUND: True})
CONCENTRATION = Edge('Concentration', category='Power', requirements={SEASONED: True, ARCANE_BACKGROUND: True})
EXTRA_EFFORT = Edge('Extra Effort', category='Power', requirements={SEASONED: True, ARCANE_BACKGROUND: 'Gifted', FOCUS: 2})
GADGETEER = Edge('Gadgeteer', category='Power', requirements={SEASONED: True, ARCANE_BACKGROUND: 'Weird Science', WEIRD_SCIENCE: 2})
HOLY_UNHOLY_WARRIOR = Edge('Holy Unholy Warrior', category='Power', requirements={SEASONED: True, ARCANE_BACKGROUND: 'Miracles', FAITH: 2})
MENTALIST = Edge('Mentalist', category='Power', requirements={SEASONED: True, ARCANE_BACKGROUND: 'Psionics', PSIONICS: 2})
NEW_POWERS = Edge('New Powers', category='Power', requirements={ARCANE_BACKGROUND: True})
POWER_POINTS = Edge('Power Points', category='Power', requirements={ARCANE_BACKGROUND: True})
POWER_SURGE = Edge('Power Surge', category='Power', requirements={WILDCARD: True, ARCANE_BACKGROUND: True})
RAPID_RECHARGE = Edge('Rapid Recharge', category='Power', requirements={SEASONED: True, ARCANE_BACKGROUND: True, SPIRIT: 2})
IMPROVED_RAPID_RECHARGE = Edge('Improved Rapid Recharge', category='Power', requirements={VETERAN: True, RAPID_FIRE: True})
SOUL_DRAIN = Edge('Soul Drain', category='Power', requirements={SEASONED: True, ARCANE_BACKGROUND: True, 'Arcane Skill': 4})
WIZARD = Edge('Wizard', category='Power', requirements={SEASONED: True, ARCANE_BACKGROUND: 'Magic', SPELLCASTING: 2})

# PROFESSIONAL EDGES
ACE = Edge('Ace', category='Professional', requirements={AGILITY: 3})
ACROBAT = Edge('Acrobat', category='Professional', requirements={AGILITY: 3, ATHLETICS: 3})
COMBAT_ACROBAT = Edge('Combat Acrobat', category='Professional', requirements={SEASONED: True, ACROBAT: True})
ASSASSIN = Edge('Assassin', category='Professional', requirements={AGILITY: 3, FIGHTING: 2, STEALTH: 3})
INVESTIGATOR = Edge('Investigator', category='Professional', requirements={SMARTS: 3, RESEARCH: 3})
JACK_OF_ALL_TRADES = Edge('Jack-of-all-Trades', category='Professional', requirements={SMARTS: 4})
MCGYVER = Edge('McGyver', category='Professional', requirements={SMARTS: 2, NOTICE: 3, REPAIR: 2})
MR_FIX_IT = Edge('Mr Fix-It', category='Professional', requirements={REPAIR: 3})
SCHOLAR = Edge('Scholar', category='Professional', requirements={RESEARCH: 3})
SOLDIER = Edge('Soldier', category='Professional', requirements={STRENGTH: 2, VIGOR: 2})
THIEF = Edge('Thief', category='Professional', requirements={AGILITY: 3, STEALTH: 2, THIEVERY: 2})
WOODSMAN = Edge('Woodsman', category='Professional', requirements={SPIRIT: 2, SURVIVAL: 3})
# SOCIAL EDGES
BOLSTER = Edge('Bolster', category='Social', requirements={SPIRIT: 3})
COMMON_BOND = Edge('Common Bond', category='Social', requirements={WILDCARD: True, SPIRIT: 3})
CONNECTIONS = Edge('Connections', category='Social')
HUMILIATE = Edge('Humiliate', category='Social', requirements={TAUNT: 3})
MENACING = Edge('Menacing', category='Social', requirements={'Any': [BLOODTHIRSTY, MEAN, RUTHLESS, UGLY]})
PROVOKE = Edge('Provoke', category='Social', requirements={TAUNT: 2})
RABBLE_ROUSER = Edge('Rabble Rouser', category='Social', requirements={SPIRIT: 3})
RELIABLE = Edge('Reliable', category='Social', requirements={SPIRIT: 3})
RETORT = Edge('Retort', category='Social', requirements={TAUNT: 2})
STREETWISE = Edge('Streetwise', category='Social', requirements={SMARTS: 2})
STRONG_WILLED = Edge('Strong Willed', category='Social', requirements={SPIRIT: 3})
IRON_WILL = Edge('Iron Will', category='Social', requirements={SEASONED: True, BRAVE: True, STRONG_WILLED: True})
WORK_THE_ROOM = Edge('Work the Room', category='Social', requirements={SPIRIT: 3})
WORK_THE_CROWD = Edge('Work the Crowd', category='Social', requirements={SEASONED: True, WORK_THE_ROOM: True})
# WEIRD EDGES
BEAST_BOND = Edge('Beast Bond', category='Weird')
BEAST_MASTER = Edge('Beast Master', category='Weird', requirements={SPIRIT: 3})
CHAMPION = Edge('Champion', category='Weird', requirements={SPIRIT: 3, FIGHTING: 2})
CHI = Edge('Chi', category='Weird', requirements={VETERAN: True, MARTIAL_WARRIOR: True})
DANGER_SENSE = Edge('Danger Sense', category='Weird')
HEALER = Edge('Healer', category='Weird', requirements={SPIRIT: 3})
LIQUID_COURAGE = Edge('Liquid Courage', category='Weird', requirements={VIGOR: 3})
SCAVENGER = Edge('Scavenger', category='Weird', requirements={LUCK})
# LEGENDARY EDGES
FOLLOWERS = Edge('Followers', category='Legendary', requirements={WILDCARD: True, LEGENDARY: True})
PROFESSIONAL = Edge('Professional', category='Legendary', requirements={LEGENDARY: True, '1 Max Rank': [AGILITY, SMARTS, SPIRIT, STRENGTH, VIGOR]})
EXPERT = Edge('Expert', category='Legendary', requirements={LEGENDARY: True, PROFESSIONAL: True})
MASTER = Edge('Master', category='Legendary', requirements={LEGENDARY: True, EXPERT: True})
SIDEKICK = Edge('Sidekick', category='Legendary', requirements={WILDCARD: True, LEGENDARY: True})
TOUGH_AS_NAILS = Edge('Tough as Nails', category='Legendary', requirements={LEGENDARY: True, VIGOR: 3})
TOUGHER_THAN_NAILS = Edge('Tougher than Nails', category='Legendary', requirements={LEGENDARY: True, VIGOR: 5, TOUGH_AS_NAILS: True})
WEAPON_MASTER = Edge('Weapon Master', category='Legendary', requirements={LEGENDARY: True, FIGHTING: 5})
MASTER_OF_ARMS = Edge('Master of Arms', category='Legendary', requirements={LEGENDARY: True, WEAPON_MASTER: True})

class Gear(ABC):
    items = []
    def __init__(self, name, **kwargs):
        super().__init__(name, kwargs)
        Gear.items.append(self)


class Wildstar:
    def __init__(self, name):
        # MACRO CHARACTER VALUES
        self.name = name
        self.race = None
        # HINDRANCES
        self.hinderances = []
        # ATTRIBUTES
        self.agility = AGILITY
        self.smarts = SMARTS
        self.spirit = SPIRIT
        self.strength = STRENGTH
        self.vigor = VIGOR
        self.attributes = {
            'Agility': self.agility.value,
            'Smarts': self.smarts.value,
            'Spirit': self.spirit.value,
            'Strength': self.strength.value,
            'Vigor': self.vigor.value
        }
        # SKILLS
        self.athletics = ATHLETICS
        self.common_knowledge = COMMON_KNOWLEDGE
        self.notice = NOTICE
        self.persuasion = PERSUASION
        self.stealth = STEALTH
        self.skills = {
            'Athletics': (find_dice_rank(self.athletics), self.athletics.attribute),
            'Common Knowledge': (find_dice_rank(self.common_knowledge), self.common_knowledge.attribute),
            'Notice': (find_dice_rank(self.notice), self.notice.attribute),
            'Persuasion': (find_dice_rank(self.persuasion), self.persuasion.attribute),
            'Stealth': (find_dice_rank(self.stealth), self.stealth.attribute)
        }
        # DERIVED STATS
        self.pace = 6
        self.parry = 2
        self.toughness = 2 + self.vigor.rank//2
        # EDGES
        self.edges = []
        # GEAR
        self.gear = []
