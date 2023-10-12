import data as Core
import item as Item
import random


def get_augmentation(ch: Core.Character):
    """
        Augmentation Rules

        HEADWARE:
        - Base Unit -> Control Rig
        - Cost essence to install into Control Rig
        - If applicable, can cost capacity to install into Cyberlimb

        EYEWARE:
        - Base Unit -> Cybereyes
        - Cost capacity to install into Cybereyes
        - Installing Cybereyes revokes any vision enhancements granted
            via metatype or other means
        - Can cost essence to install as Retinal Modifications

        EARWARE:
        - Base Unit -> Cyberears
        - Cost capacity to install into Cyberears
        - Can cost essence to install directly to inner ear

        BODYWARE:
        - Base Unit -> None
        - Cost essence to install directly
        - Can cost capacity to install into Cyberlimb

        CYBERLIMBS:
        - Have their own Strength & Agility ratings starting at 3/3
        - The Strength & Agility ratings can only be upgraed by cyberlimb
            enhancements (cyberlimb exclusive modifications) and not by
            other augmentations installed
        - Strength & Agility can only be upgraded up to characters respective
            attribute *limit*
        - Add +1 to Physical Condition Monitor Per Limb
            (Not applicable to hands or feet, or half limbs)
        - Can have cyberweapons installed to them

    """
    ch.Augmentations = {
            'Head': None, 'Eyes': None, 'Ears': None, 
            'Body': None, 'Hand': None, 'Foot': None, 
            'Fingers': None, 'Toes': None, 'Lower Arm': None, 
            'Lower Leg': None, 'Full Arm': None, 'Full Leg': None,
            'Torso': None, 'Skull': None
            }
    return


def get_eyeware(
        ch: Core.Character) -> Core.AugmentationCore | Core.Augmentation:
    eyeware = [i for i in 
                    Core.Augmentation.items + Core.AugmentationCore.items if
                    i.subtype == 'Eyeware']
    pass


def get_remove_racial_bonus(
        ch: Core.character, 
        cyberware: Core.AugmentationCore):
    WE_WILL_KNOW_WHEN_WE_WILL_KNOW = 0
    if (isinstance(ch.Metatype.racial_bonus, list)):
        racial_bonus = ch.Metatype.racial_bonus
        if cyberware.subtype == "Eyes":
            if 'Low Light Level' in racial_bonus:
                racial_bonus.pop(racial_bonus.index('Low Light Level'))
            elif 'Thermographic Visin' in racial_bonus:
                racial_bonus.pop(racial_bonus.index('Low Light Level'))
        if cyberware.subtype == 'Bodyware':
            if 'Dermal Amor' in racial_bonus:
                racial_bonus.pop(racial_bonus.index('Dermal Armor'))
    



def get_cyberlimb(ch: Core.Character, bodypart: None):
    if bodypart is None or bodypart not in ch.Augmentations.keys():
        bodypart = random.choice([
            'Hand', 'Foot', 'Lower Arm', 'Lower Leg', 'Full Arm', 'Full Leg',
            'Skull', 'Torso'])
    cyberlimb = random.choice(
            [i for i in Core.AugmentationCore if 
             i.subtype == 'Cyberlimb' and i.location == bodypart ])
    cyberlimb.Strength = Core.Attribute('Strength', value=3)
    cyberlimb.Agility = Core.Attribute('Agility', value=3)
    increase_attrs_by = random.choice([None, 'A little', 'A lot'])
    if increase_attrs_by is None:
        pass
    else:
        focused_attrs_are = random.choice(['Strength', 'Agility', 'Both'])
        cyberlimb = get_cyberlimb_customisation(
                ch, cyberlimb, increase_attrs_by, focused_attrs_are)    



def get_cyberlimb_customisation(ch: Core.Character,
                                cyberlimb: Core.AugmentationCore,
                                amt: str,
                                focus: str) -> Core.AugmentationCore:
    match increase_attrs_by:
        case 'A little':
            max_stregnth_custom = int(ch.Strength.limit / 2)
            max_agility_custom = int (ch.Agility.limit / 2)
        case 'A lot':
            max_stregnth_custom = ch.Strength.limit - 3
            max_agility_custom = ch.Agility.limit - 3
        case _:
            pass

    match focus:
        case 'Strength':
            max_agility_custom = int( round( max_agility_custom / 4))
        case 'Agility':
            max_stregnth_custom = int( round( max_strength_custom / 4))
        case 'Both' | _:
            pass

    while (cyberlimb.avail <= 12 
           or ch.Nuyen > 0 
           or cyberlimb.Strength.value < ch.Strength.limit
           or cyberlimb.Agility.value < ch.Agility.limit):
        
        pass
    return cyberlimb


def check_augmentation_elligability(ch: Core.Character):
    if ch.MagicResoUser is not None:
        return False
