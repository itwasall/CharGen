import random

def dice(dicestring):
    mod = 0
    if len(dicestring.split('+')) > 1:
        dicestring, mod = dicestring.split('+')[0], int(dicestring.split('+')[1])
    throws, sides = [int(i) for i in dicestring.split('d')]
    return sum([mod, sum([random.randint(1, sides) for _ in range(throws)])])


class ABC:
    def __init__(self, name, **kwargs):
        self.name = name
        for k, d in kwargs:
            self.__setattr__(k, d)

    def __format__(self):
        return self.name

    def __repr__(self):
        return self.__format__()


class Gear(ABC):
    items = []
    def __init__(self, name, quantity=1, **kwargs):
        super().__init__(name, kwargs)
        self.quantity=quantity
        Gear.items.append(self)

"""
    GEAR
"""
# TABLE 1
MIRRORSHADES = Gear('Mirrorshades')
CWPC_METRO_CARD = Gear('CWPC_Metro_Card')
HANGOVER = Gear('Hangover')
PACK_OF_REALTOBACCO_SMOKES = Gear('Pack_of_RealTobacco_Smokes')
FLASHBANG = Gear('Flashbang', quantity=dice("1d4+1"))
HAND_GRENADE = Gear('Hand_Grenade', quantity=dice("1d4"))
OLD_SCHOOL_MOTORCYCLE = Gear('Old_School_Motorcycle')
STOLEN_TAXI = Gear('Stolen_Taxi')
GEAR_TABLE_1 = [MIRRORSHADES, CWPC_METRO_CARD, HANGOVER,PACK_OF_REALTOBACCO_SMOKES,FLASHBANG,HAND_GRENADE,OLD_SCHOOL_MOTORCYCLE,STOLEN_TAXI]
# TABLE 2
PARACORD = Gear('Paracord')
MICRO_TORCH_CUTTER = Gear('Micro_Torch_Cutter')
BIO_ID_SCANNER = Gear('Bio_ID_Scanner')
BREATHING_MASK = Gear('Breathing_Mask')
COLLAPSIBLE_LADDER = Gear('Collapsible_Ladder')
FIRST_AID_KIT = Gear('First_Aid_Kit')
CROWBAR = Gear('Crowbar')
SUPERLUBE = Gear('Superlube')
GRAPPLING_HOOK_CROSSBOW = Gear('Grappling_Hook_Crossbow')
SMALL_BOTTLE_OF_PULVERISED_ACID = Gear('Small_Bottle_of_Pulverised_Acid')
CRIME_SCENE_KIT = Gear('Crime_Scene_Kit')
RANDOM_CYBERTECH = Gear('Random_Cybertech')
GEAR_TABLE_2 = [PARACORD,MICRO_TORCH_CUTTER,BIO_ID_SCANNER,BREATHING_MASK,COLLAPSIBLE_LADDER,FIRST_AID_KIT,CROWBAR,SUPERLUBE,GRAPPLING_HOOK_CROSSBOW,SMALL_BOTTLE_OF_PULVERISED_ACID,CRIME_SCENE_KIT,RANDOM_CYBERTECH]
# TABLE 3
RED_JUICE_STIMJECTOR = Gear('Red_Juice_Stimjector')
ADRENACHROME_HST = Gear('Adrenachrome_HST')
DRONE_SUIT = Gear('Drone_Suit')
SMALL_JAILBROKEN_ROBO_K9 = Gear('Small_Jailbroken_Robo_K9')
TINY_SURVEILLANCE_DRONE = Gear('Tiny_Surveillance_Drone')
OPTIC_CAMO_SUIT = Gear('Optic_Camo_Suit')
NOISEMAKER = Gear('Noisemaker')
FAKE_ID = Gear('Fake_ID')
VISONVISOR = Gear('Visonvisor')
CYBERDECK = Gear('Cyberdeck',slots=dice("1d3"), apps=2)
RANDOM_NANOPOWER = Gear('Random_NanoPower')
GEAR_TABLE_3 = [RED_JUICE_STIMJECTOR,ADRENACHROME_HST,DRONE_SUIT,SMALL_JAILBROKEN_ROBO_K9,TINY_SURVEILLANCE_DRONE,OPTIC_CAMO_SUIT,NOISEMAKER,FAKE_ID,VISONVISOR,RANDOM_CYBERTECH,CYBERDECK,RANDOM_NANOPOWER]

class Ability:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __add__(self, x):
        self.value += x
        return Ability(self.name, self.value)
        
    def __iadd__(self, x):
        return self.__add__(x)
