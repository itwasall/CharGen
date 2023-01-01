import random

import char_dnd_5e_core as Core

# This is to allow for further optional expansion of
#    suppliment material
RACES =  Core.RACES
SUBRACES = Core.SUBRACES
LANGUAGES = Core.LANGUAGES
CLASSES = Core.CLASSES
SUBCLASSES = Core._SubClass.items
BACKGROUNDS = Core.Background.items
ITEMS = Core.Item.items



class PartyMember:
    def __init__( self, name: str = None, **kwargs):
        """ Macro Character Stuff """
        self.name = name
        self.race = Core.DEFAULT_RACE
        self.subrace = None
        self._class = Core.DEFAULT_CLASS
        self._subclass = None
        self.languages = [Core.DEFAULT_LANGUAGE]
        """ Ability Scores """
        self.STR = Core.STR
        self.DEX = Core.DEX
        self.CON = Core.CON
        self.INT = Core.INT
        self.WIS = Core.WIS
        self.CHA = Core.CHA
        """ Skills """
        # STR
        self.athletics = Core.ATHLETICS
        # DEX
        self.acrobatics = Core.ACROBATICS
        self.sleight_of_hand = Core.SLEIGHT_OF_HAND
        self.stealth = Core.STEALTH
        # INT
        self.arcana = Core.ARCANA
        self.history = Core.HISTORY
        self.investigation = Core.INVESTIGATION
        self.nature = Core.NATURE
        self.religion = Core.RELIGION
        # WIS
        self.animal_handling = Core.ANIMAL_HANDLING
        self.insight = Core.INSIGHT
        self.medicine = Core.MEDICINE
        self.perception = Core.PERCEPTION
        self.survival = Core.SURVIVAL
        # CHA
        self.deception = Core.DECEPTION
        self.intimidation = Core.INTIMIDATION
        self.performance = Core.PERFORMANCE
        self.persuasion = Core.PERSUASION
        """ Equipment & Proficiencies """
        self.proficiencies = {'Weapon': [], 'Armor': [], 'Tool': []}
        """ Combat Stats """
        self.AC = 0
        self.initiative = 0
        self.speed = 0
        self.hit_points = 0
        self.current_hit_points = 0
        """ Possessions """
        self.money = { Core.cp: 0, Core.sp: 0, Core.ep: 0, Core.gp: 0, Core.pp: 0 }
        self.equipment = []


        for k, d in kwargs.items():
            self.__setattr__(k, d)
    
    def __repr__(self):
        return self.__format__()

    def __format__(self):
        return self.name

global CHARACTER
CHARACTER = PartyMember('Jeff')

def diceRoll(dicestring, summed=True):
    throws, sides = dicestring.split("d")
    if summed:
        return sum([random.randint(1, int(sides)) for _ in range(int(throws))])
    else:
        rolls = [random.randint(1, int(sides)) for _ in range(int(throws))]
        rolls.sort()
        return rolls

def sortReverse(l: list):
    l.sort()
    l.reverse()
    return l

def attrAsDict(_class):
    return [{i: _class._getattr(i)} for i in dir(_class) if not i.startswith("__")]

def unpackChoice(data: dict, dupes_allowed=False):
    def getRandomChoice(value: list, amt: int, dupes_allowed=False):
        chosen_values = []
        if dupes_allowed:
            chosen_values = [random.choice(value) for _ in range(amt)]
        else:
            while len(chosen_values) < amt:
                random_item = random.choice(value)
                if random_item in chosen_values:
                    chosen_values.pop(chosen_values.index(random_item))
                chosen_values.append(random_item)
        return chosen_values

    opt_bonus_value = None
    if len(data.keys()) != 1 and list(data.keys())[1] == 'Bonus':
        opt_bonus_value = data['Bonus']
    data_keys = list(data.keys())
    match data_keys[0]:
        case 'Choose 1':
            unpacked_choice = getRandomChoice(data[data_keys[0]], 1)
        case 'Choose 2':
            unpacked_choice = getRandomChoice(data[data_keys[0]], 2)
        case 'Choose 3':
            unpacked_choice = getRandomChoice(data[data_keys[0]], 3)
        case 'Choose 4':
            unpacked_choice = getRandomChoice(data[data_keys[0]], 4)
        case 'Has':
            unpacked_choice = data[data_keys[0]]
    return unpacked_choice

def genAlignment(weights: tuple):
    is_weight_a = random.randint(0, 100)
    if is_weight_a > 30 and isinstance(weights[0], str) and weights[0] != 'None':
        alignment_a = weights[0]
    else:
        alignment_a = random.choice(['Lawful', 'Chaotic', 'Neutral'])
    is_weight_b = random.randint(0, 100)
    if is_weight_b > 30 and isinstance(weights[1], str) and weights[1] != 'None':
        alignment_b = weights[1]
    else:
        alignment_b = random.choice(['Good', 'Evil', 'Neutral'])
    return Core.Alignment(alignment_a, alignment_b)

