import char_shadowrun_5e_data as Core
import char_shadowrun_5e_item as Item
import random

GEAR_SHOPPING_LIST = []
SINNER_QUALITIES = [Core.SINNER_NATIONAL, Core.SINNER_CRIMINAL, Core.SINNER_CORPORATE, Core.SINNER_CORPORATE_LIMITED]


def check_rating(rating) -> bool:
    """
        Simple boolean check against a rating, designed for skill ratings.
            Rating 1: 16% 
            Rating 2: 33% 
            Rating 3: 50%
            Rating 4: 75% 
            Rating 5: 85% 
            Rating 6: 90% 
            Rating 7: 95%
            Rating 8: 98%
    """
    rating_roll_ratio = {1: 83, 2: 66, 3: 50, 4: 25, 5: 15, 6: 10, 7: 5, 8: 2}
    if random.randint(1, 100) >= rating_roll_ratio[rating]: 
        return False
    return True


def get_gear(ch: Core.Character, budget: int) -> Core.Character:
    essentials_out = get_essentials(ch)
    for i in essentials_out:
        GEAR_SHOPPING_LIST.append(i)
    for skill in ch.Skills.keys():
        if skill in ['BLADES', 'CLUBS', 'HEAVY_WEAPONS', 'LONGARMS',
                     'PISTOLS', 'THROWING_WEAPONS', 'ARTISAN',
                     'AERONAUTICS_MECHANIC', 'ARMORER', 'AUTOMOTIVE_MECHANIC', 'CHEMISTRY',
                     'COMPUTER', 'DEMOLITIONS', 'FIRST_AID', 'FORGERY', 'HACKING', 'HARDWARE',
                     'INDUSTRIAL_MECHANIC', 'MEDICINE', 'NAUTICAL_MECHANIC',
                     ]:
            new_item = get_gear_skill_dependant(ch, skill, ch.Skills[skill].rating)
        else:
            new_item = get_gear_skill_dependant(ch, skill, ch.Skills[skill].rating, rating_roll=False)
        if new_item is None:
            continue
        if isinstance(new_item, list):
            for new_item_from_list in new_item:
                GEAR_SHOPPING_LIST.append(new_item_from_list)
        else:
            GEAR_SHOPPING_LIST.append(new_item)
    if ch.MagicResoUser in ["Magician", "Adept", "Mystic Adept", "Aspected Magician"]:
        new_items = get_gear_magic_dependant(ch)
        for new_item in new_items:
            GEAR_SHOPPING_LIST.append(new_item)

    ch.Gear = GEAR_SHOPPING_LIST
    return ch


def get_essentials(ch: Core.Character) -> list[Core.Gear]:
    gear_essentials = []
    if Core.SINNER_NATIONAL.name in ch.Qualities or Core.SINNER_CRIMINAL.name in ch.Qualities:
        Core.REAL_SIN.rating = 1
        gear_essentials.append(Item.get_item(Core.REAL_SIN))
    elif Core.SINNER_CORPORATE_LIMITED.name in ch.Qualities:
        Core.REAL_SIN.rating = 2
        gear_essentials.append(Item.get_item(Core.REAL_SIN))
    elif Core.SINNER_CORPORATE.name in ch.Qualities:
        Core.REAL_SIN.rating = 3
        gear_essentials.append(Item.get_item(Core.REAL_SIN))
    else:
        gear_essentials.append(Item.get_item(Core.FAKE_SIN))
    return gear_essentials
        

