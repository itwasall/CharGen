import random
"""
TODO:
    - Insert random.choice's in Interesting Item's where applicable 
    - Flesh out Ancestries
    - Flesh out Novice/Expert/Master Paths
"""

def attrAsDict(_class):
    return [{i: _class._getattr(i)} for i in dir(_class) if not i.startswith("__")]

def dice(dicestring):
    throws, sides = dicestring.split("d")
    return sum([random.randint(1, int(sides)) for _ in range(int(throws))])

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

class InterestingItem(ABC):
    items = []
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        InterestingItem.items.append(self)

class Path(ABC):
    items = []
    def __init__(self, name, _type, **kwargs):
        super().__init__(name, **kwargs)
        self._type = _type
        Path.items.append(self)

class AttributeScore:
    def __init__(self, name, value=0, **kwargs):
        self.name = name
        self.value = value

    def __add__(self, value):
        self.value = self.value + value
        return AttributeScore(self.name, self.value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __repr__(self):
        return str(self.value)

class AttributeBlock:
    def __init__(self, strength: AttributeScore, agility: AttributeScore, intellect: AttributeScore, will: AttributeScore):
        self.strength = strength
        self.agility = agility
        self.intellect = intellect
        self.will = will

    def __repr__(self):
        return self.__format__()

    def __format__(self):
        self.return_string = f"Strength: {self.strength}\nAgility: {self.agility}\nIntellect: {self.intellect}\nWill: {self.will}"
        return self.return_string
    

STRENGTH = AttributeScore('Strength')
AGILITY = AttributeScore('Agility')
INTELLECT = AttributeScore('Intellect')
WILL = AttributeScore('Will')

STAT_BLOCK = AttributeBlock(STRENGTH, AGILITY, INTELLECT, WILL)
# print(STAT_BLOCK)

"""
    ANCESTORIES
"""
# ssb = Starting_Stat_Block
HUMAN = Ancestory("Human", height=[3, 7], weight=[50, 500], age=[18, 70], ssb=[10, 10, 10, 10], stat_increase={'Any': 1}, perception={'Intellect': '='}, defence={'Agility': '='}, health={'Strength': '='}, healing_rate={'Health': ['1/4', 'down']}, size=[0.5, 1], speed=10, power=0, damage=0, insanity=0, corruption=0, language=['Common', {'Choose': '1'}]6)
CHANGELING = Ancestory("Changling", ssb=[], stat_increase={}, perception=, defence=, health=, healing_rate=, size=, speed=, power=, damage=, insanity=, corruption=, language=[])
CLOCKWORK = Ancestory("Clockwork", ssb=[], stat_increase={}, perception=, defence=, health=, healing_rate=, size=, speed=, power=, damage=, insanity=, corruption=, language=[])
DWARF = Ancestory("Dwarf", ssb=[], stat_increase={}, perception=, defence=, health=, healing_rate=, size=, speed=, power=, damage=, insanity=, corruption=, language=[])
GOBLIN = Ancestory("Goblin", ssb=[], stat_increase={}, perception=, defence=, health=, healing_rate=, size=, speed=, power=, damage=, insanity=, corruption=, language=[])
ORC = Ancestory("Orc", ssb=[], stat_increase={}, perception=, defence=, health=, healing_rate=, size=, speed=, power=, damage=, insanity=, corruption=, language=[])
ANCESTORIES = [HUMAN, CHANGELING, CLOCKWORK, DWARF, GOBLIN, ORC]

def gen_ancestory_demo():
    an = random.choice(ANCESTORIES)
    an_attr = attrAsDict(an)
    attributes_generated = []

    for attr in an_attr:
        match list(attr.keys())[0]:
            case 'ssb':
                pass
            case 'stat_increase':
                pass
            case 'perception':
                pass
            case 'defence':
                pass
            case 'health':
                pass
            case 'healing_rate':
                pass
            case 'size':
                pass
            case 'speed':
                pass
            case 'power':
                pass
            case 'damage':
                pass
            case 'insanity':
                pass
            case 'corruption':
                pass
            case 'language':
                pass

"""
    PROFESSIONS
"""
# COMMON
ANIMAL_TRAINER = Profession("Animal_Trainer", _type='Common')
APOTHECARY = Profession("Apothecary", _type='Common')
HEALER_P = Profession("Healer", _type='Common')
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
# ACADEMIC
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
# CRIMINAL
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
GRAVE_ROBBER = Profession("Grave Robber", _type='Criminal')
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
# MARTIAL
CONSTABLE = Profession("Constable", _type='Martial')
DETECTIVE = Profession("Detective", _type='Martial')
GUARD = Profession("Guard", _type='Martial')
JAILER = Profession("Jailer", _type='Martial')
OFFICER = Profession("Officer", _type='Martial')
MARINE = Profession("Marine", _type='Martial')
MERCENARTY = Profession("Mercenarty", _type='Martial')
MILITIA_MEMBER = Profession("Militia Member", _type='Martial')
PARTOLLER = Profession("Partoller", _type='Martial')
PEASANT_CONSCRIPT = Profession("Peasant Conscript", _type='Martial')
SLAVE = Profession("Slave", _type='Martial')
SOLIDER = Profession("Solider", _type='Martial')
SQUIRE = Profession("Squire", _type='Martial')
TORTUER = Profession("Tortuer", _type='Martial')
# WILDERNESS
BANDIT = Profession("Bandit", _type='Wilderness')
BRIGAND = Profession("Brigand", _type='Wilderness')
HIGHWAY_ROBBER = Profession("Highway Robber", _type='Wilderness')
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
# RELIGIOUS
DEVOTEE = Profession("Devotee", _type='Religious')
EVANGELIST = Profession("Evangelist", _type='Religious')
FLAGELLANT = Profession("Flagellant", _type='Religious')
HERETIC = Profession("Heretic", _type='Religious')
INITIATE_OF_THE_OLD_FAITH = Profession("Initiate of the Old Faith", _type='Religious')
MINISTER = Profession("Minister", _type='Religious')
ACOLYUTE_OF_THE_NEW_GOD = Profession("Acolyute of the New God", _type='Religious')
INQUISITORS_HENCHMEN = Profession("Inquisitors Henchmen", _type='Religious')
PILGRIM = Profession("Pilgrim", _type='Religious')
STREET_PREACHER = Profession("Street Preacher", _type='Religious')
TEMPLE_WARD = Profession("Temple Ward", _type='Religious')

PROFESSION_TYPES = []
for _type in [i._type for i in Profession.items]:
    if _type not in PROFESSION_TYPES:
        PROFESSION_TYPES.append(_type)
    else: 
        continue

"""
    INTERESTING ITEMS
"""
# TABLE 1
TABLE1_ITEM1 = InterestingItem("A tiny metal box with no opening that makes a faint ticking noise.")
TABLE1_ITEM2 = InterestingItem("A skull made from clear crystal.")
TABLE1_ITEM3 = InterestingItem("A glass ball filled with water in which swims a tiny living goldfish.")
TABLE1_ITEM4 = InterestingItem(f"{random.choice(['A curious odor', 'a pungent stench', 'a skin condition that never quite heals'])}.")
TABLE1_ITEM5 = InterestingItem("A bottle filled with a maiden’s tears.")
TABLE1_ITEM6 = InterestingItem("A flower that never withers.")
TABLE1_ITEM7 = InterestingItem(f"{random.choice(['A small magnet', 'a silver mirror'])}.")
TABLE1_ITEM8 = InterestingItem(f"An invitation to a {random.choice(['party', 'masquerade mask'])}.")
TABLE1_ITEM9 = InterestingItem("A monogrammed handkerchief that always stays clean.")
TABLE1_ITEM10 = InterestingItem("A folding knife that always stays sharp.")
TABLE1_ITEM11 = InterestingItem("A pair of dancing shoes.")
TABLE1_ITEM12 = InterestingItem("A tiny inert mechanical spider.")
TABLE1_ITEM13 = InterestingItem("A shrunken head.")
TABLE1_ITEM14 = InterestingItem(f"{random.choice(['A glass eye', 'a bezoar'])}.")
TABLE1_ITEM15 = InterestingItem(f"A book {random.choice(['written in an unknown language', 'a book containing things you never wanted to know'])}.")
TABLE1_ITEM16 = InterestingItem("A deck of fortune-teller’s cards.")
TABLE1_ITEM17 = InterestingItem("A pair of loaded dice.")
TABLE1_ITEM18 = InterestingItem("Six small cakes that can nourish the person who eats one until the next day at dawn.")
TABLE1_ITEM19 = InterestingItem("A phylactery that holds a scrap of paper on which is written a single word.")
TABLE1_ITEM20 = InterestingItem("A reputation for being a badass")
ITEM_TABLE_1 = [TABLE1_ITEM1, TABLE1_ITEM2, TABLE1_ITEM3, TABLE1_ITEM4, TABLE1_ITEM5, TABLE1_ITEM6, TABLE1_ITEM7, TABLE1_ITEM8, TABLE1_ITEM9, TABLE1_ITEM10, TABLE1_ITEM11, TABLE1_ITEM12, TABLE1_ITEM13, TABLE1_ITEM14, TABLE1_ITEM15, TABLE1_ITEM16, TABLE1_ITEM17, TABLE1_ITEM18, TABLE1_ITEM19, TABLE1_ITEM20]
# TABLE 2
TABLE2_ITEM1 = InterestingItem(f"{random.choice(['A flute', 'a set of panpipes', 'a musical instrument'])}.")
TABLE2_ITEM2 = InterestingItem(f"A reliquary containing a small bone.")
TABLE2_ITEM3 = InterestingItem(f"A tiny idol of a demon carved from green stone.")
TABLE2_ITEM4 = InterestingItem(f"A token from {random.choice(['an admirer', 'a lover'])}.")
TABLE2_ITEM5 = InterestingItem(f"A pet {random.choice(['mouse', 'squirrel', 'rabbit'])}.")
TABLE2_ITEM6 = InterestingItem(f"{random.choice(['A monocle', 'A pair of heavy goggles'])}.")
TABLE2_ITEM7 = InterestingItem(f"A silver necklace with a medallion.")
TABLE2_ITEM8 = InterestingItem(f"A snuffbox filled with snuff.")
TABLE2_ITEM9 = InterestingItem(f"A gleaming dragon’s scale.")
TABLE2_ITEM10= InterestingItem(f"A fist-sized egg covered in blue spots.")
TABLE2_ITEM11= InterestingItem(f"Unrequited love.")
TABLE2_ITEM12= InterestingItem(f"A black iron cauldron filled with bones.")
TABLE2_ITEM13= InterestingItem(f"A box of {dice('1d20')} iron nails.")
TABLE2_ITEM14= InterestingItem(f"{random.choice(['A vial of sweet perfume', 'A bottle of rotgut'])}.")
TABLE2_ITEM15= InterestingItem(f"A feather made from bronze.")
TABLE2_ITEM16= InterestingItem(f"{random.choice(['An iron coin with a scratch on one side', 'a steel coin with a dragon’s head on either side'])}.")
TABLE2_ITEM17= InterestingItem(f"A box containing {sum([dice('1d6'), 1])} brushes.")
TABLE2_ITEM18= InterestingItem(f"A bloodstained doll.")
TABLE2_ITEM19= InterestingItem(f"A silver engagement ring worth 1 ss.")
TABLE2_ITEM20= InterestingItem(f"{random.choice(['A brush', 'A comb', 'An umbrella'])}.")
ITEM_TABLE_2 = [TABLE2_ITEM1, TABLE2_ITEM2, TABLE2_ITEM3, TABLE2_ITEM4, TABLE2_ITEM5, TABLE2_ITEM6, TABLE2_ITEM7, TABLE2_ITEM8, TABLE2_ITEM9, TABLE2_ITEM10, TABLE2_ITEM11, TABLE2_ITEM12, TABLE2_ITEM13, TABLE2_ITEM14, TABLE2_ITEM15, TABLE2_ITEM16, TABLE2_ITEM17, TABLE2_ITEM18, TABLE2_ITEM19, TABLE2_ITEM20]
# TABLE 3
TABLE3_ITEM1 = InterestingItem(f"{random.choice(['A bar of soap', 'A towel'])}.")
TABLE3_ITEM2 = InterestingItem(f"One hundred feet of twine wrapped up in a ball.")
TABLE3_ITEM3 = InterestingItem(f"{random.choice(['A tiny portrait', 'a lock of hair', 'a favor'])} from someone who loves you.")
TABLE3_ITEM4 = InterestingItem(f"A small keg of beer.")
TABLE3_ITEM5 = InterestingItem(f"{random.choice(['A brace of conies', 'a pack'])} filled with pots and pans.")
TABLE3_ITEM6 = InterestingItem(f"An arrow with a silvered head.")
TABLE3_ITEM7 = InterestingItem(f"{random.choice(['Half a treasure map', 'a map of a foreign land', 'a large, blue map covered with circles with weird bits of writing between them'])}.")
TABLE3_ITEM8 = InterestingItem(f"A weapon of the GM’s choice.")
TABLE3_ITEM9 = InterestingItem(f"A {random.choice(['light', 'heavy'])} shield with an unusual heraldic device.")
TABLE3_ITEM10= InterestingItem(f"A fancy set of clothes bearing a curious stain.")
TABLE3_ITEM11= InterestingItem(f"A personal servant.")
TABLE3_ITEM12= InterestingItem(f"A silver holy symbol or a fine religious icon.")
TABLE3_ITEM13= InterestingItem(f"A bag of {dice('2d6')} {random.choice(['rocks', 'acorns', 'severed heads', 'yummy mushrooms'])}.")
TABLE3_ITEM14= InterestingItem(f"A music box that plays a sad, sad song when opened.")
TABLE3_ITEM15= InterestingItem(f"A bag of 100 marbles.")
TABLE3_ITEM16= InterestingItem(f"A glass jar filled with {random.choice(['saliva', 'a sack filled with rotting chicken parts', 'an unseemly scar'])}.")
TABLE3_ITEM17= InterestingItem(f"A small bag containing 3d6 teeth, a necklace of 1d6 ears, or {dice('1d6')} severed heads tied together by their hair.")
TABLE3_ITEM18= InterestingItem(f"A newborn baby that might or might not be yours.")
TABLE3_ITEM19= InterestingItem(f"A box of six fine white candles.")
TABLE3_ITEM20= InterestingItem(f"A small dog with a tendency toward viciousness.")
ITEM_TABLE_3 = [TABLE3_ITEM1, TABLE3_ITEM2, TABLE3_ITEM3, TABLE3_ITEM4, TABLE3_ITEM5, TABLE3_ITEM6, TABLE3_ITEM7, TABLE3_ITEM8, TABLE3_ITEM9, TABLE3_ITEM10, TABLE3_ITEM11, TABLE3_ITEM12, TABLE3_ITEM13, TABLE3_ITEM14, TABLE3_ITEM15, TABLE3_ITEM16, TABLE3_ITEM17, TABLE3_ITEM18, TABLE3_ITEM19, TABLE3_ITEM20]
# TABLE 4
TABLE4_ITEM1 = InterestingItem(f"A glass jar holding a beetle covered in glowing spots (sheds light as a candle).")
TABLE4_ITEM2 = InterestingItem(f"A pair of boots that grants you 1 boon for rolls to sneak or a gray cloak that grants you 1 boon for rolls to hide.")
TABLE4_ITEM3 = InterestingItem(f"A glass jar containing a strange organ suspended in alcohol.")
TABLE4_ITEM4 = InterestingItem(f"A tiny glass cage.")
TABLE4_ITEM5 = InterestingItem(f"A box containing {sum([dice('1d6'), 1])} bottles of ink, each a different color.")
TABLE4_ITEM6 = InterestingItem(f"A tiny inert mechanical owl.")
TABLE4_ITEM7 = InterestingItem(f"A length of rope, 20 yards long, that cannot be cut.")
TABLE4_ITEM8 = InterestingItem(f"A badge from a mercenary company.")
TABLE4_ITEM9 = InterestingItem(f"{random.choice(['A box of cigars', 'a pipe and pouch of tobacco'])}.")
TABLE4_ITEM10= InterestingItem(f"A medallion depicting a hideous woman's face.")
TABLE4_ITEM11= InterestingItem(f"A spiked collar, skin clamps, and a scourge.")
TABLE4_ITEM12= InterestingItem(f"A ten-pound bag of flour.")
TABLE4_ITEM13= InterestingItem(f"A bronze plate with a name scratched on its face.")
TABLE4_ITEM14= InterestingItem(f"A crystal bottle containing fluid that emits light in a 2-yard radius when the stopper is removed.")
TABLE4_ITEM15= InterestingItem(f"A small box holding six sticks of chalk.")
TABLE4_ITEM16= InterestingItem(f"A letter of introduction from a powerful and influential person.")
TABLE4_ITEM17= InterestingItem(f"A mirror fragment that shows a strange location on its reflective surface.")
TABLE4_ITEM18= InterestingItem(f"A small golden cage containing a living faerie that cannot talk.")
TABLE4_ITEM19= InterestingItem(f"A bottle labeled 'Eye of Newt.'")
TABLE4_ITEM20= InterestingItem(f"A bag of beans.")
ITEM_TABLE_4 = [TABLE4_ITEM1, TABLE4_ITEM2, TABLE4_ITEM3, TABLE4_ITEM4, TABLE4_ITEM5, TABLE4_ITEM6, TABLE4_ITEM7, TABLE4_ITEM8, TABLE4_ITEM9, TABLE4_ITEM10, TABLE4_ITEM11, TABLE4_ITEM12, TABLE4_ITEM13, TABLE4_ITEM14, TABLE4_ITEM15, TABLE4_ITEM16, TABLE4_ITEM17, TABLE4_ITEM18, TABLE4_ITEM19, TABLE4_ITEM20]
# TABLE 5
TABLE5_ITEM1 = InterestingItem(f"{random.choice(['A jar of grease', 'a bottle of glue'])}.")
TABLE5_ITEM2 = InterestingItem(f"A glass globe filled with swirling mist.")
TABLE5_ITEM3 = InterestingItem(f"A cloak with {dice('2d20')} pockets hidden in the lining.")
TABLE5_ITEM4 = InterestingItem(f"A pair of spectacles that sometimes let you see through up to 1 inch of solid rock.")
TABLE5_ITEM5 = InterestingItem(f"A small blue box that's bigger on the inside (twice normal capacity).")
TABLE5_ITEM6 = InterestingItem(f"A small steel ball.")
TABLE5_ITEM7 = InterestingItem(f"A petrified hand that twitches in the light of a full moon.")
TABLE5_ITEM8 = InterestingItem(f"The true name of a very minor devil.")
TABLE5_ITEM9 = InterestingItem(f"An animated mouse skeleton.")
TABLE5_ITEM10= InterestingItem(f"A weapon that always emits light in a 1-yard radius.")
TABLE5_ITEM11= InterestingItem(f"A pouch that holds {sum([dice('1d6'), 1])} pinches of dust that, when sprinkled over stone, causes up to a 1-yard cube of material to become soft clay.")
TABLE5_ITEM12= InterestingItem(f"A jar of paint that refills itself once each day at dawn.")
TABLE5_ITEM13= InterestingItem(f"A tiny metal ball that when released floats 1 inch above any solid surface.")
TABLE5_ITEM14= InterestingItem(f"A pouch holding {sum([dice('1d6'), 1])} pinches of diamond dust.")
TABLE5_ITEM15= InterestingItem(f"A brain in a jar.")
TABLE5_ITEM16= InterestingItem(f"A bag filled with curiously fleshy rods.")
TABLE5_ITEM17= InterestingItem(f"A mace made from purple metal with a name etched on the haft.")
TABLE5_ITEM18= InterestingItem(f"A giant piece of charcoal that radiates menace.")
TABLE5_ITEM19= InterestingItem(f"A piece of amber containing a human-faced fly.")
TABLE5_ITEM20= InterestingItem(f"A lifetime of regrets.")
ITEM_TABLE_5 = [TABLE5_ITEM1, TABLE5_ITEM2, TABLE5_ITEM3, TABLE5_ITEM4, TABLE5_ITEM5, TABLE5_ITEM6, TABLE5_ITEM7, TABLE5_ITEM8, TABLE5_ITEM9, TABLE5_ITEM10, TABLE5_ITEM11, TABLE5_ITEM12, TABLE5_ITEM13, TABLE5_ITEM14, TABLE5_ITEM15, TABLE5_ITEM16, TABLE5_ITEM17, TABLE5_ITEM18, TABLE5_ITEM19, TABLE5_ITEM20]
# TABLE 6
TABLE6_ITEM1 = InterestingItem(f"A reputation for being a skilled lover.")
TABLE6_ITEM2 = InterestingItem(f"A mummified halfling.")
TABLE6_ITEM3 = InterestingItem(f"A set of clothing that can change appearance once each day at dusk.")
TABLE6_ITEM4 = InterestingItem(f"A can of beets.")
TABLE6_ITEM5 = InterestingItem(f"A stalker who follows you but flees when you approach.")
TABLE6_ITEM6 = InterestingItem(f"A shameful past.")
TABLE6_ITEM7 = InterestingItem(f"A recurring and disturbing dream.")
TABLE6_ITEM8 = InterestingItem(f"A trunk filled with body parts.")
TABLE6_ITEM9 = InterestingItem(f"A wagon or cart pulled by a sad donkey.")
TABLE6_ITEM10= InterestingItem(f"Three small white mice that whisper strange things to you while you sleep.")
TABLE6_ITEM11= InterestingItem(f"{random.choice(['A tremor', 'a facial tic', 'an irritating laugh'])}.")
TABLE6_ITEM12= InterestingItem(f"A thermometer.")
TABLE6_ITEM13= InterestingItem(f"A collapsible pole, 3 yards long.")
TABLE6_ITEM14= InterestingItem(f"A shadow you cast that never quite matches your movements.")
TABLE6_ITEM15= InterestingItem(f"Fear and loathing.")
TABLE6_ITEM16= InterestingItem(f"A fondness for the bottle.")
TABLE6_ITEM17= InterestingItem(f"A thin shirt of mail that counts as light armor and can be worn under normal clothing (functions as mail and is not cumulative with other armor).")
TABLE6_ITEM18= InterestingItem(f"A bizarre fetish.")
TABLE6_ITEM19= InterestingItem(f"A demanding spouse.")
TABLE6_ITEM20= InterestingItem(f"A terrible secret that you dare not reveal.")
ITEM_TABLE_6 = [TABLE6_ITEM1, TABLE6_ITEM2, TABLE6_ITEM3, TABLE6_ITEM4, TABLE6_ITEM5, TABLE6_ITEM6, TABLE6_ITEM7, TABLE6_ITEM8, TABLE6_ITEM9, TABLE6_ITEM10, TABLE6_ITEM11, TABLE6_ITEM12, TABLE6_ITEM13, TABLE6_ITEM14, TABLE6_ITEM15, TABLE6_ITEM16, TABLE6_ITEM17, TABLE6_ITEM18, TABLE6_ITEM19, TABLE6_ITEM20]
# LIST
ITEM_TABLES = [ITEM_TABLE_1, ITEM_TABLE_2, ITEM_TABLE_3, ITEM_TABLE_4, ITEM_TABLE_5, ITEM_TABLE_6]

"""
    PATHS
"""
# NOVICE
MAGICIAN = Path("Magician", 'Novice')
PRIEST = Path("Priest", 'Novice')
ROGUE = Path("Rogue", 'Novice')
WARRIOR = Path("Warrior", 'Novice')
NOVICE_PATHS = [p for p in Path.items if p._type == 'Novice']
# EXPERT
ARTIFICER = Path("Artificer", 'Expert')
ASSASSIN = Path("Assassin", 'Expert')
BERSERKER = Path("Berserker", 'Expert')
CLERIC = Path("Cleric", 'Expert')
DRUID = Path("Druid", 'Expert')
FIGHTER = Path("Fighter", 'Expert')
ORACLE = Path("Oracle", 'Expert')
PALADIN = Path("Paladin", 'Expert')
RANGER = Path("Ranger", 'Expert')
SCOUT = Path("Scout", 'Expert')
SPELLBINDER = Path("Spellbinder", 'Expert')
THIEF = Path("Thief", 'Expert')
WARLOCK = Path("Warlock", 'Expert')
WITCH = Path("Witch", 'Expert')
WIZARD = Path("Wizard", 'Expert')
EXPERT_PATHS = [p for p in Path.items if p._type == 'Expert']
# MASTER
ABJURER = Path("Abjurer", 'Master')
ACROBAT = Path("Acrobat", 'Master')
AEROMANCER = Path("Aeromancer", 'Master')
APOCALYPTIST = Path("Apocalyptist", 'Master')
ARCANIST = Path("Arcanist", 'Master')
ASTROMANCER = Path("Astromancer", 'Master')
AVENGER = Path("Avenger", 'Master')
BARD = Path("Bard", 'Master')
BEASTMASTER = Path("Beastmaster", 'Master')
BLADE = Path("Blade", 'Master')
BRUTE = Path("Brute", 'Master')
CAVALIER = Path("Cavalier", 'Master')
CHAMPION = Path("Champion", 'Master')
CHAPLAIN = Path("Chaplain", 'Master')
CHRONOMANCER = Path("Chronomancer", 'Master')
CONJURER = Path("Conjurer", 'Master')
CONQUEROR = Path("Conqueror", 'Master')
DEATH_DEALER = Path("Death Dealer", 'Master')
DEFENDER = Path("Defender", 'Master')
DERVISH = Path("Dervish", 'Master')
DESTROYER = Path("Destroyer", 'Master')
DIPLOMAT = Path("Diplomat", 'Master')
DIVINER = Path("Diviner", 'Master')
DREADNAUGHT = Path("Dreadnaught", 'Master')
DUELIST = Path("Duelist", 'Master')
ENCHANTER = Path("Enchanter", 'Master')
ENGINEER = Path("Engineer", 'Master')
EXECUTIONER = Path("Executioner", 'Master')
EXORCIST = Path("Exorcist", 'Master')
EXPLORER = Path("Explorer", 'Master')
GEOMANCER = Path("Geomancer", 'Master')
GLADIATOR = Path("Gladiator", 'Master')
GUNSLINGER = Path("Gunslinger", 'Master')
HEALER = Path("Healer", 'Master')
HEXER = Path("Hexer", 'Master')
HYDROMANCER = Path("Hydromancer", 'Master')
ILLUSIONIST = Path("Illusionist", 'Master')
INFILTRATOR = Path("Infiltrator", 'Master')
INQUISITOR = Path("Inquisitor", 'Master')
JACK_OF_ALL_TRADES = Path("Jack of All Trades", 'Master')
MAGE_KNIGHT = Path("Mage Knight", 'Master')
MAGUS = Path("Magus", 'Master')
MARAUDER = Path("Marauder", 'Master')
MIRACLE_WORKER = Path("Miracle Worker", 'Master')
MYRMIDON = Path("Myrmidon", 'Master')
NECROMANCER = Path("Necromancer", 'Master')
POISONER = Path("Poisoner", 'Master')
PYROMANCER = Path("Pyromancer", 'Master')
RUNESMITH = Path("Runesmith", 'Master')
SAVANT = Path("Savant", 'Master')
SENTINEL = Path("Sentinel", 'Master')
SHAPESHIFTER = Path("Shapeshifter", 'Master')
SHARPSHOOTER = Path("Sharpshooter", 'Master')
STORMBRINGER = Path("Stormbringer", 'Master')
TECHNOMANCER = Path("Technomancer", 'Master')
TEMPLAR = Path("Templar", 'Master')
TENEBRIST = Path("Tenebrist", 'Master')
THAUMATURGE = Path("Thaumaturge", 'Master')
THEURGE = Path("Theurge", 'Master')
TRANSMUTER = Path("Transmuter", 'Master')
TRAVELER = Path("Traveler", 'Master')
WEAPON_MASTER = Path("Weapon Master", 'Master')
WOODWOSE = Path("Woodwose", 'Master')
ZEALOT = Path("Zealot", 'Master')
MASTER_PATHS = [p for p in Path.items if p._type == 'Master']

def choose_ancestory():
    return random.choice(ANCESTORIES)

def choose_profession(prof_type = None):
    if prof_type == None:
        prof_type = random.choice(PROFESSION_TYPES)
    if not isinstance(prof_type, str) or prof_type not in [p._type for p in Profession.items]:
        raise ValueError("Invalid profession type silly. Input is probably case sensitive.")
    return random.choice([prof for prof in Profession.items if prof._type == prof_type])

def choose_interesting_item():
    item_table = random.choice(ITEM_TABLES)
    return random.choice(item_table)


def run_demo():
    ancestory = choose_ancestory()
    profession = choose_profession()
    i_item = choose_interesting_item()
    i_item.name = i_item.name.lower()
    if ancestory == ORC:
        print(f'You are an {ancestory.name} {profession.name} with {i_item.name[:-1]}')
    else:
        print(f'You are a {ancestory.name} {profession.name} with {i_item.name[:-1]}')


for i in range(10):
    run_demo()
    pass