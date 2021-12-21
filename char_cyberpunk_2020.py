from math import floor
from random import choice, choices, randint, shuffle

character = {
    "name": "",
    "role": "",
    "character_points": 0,
    "stats": {
        "Intelligence": 0,
        "Reflexes": [0, 0],
        "Technical Ability": 0,
        "Cool": 0,
        "Attractiveness": 0,
        "Luck": 0,
        "Movement Allowance": 0,
        "Body Type": 0,
        "Empathy": [0, 0],
    },
    "movement_stats":{
        "Run": 0,
        "Leap": 0
    },
    "humanity": 0,
    "save": 0,
    "body_type_modifier": ["", 0],
    "armor": {
        "head": 0,
        "torso": 0,
        "right_arm": 0,
        "left_arm": 0,
        "right_leg": 0,
        "left_leg": 0
    },
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
        "ATTR": {
            "Personal_Grooming": 0,
            "Wardrobe_and_Style": 0
        },
        "BODY": {
            "Endurance": 0,
            "Strength_Feat": 0,
            "Swimming": 0
        },
        "COOL_WILL": {
            "Interrogation": 0,
            "Intimidate": 0,
            "Oratory": 0,
            "Resist_TortureDrugs": 0,
            "Streetwise": 0
        },
        "EMPATHY": {
            "Human_Perception": 0,
            "Interview": 0,
            "Leadership": 0,
            "Seduction": 0,
            "Social": 0,
            "Persuasion_and_FastTalk": 0,
            "Perform": 0
        },
        "INT": {
            "Accounting": 0,
            "Anthropology": 0,
            "Awareness_Notice": 0,
            "Biology": 0,
            "Botany": 0,
            "Chemistry": 0,
            "Composition": 0,
            "Diagnose_Illness": 0,
            "Education_and_Gen_Knowledge": 0,
            "Expert": ["", 0],
            "Gamble": 0,
            "Geology": 0,
            "Hide_Evade": 0,
            "History": 0,
            "Language1": ["", 0],
            "Language2": ["", 0],
            "Language3": ["", 0],
            "Library_Search": 0,
            "Mathematics": 0,
            "Physics": 0,
            "Programming": 0,
            "Shadow_Track": 0,
            "Stock_Market": 0,
            "System_Knowledge": 0,
            "Teaching": 0,
            "Wilderness_Survival": 0,
            "Zoology": 0
        },
        "REF": {
            "Archery": 0,
            "Athletics": 0,
            "Brawling": 0,
            "Dance": 0,
            "Dodge_and_Escape": 0,
            "Driving": 0,
            "Fencing": 0,
            "Handgun": 0,
            "Heavy_Weapons": 0,
            "Martial_Art1": ["", 0],
            "Martial_Art2": ["", 0],
            "Martial_Art3": ["", 0],
            "Melee": 0,
            "Motorcycle": 0,
            "Operate_Hvy_Machinary": 0,
            "Pilot_Gyro": 0,
            "Pilot_FixedWing": 0,
            "Pilot_Dirigible": 0,
            "Pilot_VectThrustVechicle": 0,
            "Rifle": 0,
            "Stealth": 0,
            "Submachinegun": 0
        },
        "TECH": {
            "AeroTech": 0,
            "AVTech": 0,
            "BasicTech": 0,
            "Cryotank_Operation": 0,
            "Cyberdeck_Design": 0,
            "CyberTech": 0,
            "Demolitions": 0,
            "Disguise": 0,
            "Electronics": 0,
            "Electronic_Security": 0,
            "First_Aid": 0,
            "Forgery": 0,
            "Gyro_Tech": 0,
            "Paint_or_Draw": 0,
            "Photo_and_Film": 0,
            "Pharmacuticals": 0,
            "Pick_Lock": 0,
            "Pick_Pocket": 0,
            "Play_Instrument": 0,
            "Weaponsmith": 0,
        },
        "OTHER": {
            "Other1": ["", 0],
            "Other2": ["", 0],
            "Other3": ["", 0],
            "Other4": ["", 0],
            "Other5": ["", 0],
            "Other6": ["", 0],
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
        "style": {
            "clothes": "",
            "hair": "",
            "affectations": "",
            "ethnicity": "",
            "language": ""
        },
        "family_background": "",
        "siblings": {
            "male": 0,
            "female": 0
        },
        "motivations": {
            "traits": "",
            "valued_person": "",
            "feel_about_people": "",
            "valued_possession": ""
        },
        "life_events": {
            "year": "",
        }
    },
    "gear": {
        "gear_type": {"cost": 0, "weight": 0}
    },
    "weapons": {
        "weapon_name": {
            "weapon_type": "",
            "WA": "",
            "conc": "",
            "availability": "",
            "damage": "",
            "no_shots": 0,
            "rate_of_fire": 0,
            "rel": ""
        }
    }
}


