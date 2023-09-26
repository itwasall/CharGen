import yaml
import random

with open("data.yaml") as file:
        data = yaml.safe_load(file)
        # jobs is a dict containing class name, class stat priorities (i.e. what stat most beneficial to this class), starting health and hp dice roll per level
        jobs = data['classes']
        # races in a dict containing race name, male/female/surname names, score bonuses, avg. age/height, size, speed, speed penalties (for heavy armor usage), darkvision amount, tool/combat proficiencies, languages spoken, if they have cantrips
        races = data['races']
        languages = data['languages']
        equipment = data['equipment']

def dice(sides=6, rolls=1):
    total = 0
    for roll in range(rolls):
        total += random.randint(1,sides)
    return total

def ability_gen(job_gen):
    ability_scores = {'STR':0, 'DEX':0, 'CON':0, 'INT':0, 'WIS':0, 'CHA':0}
    ability_dice_rolls = []
    for i in range(8):
        ability_dice_rolls.append(dice(6,3))
    ability_dice_rolls.sort(reverse=True)
    ability_scores[job_gen['stat_priority_1']] = ability_dice_rolls[0]
    ability_scores[job_gen['stat_priority_2']] = ability_dice_rolls[1]
    for it, ability_score in enumerate(ability_scores):
        if ability_scores[ability_score] > 1:
            pass
        else:
            ability_scores[ability_score] = ability_dice_rolls[it+2]

    ability_score_mods = {1:-5, 2:-4, 3:-4, 4:-3, 5:-3, 6:-2, 7:-2, 8:-1, 9:-1, 10:0,
                          11:0, 12:1, 13:1, 14:2, 15:2, 16:3, 17:3, 18:4, 19:4, 20:5,
                          21:5, 22:6, 23:6, 24:7, 25:7, 26:8, 27:8, 28:9, 29:9, 30:10}
    score_mods = {}
    for stat, value in ability_scores.items():
        score_mods[stat] = ability_score_mods[value]

    return ability_scores, score_mods

def language_gen(tounges, race):
    weights_no = len(languages)
    weight = []
    for it, language in enumerate(languages):
        weight.append(1)
        if language['script'] == 'Dwarvish' and race['name'] == 'Mountain Dwarf' or race['name'] == 'Hill Dwarf':
            weight[it] += 2
        if language['script'] == 'Elvish' and race['name'] == 'High Elf' or race['name'] == 'Wood Elf' or race['name'] == 'Drow Elf':
            weight[it] += 2
        if language['type'] == 'Standard' and race['name'] != 'Tiefling':
            weight[it] += 2
        if language['type'] == 'Exotic' and race['name'] == 'Tiefling':
            weight[it] += 1
    language_names = [i for i in languages]
    x = random.choices(language_names, weights=weight)
    while x in tounges:
        x = random.choices(languages, weights=weight)
    else:
        extra_tongue = x
    return extra_tongue

"""
Generates equipment based on class spec. Has lists for generic pools of items
"""

def equip_gen(job, equipment):
    simple_melee_weapons = equipment['simple_melee_weapons']
    simple_ranged_weapons = equipment['simple_ranged_weapons']
    martial_melee_weapons = equipment['martial_melee_weapons']
    martial_ranged_weapons = equipment['martial_ranged_weapons']
    musical_instruments = equipment['musical_instruments']
    packs = equipment['packs']
    simple_weapons = [melee for melee in simple_melee_weapons] + [ranged for ranged in simple_ranged_weapons]
    martial_weapons = [melee for melee in martial_melee_weapons] + [ranged for ranged in martial_ranged_weapons]
    equipment = []
    tests = ['equipment1', 'equipment2', 'equipment3', 'equipment4']
    item_check_list = {'simple Weapon':simple_weapons, 'simple Melee Weapon':simple_melee_weapons, 'martial Weapon':martial_weapons, 'martial Melee Weapon':martial_melee_weapons, 'musical Instrument':musical_instruments}
    for test in tests:
        try:
            equipment.append(random.choice(job[test]))
        except KeyError:
            continue
    try:
        for item in job['equipment']:
            equipment.append(item)
    except KeyError:
        pass
