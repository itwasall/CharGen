"""
The purpose of this program is to generate a DND character. So far race selection, attribute generation, class selection and attribute allocation have been implimented.
"""
import random
import json
rInt = random.randint

# Here are some boiler plate definitions for certain parameters including ability scores, alignments, races and subraces and classes
attributes = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']

alignment_h = ['Lawful ', 'Neutral ', 'Chaotic ']
alignment_v = ['Good', 'Neutral', 'Evil']

races = ['Elf', 'Dwarf', 'Halfling', 'Gnome', 'Human', 'Dragonborn', 'Half-Elf', 'Half-Orc', 'Tiefling']
races_elf = ['High ', 'Wood ', 'Drow ']
races_dwarf = ['Hill ', 'Mountain ']
races_halfling = ['Stout ', 'Lightfoot ']
races_gnome = ['Forest ', 'Rock ']
races_human = ['Calishite ', 'Chondathan ', 'Damaran ', 'Illuskan ', 'Mulan ', 'Rashemi', 'Shou ', 'Turami ']
gender = ['Male', 'Female']

classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter (DEX)', 'Fighter (STR)', 'Eldritch Knight', 'Monk',
           'Paladin', 'Ranger (DEX)', 'Ranger (STR)', 'Rogue', 'Arcane Trickster', 'Sorcerer', 'Warlock', 'Wizard']


