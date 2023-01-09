import random

class ABC:
    def __init__(self, name, **kwargs):
        self.name = name
        for k, d in kwargs.items():
            self.__setattr__(k, d)

    def __repr__(self):
        return self.__format__()
    
    def __format__(self):
        return self.name

class Ancestory(ABC):
    items = []
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        Ancestory.items.append(self)

class Profession(ABC):
    items = []
    def __init__(self, name, _type, **kwargs):
        super().__init__(name, **kwargs)
        self._type = _type
        Profession.items.append(self)


HUMAN = Ancestory("Human")
CHANGELING = Ancestory("Changling")
CLOCKWORK = Ancestory("Clockwork")
DWARF = Ancestory("Dwarf")
GOBLIN = Ancestory("Goblin")
ORC = Ancestory("Orc")
ANCESTORIES = [HUMAN, CHANGELING, CLOCKWORK, DWARF, GOBLIN, ORC]

ANIMAL_TRAINER = Profession("Animal_Trainer", _type='Common')
APOTHECARY = Profession("Apothecary", _type='Common')
HEALER = Profession("Healer", _type='Common')
ARTISAN = Profession("Artisan", _type='Common', _subtype=['Baker', 'Blacksmith', 'Bookbinder', 'Brewer', 'Carpenter', 'Chandler', 'Cobbler', 'Dyer', 'Glassblower', 'Jeweler', 'Leatherworker', 'Mason', 'Potter', 'Printer', 'Tailor'])
ARTIST = Profession("Artist", _type='Common', _subtype=['Painter', 'Poet', 'Sculptor', 'Writer'])
BOATMAN = Profession("Boatman", _type='Common')
BUTCHER = Profession("Butcher", _type='Common')
COOK = Profession("Cook", _type='Common')
DROVER = Profession("Drover", _type='Common')
HERDER = Profession("Herder", _type='Common')
ENTERTAINER = Profession("Entertainer", _type='Common', _subtype=['Actor', 'Athlete', 'Comedian', 'Courtesan', 'Dancer', 'Orator', 'Puppeteer', 'Singer', 'Storyteller'])
FARMER = Profession("Farmer", _type='Common')
FISHER = Profession("Fisher", _type='Common')
WHALER = Profession("Whaler", _type='Common')
GROOM = Profession("Groom", _type='Common')
LABORER = Profession("Laborer", _type='Common', _subtype=['Chimneysweep', 'Gravedigger', 'Porter', 'Stevedore', 'Street-Sweeper'])
MERCHANT = Profession("Merchant", _type='Common', _subtype=['Arms', 'Grains', 'Livestock', 'Slaves', 'Spices', 'Textiles'])
MINER = Profession("Miner", _type='Common')
MUSICIAN = Profession("Musician", _type='Common', _instrument=['Percussion', 'String', 'Wind'])
SAILOR = Profession("Sailor", _type='Common')
SERVANT = Profession("Servant", _type='Common')
VALET = Profession("Valet", _type='Common')
SHOPKEEPER = Profession("Shopkeeper", _type='Common')
TEAMSTER = Profession("Teamster", _type='Common')

SCHOLAR_ARCHITECTURE = Profession("Scholar of Architecture", _type='Academic')
SCHOLAR_ASTROLOGY = Profession("Scholar of Astrology", _type='Academic')
SCHOLAR_ENGINEERING = Profession("Scholar of Engineering", _type='Academic')
SCHOLAR_ETIQUETTE = Profession("Scholar of Etiquette", _type='Academic')
SCHOLAR_FOLKLORE = Profession("Scholar of Folklore", _type='Academic')
SCHOLAR_GEOGRAPHY = Profession("Scholar of Geography", _type='Academic')
SCHOLAR_HERALDRY = Profession("Scholar of Heraldry", _type='Academic')
SCHOLAR_HISTORY = Profession("Scholar of History", _type='Academic')
SCHOLAR_LAW = Profession("Scholar of Law", _type='Academic')
SCHOLAR_LITERATURE = Profession("Scholar of Literature", _type='Academic')
SCHOLAR_MAGIC = Profession("Scholar of Magic", _type='Academic')
SCHOLAR_MEDICINE = Profession("Scholar of Medicine", _type='Academic')
SCHOLAR_NAVIGATION = Profession("Scholar of Navigation", _type='Academic')
SCHOLAR_OCCULT = Profession("Scholar of Occult", _type='Academic')
SCHOLAR_PHILOSOPHY = Profession("Scholar of Philosophy", _type='Academic')
SCHOLAR_POLITICS = Profession("Scholar of Politics", _type='Academic')
SCHOLAR_NATURE = Profession("Scholar of Nature", _type='Academic')
SCHOLAR_RELIGION = Profession("Scholar of Religion", _type='Academic')
SCHOLAR_SCIENCE = Profession("Scholar of Science", _type='Academic')
SCHOLAR_WAR = Profession("Scholar of War", _type='Academic')

