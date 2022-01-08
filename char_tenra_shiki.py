from random import choice, randint

def roll(string):
    throws, sides = string.split('d')
    return sum(randint(1, int(sides)) for _ in range(int(throws)))

ability_chart_0s ={1: 0,      2: 0,       3: 0,       4: 0,       5: 0,        6: 0}
ability_chart_03 ={1: [0, 3], 2: [0,  3], 3: [0,  3], 4: [0,  3], 5: [  0, 3], 6: [0,  3]}
ability_chart_05 ={1: [0, 5], 2: [0,  5], 3: [0,  5], 4: [0,  5], 5: [  0, 5], 6: [0,  5]}
ability_chart_1s ={1: 1,      2: 1,       3: 1,       4: 1,       5: 1,        6: 1}
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
    'Possession': ability_chart_3a,
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
    'Additional Damage': ability_chart_2a,
    'Soulfind - 2': ability_chart_1,
    'Roll three more times then stop': ability_chart_0s
}

shiki_ability_roll = choice(list(shiki_power_chart.keys()))
shiki_power_roll = shiki_power_chart[shiki_ability_roll][roll('1d6')]

print(shiki_ability_roll, shiki_power_roll)