# This code is checking to see if a) an item is not specific and needs to pull its result from a predetermined list and b) to make sure duplicates do not appear. I will think about adding the possibilty for dual weilding later on but right now my previous code *always* resulted in the character recieving the same item twice.
    for it, item in enumerate(equipment):
        if item.__class__ == dict:
            pass
        else:
            if item.__class__ == list:
                for subitem in item:
                    if subitem in item_check_list.keys():
                        add = item_check(equipment,item_check_list[subitem])
                        equipment.append(add)
                    else: continue
                equipment.pop(it)
            elif item in item_check_list.keys():
                add = item_check(equipment, item_check_list[item])
                equipment.append(add)
                equipment.pop(it)
            elif item in packs:
                pack_ref = item
                equipment.pop(it)
                pack = {pack_ref:[]}
                for pack_item in packs[pack_ref]:
                    pack[pack_ref].append(pack_item)
                equipment.append(pack)
            else: continue
    return equipment

"""
This function is to check whether or not a piece of equipment is already in the characters posession. Some classes have the option to obtain two simple weapons for example. This function's purpose is to stop that character cross-weilding crossbows.
"""
def item_check(equipment, item_list):
    add = random.choice(item_list)
    while add in equipment:
        add = random.choice(item_list)
    return add

def profs(race, job):
    total_skill_list = data['skills']
    if race['tool_prof'] == "Bard":
        race['tool_prof'] = []
        for i in range(3):
            race['tool_prof'].append(random.choice(equipment['musical_instruments']))
    # if race['combat_prof'] == 'Half-Elf':
    #    race['combat_prof'] = ["None"]
    #    job['skills'] = job['skills'] + 2
    #    job['sk_pool'] = 'all'
    proficiencies = {'tools':[i for i in race['tool_prof']], 'skills':[]} #, 'combat':[i for i in race['combat_prof']], 'skills':[]}
    if job['sk_pool'] == "all":
        skill_list = total_skill_list
    else:
        skill_list = job['sk_pool']
    for i in range(job['skills']):
        pro = random.choice(skill_list)
        while pro in proficiencies['skills']:
            pro = random.choice(skill_list)
        proficiencies['skills'].append(pro)

    return proficiencies


"""
Main character generation function. All other smaller facets, like ability score calculation and equipment rolling are done in their own functions, but they're called from here.
"""
def char_gen():
    race_gen = random.choice(races)
    job_gen =  random.choice(jobs)

    ability_scores, score_mods = ability_gen(job_gen)
    char_profs = profs(race_gen, job_gen)
    char_tounges = [i for i in race_gen['languages'] if not i=="any"]
    if "any" in race_gen['languages']:
        extra = (language_gen(char_tounges, race_gen))
        char_tounges.append(extra[0]['name'])
    char_equipment = equip_gen(job_gen, equipment)

    height_calc_ft = random.randint(race_gen['height'][0], race_gen['height'][1])
    height_calc_in = random.randint(0,11)

    char_race = race_gen['name']
    char_name = random.choice(race_gen[random.choice(['male', 'female'])]) + ' ' + random.choice(race_gen['surname'])
    char_age = random.randint(race_gen['age'][0], race_gen['age'][1])
    char_height = f"{height_calc_ft}'"f'{height_calc_in}"'
    char_job = job_gen['name']

    character = {'name':      char_name,
                 'race':      char_race,
                 'age':       char_age,
                 'height':    char_height,
                 'job':       char_job,
                 'stats':     ability_scores,
                 'stat_mods': score_mods,
                 'languages': char_tounges,
                 'equipment': char_equipment,
                 'proficiencies': char_profs
                }

    output(character)

"""
Just for organisational purposes, this function deals with printing the results of name, age, height, class, ability scores, ability score mods, languages spoken and equipment.
"""
def output(character):
    file_reset = open("output.yaml", 'w')
    print(character['name'],"the", character['race'], character['job'])
    print("Age:", character['age'], " Height:", character['height'])
    for it, scores in enumerate(character['stats'].keys()):
        s = 'stat_mods'
        print(f'{scores}:', character['stats'][scores], f"  ({character[s][scores]})")
    print('Can speak', character['languages'])
    print(character['equipment'])
    skill_set = ['Tools', 'Combat', 'Skills']
    print("Proficiencies:")
    for it, skill_type in enumerate(character['proficiencies'].items()):
        print(f'    {skill_set[it]}: {skill_type[1]}')
    out_order = ['name', 'race', 'age', 'height', 'languages', 'job', 'equipment', 'stats', 'stat_mods']
    stream = open("output.yaml", "w")
    yaml.dump(character, stream)


char_gen()