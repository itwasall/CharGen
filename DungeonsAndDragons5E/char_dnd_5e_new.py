import random
from cli_ui import info, bold, red, blue, black, reset

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
        self.languages = []
        """ Ability Scores """
        self.STR = Core.STR
        self.DEX = Core.DEX
        self.CON = Core.CON
        self.INT = Core.INT
        self.WIS = Core.WIS
        self.CHA = Core.CHA
        self.ability_scores = {'STR': self.STR, 'DEX': self.DEX, 'CON': self.CON, 'INT': self.INT, 'WIS': self.WIS, 'CHA': self.CHA}
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

    def getStats(self):
        print(f"STR: {self.ability_scores['STR'].value} || DEX: {self.ability_scores['DEX'].value} || CON: {self.ability_scores['CON'].value}\nINT: {self.ability_scores['INT'].value} || WIS: {self.ability_scores['WIS'].value} || CHA: {self.ability_scores['CHA'].value}")

    def getEquipment(self):
        self.equipment = [equip.name if not isinstance(equip, str) else equip for equip in self.equipment]
        for item in self.equipment:
            if self.equipment.count(item) > 1:
                new_item = f"{item} x{self.equipment.count(item)}"
                while item in self.equipment:
                    self.equipment.pop(self.equipment.index(item))
                self.equipment.append(new_item)
        self.equipment.sort()
        print(self.equipment)

    def getSpells(self):
        print(f"Cantrips: {self.cantrips}")
        print(f"Known spells: {self.spells}")
        print(f"Prepared: {self.spell_slots}")

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
    # return _class.__dict__

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
    # print(CHARACTER.race)
    # print(data)
    match data[0]:
        case Core.STR:
            CHARACTER.ability_scores['STR'] += data[1]
        case Core.DEX:
            CHARACTER.ability_scores['DEX'] += data[1]
        case Core.CON:
            CHARACTER.ability_scores['CON'] += data[1]
        case Core.INT:
            CHARACTER.ability_scores['INT'] += data[1]
        case Core.WIS:
            CHARACTER.ability_scores['WIS'] += data[1]
        case Core.CHA:
            CHARACTER.ability_scores['CHA'] += data[1]

def genRaceAttributeBonus(data):
    for item in data:
        if isinstance(item, tuple):
            raiseAbilityScore(item)
        elif isinstance(item, dict):
            unpacked_item = unpackChoice(item)
            if isinstance(unpacked_item, list):
                genRaceAttributeBonus(unpacked_item)
            else:
                raiseAbilityScore(unpackChoice(item))

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
        if not isinstance(CHARACTER.spells, list) and len(CHARACTER.spells['1st Level']) == 0:
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

def genSubClass(subclass):
    char_subclass_attributes = attrAsDict(subclass)
    attributes_generated = []

    for attr in char_subclass_attributes:
        match list(attr.keys())[0]:
            case 'spells':
                genSpells(spells=attr['spells'])
                # CHARACTER.spells = [spell for spell in subclass.spells]
                prepped_spells = []
                if not isinstance(CHARACTER.spell_slots, list):
                    if isinstance(CHARACTER.spell_slots['1st Level'], list):
                        CHARACTER.spell_slots['1st Level'].append(prepped_spells)
                    else:
                        for i in range(CHARACTER.spell_slots['1st Level']):
                            prepped_spells.append(random.choice(CHARACTER.spells))
                            CHARACTER.spell_slots = prepped_spells
            case 'profs':
                for key in attr['profs'].keys():
                    match key:
                        case 'Weapon':
                            try:
                                CHARACTER.proficiencies['Weapon'].append(attr['profs']['Weapon'])
                            except:
                                CHARACTER.proficiencies['Weapon'] = attr['profs']['Weapon']
                        case 'Armor':
                            try:
                                CHARACTER.proficiencies['Armor'].append(attr['profs']['Armor'])
                            except:
                                CHARACTER.proficiencies['Armor'] = attr['profs']['Armor']
                        case 'Skill':
                            skills = unpackChoice(attr['profs']['Skill'])
                            for skill in skills:
                                CHARACTER.SKILLS[skill.name].prof=True
            case 'language':
                langs = unpackChoice(attr['language'])
                for lang in langs:
                    if lang not in CHARACTER.languages:
                        CHARACTER.languages.append(lang)
                    else:
                        pass
            case 'cantrip':
                if isinstance(attr['cantrip'], dict):
                    cantrips = unpackChoice(attr['cantrip'])
                else:
                    cantrips = attr['cantrip']
                for cantrip in cantrips:
                    CHARACTER.cantrips.append(cantrip)




