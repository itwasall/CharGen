from chargen import yaml_importer
import random
from random import choice, randint, choices
from math import ceil, floor
from cli_ui import info
import cli_ui


data_classes = yaml_importer('dnd_5e_data/classes.yaml')
dnd_classs = data_classes['classes']
backgrounds = yaml_importer('dnd_5e_data/backgrounds.yaml')
equip = yaml_importer('dnd_5e_data/equipment.yaml')
lang = yaml_importer('dnd_5e_data/languages.yaml')
races = yaml_importer('dnd_5e_data/races.yaml')
skills = yaml_importer('dnd_5e_data/skills.yaml')
weapons = yaml_importer('dnd_5e_data/weapons.yaml')
magic = yaml_importer('dnd_5e_data/magic.yaml')


character = {
    'name': "",
    'age': 0,
    'height': "",
    'race': '',
    'dnd_class': '',
    'ability_scores': {'STR': 0, 'DEX': 0, 'CON': 0, 'INT': 0, 'WIS': 0, 'CHA': 0},
    'ability_mods': {'STR': 0, 'DEX': 0, 'CON': 0, 'INT': 0, 'WIS': 0, 'CHA': 0},
    'proficiency_bonus': 2,
    'saving_throws': {'STR': 0, 'DEX': 0, 'CON': 0, 'INT': 0, 'WIS': 0, 'CHA': 0},
    'skills': {
        'Acrobatics': 0,
        'Animal Handling': 0,
        'Arcana': 0,
        'Athletics': 0,
        'Deception': 0,
        'History': 0,
        'Insight': 0,
        'Intimidation': 0,
        'Investigation': 0,
        'Medicine': 0,
        'Nature': 0,
        'Perception': 0,
        'Persuasion': 0,
        'Religion': 0,
        'Sleight of Hand': 0,
        'Stealth': 0,
        'Survival': 0
    },
    'armor_class': 0,
    'initiative': 0,
    'speed': {'Walking': 0, 'Flying': 0, 'Climbing': 0},
    'hit_points': 0,
    'hit_dice': "",
    'proficiencies': {'weapons': [], 'armor': [], 'tools': [], 'languages': []},
    'equipment': [],
    'actions': [],
    'attacks': [
                {'name':"", 'bonus': 0, 'damage': ['dice', 0], 'type': ""}
        ],
    'spellcasting_ability': "",
    'spell_save_dc': 0,
    'spell_attack_bonus': 0
}

def dice(sides, throws):
    total = 0
    for i in range(throws):
        total += randint(1,sides)
    return total

def dnd_class(race):
    # Weighting class roll against character race. This information was taken from someones
    #  meta-gaming analysis on which races are best suited for each class. I might've tweaked
    #  a few numbers here or there, I cannot remember
    race_dnd_class_weights = {
        'High Elf': [1, 4, 2, 2, 2, 4, 2, 5, 5, 2, 2, 6],
        'Wood Elf': [3, 4, 5, 5, 2, 6, 2, 6, 5, 2, 3, 2],
        'Drow Elf': [2, 6, 3, 3, 2, 5, 5, 5, 5, 6, 6, 1],
        'Stout Halfling': [6, 5, 4, 4, 2, 6, 4, 6, 5, 4, 4, 4],
        'Lightfoot Halfling': [4, 6, 4, 4, 2, 6, 2, 5, 6, 6, 6, 3],
        'Mountain Dwarf': [6, 2, 4, 4, 6, 3, 6, 2, 2, 2, 2, 2],
        'Hill Dwarf': [6, 2, 4, 4, 6, 3, 6, 2, 2, 2, 2, 2],
        'Forest Gnome': [2, 2, 2, 2, 2, 3, 2, 3, 4, 2, 2, 6],
        'Rock Gnome': [2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 6],
        'Human': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
        'Half-Elf': [4, 7, 4, 4, 4, 4, 7, 4, 4, 7, 7, 4],
        'Half-Orc': [6, 3, 3, 4, 6, 2, 6, 4, 4, 2, 6, 2],
        'Dragonborn': [6, 5, 4, 2, 6, 2, 6, 3, 2, 5, 5, 2],
        'Tiefling': [2, 6, 2, 2, 2, 2, 5, 2, 4, 6, 6, 5]
    }
    char_dnd_class = choices(dnd_classs, weights=race_dnd_class_weights[race])
    return char_dnd_class[0]