"""
charGen is the main function for generating a character. Or at least for now its the function where everything happens.
"""
def charGen():
    rolls = []
    # Rolling 4d6 for each attribute in the game. Although this is done for each attribute, the allocation happens later on when class is determined
    for attribute in attributes:
        die_roll = dice(4,6)
        rolls.append(die_roll)

    # Selecting race. If a race has any sub-races, that gets messily done after on a per-race basis.
    race = random.choice(races)

    if race == 'Elf':
        # Code for determining subrace
        race = random.choice(races_elf) + race
        if race == 'High Elf':
            # This long list of numbers represents the probabilities for the class the NPC will have. I literally took the figures from an
            # analysis of which classes worked best with each race, so the numbers aren't equal between races.
            job, rolls = job_gen(rolls, [1, 4, 2, 2, 6, 2, 6, 4, 2, 5, 2, 5, 6, 2, 2, 6])
            # job_gen allocateds the previously rolled ability scores according to the class chosen. Only after that's done do I add the racial bonuses cuz otherwise I'd have to write
            # shit out separately.
            rolls[3] += 1
        elif race == 'Wood Elf':
            job, rolls = job_gen(rolls, [3, 4, 5, 5, 6, 2, 4, 6, 2, 6, 3, 5, 5, 2, 3, 2])
            rolls[4] += 1
        elif race == 'Drow Elf':
            job, rolls = job_gen(rolls, [2, 6, 3, 3, 5, 2, 4, 5, 5, 5, 2, 5, 5, 6, 6, 1])
            rolls[5] += 1
        rolls[1] += 2

    elif race == 'Halfling':
        race = random.choice(races_halfling) + race
        if race == 'Stout Halfling':
            job, rolls = job_gen(rolls, [6, 5, 4, 4, 6, 2, 4, 6, 4, 6, 2, 5, 5, 4, 4, 4])
            rolls[2] += 1
        elif race == 'Lightfoot Halfling':
            job, rolls = job_gen(rolls, [4, 6, 4, 4, 6, 2, 3, 6, 2, 5, 2, 6, 6, 6, 6, 3])
            rolls[5] += 1
        rolls[1] += 2

    elif race == 'Dwarf':
        race = random.choice(races_dwarf) + race
        if race == 'Mountain Dwarf':
            job, rolls = job_gen(rolls, [6, 2, 4, 4, 3, 6, 5, 3, 6, 2, 6, 2, 2, 2, 2, 2])
            rolls[0] += 2
        elif race == 'Hill Dwarf':
            job, rolls = job_gen(rolls, [6, 2, 4, 4, 3, 6, 5, 3, 6, 2, 6, 2, 2, 2, 2, 2])
            rolls[4] += 1
        rolls[2] += 2

    elif race == 'Gnome':
        race = random.choice(races_gnome) + race
        if race == 'Forest Gnome':
            job, rolls = job_gen(rolls, [2, 2, 2, 2, 3, 2, 6, 3, 2, 3, 2, 4, 6, 2, 2, 6])
            rolls[1] += 1
        elif race == 'Rock Gnome':
            job, rolls = job_gen(rolls, [2, 2, 2, 2, 2, 2, 5, 2, 2, 2, 2, 3, 5, 2, 2, 6])
            rolls[2] += 1
        rolls[3] += 2

    elif race == 'Human':
        race = random.choice(races_human) + race
        job, rolls = job_gen(rolls, [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4])
        # Humans get +1 in each attribute
        for i, _ in enumerate(rolls):
            rolls[i] += 1

    elif race == 'Half-Elf':
        job, rolls = job_gen(rolls, [4, 7, 4, 4, 4, 4, 4, 4, 7, 4, 4, 4, 4, 7, 7, 4])
        rolls[5] += 2

    elif race == 'Half-Orc':
        job, rolls = job_gen(rolls, [6, 3, 3, 4, 4, 6, 6, 2, 6, 4, 6, 4, 4, 2, 6, 2])
        rolls[0] += 2
        rolls[2] += 1

    elif race == 'Dragonborn':
        job, rolls = job_gen(rolls, [6, 5, 4, 2, 6, 6, 6, 2, 6, 3, 5, 2, 3, 5, 5, 2])
        rolls[0] += 2
        rolls[5] += 1

    elif race == 'Tiefling':
        job, rolls = job_gen(rolls, [2, 6, 2, 2, 2, 2, 3, 2, 5, 2, 2, 4, 4, 6, 6, 5])
        rolls[3] += 1
        rolls[5] += 2

    else:
        pass
    ability_score_mods = {1:-5, 2:-4, 3:-4, 4:-3, 5:-3, 6:-2, 7:-2, 8:-1, 9:-1,
                         10:0, 11:0, 12:1, 13:1, 14:2, 15:2, 16:3, 17:3, 18:4,
                         19:4, 20:5, 21:5, 22:6, 23:6, 24:7, 25:7, 26:8, 27:8,
                         28:9, 29:9, 30:10}
    rolls_mod = []
    for it, stat in enumerate(rolls):
        rolls_mod.append(ability_score_mods[stat])
    hp = hit_points(job, rolls_mod[2])
    gender_roll = random.choice(gender)
    name_roll = name(race, gender_roll)
    print(f'[{name_roll}] the [{race}] [{job}]')
    print(f'HP  {hp}')
    for i, _ in enumerate(attributes):
        if rolls_mod[i] >= 1:
            print(f'{attributes[i]} {rolls[i]} (+{rolls_mod[i]})')
        elif rolls_mod[i] < 0:
            print(f'{attributes[i]} {rolls[i]}  ({rolls_mod[i]})')
        elif rolls_mod[i] == 0:
            print(f'{attributes[i]} {rolls[i]} ( {rolls_mod[i]})')

"""
This is the name generation. Needs a race and gender to determine which lists to pull from
"""
def name(race, gender):
    name_roll = ""
    # All the names are stored in json format for easy expansion
    with open("F://CharGen//names.json") as file:
        name_list = json.load(file)
        for i in name_list:
            if race == i['race']:
                if gender == 'Male':
                    # name_roll = [random first name] + [random surname]
                    name_roll = random.choice(i['male']) + ' ' + random.choice(i['surname'])
                elif gender == 'Female':
                    name_roll = random.choice(i['female']) + ' ' + random.choice(i['surname'])
    return name_roll

