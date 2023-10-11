import data as Core
import item as Item
import random

"""
    THE PLAN

    FOR -WARE:
        Spawn AugmentationCore.items item
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


def get_augmentation(ch: Core.Character, aug_type=None, aug_bodyloc=None):
    essence_budget = get_essence_budget(ch)
    print(f'Character Essence attribute is {ch.Essence.value}\nEssence budget is {essence_budget}')
    augmentation_routine =['Cyberware', 'Bioware', 'Cyberlimb']
    if aug_type is None:
        aug_type = random.choice(augmentation_routine)
    if essence_budget <= 0:
        print(f"essence budget 0 or negative: {essence_budget}")
        return
    match aug_type:
        case 'Cyberware':
            if aug_bodyloc is None:
                aug_bodyloc = random.choice('Earware', 'Eyeware', 'Headware', 'Bodyware')
                ch = get_augmentation_regular(ch, essence_budget, aug_bodyloc)
            elif aug_bodyloc in ['Earware', 'Eyeware', 'Headware']:
                ch = get_augmentation_regular(ch, essence_budget, aug_bodyloc)
        case 'Cyberlimbs':
            if aug_bodyloc is None:
                aug_bodyloc = random.choice(['Hand', 'Foot', 'Lower Arm', 'Lower Leg', 'Full Arm', 'Full Leg'])
                ch = get_augmentation_cyberlimb(ch, essence_budget, aug_bodyloc)
            else:
                ch = get_augmentation_cyberlimb(ch, aug_bodyloc)
        case 'Bioware':
            print("TODO")
            aug=None
        case _:
            raise ValueError(f"Incorrect aug_type! ({aug_type})")
    return


def get_augmentation_regular(ch: Core.Character, ess: int, aug_bodyloc) -> Core.Character:
    if aug_bodyloc == 'Eyeware' and random.randint(1,2) == 1:
        RETINAL_ENHANCEMENT = True
    elif aug_bodyloc == 'Earware' and random.randint(1, 2) == 1:
        INNER_EAR_ENHANCEMENT = True
    else:
        RETINAL_ENHANCEMENT = False
        INNER_EAR_ENHANCEMENT = False

    aug_options = [i for i in Core.Augmentation.items if i.subtype == aug_bodyloc]
    if RETINAL_ENHANCEMENT:
        ch.Augmentations['Eyes'] = random.choice(aug_options)
        ch.Augmentations['Eyes'].name += " (Retinal Enhancement)"
        ch.Essence.value -= ch.Augmentations['Eyes'].essence
        return ch
    elif INNER_EAR_ENHANCEMENT:
        ch.Augmentations['Ears'] = random.choice(aug_options)
        ch.Augmentations['Ears'].name += " (Inner Ear Enhancement)"
        ch.Essence.value -= ch.Augmentations['Ears'].essence
        return ch
    aug_base = Item.get_item(random.choice([i for i in Core.AugmentationCore.items if hasattr(i, "rating") and i.subtype == aug_bodyloc]))
    aug_options = [i for i in Core.Augmentation.items if i.subtype == aug_bodyloc]
    catchall = 0
    while aug_base.capacity > 0 or catchall < 10:
        new_aug = Item.get_item(random.choice(aug_options))
        if hasattr(new_aug, "capacity"):
            if aug_base.capacity < new_aug.capacity:
                catchall += 1
                continue
            if new_aug in aug_base.mods:
                catchall += 1
                continue
            aug_base.mods.append(new_aug)
            aug_base.capacity -= new_aug.capacity
        else:
            catchall += 1
            continue
    
    aug_bodyloc_dict = {'Earware': 'Ears', 'Eyeware': 'Eyes', 'Bodyware': 'Body', 'Headware': 'Head'}
    bodyl = aug_bodyloc_dict[aug_bodyloc]
    ch.Augmentations[bodyl] = aug_base
    ch.Essence.value -= ch.Augmentations[bodyl].essence
    return ch


def get_augmentation_cyberlimb(ch: Core.Character, ess:int, aug_bodyloc) -> Core.AugmentationCore:
    cyberlimb_base = random.choice([i for i in Core.AugmentationCore.items if i.subtype == 'Cyberlimbs' and i.location == aug_bodyloc])
    return cyberlimb_base


def get_essence_budget(ch: Core.Character):
    if ch.Magic is not None or ch.Resonance is not None:
        quarter_essence = ch.Essence.value / 4
        if quarter_essence > 1:
            return quarter_essence
        else:
            return 0
    else:
        aug_counts = {}
        for d in ch.Augmentations.values():
            if type(d) in aug_counts:
                aug_counts[type(d)] += 1
            else:
                aug_counts[type(d)] = 1
        return ch.Essence.value


def format_augmentations(ch: Core.Character, compact=False):
    if compact:
        return str(f"Augmentations: {x.Augmentations}")

    print("===\nAUGMENTATIONS")
    
    no_augs = []
    for key, value in x.Augmentations.items():
        if x.Augmentations[key] is None:
            no_augs.append(key)
        else:
            print(f"{key} - {value}")

    if len(no_augs) > 0:
        print(f"No augs in {', '.join(no_augs)}")
if __name__ == "__main__":
    import char_shadowrun_5e as Run
    x, _, _ = Run.generate_character()
    eyeware_example = get_augmentation(x, aug_type='Cyberware', aug_bodyloc='Eyeware')
    format_augmentations(x)

    cyberlimb_example = get_augmentation(x, aug_type='Cyberlimbs')

    format_augmentations(x)