def genClass(ability_score_rolls, force_class = None):
    if force_class is not None and force_class in [i.name for i in CLASSES]:
        char_class = [_ for _ in CLASSES if _.name == force_class][0]
    else:
        char_class = random.choice(CLASSES)
    # char_class = Core.CLERIC
    CHARACTER._class = char_class
    top_rolls = ability_score_rolls[0:2]
    bottom_rolls = ability_score_rolls[2:]
    
    char_class_attributes = attrAsDict(char_class)
    attributes_generated = []

    for attr in char_class_attributes:
        match list(attr.keys())[0]:
            case 'proficiencies':
                attributes_generated.append('proficiencies')

            case 'saving_throws':
                attributes_generated.append('saving_throws')
                CHARACTER.saving_throws = attr['saving_throws']
                top_skill = random.choice(CHARACTER.saving_throws)
                for ab in [i for i in CHARACTER.ability_scores.keys()]:
                    if ab == top_skill.name and ab in [i.name for i in CHARACTER.saving_throws]:
                        CHARACTER.ability_scores[ab] += top_rolls[0]
                    elif ab != top_skill.name and ab in [i.name for i in CHARACTER.saving_throws]:
                        CHARACTER.ability_scores[ab] += top_rolls[1]
                    else:
                        idx = random.randint(0, len(bottom_rolls)-1)
                        CHARACTER.ability_scores[ab] += bottom_rolls[idx]
                        bottom_rolls.pop(idx)

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
                elif isinstance(attr['equipment_pack'], dict):
                    CHARACTER.equipment += unpackChoice(attr['equipment_pack'])[0]
            case 'cantrips':
                attributes_generated.append('cantrips')
                CHARACTER.cantrips = unpackChoice(attr['cantrips'])
            case 'spells':
                attributes_generated.append('spells')
                if isinstance(CHARACTER.spells, list) or len(CHARACTER.spells['1st Level']) != 0:
                    pass
                else:
                    CHARACTER.spells = genSpells(spells=attr['spells'])
            case 'spell_slots':
                attributes_generated.append('spell_slots')
                CHARACTER.spell_slots = genSpells(spell_slots=attr['spell_slots']['1st Level'], _class=char_class)
            case 'spellcasting_ab':
                attributes_generated.append('spellcasting_ab')
                CHARACTER.spellcasting_ability_score = attr['spellcasting_ab']
                CHARACTER.spell_save_dc = 0
            case 'requires_subclass':
                subclasses = [subclass for subclass in Core._SubClass.items if subclass._class == char_class]
                CHARACTER.subclass = random.choice(subclasses)
                genSubClass(CHARACTER.subclass)

            case _:
                attributes_generated.append('_getattr')
                attributes_generated.append('items')
                attributes_generated.append('name')




def genRace(subrace=None):
    if subrace == None:
        char_race = random.choice(Core.RACES)
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
                for key in attr['racial_prof'].keys():
                    match key:
                        case 'Weapon':
                            try:
                                CHARACTER.proficiencies['Weapon'].append(attr['racial_prof']['Weapon'])
                            except: 
                                CHARACTER.proficiencies['Weapon'] = attr['racial_prof']['Weapon']
                        case 'Armor':
                            try:
                                CHARACTER.proficiencies['Armor'].append(attr['racial_prof']['Armor'])
                            except:
                                CHARACTER.proficiencies['Armor'] = attr['racial_prof']['Armor']
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

def genBackground():
    char_bg = random.choice(BACKGROUNDS)
    char_bg_attributes = attrAsDict(char_bg)

    CHARACTER.background = char_bg

    attributes_generated = []

    for attr in char_bg_attributes:
        match list(attr.keys())[0]:
            case 'skill_profs':
                attributes_generated.append('skill_profs')
                for skill in attr['skill_profs']:
                    CHARACTER.SKILLS[skill.name].prof = True
            case 'tool_profs':
                if len(attr['tool_profs']) == 0:
                    pass
                CHARACTER.proficiencies['Tool'] = []
                attributes_generated.append('tool_profs')
                for tool in attr['tool_profs']:
                    if isinstance(tool, dict):
                        tool = unpackChoice(tool)[0]
                    if tool in CHARACTER.proficiencies['Tool']:
                        pass
                    else:
                        CHARACTER.proficiencies['Tool'].append(tool)
            case 'language':
                attributes_generated.append('langauge')
                for lang in attr['language']:
                    if isinstance(lang, dict):
                        lang = unpackChoice(lang)[0]
                    if lang in CHARACTER.languages:
                        pass
                    else:
                        CHARACTER.languages.append(lang)
            case 'equipment':
                attributes_generated.append('equipment')
                for equip in attr['equipment']:
                    if isinstance(equip, dict):
                        equip = unpackChoice(equip)[0]
                    CHARACTER.equipment.append(equip)
            case 'money':
                attributes_generated.append('money')
                CHARACTER.money += attr['money'][0]
            case _:
                attributes_generated.append('_getattr')
                attributes_generated.append('name')

def genCharacter(force_class=None):
    ability_score_rolls = []
    for _ in range(6):
        rolls = diceRoll("4d6", summed=False)
        rolls = sortReverse(rolls)
        rolls.pop()
        ability_score_rolls.append(sum(rolls))
    
    ability_score_rolls = sortReverse(ability_score_rolls)

    genRace()
    if force_class is not None:
        genClass(ability_score_rolls, force_class)
    else:
        genClass(ability_score_rolls)
    genBackground()

    # char_race = random.choice(RACES)
    char_race = [i for i in RACES if i.name == 'Dragonborn'][0]
    if hasattr(char_race, "has_subrace"):
        char_subrace = random.choice([subrace for subrace in SUBRACES if subrace.race == char_race])
    else:
        char_subrace = None

#    print(char_race, char_subrace)
    char_class = random.choice(CLASSES)
    # print(f"{CHARACTER.STR}\n{CHARACTER.DEX}\n{CHARACTER.CON}\n{CHARACTER.INT}\n{CHARACTER.WIS}\n{CHARACTER.CHA}")
    import yaml
    character_names = yaml.safe_load(open('dnd_5e_data/races.yaml', 'rt'))
    CHARACTER.name = f'{random.choice(race[random.choice(["male", "female"])])} {random.choice(race["surname"])}'
    info(bold, f'The {CHARACTER.race.name} {CHARACTER._class.name}', reset, ', ', bold, f'{CHARACTER.background.name} {CHARACTER.name}')
    # print(CHARACTER.race.name)
    # print(CHARACTER._class.name)
    # print(CHARACTER.background.name)
    CHARACTER.getStats()
    CHARACTER.getEquipment()
    CHARACTER.getSpells()
    return CHARACTER

if __name__ == "__main__":
    a = genCharacter(force_class='Barbarian')
