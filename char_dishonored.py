import random

def dice(dicestring):
    throws, sides = dicestring.split('d')
    return sum([random.randint(1, int(sides)) for _ in range(int(throws))])

def flatten(*n):
    return (e for a in n for e in (flatten(*a) if isinstance(a, (tuple, list)) else (a,)))

def attrAsDict(_class):
    return [{i: _class._getattr(i) for i in dir(_class) if not i.startswith("__")}]


class PartyMember:
    def __init__(self, **kwargs):
        for k, d in kwargs.items():
            self.__setattr__(k, d)


class ABC:
    def __init__(self, name, **kwargs):
        self.name = name
        for k, d in kwargs.items():
            self.__setattr__(k, d)

    def __repr__(self):
        return self.__format__()

    def __format__(self):
        return self.name
    
    def _getattr(self, attribute):
        return self.__getattribute__(attribute)


class Item(ABC):
    items = []
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        Item.items.append(self)


class Weapon(Item):
    items = []
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        Weapon.items.append(self)


class Skill(ABC):
    items = []
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        self.rating_min = 4
        self.rating_max = 8
        Skill.items.append(self)


class Style(ABC):
    items = []
    def __init__(self, name,  **kwargs):
        super().__init__(name, **kwargs)
        self.rating_min = 4
        self.rating_max = 8
        Style.items.append(self)


class Focus(ABC):
    items = []
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        self.rating_min = 1
        self.rating_max = 5
        Focus.items.append(self)


class Archetype(ABC):
    items = []
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        Archetype.items.append(self)


"""
    SKILLS
"""
FIGHT = Skill('Fight')
MOVE = Skill('Move')
STUDY = Skill('Study')
SURVIVE = Skill('Survive')
TALK = Skill('Talk')
TINKER = Skill('Tinker')

"""
    STYLES
"""
BOLDLY = Style('Boldly')
CAREFULLY = Style('Carefully')
CLEVERLY = Style('Cleverly')
FORCEFULLY = Style('Forcefully')
QUIETLY = Style('Quietly')
SWIFTLY = Style('Swiftly')


"""
    FOCUSES
"""
ACROBATICS = Focus('Arcobatics')
ARCHERY = Focus('Archery')
BOATS = Focus('Boats')
BRAWLING = Focus('Brawling')
CARRIAGES = Focus('Carriages')
CONCERNTRATE = Focus('Concerntrate')
COUNSEL = Focus('Counsel')
DECEIVE = Focus('Deceive')
ENGINEERING = Focus('Engineering')
ETIQUETTE = Focus('Etiquette')
EXPLOSIVES = Focus('Explosives')
FENCING = Focus('Fencing')
FIREARMS = Focus('Firearms')
FREERUNNING = Focus('Freerunning')
HISTORY = Focus('History')
INNUENDO = Focus('Innuendo')
INTIMIDATE = Focus('Intimidate')
LOCKS = Focus('Locks')
MEDICINE = Focus('Medicine')
NATURAL_PHILOSOPHY = Focus('Natural_Philosophy')
NEGOTIATE = Focus('Negotiate')
PERSUADE = Focus('Persuade')
POISONS = Focus('Poisons')
RESILIANCE = Focus('Resiliance')
RESOLVE = Focus('Resolve')
RIDE = Focus('Ride')
SHIPS = Focus('Ships')
SOCIETY = Focus('Society')
STEALTH = Focus('Stealth')
STREETWISE = Focus('Streetwise')
SURGERY = Focus('Surgery')
SWIMMING = Focus('Swimming')
SWORDS = Focus('Swords')
THEOLOGY = Focus('Theology')
TRACKING = Focus('Tracking')
VOID_LORE = Focus('Void_Lore')
WILDERNESS = Focus('Wilderness')

def gen_rating(rating_min: int, rating_max: int) -> int:
    return random.randint(rating_min, rating_max)

"""
    ITEMS
"""
# WEAPONS
SWORD = Weapon('Sword', damage=3, hq_buff=1, cost=50, qualities=['Melee'])