def alignment(race, other_gen: bool = False):
    """
    The Players Handbook rather racistly states that some races are more likely to be
     some alignments over others. What this problematically boils down to is that apparently
     some races are more evil than others, or are more chaotic than others.
    The default is to abide by this, as that follows the book as best it can.
    The other_gen bool instead chooses an alignment at random, not taking into account race
     at all.
    """
    alignments_1 = ['Lawful ', 'Neutral ', 'Chaotic ']
    alignments_2 = ['Good', 'Neutral', 'Evil']
    character_alignment = str(choices(alignments_1, race['alignment_weights'][0])[0]) + \
                          str(choices(alignments_2, race['alignment_weights'][1])[0])
    if other_gen:
        character_alignment = alignments_1[randint(1,3)] + alignments_2[randint(1, 3)]
    return character_alignment

def ability_scores(race, dnd_class):
    scores = []
    ab_score = {'STR': 0, 'DEX': 0, 'CON': 0, 'INT': 0, 'WIS': 0, 'CHA': 0}
    ab_mod = {'STR': 0, 'DEX': 0, 'CON':0,  'INT': 0, 'WIS': 0, 'CHA': 0}
    ab_sav = {'STR': 0, 'DEX': 0, 'CON':0,  'INT': 0, 'WIS': 0, 'CHA': 0}
    # rolling for values
    for i in range(6):
        score = score_roll()
        # ensuring no repeats
        while score in scores:
            score = score_roll()
        scores.append(score)
    scores.sort(reverse=True)
    # allocating the highest number to the priority stats
    ab_score[dnd_class['stat_priority_1']] = scores[0]
    scores.pop(0)
    ab_score[dnd_class['stat_priority_2']] = scores[0]
    scores.pop(0)
    # randomly assigning the rest of the rolls to the rest of the stats
    for key, value in ab_score.items():
        if ab_score[key] == 0:
            score_gen = choice(scores)
            # removing the value from the values rolled list
            for it, sc in enumerate(scores):
                if score_gen == sc:
                    scores.pop(it)
            ab_score[key] = score_gen
        else: continue
    # Dumb exception for half-elfs because they get to choose their own ability score bonuses
    if race['name'] == "Half-Elf":
        race['ab_bonus'] = EXCEPT_ability_rolls_half_elf(race, dnd_class)
    for key, value in race['ab_bonus'].items():
        ab_score[key] += value
    # Since ability score mods increase by 1 for every 2 points in ability score, halfing the score and using math.floor to round down to get the correct mod looks neater than writing out the mod for each possible ability score value
    mod_calc_ref = {1:-4, 2:-3, 3:-2, 4:-1, 5:0, 6:1, 7:2, 8:3, 9:4, 10:5}
    for key, value in ab_mod.items():
        ab_mod[key] = mod_calc_ref[floor(ab_score[key]/2)]
    # Calculating the saving throws
    for key, value in ab_sav.items():
        if key in dnd_class['sav_throws']:
            ab_sav[key] = ab_mod[key] + character['proficiency_bonus']
        else:
            ab_sav[key] = ab_mod[key]
    return ab_score, ab_mod, ab_sav

def score_roll():
    rolls = [dice(6,1) for _ in range(4)]
    rolls.sort()
    rolls.pop(0)
    score = sum(rolls)
    return score

def EXCEPT_ability_rolls_half_elf(race, dnd_class):
    ability_scores_ref = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
    race['ab_bonus'] = {'CHA': 2}
    ability_scores_ref.pop(5)
    for i in range(2):
        bonus = choice(ability_scores_ref)
        for it, j in enumerate(ability_scores_ref):
            if bonus == j:
                ability_scores_ref.pop(it)
        race['ab_bonus'][bonus] = 1
    return race['ab_bonus']


def age_height_weight(race):
    age = randint(race['age'][0], race['age'][0])
    height_inches = race['height'][0] + dice(race['height'][2], race['height'][1])
    height = [int((height_inches - height_inches % 12)/12), height_inches % 12]
    height_format = f"{height[0]}'" + f'{height[1]}"'
    weight = race['weight'][0] + dice(race['weight'][2], race['weight'][1])
    weight_format = f"{weight}lbs"
    return age, height_format, weight_format

