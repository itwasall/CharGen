import char_shadowrun_5e_data as Core
import char_shadowrun_5e_item as Item
import char_shadowrun_5e_gear as Gear
import random

"""
    THE PLAN

    FOR -WARE:
        Spawn AugmentationCore item
        Roll Augmentation items with matching subtype until limit is met.
        Limits include:
            - Hitting Essence Value (e.g. 1, 2, 6)
            - Hitting Capacity Value

        FOR HEADWARE: 
            ANY augs must be installed to either cyberlimbs (if applicable) or a control rig
                Installing headware to cyberlimbs costs capacity
                Installing headware to control rig costs essence
        FOR EYEWARE:
            ALL augs must be installed as retinal enchancements to the natural eye or to cybereyes 
                Installing eyeware as retinal enhancements costs Essence
                Installing eyeware to cybereyes costs Capacity
                All augs are installed for both eyes.
        FOR EARWARE:
            ALL augs must be installed as enhancements to the natrual inner ear or to cyberears
                Installing earware as inner ear enhancements costs Essence
                Installing earware to cyberears costs Capacity
                All augs are installed for both ears.
        FOR BODYWARE: 
            NO central core unit to install mods into. If applicable, some bodyware can be installed into cyberlimbs
                Installing bodyware to cyberlimbs costs Capacity
                Installing bodyware costs Essence
"""

def get_augmentation(aug_type=None):
    if aug_type=='Eyeware' or aug_type == 'Earware' or aug_type == 'Headware':
        aug_base = random.choice([i for i in Core.AugmentationCore.items if i.subtype == aug_type])

