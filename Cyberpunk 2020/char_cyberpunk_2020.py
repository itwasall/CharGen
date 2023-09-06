from math import floor
from random import choice, choices, randint, shuffle
from chargen import roll, yaml_importer
import yaml

data_careerskills = yaml_importer('cyberpunk_2020_data/careerskills.yaml')
data_languages = yaml_importer('cyberpunk_2020_data/languages.yaml')
data_martial_arts = yaml_importer('cyberpunk_2020_data/martial_arts.yaml')
data_origins_and_style = yaml_importer('cyberpunk_2020_data/origins_and_style.yaml')
data_weapons = yaml_importer('cyberpunk_2020_data/weapons.yaml')
data_motivations = yaml_importer('cyberpunk_2020_data/motivations.yaml')


character = {
    "name": "",
    "role": "",
    "character_points": 0,
    "stats": { "Intelligence": 0, "Reflexes": [0, 0], "Technical Ability": 0, "Cool": 0, "Attractiveness": 0, "Luck": 0, "Movement Allowance": 0, "Body Type": 0, "Empathy": [0, 0], },
    "movement_stats":{ "Run": 0, "Leap": 0 },
    "humanity": 0,
    "save": 0,
    "body_type_modifier": ["", 0],
    "armor": { "head": 0, "torso": 0, "right_arm": 0, "left_arm": 0, "right_leg": 0, "left_leg": 0 },
    "skills": {
        "Special_Abilities": {
            "Authority": 0,
            "Charismatic_Leadership": 0,
            "Combat_Sense": 0,
            "Credibility": 0,
            "Family": 0,
            "Interface": 0,
            "Jury_Rig": 0,
            "Medical_Tech": 0,
            "Resources": 0,
            "Streetdeal": 0
        },
        "ATTR": { "Personal_Grooming": 0, "Wardrobe_and_Style": 0 },
        "BODY": { "Endurance": 0, "Strength_Feat": 0, "Swimming": 0 },
        "COOL_WILL": { "Interrogation": 0, "Intimidate": 0, "Oratory": 0, "Resist_TortureDrugs": 0, "Streetwise": 0 },
        "EMPATHY": { "Human_Perception": 0, "Interview": 0, "Leadership": 0, "Seduction": 0, "Social": 0, "Persuasion_and_FastTalk": 0, "Perform": 0 },
        "INT": {
            "Accounting": 0, "Anthropology": 0, "Awareness_Notice": 0, "Biology": 0, "Botany": 0, "Chemistry": 0, "Composition": 0, "Diagnose_Illness": 0,
            "Education_and_Gen_Knowledge": 0, "Expert": ["", 0], "Gamble": 0, "Geology": 0, "Hide_Evade": 0, "History": 0, "Language1": ["", 0], "Language2": ["", 0],
            "Language3": ["", 0], "Library_Search": 0, "Mathematics": 0, "Physics": 0, "Programming": 0, "Shadow_Track": 0, "Stock_Market": 0, "System_Knowledge": 0,
            "Teaching": 0, "Wilderness_Survival": 0, "Zoology": 0
        },
        "REF": {
            "Archery": 0, "Athletics": 0, "Brawling": 0, "Dance": 0, "Dodge_and_Escape": 0, "Driving": 0, "Fencing": 0, "Handgun": 0, "Heavy_Weapons": 0, "Martial_Art1": ["", 0],
            "Martial_Art2": ["", 0], "Martial_Art3": ["", 0], "Melee": 0, "Motorcycle": 0, "Operate_Hvy_Machinary": 0, "Pilot_Gyro": 0, "Pilot_FixedWing": 0, "Pilot_Dirigible": 0,
            "Pilot_VectThrustVechicle": 0, "Rifle": 0, "Stealth": 0, "Submachinegun": 0
        },
        "TECH": {
            "AeroTech": 0, "AVTech": 0, "BasicTech": 0, "Cryotank_Operation": 0, "Cyberdeck_Design": 0, "CyberTech": 0, "Demolitions": 0, "Disguise": 0, "Electronics": 0,
            "Electronic_Security": 0, "First_Aid": 0, "Forgery": 0, "Gyro_Tech": 0, "Paint_or_Draw": 0, "Photo_and_Film": 0, "Pharmacuticals": 0, "Pick_Lock": 0, "Pick_Pocket": 0,
            "Play_Instrument": 0, "Weaponsmith": 0, },
        "OTHER": {
            "Other1": ["", 0], "Other2": ["", 0], "Other3": ["", 0], "Other4": ["", 0], "Other5": ["", 0], "Other6": ["", 0],
        }
    },
    "cybernetics": {
        "cybernetics_type": {"HL": 0, "cost": 0},
    },
    "cybernetics_totals": {
        "HL": 0,
        "euro": 0
    },
    "lifepath": {
        "style": { "clothes": "", "hair": "", "affectations": "", "ethnicity": "", "language": "" },
        "family_background": "",
        "siblings": { "male": 0, "female": 0 },
        "motivations": { "traits": "", "valued_person": "", "feel_about_people": "", "valued_possession": "" },
        "life_events": { "year": "", }
    },
    "gear": {
        "gear_type": {"cost": 0, "weight": 0}
    },
    "weapons": {
        "weapon_name": {
            "weapon_type": "", "weapon_accuray": "", "conceilability": "", "availability": "", "damage": "",
            "magazine_size": 0, "rate_of_fire": 0, "reliability": "" }
    }
}