def name(race, gender=""):
    gender = choice(['male', 'female'])
    name = choice(race[gender]) + " " + choice(race['surname'])
    return name

def skill_prof(race, dnd_class):
    skill_prof = {}
    if race['name'] == 'Half-Elf':
        skill_prof_amount = dnd_class['skills'] + 2
        skill_pool = skills
    else:
        skill_prof_amount = dnd_class['skills']
        if dnd_class['sk_pool'] == 'all':
            skill_pool = skills
        else:
            skill_pool = dnd_class['sk_pool']
    for i in range(skill_prof_amount):
        skill = choice(skill_pool)
        while skill in skill_prof:
            skill = choice(skill_pool)
        skill_prof[skill] = 2
    return skill_prof

def proficiencies(race, dnd_class):
    armor_prof = []
    weap_prof = []
    languages = [i for i in race['languages'] if not i=="any"]
    if "any" in race['languages']:
        extra = (EXCEPT_language_any(languages, race))
        languages.append(extra[0]['name'])
    armor_prof = dnd_class['armor_prof'] + race['armor_prof']
    weap_prof = dnd_class['weap_prof'] + race['weap_prof']
    if dnd_class['tool_prof'] == "Monk":
        tool_prof = EXCEPT_tool_prof_monk(race, dnd_class)
    elif dnd_class['tool_prof'] == "Bard":
        tool_prof = EXCEPT_tool_prof_bard(race, dnd_class)
    else:
        tool_prof = dnd_class['tool_prof'] and race['tool_prof']
    return armor_prof, weap_prof, tool_prof, languages

def EXCEPT_language_any(tongues, race):
    weights_no = len(lang)
    weight = []
    for it, language in enumerate(lang):
        weight.append(1)
        if language['script'] == 'Dwarvish' and race['name'] == 'Mountain Dwarf' or race['name'] == 'Hill Dwarf':
            weight[it] += 2
        if language['script'] == 'Elvish' and race['name'] == 'High Elf' or race['name'] == 'Wood Elf' or race['name'] == 'Drow Elf':
            weight[it] += 2
        if language['type'] == 'Standard' and race['name'] != 'Tiefling':
            weight[it] += 2
        if language['type'] == 'Exotic' and race['name'] == 'Tiefling':
            weight[it] += 1
    language_names = [i for i in lang]
    x = random.choices(language_names, weights=weight)
    while x in tongues:
        x = random.choices(lang, weights=weight)
    else:
        extra_tongue = x
    return extra_tongue

def EXCEPT_tool_prof_monk(race, dnd_class):
    tool_prof = []
    monk_tool_type_choose = choice(['artisans_tool_prof', 'musical_instruments'])
    tool_prof.append(choice(equip[monk_tool_type_choose]))
    return tool_prof

def EXCEPT_tool_prof_bard(race, dnd_class):
    tool_prof = []
    for i in range(3):
        tool_prof.append(choice(equip['musical_instruments']))
    return tool_prof

def hp(race, dnd_class, mod):
    dnd_class_dice = {"1d6": {'name':'1d6', 'calc': dice(6,1)},
                "1d8": {'name':'1d8', 'calc': dice(8,1)},
                "1d10":{'name':'1d10', 'calc': dice(10,1)},
                "1d12": {'name':'1d12', 'calc': dice(12,1)}}
    hit_points = dnd_class['hp_start'][0] + mod['CON']
    hit_die = dnd_class_dice[dnd_class['hp_start'][1]]
    return hit_points, hit_die

