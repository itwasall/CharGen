from typing import List, Dict

from random import choice, randint
from math import floor

def roll(string):
    throws, sides = string.split('d')
    return sum(randint(1, int(sides)) for _ in range(int(throws)))

ability_chart_0s ={1: [0, 0], 2: [0,  0], 3: [0,  0], 4: [0,  0], 5: [ 0,  0], 6: [0, 0]}
ability_chart_03 ={1: [0, 3], 2: [0,  3], 3: [0,  3], 4: [0,  3], 5: [  0, 3], 6: [0,  3]}
ability_chart_05 ={1: [0, 5], 2: [0,  5], 3: [0,  5], 4: [0,  5], 5: [  0, 5], 6: [0,  5]}
ability_chart_1 = {1: [1, 1], 2: [2,  2], 3: [3,  3], 4: [4,  4], 5: [ 5,  5], 6: [6,  6]}
ability_chart_1a ={1: [1, 1], 2: [3,  3], 3: [5,  5], 4: [5,  5], 5: [10, 10], 6: [15, 15]}
ability_chart_1b ={1: [1, 1], 2: [1,  1], 3: [3,  3], 4: [3,  3], 5: [10, 10], 6: [15, 15]}
ability_chart_2 = {1: [1, 2], 2: [2,  4], 3: [3,  6], 4: [4,  8], 5: [ 5, 10], 6: [6, 12]}
ability_chart_2a ={1: [1, 2], 2: [3,  6], 3: [5, 10], 4: [5, 10], 5: [10, 20], 6: [15, 30]}
ability_chart_3 = {1: [1, 3], 2: [2,  6], 3: [3,  9], 4: [4, 12], 5: [ 5, 15], 6: [6, 18]}
ability_chart_3a ={1: [1, 3], 2: [3,  9], 3: [3,  9], 4: [5, 15], 5: [ 5, 15], 6: [10, 30]}
ability_chart_3b ={1: [1, 3], 2: [1,  3], 3: [3,  9], 4: [3,  9], 5: [10, 30], 6: [10, 30]}
ability_chart_5 = {1: [1, 5], 2: [2, 10], 3: [3, 15], 4: [4, 20], 5: [ 5, 25], 6: [6, 30]}
ability_chart_5a ={1: [1, 5], 2: [3, 15], 3: [3, 15], 4: [5, 25], 5: [ 5, 25], 6: [10, 50]}
ability_chart_6 = {1: [1, 6], 2: [2, 12], 3: [3, 18], 4: [4, 24], 5: [ 5, 30], 6: [6, 36]}
ability_chart_6a ={1: [1, 6], 2: [3, 18], 3: [3, 18], 4: [5, 30], 5: [ 5, 30], 6: [10, 60]}

shiki_power_chart = {
    'The shiki becomes a runaway': ability_chart_0s,
    'Prolong Summoning': ability_chart_3,
    'Regeneration': ability_chart_3,
    'Ranged Attack': ability_chart_2,
    'Transmutation': ability_chart_6,
    'Combat Ability': ability_chart_3,
    'Possession': ability_chart_3,
    'Roll again, and double the ability and cost rolled': ability_chart_0s,
    'Poison': ability_chart_3,
    'Flying': ability_chart_1,
    'Possession - 2': ability_chart_3a,
    'Shapechange': ability_chart_05,
    'Prolong Summoning - 2': ability_chart_3a,
    'Phantasm': ability_chart_3,
    'Roll once more and stop': ability_chart_0s,
    'Poison - 2': ability_chart_3a,
    'Regeneration - 2': ability_chart_3a,
    'Ranged Attack - 2': ability_chart_2a,
    'Shiki Destroyer': ability_chart_5,
    'Additional Damage': ability_chart_2,
    'Soulfind': ability_chart_1,
    'The shiki becomes a chimera': ability_chart_0s,
    'Gaseous Form': ability_chart_03,
    'Phantasm - 2': ability_chart_3b,
    'Explode': ability_chart_1,
    'Flying - 2': ability_chart_1a,
    'Shapechange - 2': ability_chart_05,
    'Transmutation - 2': ability_chart_6a,
    'Roll again, and halve the ability and cost rolled': ability_chart_0s,
    'Explode - 2': ability_chart_1b,
    'Combat Ability - 2': ability_chart_3b,
    'Shiki Destroyer - 2': ability_chart_5a,
    'Gaseous Form - 2': ability_chart_03,
    'Additional Damage - 2': ability_chart_2a,
    'Soulfind - 2': ability_chart_1,
    'Roll three more times then stop': ability_chart_0s
}