# ====== FLAGS ======
global LIFE_EVENT_ILLNESS, LIFE_EVENT_ACCIDENT_DISFIGUREMENT
LIFE_EVENT_ILLNESS = 0
LIFE_EVENT_ACCIDENT_DISFIGUREMENT = 0

# ===== GEN =========

def gen_stats(stat_gen_type):
    """Generates stat pool based on stat generation type
    Types:
        - random: Roll 9D10s, total results
        - fast: Roll 9D10s, rerolling any >2's
        - cinematic: Predetermined number of stat points based on cinematic type"""
    stat_gen_type = stat_gen_type.lower()
    if stat_gen_type == "random":
        # Random type ~ Roll 9D10s, total results
        total_stats = roll("9d10")
    elif stat_gen_type == "fast":
        # Fast type ~ Roll 9D10s, rerolling any 2 or belows as many times as you like
        fast_stats = []
        while len(fast_stats) < 9:
            fast_roll_try = roll("1d10")
            if fast_roll_try >= 3:
                fast_stats.append(fast_roll_try)
            else:
                continue
        total_stats = sum(fast_stats)
    elif stat_gen_type == "cinematic":
        cinematic_types = {"Major Hero": 80,
                           "Major Supporting Character": 70,
                           "Minor Hero": 75,
                           "Minor Supporting Character": 60,
                           "Average": 50}
        total_stats = cinematic_types[choice(list(cinematic_types.keys()))]
    else:
        raise Exception
    return total_stats


def gen_family_background():
    """Generates family background based on options in Corebook"""
    family_ranking_list = data_origins_and_style['family_ranking']
    parents_something_happened_list = data_origins_and_style['parents_something_happened']
    family_tragedy_list = data_origins_and_style['family_tragedy']
    childhood_environment_list = data_origins_and_style['childhood_environment']
    family_status_list = ['Family status is in danger, and you risk losing everything', 'Family status is OK, even if parents are missing or dead']
    parents = ['Both parents are living', 'Something has happened to one or both parents']
    family_background = {}

    # Family Ranking
    family_background['Family Ranking'] = choice(family_ranking_list)

    # Are parents alive or dead?
    family_background['Parental Status'] = choices(parents, [6, 3])[0]
    if family_background['Parental Status'] == parents[1]:
        # If parent(s) are not alive
        family_background['Something Happened to Parents'] = choice(parents_something_happened_list)

    # Is family status in danger?
    family_background['Family Status'] = choices(family_status_list, [6, 3])[0]
    if family_background['Family Status'] == family_status_list[0]:
        # Family status is in danger
        family_background['Family Tragedy'] = choice(family_tragedy_list)

    # How you grew up
    family_background['Childhood Environment'] = choice(childhood_environment_list)
    return family_background