def equiping(dnd_class, equip):
    simple_melee_weapons = equip['simple_melee_weapons']
    simple_ranged_weapons = equip['simple_ranged_weapons']
    martial_melee_weapons = equip['martial_melee_weapons']
    martial_ranged_weapons = equip['martial_ranged_weapons']
    musical_instruments = equip['musical_instruments']
    simple_weapons = [melee for melee in simple_melee_weapons] + [ranged for ranged in simple_ranged_weapons]
    martial_weapons = [melee for melee in martial_melee_weapons] + [ranged for ranged in martial_ranged_weapons]
    equipment = []
    tests = ['equipment1', 'equipment2', 'equipment3', 'equipment4']
    item_check_list = {
        'simple Weapon': simple_weapons,
        'simple Melee Weapon': simple_melee_weapons,
        'martial Weapon': martial_weapons,
        'martial Melee Weapon': martial_melee_weapons,
        'musical Instrument': musical_instruments
    }

    for test in tests:
        try:
            # Choosing which item to get from a set list. Each class has 2-4 of these, each with 2-3 items
            item_to_add = choice(dnd_class[test])
            while item_to_add in equipment:
                item_to_add = choice(dnd_class[test])
            equipment.append(item_to_add)
        except KeyError:
            pass
    # Adding the list of items that a character will recieve regardless
    for item_definite in dnd_class['equipment']:
        equipment.append(item_definite)
    pop_list = []
    for it, item in enumerate(equipment):
        # Checking if the item is supposed to be rolled from a list; e.g. Martial Melee Weapons
        if item in list(item_check_list.keys()):
            # Changing the generic list name to the item rolled
            equipment[it] = choice(item_check_list[item])
        # Same as above but for classes like Fighter which choose between two lists of items that need to be rolled for
        if item.__class__ == list:
            pop_list.append(it)
            for its, subitem in enumerate(item):
                if subitem in list(item_check_list.keys()):
                    equipment[it][its] = choice(item_check_list[subitem])
                # Adding all items from an internal list back out to the main one
                equipment.append(subitem)
    # Removing the internal list from equipment
    pop_list.reverse()
    for it in pop_list:
        equipment.pop(it)
    # Sorts alphabetically
    try:
        equipment.sort()
    except TypeError as e:
        exit()
    return equipment

def wealth(dnd_class):
    wealth_calc = dnd_class['wealth']
    wealth = wealth_calc[0] + dice(wealth_calc[2], wealth_calc[1])
    return wealth

def background(lang, skills, tools, equipment, race):
    background = choice(backgrounds)
    if background['languages'] == 'any':
        extra = EXCEPT_language_any(lang, race)
        lang.append(extra[0]['name'])
    if background['tool_prof_pick'] is list:
        background['tool_prof'].append(choice(background['tool_prof_pick']))
    for tool in background['tool_prof']:
        if tool in tools:
            continue
        else: tools.append(tool)
    for skill in background['skill_prof']:
        if skill in skills:
            skills[skill] += 2
        else: skills[skill] = 2
    if background['equipment_pick'] is list:
        for it, item in enumerate(background['equipment_pick']):
            if item in equipment:
                background['equipment_pick'].pop(it)
        background['equipment'].append(choice(background['equipment_pick']))
    return background, skills, tools, equipment, lang

def actions(equipment, dnd_class, race):
    standard_actions = {'Standard Actions': [
        'Attack',
        'Cast a Spell',
        'Dash',
        'Disengage',
        'Dodge',
        'Help',
        'Hide',
        'Ready',
        'Search',
        'Use an Object',
        'Two-Weapon Fighting',
        'Interact with an Object'
    ]}
    weapon_attacks = {}
    for item in equipment:
        for weapon in weapons.values():
            if item == weapon['name']:
                weapon_attacks[item] = weapon['damage']
    return standard_actions, weapon_attacks

def magical(dnd_class, race, ab_mod):
    cantrip_list = []
    spell_list = []
    spell_save = 0
    spell_atk = 0
    no_magic = [
        'Barbarian',
        'Fighter',
        'Monk',
        'Paladin',
        'Ranger',
        'Rogue'
    ]
    if dnd_class['name'] in no_magic:
        return spell_list, cantrip_list, spell_save, spell_atk
    else:
        for item in magic:
            if dnd_class['name'] == item:
                for i in range(dnd_class['cantrip']):
                    cantrip = choice(magic[dnd_class['name']]['cantrip'])
                    while cantrip in cantrip_list:
                        cantrip = choice(magic[dnd_class['name']]['cantrip'])
                    cantrip_list.append(cantrip)
                for i in range(dnd_class['spells']):
                    spell = choice(magic[dnd_class['name']]['one'])
                    while spell in spell_list:
                        spell = choice(magic[dnd_class['name']]['one'])
                    spell_list.append(spell)
                if dnd_class['name'] == 'Cleric':
                    spell_list = EXCEPT_magical_cleric(dnd_class, spell_list)

    spell_save = dnd_class['spell_save'][0] + ab_mod[dnd_class['spell_save'][1]]
    spell_atk = dnd_class['spell_attack'][0] + ab_mod[dnd_class['spell_attack'][1]]
    return spell_list, cantrip_list, spell_save, spell_atk

