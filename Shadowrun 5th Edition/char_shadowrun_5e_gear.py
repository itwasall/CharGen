import char_shadowrun_5e_data as Core
import char_shadowrun_5e_item as Item
import random


def get_gear(ch: Core.Character, budget: int) -> Core.Character:
    gear_shopping_list = []
    essentials_out = get_essentials(ch)
    gear_shopping_list.append(essentials_out)
    for skill in ch.Skills.keys():
        new_item = get_gear_skill_dependant(skill)
        if new_item is None:
            continue
        gear_shopping_list.append(new_item)
    ch.Gear = gear_shopping_list
    return ch

######################################################################

def get_gear_skill_dependant(skill) -> list[Core.Gear]:
    match skill:
        case "Automatics":
            return random.choice([p for p in Core.Firearm.items if
                                  p.subtype in ['Assault Rifle',
                                                'Machine Pistol',
                                                'Submachine Gun']])
        case "Pistols":
            return random.choice([p for p in Core.Firearm.items if 
                                  p.subtype in ['Light Pistol', 
                                                'Heavy Pistol',
                                                'Machine Pistol',
                                                'Hold-Out', 'Taser']])
        case _:
            return





def get_essentials(ch: Core.Character) -> list[Core.Gear]:
    gear_essentials = []
    if Core.SINNER_NATIONAL.name in ch.Qualities or Core.SINNER_CRIMINAL.name in ch.Qualities:
        Core.REAL_SIN.rating = 1
        gear_essentials.append(Core.REAL_SIN)
    elif Core.SINNER_CORPORATE_LIMITED.name in ch.Qualities:
        Core.REAL_SIN.rating = 2
        gear_essentials.append(Core.REAL_SIN)
    elif Core.SINNER_CORPORATE.name in ch.Qualities:
        Core.REAL_SIN.rating = 3
        gear_essentials.append(Core.REAL_SIN)
    else:
        gear_essentials.append(Item.get_item(Core.FAKE_SIN))
    return gear_essentials
        
################################################################################

def get_lifestyle(ch: Core.Character) -> None:
    if ch.PrimaryLifestyle is None:
        ch.PrimaryLifestyle = random.choice(Core.LIFESTYLES)
    elif isinstance(ch.PrimaryLifestyle, Core.Lifestyle):
        lifestyles = [
                i for i in Core.Lifestyle.items if i.cost < 
                ch.PrimaryLifestyle.cost ]
        ch.PrimaryLifestyle = random.choice(lifestyles)