def gen_motivations():
    """Generates character motivations based on options in Corebook"""
    personality_traits_list = data_motivations['personality_traits']
    person_valued_most_list = data_motivations['person_valued_most']
    thing_valued_most_list = data_motivations['thing_valued_most']
    disp_towards_others_list = data_motivations['disp_towards_others']
    possession_valued_most_list = data_motivations['possession_valued_most']

    motivations = {}

    motivations['Personality'] = choice(personality_traits_list)
    motivations['Person you value most'] = choice(person_valued_most_list)
    motivations['Thing you value most'] = choice(thing_valued_most_list)
    motivations['Disposition towards others'] = choice(disp_towards_others_list)
    motivations['Most valued possession'] = choice(possession_valued_most_list)

    return motivations


def gen_life_events():
    def gen_life_events_bpbw():
        global LIFE_EVENT_ILLNESS, LIFE_EVENT_ACCIDENT_DISFIGUREMENT

        coinflip = choice(['Heads', 'Tails'])
        life_event = {}
        event_roll = roll("1d10")
        if coinflip == 'Heads':
            # Disaster strikes!
            match event_roll:
                case 1:
                    financial_loss_or_debt_roll = roll("100d10")
                    return f'Financial loss or debt: You have lost {financial_loss_or_debt_roll} eurodollars. If you can\'t pay this now, you have a debt to pay, in cash - or blood'
                case 2:
                    imprisonment_roll = roll("1d10")
                    imprisonment_type = choice(['in prison', 'held hostage'])
                    return f'Imprisonment: You have been {imprisonment_type} for {imprisonment_roll} months this year'
                case 3:
                    LIFE_EVENT_ILLNESS += 1
                    return f'Illness or Addiction: You have contracted either an illness or drug habit in this time.'
                case 4:
                    betrayal = choices(['You are being blackmailed', 'A secret was exposed', 'You were betrayed by a close friend in romance', 'You were betrayed by a close friend in your career path'], [3, 4, 2, 1])[0]
                    life_event['Betrayal'] = f"You've been betrayed! {betrayal}."
                    return f'Betrayal: You\'ve been betrayed! {betrayal}'
                case 5:
                    accident = choices(['You were terribly disfigured', f'You were hospitalised for {roll("1d10")} months this year', f'You have lost {roll("1d10")} months of memory this year', 'You constantly relive nightmares of the accident each night and wake up screaming'], [4, 2, 2, 2])
                    if accident == 'You were terribly disfigured':
                        LIFE_EVENT_ACCIDENT_DISFIGUREMENT -= 5
                    return f'Accident: You\'ve had an accident. {accident}'
                case 6:
                    who_got_killed = choice(['Friend', 'Lover', 'Relative'])
                    killed = choices(['They died accidentally', 'They were murdered by unknown parties', 'They were murdered and you know who did it. You just need the proof'], [5, 3, 2])[0]
                    return f'{who_got_killed} died: You lost a {who_got_killed} that meant a lot to you. {killed}.'
                case 7:
                    false_accusation = choices(['the accusation is theft', "it's cowardice", "it's murder", "it's rape", "it's lying or betrayal"], [3, 2, 3, 1, 1])
                case _:
                    pass
        return life_event


    def gen_life_events_fae():
        pass


    def gen_life_events_ri():
        pass

    def yearly_event(adult_year, life_events):
        match event_roll := roll("1d10"):
            case 1:
                life_events[f'Age {adult_year + 16}'] = gen_life_events_bpbw()
            case 4|5|6:
                life_events[f'Age {adult_year + 16}'] = gen_life_events_fae()
            case 7|8:
                life_events[f'Age {adult_year + 16}'] = gen_life_events_ri()
            case _:
                life_events[f'Age {adult_year + 16}'] = 'Nothing happened that year'
    age = roll("2d6") + 16
    life_events = {}
    for adult_year in range(age-16):
        yearly_event(adult_year, life_events)
    return life_events

print(gen_life_events())



def calc_movement_stats(movement_allowance):
    """Calculates run + leap values from [arg]movement_allowance input var"""
    run = movement_allowance * 3
    leap = floor(movement_allowance/4)
    return run, leap


