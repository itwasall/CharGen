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
        self.level = 1
        self.languages = [Core.DEFAULT_LANGUAGE]
        """ Ability Scores """
        self.STR = Core.STR
        self.DEX = Core.DEX
        self.CON = Core.CON
        self.INT = Core.INT
        self.WIS = Core.WIS
        self.CHA = Core.CHA
        """ Skills """
        self.SKILLS = {
            # STR
            'Athletics': Core.ATHLETICS,
            # DEX
            'Acrobatics': Core.ACROBATICS,
            'Sleight of Hand': Core.SLEIGHT_OF_HAND,
            'Stealth': Core.STEALTH,
            # INT
            'Arcana': Core.ARCANA,
            'History': Core.HISTORY,
            'Investigation': Core.INVESTIGATION,
            'Nature': Core.NATURE,
            'Religion': Core.RELIGION,
            # WIS
            'Animal Handling': Core.ANIMAL_HANDLING,
            'Insight': Core.INSIGHT,
            'Medicine': Core.MEDICINE,
            'Perception': Core.PERCEPTION,
            'Survival': Core.SURVIVAL,
            # CHA
            'Deception': Core.DECEPTION,
            'Intimidation': Core.INTIMIDATION,
            'Performance': Core.PERFORMANCE,
            'Persuasion': Core.PERSUASION
        }
        """ Equipment & Proficiencies """
        self.proficiencies = {'Weapon': [], 'Armor': [], 'Tool': []}
        """ Combat Stats """
        self.AC = 0
        self.initiative = 0
        self.speed = 0
        self.hit_points = 0
        self.current_hit_points = 0
        """ Magic """
        self.cantrips = []
        self.spells = {'1st Level': []}
        self.spell_slots = {'1st Level': []}
        self.spell_save_dc = 0
        self.spell_attack_modifier = 0
        self.spellcasting_ability_score = None
        """ Possessions """
        self.money = 0
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

def unpackChoice(data: dict, dupes_allowed=False) -> list:
    def getRandomChoice(value: list, amt: int, dupes_allowed=False) -> list:
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
        case 'Choose 5':
            unpacked_choice = getRandomChoice(data[data_keys[0]], 4)
        case 'Choose 6':
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

def genSpells(spells = None, spell_slots = None, _class = None):
    # Druid exception (the first one like 1600 lines in :c )
    #   Druid spell slots = The greater of (WIS Mod + Character Level || 1)
    if _class != None and _class.name == "Druid":
        druid_spells_amount = CHARACTER.WIS.modifier + CHARACTER.level
        if druid_spells_amount < 1:
            druid_spells_amount = 1
        _class.spells['1st Level'] = {f"Choose {druid_spells_amount}": _class.spells['1st Level']}

    if spells != None and len(CHARACTER.spells) == 0:
        return unpackChoice(spells['1st level'])
    if spell_slots != None:
        # Because god has cursed me for my hubris, '_' is apparently alphabettically ahead
        #   of 's', meaning the 'spell_' of 'spell_slots' will be dealt with before
        #   'spells'. Can't allocated spells to spell slots if you've no spells to do so
        #   with, so hurry, more shitey code : ) 
        if len(CHARACTER.spells['1st Level']) == 0:
            if isinstance(_class.spells['1st Level'], dict):
                CHARACTER.spells = unpackChoice(_class.spells['1st Level'])
            elif isinstance(_class.spells['1st Level'], list):
                CHARACTER.spells = _class.spells['1st Level']
        return [random.choice(CHARACTER.spells) for _ in range(spell_slots)]



def genSpellbook():
    spellbook_spells_pool = [spell for spell in Core.WIZARD_FIRST_LEVEL if spell not in CHARACTER.spells]
    return unpackChoice({'Choose 6': spellbook_spells_pool})

def genSkills(_class):
    skills = unpackChoice(_class.skills)
    for skill in skills:
        CHARACTER.SKILLS[skill.name].prof = True

def genClass():
    char_class = random.choice(CLASSES)
    print(char_class.name)

    char_class_attributes = attrAsDict(char_class)
    attributes_generated = []

    for attr in char_class_attributes:
        match list(attr.keys())[0]:
            case 'proficiencies':
                attributes_generated.append('proficiencies')
            case 'saving_throws':
                attributes_generated.append('saving_throws')
            case 'skills':
                attributes_generated.append('skills')
                genSkills(char_class)
                
            case 'hit_dice':
                attributes_generated.append('hit_dice')
                CHARACTER.hit_dice = attr['hit_dice']
            case 'initial_health':
                attributes_generated.append('initial_heath')
                CHARACTER.hit_points = attr['initial_health'] + CHARACTER.CON.modifier
            case 'starting_money':
                attributes_generated.append('starting_money')
                CHARACTER.money += diceRoll(attr['starting_money'][0]) + attr['starting_money'][1]
            case 'equipment':
                attributes_generated.append('equipment')
                CHARACTER.equipment += Core.getEquipment(attr['equipment'])
            case 'equipment_pack':
                attributes_generated.append('equipment_pack')
                if isinstance(attr['equipment_pack'], list):
                    CHARACTER.equipment += attr['equipment_pack']
                elif isinstance(attr['equipment_pack'], list):
                    CHARACTER.equipment += unpackChoice(attr['equipment_pack'])
            case 'cantrips':
                attributes_generated.append('cantrips')
                CHARACTER.cantrips = unpackChoice(attr['cantrips'])
            case 'spells':
                attributes_generated.append('spells')
                CHARACTER.spells = genSpells(spells=attr['spells'])
            case 'spell_slots':
                attributes_generated.append('spell_slots')
                CHARACTER.spell_slots = genSpells(spell_slots=attr['spell_slots']['1st Level'], _class=char_class)
            case 'spellcasting_ab':
                attributes_generated.append('spellcasting_ab')
                CHARACTER.spellcasting_ability_score = attr['spellcasting_ab']
                CHARACTER.spell_save_dc = 0
            case _:
                attributes_generated.append('_getattr')
                attributes_generated.append('items')
                attributes_generated.append('name')


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
        match list(attr.keys())[0]:
            case '_getattr':
                attributes_generated.append('_getattr')
            case 'ab_score':
                attributes_generated.append('ab_score')
                genRaceAttributeBonus(attr['ab_score'])
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
    # print(f"{CHARACTER.STR}\n{CHARACTER.DEX}\n{CHARACTER.CON}\n{CHARACTER.INT}\n{CHARACTER.WIS}\n{CHARACTER.CHA}")
    print(CHARACTER.hit_points)
    return "nice"

print(genCharacter())