def get_gear_skill_dependant(ch, skill, rating, rating_roll=True) -> list[Core.Gear]:
    """
        skill: Core.Skill
        rating: Core.Skill.rating
        rating_roll: bool -> If a skill's rating should influence whether or not an
            item is rolled.
            e.g. Someone mildly skilled at pistols might not own one right now, but
                someone mildly skilled at piloting aircraft probably does
    """
    if rating_roll:
        if not check_rating(rating):
            return

    # Makes it more likely to have more than one weapon with a modification if skills are
    #   of higher rating
    sec_wpn_mod_chance = 40
    sec_wpn_mod_chance += sum([ch.Skills[skill].rating for skill in ch.Skills if skill in ["Automatics", "Pistols", "Heavy Weapons"]]) * 5

    
    match skill:
        case "Automatics":
            # Roll second weapon without mods if a Firearm has already been rolled with one
            if (Core.Firearm in [i.__class__ for i in GEAR_SHOPPING_LIST if 
                hasattr(i, "mods") and i.mods is not None]) and random.randint(1, 100) <= sec_wpn_mod_chance:
                return Item.get_weapon(skill, no_mod=True)
            return Item.get_weapon(skill)
        case "Pistols":
            if (Core.Firearm in [i.__class__ for i in GEAR_SHOPPING_LIST if 
                hasattr(i, "mods") and i.mods is not None]) and random.randint(1, 100) <= sec_wpn_mod_chance:
                return Item.get_weapon(skill, no_mod=True)
            return Item.get_weapon(skill)
        case "Heavy Weapons":
            if (Core.Firearm in [i.__class__ for i in GEAR_SHOPPING_LIST if 
                hasattr(i, "mods") and i.mods is not None]) and random.randint(1, 100) <= sec_wpn_mod_chance:
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
        case "Hardware" | "Locksmith":
            items = []
            for idx in range(rating):
                if idx is False:
                    new_item = Item.get_item(None, skill)
                    items.append(Item.get_item(None, skill))
                elif random.randint(1,10) >= 5:
                    items.append(Item.get_item(None, skill))
                else:
                    continue
            return items 
        case _:
            return


def get_gear_magic_dependant(ch: Core.Character) -> list[Core.Gear]:
    magic_items = []

    # If a character doesn't have a legal SIN, give them a fake license to practise magic
    if len([q for q in ch.Qualities.keys() if q in [i.name for i in SINNER_QUALITIES]]) == 0:
        magic_items.append(Item.get_fake_license(license_type="to Practise Magic"))

    if ch.MagicResoUser == 'Adept':
        if random.randint(1, 100) > 50:
            magic_items.append(Item.get_magic_item('Qi', ch))

    if 'Alchemy' in ch.Skills.keys():
        if check_rating(ch.Skills['Alchemy'].rating):
            magic_items.append(Item.get_magic_item('Alchemy', ch))
    if 'Disenchanting' in ch.Skills.keys():
        if check_rating(ch.Skills['Disenchanting'].rating):
            magic_items.append(Item.get_magic_item('Disenchanting', ch))

    return magic_items

def roll_new_item(req: list):
    ammended_requirements  = [i for i in req if avail <= 12]


def get_lifestyle(ch: Core.Character) -> None:
    if ch.PrimaryLifestyle is None:
        ch.PrimaryLifestyle = random.choice(Core.LIFESTYLES)
    elif isinstance(ch.PrimaryLifestyle, Core.Lifestyle):
        lifestyles = [
                i for i in Core.Lifestyle.items if i.cost < 
                ch.PrimaryLifestyle.cost ]
        ch.PrimaryLifestyle = random.choice(lifestyles)


def check_legality(ch: Core.Character, gear_list = GEAR_SHOPPING_LIST) -> None:
    added_licenses = []
    for gear in gear_list:
        if hasattr(gear, "legality") and gear.legality == Core.RESTRICTED:
            new_license = Item.get_fake_license(item=gear)
            if new_license.name in [l.name for l in added_licenses]:
                continue
    # If item is a magic item and character alreaady has a fake license for magic, continue
            elif isinstance(gear, Core.MagicItem) and "Fake License (to Practise Magic)" in [l.name for l in added_licenses] + [g.name for g in gear_list]:
                continue

            else:
                added_licenses.append(new_license)
    return added_licenses
            

    
