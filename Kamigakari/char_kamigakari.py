#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import ceil

class CombatStats:
    def __init__(self):
        self.accuracy = None
        self.evasion = None
        self.invocation = None
        self.resistance = None
        self.instinct = None
        self.physical_damage = None
        self.magical_damage = None
        self.initative = None
        self.hit_points = None

class Stats:
    def __init__(self, strength, agility, intellect, will, luck):
        self.strength = strength
        self.agility = agility
        self.intellect = intellect
        self.will = will
        self.luck = luck

    def __repr__(self):
        return f"Strength: {self.strength}\nAgility: {self.agility}\nIntellect: {self.intellect}\nWill: {self.will}\nLuck: {self.luck}"

class SubStats:
    def __init__(self, stats: Stats, level: int):
        self.pd = ceil(stats.strength / 2)
        self.md = ceil(stats.intellect / 2)
        self.initative = stats.agility + 5
        self.hp = stats.strength + stats.will + (level * 3)

    def __repr__(self):
        return f"PD: {self.pd}\nMD: {self.md}\nInitative: {self.initative}\nHP: {self.hp}"


ParagonWarrior = Stats(5, 4, 2, 2, 2)
ParagonAdept = Stats(4, 4, 2, 1, 4)
ParagonOccultist = Stats(2, 3, 5, 4, 1)

class Character:
    def __init__(self, stats: Stats):
        self.name = None
        self.level = 1
        self.stats: Stats = stats
        self.substats = SubStats(self.stats, self.level)

jerry = Character(ParagonWarrior)
print(jerry.stats)
print(jerry.substats)

def gen_character():
    # Step 1. Set level
        # 1
    # Step 2. Choose Ancestry
        # Ancestry name
        # Stat type (warrior, adept, occultist)
        # Ancestrial trait
        # Add 1 point to any stat
    # Step 3. Calculate Substats
        # substats class
    # Step 4. Choose facets
        # Choose two facets
        # Each facet has a beta and alpha variant, it's possibile to choose the same facet so long as they are of different variants
        # Facet Name
        # Type (beta/alpha)
        # Group
        # Combat mods
    # Step 5. Calculate combat stats
        # Using the combat mods + stats + substats, calculate combat stats
    # Step 6. Pick talents
        # The PC is granted all Facet Talents from their chosen facets that are marked with the word "key"
        # Pick two Ancestry talents
        # Pick two additional basic talents that the PC is eligible for
    # Step 7. Purchase Items
        # lmao fuck you you buy all your items
        # Weapons
        # Protection
        # Accessories
        # Sacraments
        # Consumables
        # Starting gold is 5,000g at level 1
        # else Gold = [(Level - 1) * 1,500g] + 5000g
        # Equip items and add their mods to combat stats
    # Step 8. Choose Facade
    # Step 9. Details
        # Use in-book chargen shit
    # Step 10. Finished
        # This is not a fucking step
    pass
