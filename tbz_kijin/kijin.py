#!/usr/bin/env python
# -*- coding: utf-8 -*-

from yaml import safe_load

data = safe_load(open("tbz_data/mechanica.yaml", 'rt'))

class Kijin:
    def __init__(self, body_parts, extras):
        self.body_parts = body_parts
        self.extras = extras

data_mechanica = data['mechanica']
data_slots = data['mechanica']

book_templates = {
    'Man-Gohki':  {
        'Body Parts': {
            'Sensors': 'Hei',
            'Arms': 'Otsu',
            'Torso': 'Hei',
            'Legs': 'Hei'
        },
        'Mechanica': {
            'Sensors': ['Flash Burst'],
            'Arms': ['Vajra Claws', 'White Heat Palm'],
            'Torso': ['Heart Engine'],
            'Legs': ['Roller Type Feet']
        },
        'Heart Engine': True,
        'Weapon Interface': {'Arms': 'Vajra Claws'},
    }
}