def genLanguage(languages, banlist=None):
    if banlist == None:
        banlist = []
    return_languages = []
    for lang in languages:
        if isinstance(lang, dict):
            chosen_lang = unpackChoice(lang)
            while chosen_lang in return_languages:
                chosen_lang = unpackChoice(lang)
            return_languages.append(chosen_lang)
        elif isinstance(lang, Core.Language):
            chosen_lang = lang
            return_languages.append(chosen_lang)
    return return_languages

def raiseAbilityScore(data: tuple):
    match data[0]:
        case Core.STR:
            CHARACTER.STR += data[1]
        case Core.DEX:
            CHARACTER.DEX += data[1]
        case Core.CON:
            CHARACTER.CON += data[1]
        case Core.INT:
            CHARACTER.INT += data[1]
        case Core.WIS:
            CHARACTER.WIS += data[1]
        case Core.CHA:
            CHARACTER.CHA += data[1]

def genRaceAttributeBonus(data):
    for item in data:
        if isinstance(item, tuple):
            raiseAbilityScore(item)
        elif isinstance(item, dict):
            unpacked_item = unpackChoice(item)
            print(unpacked_item)
            raiseAbilityScore(unpackChoice(item)[0])

def genClass():
    char_class = random.choice(CLASSES)

    char_class_attributes = attrAsDict(char_class)
    attributes_generated = []

    for attr in char_class_attributes:
        match list(attr.keys())[0]:
            case '_getattr':
                attributes_generated.append('_getattr')
            case 'items':
                attributes_generated.append('items')
            case 'proficiencies':
                attributes_generated.append('proficiencies')
            case 'saving_throws':
                attributes_generated.append('saving_throws')
            case 'skills':
                attributes_generated.append('skills')
            case 'hit_dice':
                attributes_generated.append('hit_dice')
            case 'initial_health':
                attributes_generated.append('initial_heath')
            case 'starting_money':
                attributes_generated.append('starting_money')
            case 'equipment':
                attributes_generated.append('equipment')
                attributes_generated.append('equipment_pack')
            case 'equipment_pack':
                pass

    print("generated: ", attributes_generated)
    print("not generated: ", [list(attr.keys())[0] for attr in char_class_attributes if list(attr.keys())[0] not in attributes_generated])


def genRace(subrace=None):
    if subrace == None:
        # char_race = random.choice(Core.RACES)
        char_race = Core.ELF
        CHARACTER.race = char_race
    else:
        char_race = subrace

    char_race_attributes = attrAsDict(char_race)
    attributes_generated = []
    
    for attr in char_race_attributes:
        print(list(attr.keys()))
        match list(attr.keys())[0]:
            case '_getattr':
                attributes_generated.append('_getattr')
            case 'ab_score':
                attributes_generated.append('ab_score')
                genRaceAttributeBonus(attr['ab_score'])
                print(f"{CHARACTER.STR}\n{CHARACTER.DEX}\n{CHARACTER.CON}\n{CHARACTER.INT}\n{CHARACTER.WIS}\n{CHARACTER.CHA}")
            case 'has_subrace':
                attributes_generated.append('has_subrace')
                char_subrace = random.choice([subrace for subrace in Core.SUBRACES if subrace.race == char_race])
                genRace(char_subrace)
                CHARACTER.subrace = char_subrace
            case 'alignment':
                attributes_generated.append('alignment')
                CHARACTER.alignment = genAlignment(attr['alignment'])
            case 'age':
                attributes_generated.append('age')
                CHARACTER.age = random.randint(attr['age'][0], attr['age'][1])
            case 'size':
                attributes_generated.append('size')
                CHARACTER.size = attr['size']
            case 'speed':
                attributes_generated.append('speed')
                CHARACTER.speed = attr['speed']
            case 'language':
                attributes_generated.append('language')
                CHARACTER.languages = list(Core.flatten(genLanguage(char_race.language)))
            case 'racial_prof':
                attributes_generated.append('racial_prof')
                CHARACTER.proficiencies = attr['racial_prof']
            case 'ancestory':
                attributes_generated.append('ancestory')
                CHARACTER.ancestory = unpackChoice(attr['ancestory'])
            case 'darvision':
                attributes_generated.append('darkvision')
                CHARACTER.darkvision = attr['darkvision']
            case 'hit_point_increase':
                attributes_generated.append('hit_point_increase')
                CHARACTER.hit_points += 1

            case _:
                if 'has_subrace' not in attributes_generated:
                    char_subrace = None
                if 'alignment' not in attributes_generated:
                    char_alignment = genAlignment((False, False))
                if 'size' not in attributes_generated:
                    char_size = "SIZE NOT FOUND"
        

def genCharacter():

    ability_score_rolls = []
    for _ in range(6):
        rolls = diceRoll("4d6", summed=False)
        sortReverse(rolls)
        rolls.pop()
        ability_score_rolls.append(rolls)
    
    ability_score_rolls.sort()

    genRace()
    genClass()

    # char_race = random.choice(RACES)
    char_race = [i for i in RACES if i.name == 'Dragonborn'][0]
    if hasattr(char_race, "has_subrace"):
        char_subrace = random.choice([subrace for subrace in SUBRACES if subrace.race == char_race])
    else:
        char_subrace = None

#    print(char_race, char_subrace)
    char_class = random.choice(CLASSES)
    return "nice"

print(genCharacter())
