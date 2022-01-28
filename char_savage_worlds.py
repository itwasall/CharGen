#!/usr/bin/env python
# -*- coding: utf-8 -*-
from chargen import roll, yaml_importer, BaseAttributeClass, BaseInventoryClass, BaseItemClass, BaseWeaponClass

Agility = BaseAttributeClass('Agility')
print(Agility)
Agility += 2
print(Agility)

character_inventory = BaseInventoryClass()

sword = BaseWeaponClass('Sword')


character_inventory += sword

print(character_inventory)

character = {
    'Concept': str,
    'Race': dict,
    'Hinderances': dict,
    'Traits' : {
        'Attributes': dict,
        'Skills': dict
    },
}