"""
    ARCHETYPES
"""
ASSASSIN = Archetype('Assassin', skills={FIGHT: 2, TALK: 2, 'Choose 1': [MOVE, STUDY]}, styles={'Choose 2': [CAREFULLY, CLEVERLY, QUIETLY]}, focuses=[LOCKS, STEALTH, STREETWISE, RESOLVE, POISONS], talents=['Bespoke Bloodletting', 'The Great Equalizer', 'Inhumane Determination', 'Outisder\'s Grin'], belongings=[], contacts=[])
COMMANDER = Archetype('Commander', skills={FIGHT: 2, TALK: 2, 'Choose 1': [MOVE, STUDY]}, styles={'Choose 2': [BOLDLY, FORCEFULLY, SWIFTLY]}, focuses=[ARCHERY, COUNSEL, INTIMIDATE, RESOLVE, SWORDS], talents=['Whiskey and Cigars', 'Get Back to It!', 'Pull Rank', 'Rally'], belongings=[], contacts=[])
COURIER = Archetype('Courier', skills={MOVE: 2, TALK: 2, 'Choose 1': [TINKER, SURVIVE]}, styles={'Choose 2': [CAREFULLY, CLEVERLY, QUIETLY]}, focuses=[BOATS, CARRIAGES, ETIQUETTE, FREERUNNING, INNUENDO, NEGOTIATE, STEALTH, STREETWISE], talents=['City of Whispers', 'Friends Everywhere', 'Summgler\'s Secrets', 'Supply and Demand'], belongings=[], contacts=[])
DUELIST = Archetype('Duelist', skills={FIGHT: 2, MOVE: 2, 'Choose 1': [STUDY, TALK]}, styles={'Choose 2': [BOLDLY, QUIETLY, SWIFTLY]}, focuses=[ACROBATICS, FIREARMS, INTIMIDATE, STEALTH, SWORDS], talents=['Bravura Blade', 'Flashing Steel', 'Footwork', 'Measured Strike'], belongings=[], contacts=[])
ENTREPRENEUR = Archetype('Entrepreneur', skills={TALK: 2, TINKER: 2, 'Choose 1': [MOVE, STUDY]}, styles={'Choose 2': [BOLDLY, CLEVERLY, QUIETLY]}, focuses=[DECEIVE, ENGINEERING, INNUENDO, LOCKS, MEDICINE, NATURAL_PHILOSOPHY, NEGOTIATE, STREETWISE], talents=['Black Marketeer', 'Investors', 'Sales Pitch', 'Self-Made'], belongings=[], contacts=[])
EXPLORER = Archetype('Explorer', skills={STUDY: 2, SURVIVE: 2, 'Choose 1': [FIGHT, TINKER]}, styles={'Choose 2': [CAREFULLY, FORCEFULLY, SWIFTLY]}, focuses=[BOATS, MEDICINE, NATURAL_PHILOSOPHY, RESILIANCE, RESOLVE, SHIPS, SWIMMING, TRACKING, WILDERNESS], talents=['Expert Cartographer', 'First Glance', 'Hardy Traveler', 'Surveyor'], belongings=[], contacts=[])
GUIDE = Archetype('Guide', skills={MOVE: 2, SURVIVE: 2, 'Choose 1': [TALK, TINKER]}, styles={'Choose 2': [CAREFULLY, FORCEFULLY, SWIFTLY]}, focuses=[ETIQUETTE, RESILIANCE, RESOLVE, STREETWISE, TRACKING, WILDERNESS], talents=['Companion', 'Fieldcraft', 'Forager', 'Sage Advice'], belongings=[], contacts=[])
HUNTER = Archetype('Hunter', skills={SURVIVE: 2, TINKER: 2, 'Choose 1': [FIGHT, STUDY]}, styles={'Choose 2': [CAREFULLY, CLEVERLY, QUIETLY]}, focuses=[ARCHERY, EXPLOSIVES, FIREARMS, STEALTH, STREETWISE, TRACKING, WILDERNESS], talents=['Ambush Expertise', 'Familiar Tactics', 'Predator\'s Patience', 'Trapper'], belongings=[], contacts=[])
INVENTOR = Archetype('Inventor', skills={STUDY: 2, TINKER: 2, 'Choose 1': [SURVIVE, TALK]}, styles={'Choose 2': [BOLDLY, CAREFULLY, CLEVERLY]}, focuses=[CARRIAGES, ENGINEERING, EXPLOSIVES, FIREARMS, LOCKS, MEDICINE, NATURAL_PHILOSOPHY, SURGERY], talents=['Controlled Detonation', 'Personal Notes', 'Pushing the Boundaries of Progress', 'Salvage for Parts'], belongings=[], contacts=[])
SCHOLAR = Archetype('Scholar', skills={TALK: 2, STUDY: 2, 'Choose 1': [SURVIVE, TINKER]}, styles={'Choose 2': [BOLDLY, CLEVERLY, FORCEFULLY]}, focuses=[COUNSEL, ETIQUETTE, HISTORY, MEDICINE, NATURAL_PHILOSOPHY, SOCIETY, THEOLOGY, VOID_LORE], talents=['Deep Expertise', 'Did the Research', 'Erudite Exposition', 'Librarian'], belongings=[], contacts=[])
SCOUT = Archetype('Scout', skills={MOVE: 2, STUDY: 2, 'Choose 1': [FIGHT, TALK]}, styles={'Choose 2': [CAREFULLY, CLEVERLY, QUIETLY]}, focuses=[CONCERNTRATE, ETIQUETTE, FREERUNNING, INNUENDO, RESOLVE, SOCIETY, STEALTH, STREETWISE, TRACKING], talents=['Constantly Alert', 'Fighting Fit', 'Hit and Run', 'Like a Shadow'], belongings=[], contacts=[])
SHARPSHOOTER = Archetype('Sharpshooter', skills={FIGHT: 2, TINKER: 2, 'Choose 1': [MOVE, STUDY]}, styles={'Choose 2': [BOLDLY, CAREFULLY, SWIFTLY]}, focuses=[ARCHERY, ENGINEERING, EXPLOSIVES, FIREARMS, RESOLVE, STEALTH], talents=['Crack Shot', 'Exploit Weakness', 'Prized Weapon', 'Saboteur'], belongings=[], contacts=[])
MISCREANT = Archetype('Miscreant', skills={FIGHT: 2, SURVIVE: 2, 'Choose 1': [MOVE, TALK]}, styles={'Choose 2': [BOLDLY, CAREFULLY, FORCEFULLY]}, focuses=[BRAWLING, INTIMIDATE, RESILIANCE, RESOLVE, SWORDS], talents=['Dautless', 'Fight Dirty', 'Put Your Back Into It!', 'Shoulder Charge'], belongings=[], contacts=[])
