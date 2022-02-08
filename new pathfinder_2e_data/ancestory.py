#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from yaml import safe_load


if sys.os != "linux":
    data_path = "F://CharGen//pathfinder_2e_data"
else:
    data_path = "/home/refrshrs/code/python/CharGen/CharGen/pathfinder_2e_data"
sys.path.append(data_path)

data_ancestry = safe_load(open(f"{data_path}/ancestry.yaml", "rt"))

core, extra = 'Core', 'Extra'

class AncestoryBaseClass:
    def __init__(self, name: str, heritage: str):
        self.name = name
        self.sample_names = []
        self.base_hit_points = 0
        self.size = ""
        self.ability_boost = []
        self.ability_flaw = []
        self.languages = {core: [], extra: []}
        self.heritage = self.get_heritage(heritage)

    def get_heritage(self, heritage):
        return NotImplemented

class Heritage:
    def __init__(self, name: str, race: str, desc:str, effects: dict):
        self.name = name
        self.race = race
        self.effects = effects
        self.desc = desc

Dwarf_AncientBlooded, Dwarf_Warden, Dwarf_Rock, Dwarf_StrongBlooded = [Heritage(i, 'Dwarf', i['desc'], i['effects']) for i in data_ancestry['Dwarf']['heritages'].keys()]
