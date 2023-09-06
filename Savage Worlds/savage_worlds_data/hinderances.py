#!/usr/bin/env python
# -*- coding: utf-8 -*-
from yaml import safe_load

"""
So like, what the fuck does this do?

In order to populate the SavageHinderanceClass's data correctly,
    I'm first declaring them all as empty first, putting them in a list,
    then iterating over the keys in the hinderances.yaml file (as they are of equal length)
    and populating the [desc], [rank], [conflict], [penalty] & [bonus] fields if they
    exist in the .yaml file.

This way I can have all the classes ready, even if the data isn't fully ready yet. If a
    key doesn't exist it'll simply show up as [None] until the work is done.
"""

hinderance_data = safe_load(open('savage_worlds_data/hinderances.yaml', 'rt'))

h_data = hinderance_data

class SavageHinderanceClass:
    def __init__(
        self,
        name: str = None,
        desc: str = None,
        rank: str = None,
        conflict: str = None,
        penalty: dict = None,
        bonus: dict = None
    ):
        self.name = name
        self.desc = desc
        self.rank = rank
        self.conflict = conflict
        self.penalty = penalty
        self.bonus = bonus
        self.cost = 0

    def get_cost(self, rank: str):
        if rank.capitalize == 'Minor':
            return 1
        elif rank.capitalize == 'Major':
            return 2

    def __repr__(self):
        return self.name

All_Thumbs = SavageHinderanceClass()
Anemic = SavageHinderanceClass()
Arrogant = SavageHinderanceClass()
BadEyes_Minor = SavageHinderanceClass()
BadEyes_Major = SavageHinderanceClass()
BadLuck = SavageHinderanceClass()
BigMouth = SavageHinderanceClass()
Blind = SavageHinderanceClass()
Bloodthirsty = SavageHinderanceClass()
CantSwim = SavageHinderanceClass()
Cautious = SavageHinderanceClass()
Clueless = SavageHinderanceClass()
CodeOfHonor = SavageHinderanceClass()
Curious = SavageHinderanceClass()
DeathWish = SavageHinderanceClass()
Delusional_Minor = SavageHinderanceClass()
Delusional_Major = SavageHinderanceClass()
DoubtingThomas = SavageHinderanceClass()
Driven_Minor = SavageHinderanceClass()
Driven_Major = SavageHinderanceClass()
Elderly = SavageHinderanceClass()
Enemy_Minor = SavageHinderanceClass()
Enemy_Major = SavageHinderanceClass()
Greedy_Minor = SavageHinderanceClass()
Greedy_Major = SavageHinderanceClass()
Habit_Minor = SavageHinderanceClass()
Habit_Major = SavageHinderanceClass()
HardOfHearing_Minor = SavageHinderanceClass()
HardOfHearing_Major = SavageHinderanceClass()
Heroic = SavageHinderanceClass()
Hesitant = SavageHinderanceClass()
Illiterate = SavageHinderanceClass()
Impulsive = SavageHinderanceClass()
Jealous_Minor = SavageHinderanceClass()
Jealous_Major = SavageHinderanceClass()
Loyal = SavageHinderanceClass()
Mean = SavageHinderanceClass()
MildMannered = SavageHinderanceClass()
Mute = SavageHinderanceClass()
Obese = SavageHinderanceClass()
Obligation_Minor = SavageHinderanceClass()
Obligation_Major = SavageHinderanceClass()
OneArm = SavageHinderanceClass()
OneEye = SavageHinderanceClass()
Outsider_Minor = SavageHinderanceClass()
Outsider_Major = SavageHinderanceClass()
Overconfident = SavageHinderanceClass()
Pacifist_Minor = SavageHinderanceClass()
Pacifist_Major = SavageHinderanceClass()
Phobia_Minor = SavageHinderanceClass()
Phobia_Major = SavageHinderanceClass()
Poverty = SavageHinderanceClass()
Quirk = SavageHinderanceClass()
Ruthless_Minor = SavageHinderanceClass()
Ruthless_Major = SavageHinderanceClass()
Secret_Minor = SavageHinderanceClass()
Secret_Major = SavageHinderanceClass()
Shamed_Minor = SavageHinderanceClass()
Shamed_Major = SavageHinderanceClass()
Slow_Minor = SavageHinderanceClass()
Slow_Major = SavageHinderanceClass()
Small = SavageHinderanceClass()
Stubborn = SavageHinderanceClass()
Suspicious_Minor = SavageHinderanceClass()
Suspicious_Major = SavageHinderanceClass()
ThinSkinned_Minor = SavageHinderanceClass()
ThinSkinned_Major = SavageHinderanceClass()
TongueTied = SavageHinderanceClass()
Ugly_Minor = SavageHinderanceClass()
Ugly_Major = SavageHinderanceClass()
Vengeful_Minor = SavageHinderanceClass()
Vengeful_Major = SavageHinderanceClass()
Vow_Minor = SavageHinderanceClass()
Vow_Major = SavageHinderanceClass()
Wanted_Minor = SavageHinderanceClass()
Wanted_Major = SavageHinderanceClass()
Yellow = SavageHinderanceClass()
Young_Minor = SavageHinderanceClass()
Young_Major = SavageHinderanceClass()

hinderances = [
    All_Thumbs, Anemic, Arrogant, BadEyes_Minor, BadEyes_Major, BadLuck, BigMouth, Blind, Bloodthirsty, CantSwim, Cautious, Clueless,
    CodeOfHonor, Curious, DeathWish, Delusional_Minor, Delusional_Major, DoubtingThomas, Driven_Minor, Driven_Major, Elderly, Enemy_Minor,
    Enemy_Major, Greedy_Minor, Greedy_Major, Habit_Minor, Habit_Major, HardOfHearing_Minor, HardOfHearing_Major, Heroic, Hesitant,
    Illiterate, Impulsive, Jealous_Minor, Jealous_Major, Loyal, Mean, MildMannered, Mute, Obese, Obligation_Minor, Obligation_Major,
    OneArm, OneEye, Outsider_Minor, Outsider_Major, Overconfident, Pacifist_Minor, Pacifist_Major, Phobia_Minor, Phobia_Major, Poverty,
    Quirk, Ruthless_Minor, Ruthless_Major, Secret_Minor, Secret_Major, Shamed_Minor, Shamed_Major, Slow_Minor, Slow_Major, Small, Stubborn,
    Suspicious_Minor, Suspicious_Major, ThinSkinned_Minor, ThinSkinned_Major, TongueTied, Ugly_Minor, Ugly_Major, Vengeful_Minor,
    Vengeful_Major, Vow_Minor, Vow_Major, Wanted_Minor, Wanted_Major, Yellow, Young_Minor, Young_Major
]

for it, key in enumerate(h_data.keys()):
    hinderances[it].name = key
    if 'desc' in h_data[key].keys():
        hinderances[it].desc = h_data[key]['desc']
    if 'rank' in h_data[key].keys():
        hinderances[it].rank = h_data[key]['rank']
        hinderances[it].cost = hinderances[it].get_cost(h_data[key]['rank'])
    if 'conflict' in h_data[key].keys():
        hinderances[it].conflict = h_data[key]['conflict']
    if 'penalty' in h_data[key].keys():
        hinderances[it].penalty = h_data[key]['penalty']
    if 'bonus' in h_data[key].keys():
        hinderances[it].bonus = h_data[key]['bonus']