AGITATOR = Profession("Agitator", _type='Criminal')
BEGGAR = Profession("Beggar", _type='Criminal')
BURGLAR = Profession("Burglar", _type='Criminal')
CAROUSER = Profession("Carouser", _type='Criminal')
RAKE = Profession("Rake", _type='Criminal')
CHARLATAN = Profession("Charlatan", _type='Criminal')
CONFIDENCE_ARTIST = Profession("Confidence_Artist", _type='Criminal')
CULTIST = Profession("Cultist", _type='Criminal')
FENCE = Profession("Fence", _type='Criminal')
FORGER = Profession("Forger", _type='Criminal')
GAMBLER = Profession("Gambler", _type='Criminal')
GRAVE_ROBBER = Profession("Grave_Robber", _type='Criminal')
INFORMANT = Profession("Informant", _type='Criminal')
MURDERER = Profession("Murderer", _type='Criminal')
PICKPOCKET = Profession("Pickpocket", _type='Criminal')
PIRATE = Profession("Pirate", _type='Criminal')
PROSITUTE = Profession("Prositute", _type='Criminal')
REBEL = Profession("Rebel", _type='Criminal')
TERRORIST = Profession("Terrorist", _type='Criminal')
SABOTEUR = Profession("Saboteur", _type='Criminal')
SPY = Profession("Spy", _type='Criminal')
THUG = Profession("Thug", _type='Criminal')
URCHIN = Profession("Urchin", _type='Criminal')

CONSTABLE = Profession("Constable", _type='Martial')
DETECTIVE = Profession("Detective", _type='Martial')
GUARD = Profession("Guard", _type='Martial')
JAILER = Profession("Jailer", _type='Martial')
OFFICER = Profession("Officer", _type='Martial')
MARINE = Profession("Marine", _type='Martial')
MERCENARTY = Profession("Mercenarty", _type='Martial')
MILITIA_MEMBER = Profession("Militia_Member", _type='Martial')
PARTOLLER = Profession("Partoller", _type='Martial')
PEASANT_CONSCRIPT = Profession("Peasant_Conscript", _type='Martial')
SLAVE = Profession("Slave", _type='Martial')
SOLIDER = Profession("Solider", _type='Martial')
SQUIRE = Profession("Squire", _type='Martial')
TORTUER = Profession("Tortuer", _type='Martial')

BANDIT = Profession("Bandit", _type='Wilderness')
BRIGAND = Profession("Brigand", _type='Wilderness')
HIGHWAY_ROBBER = Profession("Highway_Robber", _type='Wilderness')
BARBARIAN = Profession("Barbarian", _type='Wilderness')
EXILE = Profession("Exile", _type='Wilderness')
GATHERER = Profession("Gatherer", _type='Wilderness')
GUIDE = Profession("Guide", _type='Wilderness')
HERMIT = Profession("Hermit", _type='Wilderness')
HUNTER = Profession("Hunter", _type='Wilderness')
NOMAND = Profession("Nomand", _type='Wilderness')
VAGABOND = Profession("Vagabond", _type='Wilderness')
PIONEER = Profession("Pioneer", _type='Wilderness')
POACHER = Profession("Poacher", _type='Wilderness')
RUSTLER = Profession("Rustler", _type='Wilderness')
PROSPECTOR = Profession("Prospector", _type='Wilderness')
OUTLAW = Profession("Outlaw", _type='Wilderness')
REFUGEE = Profession("Refugee", _type='Wilderness')
SPELUNKER = Profession("Spelunker", _type='Wilderness')
TRACKER = Profession("Tracker", _type='Wilderness')
TRAPPER = Profession("Trapper", _type='Wilderness')
WOODCUTTER = Profession("Woodcutter", _type='Wilderness')

DEVOTEE = Profession("Devotee", _type='Religious')
EVANGELIST = Profession("Evangelist", _type='Religious')
FLAGELLANT = Profession("Flagellant", _type='Religious')
HERETIC = Profession("Heretic", _type='Religious')
INITIATE_OF_THE_OLD_FAITH = Profession("Initiate_of_the_Old_Faith", _type='Religious')
MINISTER = Profession("Minister", _type='Religious')
ACOLYUTE_OF_THE_NEW_GOD = Profession("Acolyute_of_the_New_God", _type='Religious')
INQUISITORS_HENCHMEN = Profession("Inquisitors_Henchmen", _type='Religious')
PILGRIM = Profession("Pilgrim", _type='Religious')
STREET_PREACHER = Profession("Street_Preacher", _type='Religious')
TEMPLE_WARD = Profession("Temple_Ward", _type='Religious')

PROFESSION_TYPES = []
for _type in [i._type for i in Profession.items]:
    if _type not in PROFESSION_TYPES:
        PROFESSION_TYPES.append(_type)
    else: 
        continue

def choose_ancestory():
    return random.choice(ANCESTORIES)

def choose_profession(prof_type = None):
    if prof_type == None:
        prof_type = random.choice(PROFESSION_TYPES)
    if not isinstance(prof_type, str) or prof_type not in [p._type for p in Profession.items]:
        raise ValueError("Invalid profession type silly. Input is probably case sensitive.")
    return random.choice([prof for prof in Profession.items if prof._type == prof_type])

def first_run_demo():
    ancestory = choose_ancestory()
    profession = choose_profession()
    if ancestory == ORC:
        print(f'You are an {ancestory.name} {profession.name}')
    else:
        print(f'You are a {ancestory.name} {profession.name}')

for i in range(10):
    first_run_demo()