"""
Determines character alignment. Not actually implimented into the charGen function yet, as I need to do probability weighting for each race
"""
def alignment():
    aligned = alignment_h[rInt(0, 2)] + alignment_v[rInt(0, 2)]
    print(aligned)

"""
Dice rolling function. Allows for multiple throws of the same dice.
"""
def dice(throws=1, sides=6):
    total = 0
    for throw in range(throws):
        total += random.randint(1,sides)
    return total

def job_gen(ab_score, w):
    # rolls is not the same as rolls in charGen, ab_score is. job_gen.rolls is just being populated with 0s to make things easy for me later
    rolls = [0, 0, 0, 0, 0, 0]
    # Code to select the class, using the list of numbers as weights
    job = random.choices(classes, weights=w)
    # Here we sort the charGen.rolls into reverse order. Or basically largest first. This makes allocation easier as each class has different
    # ability scores that are gonna be more effective, having the rolled numbers in order beforehand makes the code below easier to understand. Slightly.
    ab_score.sort(reverse=True)
    # Essentially just a giant excuse of a switch case table. Each number in the value list pair represents an attribute as they're indexed in the attributes list
    # at the top. 0 = STR, 1 = DEX etc.
    job_ability_priority = {'Barbarian': [0, 2],
                            'Bard': [5, 1],
                            'Cleric': [4, 2],
                            'Druid': [4, 3],
                            'Fighter (DEX)': [1, 2],
                            'Fighter (STR)': [0, 2],
                            'Eldritch Knight': [3, 4],
                            'Monk': [2, 4],
                            'Paladin': [0, 5],
                            'Ranger (DEX)': [1, 4],
                            'Ranger (STR)': [0, 1],
                            'Rogue': [1, 3],
                            'Sorcerer': [5, 2],
                            'Arcane Trickster': [3, 1],
                            'Warlock': [5, 2],
                            'Wizard': [3, 2]}
    # For some reason random.choices gives a 1 item-long list, so having the job[0] amidst everything makes this almost unreadable. Basically we're using the pair
    # of numbers in the above switch case to determine which of the two highest rolls go to which ability score.
    for i in range(2):
        rolls[job_ability_priority[job[0]][i]] = ab_score[i]
    # and now we do the rest. I have to loop 6 times here because I won't know which roll values aren't 0 and need populating, so I have a try/except to hand-wave
    # the inevitable indexErrors
    for i in range(6):
        if rolls[i] < 1:
            try:
                rolls[i] = ab_score[2+i]
            except IndexError:
                rolls[i] = ab_score[i]
                continue
    # Now we return with the class name (1 value list dictates I have to do this weird notation to just get the class name in string format) and the properly
    # allocated rolls.
    return job[0], rolls

"""
This calculates hit points based on the class and constitution mod.
Also has code for calculating HP if they aren't level 1 for some reason.
"""
def hit_points(job, con_mod=0, level=1, total_hp=0):
    hp_gains = {'Barbarian':[12, dice(1,12)],
                'Bard':[8, dice(1,8)],
                'Cleric':[8, dice(1,8)],
                'Druid':[8, dice(1,8)],
                'Fighter (STR)':[10, dice(1,10)],
                'Fighter (DEX)':[10, dice(1,10)],
                'Eldritch Knight':[10, dice(1,10)],
                'Monk':[8,dice(1,8)],
                'Paladin':[10, dice(1,10)],
                'Ranger (STR)':[10, dice(1,10)],
                'Ranger (DEX)':[10, dice(1,10)],
                'Rogue':[8, dice(1,8)],
                'Arcane Trickster':[8, dice(1,8)],
                'Sorcerer':[6, dice(1,6)],
                'Warlock':[8,dice(1,8)],
                'Wizard':[6, dice(1,6)]}
    if level == 1:
        hp = hp_gains[job][0] + con_mod
    else:
        hp = total_hp + hp_gains[job][1]
    return hp

charGen()
alignment()