def calc_body_type_modifier(body_type):
    """Calculates BTM value from [arg]body_type input var"""
    body_type_mod_list = {0: ["Very Weak", 0], 1: ["Very Weak", 0], 2: ["Very Weak", 0],
                          3: ["Weak", -1], 4: ["Weak", -1],
                          5: ["Average", -2], 6: ["Average", -2], 7: ["Average", -2],
                          8: ["Strong", -3], 9: ["Strong", -3],
                          10: ["Very Strong", -4]}
    return body_type_mod_list[body_type]

def calc_save_number(body_type):
    """Calculates save number value from [arg]body_type input var"""
    return body_type

def calc_humanity(empathy):
    """Calculates humanity value from [arg]empathy input var"""
    return empathy * 10

def gen_fast_char():
    """Generates an NPC based on the 'Fast NPC' rules laid out in the Corebook"""
    fast_npc = {'stats':{}}
    fast_npc_stats = ["INT", "REF", "COOL", "LUCK", "ATTR", "TECH", "BODY", "MA", "EMP"]
    stat_rolls = []
    while len(stat_rolls) < 9:
        # For fast NPC generation, you roll 2d6 for each stat, rerolling anything higher than an eleven
        fast_npc_stat_roll = roll("2d6")
        if fast_npc_stat_roll >= 11:
            continue
        else:
            stat_rolls.append(fast_npc_stat_roll)
    for it, stat in enumerate(fast_npc_stats):
        fast_npc['stats'][stat] = stat_rolls[it]
    return fast_npc

def starting_cash(role, special_ability_level):
    """Generates starting cash amount based on [arg1]role and [arg2]special_ability_level input vars"""
    occupations = {'Rocker': {1: 1_000, 2: 1_000, 3: 1_000, 4: 1_000, 5:1_000, 6: 1_500, 7: 2_000, 8: 5_000, 9: 8_000, 10: 12_000},
                   'Solo': {1: 2_000, 2: 2_000, 3: 2_000, 4: 2_000, 5:2_000, 6: 3_000, 7: 4_500, 8: 7_000, 9: 9_000, 10: 12_000},
                   'Cop': {1: 1_000, 2: 1_000, 3: 1_000, 4: 1_000, 5:1_000, 6: 1_200, 7: 3_000, 8: 5_000, 9: 7_000, 10: 9_000},
                   'Coproate': {1: 1_500, 2: 1_500, 3: 1_500, 4: 1_500, 5:1_500, 6: 3_000, 7: 5_000, 8: 7_000, 9: 9_000, 10: 12_000},
                   'Media': {1: 1_000, 2: 1_000, 3: 1_000, 4: 1_000, 5:1_000, 6: 1_200, 7: 3_000, 8: 5_000, 9: 7_000, 10: 9_000},
                   'Fixer': {1: 1_500, 2: 1_500, 3: 1_500, 4: 1_500, 5:1_500, 6: 3_000, 7: 5_000, 8: 7_000, 9: 8_000, 10: 10_000},
                   'Techie': {1: 1_000, 2: 1_000, 3: 1_000, 4: 1_000, 5:1_000, 6: 2_000, 7: 3_000, 8: 4_000, 9: 5_000, 10: 8_000},
                   'Netrunner': {1: 1_000, 2: 1_000, 3: 1_000, 4: 1_000, 5:1_000, 6: 2_000, 7: 3_000, 8: 5_000, 9: 7_000, 10: 10_000},
                   'Medtechie': {1: 1_600, 2: 1_600, 3: 1_600, 4: 1_600, 5:1_600, 6: 3_000, 7: 5_000, 8: 7_000, 9: 10_000, 10: 15_000},
                   'Nomad': {1: 1_000, 2: 1_000, 3: 1_000, 4: 1_000, 5:1_000, 6: 1_500, 7: 2_000, 8: 3_000, 9: 4_000, 10: 5_000}
    }
    starting_salary = occupations[role][special_ability_level]
    money = starting_salary * roll("1d3")
    return money

"""
SKILL EXCEPTIONS:
    [Rocker] with [Oratory] of 6+ get to add +1 when using their [Charasmatic Leadership] ability
    [Physics] skill requires [Mathematics] skill of +4
    [Zoology] of +8 grants a +1 advantage to any [Wilderness Survival] skill
"""

if __name__ == "__main__":
    x = gen_motivations()
    for i in x:
        print(f"{i}: {x[i]}")