def generate_shiki(shiki_level: int, knowledge_stat: int, verbose: bool = False):
    """
    Generates a shiki talisman based on the chart provided in the book
    Args:
        shiki_level (int): The onmyojutsu or shiki crafting skill level of character
        knowledge_stat (int) : The knowledge stat of character

    Returns:

    """
    if shiki_level == 1:
        shiki_level += 1 # Avoiding multiplying by zero below
    max_creation_points: int = (shiki_level - 1) * knowledge_stat
    used_creation_points: int = 0
    talisman_abilities: List = []
    level_count: Dict = {}
    ROLL_DOUBLE = False
    ROLL_HALF = False
    CHIMERA = False
    RUNAWAY = False
    ROLL_ONCE_MORE = False
    ROLL_THRICE_MORE = False
    if verbose:
        print(max_creation_points)

    while used_creation_points < max_creation_points:
        # If shiki became a runaway or chimera, stop
        if CHIMERA or RUNAWAY:
            break

        shiki_ability_roll = choice(list(shiki_power_chart.keys()))
        level, creation_point_cost = shiki_power_chart[shiki_ability_roll][roll('1d6')]

        # If the previous roll was a 'Double' or 'Half' special roll
        if ROLL_HALF or ROLL_DOUBLE:
            # Ignoring the unlevelled abilities, in case of a divide by zero
            if shiki_ability_roll == 'Gaseous Form' or shiki_ability_roll == 'Shapechange':
                pass
            else:
                if ROLL_HALF:
                    level = floor(level / 2)
                    creation_point_cost = floor(creation_point_cost / 2)
                elif ROLL_DOUBLE:
                    level = level * 2
                    creation_point_cost = creation_point_cost * 2
            ROLL_HALF = False
            ROLL_DOUBLE = False
        if verbose:
            print(f'rolled {shiki_ability_roll} at level {level} for cost {creation_point_cost}')

        # Because most abilities appear multiple times on the chart with different level/cost requirements
        #   their names were appended with a '- 2' in order to avoid dupe keys. This gets rid of that so
        #   totals can be accurate
        if shiki_ability_roll.endswith("- 2"):
            shiki_ability_roll = shiki_ability_roll[:-4]


        used_creation_points += creation_point_cost
        if shiki_ability_roll in list(level_count.keys()):
            # These abilities can only be gotten once, so we just continue to the next role. The creation
            #   point cost is refunded back into the pool beforehand
            if shiki_ability_roll == 'Gaseous Form' or shiki_ability_roll == 'Shapechange':
                used_creation_points += creation_point_cost
                continue
            level_count[shiki_ability_roll][0] += level
            level_count[shiki_ability_roll][1] += creation_point_cost
        else:
            level_count[shiki_ability_roll] = [level, creation_point_cost]

        # If the "roll three more times then stop" ability was previously rolled, this increments
        #   that counter until a break at 3
        if ROLL_THRICE_MORE > 0:
            ROLL_THRICE_MORE += 1
            if ROLL_THRICE_MORE == 3:
                break

        # If the "roll once more then stop" ability was previously rolled, break here. This is after the
        #   next ability has been added to the list
        if ROLL_ONCE_MORE:
            break

        # Here are all the flag checks, with the flag-raising abilities being popped from the list as they
        #   are rolled.
        if shiki_ability_roll.startswith('Roll once more and stop'):
            ROLL_ONCE_MORE = True
            shiki_power_chart.pop('Roll once more and stop')
            level_count.pop('Roll once more and stop')
        if shiki_ability_roll.startswith('The shiki becomes a runaway'):
            RUNAWAY = True
            shiki_power_chart.pop('The shiki becomes a runaway')
            level_count.pop('The shiki becomes a runaway')
        if shiki_ability_roll.startswith('The shiki becomes a chimera'):
            CHIMERA = True
            shiki_power_chart.pop('The shiki becomes a chimera')
            level_count.pop('The shiki becomes a chimera')
        if shiki_ability_roll.startswith('Roll again, and double the ability and cost rolled'):
            ROLL_DOUBLE = True
            shiki_power_chart.pop('Roll again, and double the ability and cost rolled')
            level_count.pop('Roll again, and double the ability and cost rolled')
        if shiki_ability_roll.startswith('Roll again, and halve the ability and cost rolled'):
            ROLL_HALF = True
            shiki_power_chart.pop('Roll again, and halve the ability and cost rolled')
            level_count.pop('Roll again, and halve the ability and cost rolled')
        if shiki_ability_roll.startswith('Roll three more times then stop'):
            ROLL_THRICE_MORE = 1
            # Just to make sure the three extra rolls aren't going to be stopped by a lack of points
            max_creation_points += 1000
            shiki_power_chart.pop('Roll three more times then stop')
            level_count.pop('Roll three more times then stop')

    shiki = {'Name': 'Custom Shiki',
             'Creation Points': used_creation_points
             }
    for item in level_count:
        if item == 'Gaseous Form' or item == 'Shapechange':
            shiki[item] = True
        else:
            shiki[item] = level_count[item][0]

    return shiki

print(generate_shiki(3, 8))