def roll(throws, sides=0):
    if isinstance(throws, str):
        throw_parse = throws.split("d")
        return (sum(randint(1, int(throw_parse[1])) for _ in range(int(throw_parse[0]))))
    else:
        return sum(randint(1,sides) for _ in range(throws))

def gen_stats(stat_gen_type):
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


def calc_movement_stats(movement_allowance):
    run = movement_allowance * 3
    leap = floor(movement_allowance/4)
    return run, leap

def calc_body_type_modifier(body_type):
    body_type_mod_list = {0: ["Very Weak", 0], 1: ["Very Weak", 0], 2: ["Very Weak", 0],
                          3: ["Weak", -1], 4: ["Weak", -1],
                          5: ["Average", -2], 6: ["Average", -2], 7: ["Average", -2],
                          8: ["Strong", -3], 9: ["Strong", -3],
                          10: ["Very Strong", -4]}
    return body_type_mod_list[body_type]

def calc_save_number(body_type):
    return body_type

def calc_humanity(empathy):
    return empathy * 10

def gen_fast_char():
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
    occupations = {'Rocker': {1: 1_000, 2: 1_000, 3: 1_000, 4: 1_000, 5:1_000, 6: 1_500, 7: 2_000, 8: 5_000, 9: 8_000, 10: 12_000},
                   'Solo': {1: 2_000, 2: 2_000, 3: 2_000, 4: 2_000, 5:2_000, 6: 3_000, 7: 4_500, 8: 7_000, 9: 9_000, 10: 12_000},
                   'Cop': {1: 1_000, 2: 1_000, 3: 1_000, 4: 1_000, 5:1_000, 6: 1_200, 7: 3_000, 8: 5_000, 9: 7_000, 10: 9_000},
                   'Coproate': {1: 1_500, 2: 1_500, 3: 1_500, 4: 1_500, 5:1_500, 6: 3_000, 7: 5_000, 8: 7_000, 9: 9_000, 10: 12_000},
                   'Media': {1: 1_000, 2: 1_000, 3: 1_000, 4: 1_000, 5:1_000, 6: 1_200, 7: 3_000, 8: 5_000, 9: 7_000, 10: 9_000},
                   'Solo': {1: 1_000, 2: 1_000, 3: 1_000, 4: 1_000, 5:1_000, 6: 1_500, 7: 2_000, 8: 5_000, 9: 8_000, 10: 12_000},
                   'Solo': {1: 1_000, 2: 1_000, 3: 1_000, 4: 1_000, 5:1_000, 6: 1_500, 7: 2_000, 8: 5_000, 9: 8_000, 10: 12_000},
                   'Solo': {1: 1_000, 2: 1_000, 3: 1_000, 4: 1_000, 5:1_000, 6: 1_500, 7: 2_000, 8: 5_000, 9: 8_000, 10: 12_000},
                   'Solo': {1: 1_000, 2: 1_000, 3: 1_000, 4: 1_000, 5:1_000, 6: 1_500, 7: 2_000, 8: 5_000, 9: 8_000, 10: 12_000},
                   'Solo': {1: 1_000, 2: 1_000, 3: 1_000, 4: 1_000, 5:1_000, 6: 1_500, 7: 2_000, 8: 5_000, 9: 8_000, 10: 12_000},
                   

"""
SKILL EXCEPTIONS:
    [Rocker] with [Oratory] of 6+ get to add +1 when using their [Charasmatic Leadership] ability
    [Physics] skill requires [Mathematics] skill of +4
    [Zoology] of +8 grants a +1 advantage to any [Wilderness Survival] skill

"""

if __name__ == "__main__":
    print(gen_fast_char())