def EXCEPT_magical_cleric(dnd_class, spell_list):
    if dnd_class['name'] != 'Cleric':
        pass
    else:
        domain = choice(dnd_class['cleric_domain'])
        for i in magic['Cleric'][domain]:
            if i in spell_list:
                continue
            else:
                spell_list.append(i)
    return spell_list

def print_format_profs(prof_name, prof_list):
    dupe_check = []
    info(cli_ui.bold, prof_name)
    if len(char_tool_prof) == 0:
        info(cli_ui.green, "None", cli_ui.reset)
    for k in prof_list:
        if k in dupe_check:
            continue
        else:
            dupe_check.append(k)
            info(cli_ui.green, k, cli_ui.reset)



def char_gen():
    global char_arm_prof, char_wea_prof, char_tool_prof, char_lang, char_equipment
    char_race = choice(races)
    char_age, char_height, char_weight = age_height_weight(char_race)
    char_name = name(char_race)
    char_dnd_class = dnd_class(char_race['name'])
    char_alignment = alignment(char_race)
    char_ab_score, char_ab_mod, char_ab_sav = ability_scores(char_race, char_dnd_class)
    char_skill_prof = skill_prof(char_race, char_dnd_class)
    char_arm_prof, char_wea_prof, char_tool_prof, char_lang = proficiencies(char_race, char_dnd_class)
    char_hit_points, char_hit_die = hp(char_race, char_dnd_class, char_ab_mod)
    char_equipment = equiping(char_dnd_class, equip)
    char_wealth = wealth(char_dnd_class)
    char_background, char_skill_prof, char_tool_prof, char_equipment, char_lang = background(char_lang, char_skill_prof, char_tool_prof, char_equipment, char_race)
    char_actions, char_attack_actions = actions(char_equipment, char_dnd_class, char_race)
    char_magic, char_cantrip, char_spell_sav, char_spell_atk = magical(char_dnd_class, char_race, char_ab_mod)

    info(cli_ui.bold, '==== INFORMATION =====')
    info(cli_ui.yellow, f'{char_name}', cli_ui.reset, 'the', cli_ui.magenta, char_race['name'])
    print(char_alignment)
    print(f'{char_age} years old', char_height, char_weight)
    print('Formally',char_dnd_class['name'])
    info(cli_ui.yellow, "Health/Hit Dice:  ", cli_ui.green, f'{char_hit_points}/{char_hit_die["name"]}', cli_ui.reset)
    info(cli_ui.yellow, "Spell Save/Attack:", cli_ui.green, f'{char_spell_sav}/{char_spell_atk}', cli_ui.reset)
    info(cli_ui.bold, '=== ABILITY SCORES ===')
    for k, d in char_ab_score.items():
        info(cli_ui.green, k, cli_ui.reset, d, cli_ui.yellow, f'   ({char_ab_mod[k]})', cli_ui.reset, cli_ui.green , f'  Save:', cli_ui.reset, f'{char_ab_sav[k]}')
    info(cli_ui.bold, '=== PROFICIENCIES ====')
    info(cli_ui.bold, 'Skills')
    for k, d in char_skill_prof.items():
        info(cli_ui.yellow, f'+{d}', cli_ui.reset, '- ', cli_ui.green, k, cli_ui.reset)
    print_format_profs('Weapons', char_wea_prof)
    print_format_profs('Armor', char_arm_prof)
    print_format_profs('Tools', char_tool_prof)
    print_format_profs('Languages', char_lang)
    info(cli_ui.bold, '=== EQUIPMENT ========')
    info(cli_ui.bold, "Starting wealth", cli_ui.reset)
    info(cli_ui.green, char_wealth, cli_ui.reset, 'bronze pieces')
    print_format_profs('Equipment', char_equipment)
    info(cli_ui.bold, '=== ACTIONS ==========')
    print_format_profs('Attacks', char_attack_actions)
    print_format_profs('Other Actions', char_actions)
    print_format_profs('Magic Actions', char_magic)
    print_format_profs('Cantrips', char_cantrip)

if __name__ == "__main__":
    char_gen()

    def try_100():
        failed = 0
        sucess = 0
        for i in range(100):
            try:
                char_gen()
                sucess += 1
            except err as Error:
                failed += 1
                print(err)
        print(f'Succeeded: {sucess} Failed: {failed}')

    #try_100()
