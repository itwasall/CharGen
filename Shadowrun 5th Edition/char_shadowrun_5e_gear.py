import char_shadowrun_5e_data as Core
import char_shadowrun_5e_item as Item
import random

GEAR_SHOPPING_LIST = []

def get_gear(ch: Core.Character, budget: int) -> Core.Character:
    essentials_out = get_essentials(ch)
    for i in essentials_out:
        GEAR_SHOPPING_LIST.append(i)
    for skill in ch.Skills.keys():
        if skill in ['BLADES', 'CLUBS', 'ESCAPE_ARTIST', 'HEAVY_WEAPONS', 'LONGARMS',
                     'PISTOLS', 'THROWING_WEAPONS', 'PERFORMANCE', 'ARTISAN',
                     'AERONAUTICS_MECHANIC', 'ARMORER', 'AUTOMOTIVE_MECHANIC', 'CHEMISTRY',
                     'COMPUTER', 'DEMOLITIONS', 'FIRST_AID', 'FORGERY', 'HACKING', 'HARDWARE',
                     'INDUSTRIAL_MECHANIC', 'MEDICINE', 'NAUTICAL_MECHANIC', 'SOFTWARE',
                     ]:
            new_item = get_gear_skill_dependant(skill, ch.Skills[skill].rating)
        else:
            new_item = get_gear_skill_dependant(skill, ch.Skills[skill].rating, rating_roll=False)
        if new_item is None:
            continue
        if isinstance(new_item, list):
            for new_item_from_list in new_item:
                GEAR_SHOPPING_LIST.append(new_item_from_list)
        else:
            GEAR_SHOPPING_LIST.append(new_item)
    ch.Gear = GEAR_SHOPPING_LIST
    return ch

######################################################################

def roll_new_item(req: list):
    ammended_requirements  = [i for i in req if avail <= 12]

def get_gear_skill_dependant(skill, rating, rating_roll=True) -> list[Core.Gear]:
    """
        skill: Core.Skill
        rating: Core.Skill.rating
        rating_roll: bool -> If a skill's rating should influence whether or not an
            item is rolled.
            e.g. Someone mildly skilled at pistols might not own one right now, but
                someone mildly skilled at piloting aircraft probably does
    """
    if rating_roll:
        match rating:
            case 1:
                if random.randint(1, 100) >= 83:
                    return None
            case 2:
                if random.randint(1, 100) >= 66:
                    return None
            case 3:
                if random.randint(1, 100) >= 50:
                    return None
            case 4:
                if random.randint(1, 100) >= 25:
                    return None
            case 5:
                if random.randint(1, 100) >= 10:
                    return None
            case _:
                pass
    
    match skill:
        case "Automatics":
            if Core.Firearm in [i.__class__ for i in GEAR_SHOPPING_LIST] and random.randint(1, 100) >= 50:
                return Item.get_weapon(skill, no_mod=True)
            return Item.get_weapon(skill)
        case "Pistols":
            if Core.Firearm in [i.__class__ for i in GEAR_SHOPPING_LIST] and random.randint(1, 100) >= 50:
                return Item.get_weapon(skill, no_mod=True)
            return Item.get_weapon(skill)
        case "Heavy Weapons":
            if Core.Firearm in [i.__class__ for i in GEAR_SHOPPING_LIST] and random.randint(1, 100) >= 50:
                return Item.get_weapon(skill, no_mod=True)
            return Item.get_weapon(skill)
        case "Archery":
            if Core.ProjectileWeapon in [i.__class__ for i in GEAR_SHOPPING_LIST]:
                return
            projectile_weapon = Item.get_weapon(skill)
            try:
                projectile_ammo = random.choice([i for i in Core.ProjectileWeapon.items if 
                                                 i.subtype == "Ammo" and projectile_weapon.name in i.requires])
            except IndexError:
                return projectile_weapon
            return [projectile_weapon, projectile_ammo]
        case "Blades":
            if Core.MeleeWeapon in [i.__class__ for i in GEAR_SHOPPING_LIST] and random.randint(1, 100) >= 50:
                return
            return Item.get_weapon(skill)
        case "Clubs":
            if Core.MeleeWeapon in [i.__class__ for i in GEAR_SHOPPING_LIST] and random.randint(1, 100) >= 50:
                return
            return Item.get_weapon(skill)
        case "Throwing Weapons":
            return Item.get_weapon(skill)
        case "Pilot Ground Craft" | "Pilot Aircraft" | "Pilot Watercraft" | "Pilot Walker":
            return Item.get_vehicle(skill)
        case "Hardware" | "Software" | "Locksmith":
            items = []
            for idx in range(rating):
                if idx is False:
                    items.append(Item.get_item(None, skill))
                elif random.randint(1,10) >= 5:
                    items.append(Item.get_item(None, skill))
                else:
                    continue
            return items 
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
