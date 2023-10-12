import data as Core
import item as Item
import random

GEAR_SHOPPING_LIST = []
SINNER_QUALITIES = [Core.SINNER_NATIONAL, Core.SINNER_CRIMINAL, Core.SINNER_CORPORATE, Core.SINNER_CORPORATE_LIMITED]

"""
Get's gear

TODO:
- Chars with one of the SINner qualities will not be given a fake SIN
- Chars with piloting skills should have an appropriate vehicle, 
    maybe one or more depending on which skills are more prominant, and at
    what ratings
- Chars with skills relating to hacking should have a cyberdeck. This will
    almost certainly require it's own separate generate function
- Chars with skills relating to firearms should have more weapons, with a 
    slight/heavy lean towards weaponary they are skilled in. Slight lean for
    stuff like heavy weapons (e.g. they probably wont be without a pistol).
    Heavy lean for stuff like melee weapons (You studied the blade, not the 
    gun afterall)
- Chars with more nuyen are more likely to have bio augs if they are going to
    have augmentations at all. Poorer characters likely to have cyberwear
- Chars of magic tendancies must have some magic items
- Chars most likely will have a commlink. Skills + nuyen to influence what kind
    (e.g. techy/rich folk likely to have a better commlink)
- Chars without arcana skill won't get magic formulae, chars with arcana will
    be likely to possess it
"""

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
    rating_roll_ratio = {-1: 101, 0: 101, 1: 83, 2: 66, 3: 50, 4: 25, 5: 15, 6: 10, 7: 5, 8: 2}
    if random.randint(1, 100) >= rating_roll_ratio[rating]: 
        return False
    return True


def get_gear(ch: Core.Character, budget: int) -> Core.Character:
    essentials_out = get_essentials(ch)
    for i in essentials_out:
        GEAR_SHOPPING_LIST.append(i)
    armor_roll = random.randint(1, 100)
    if armor_roll <= 10:
        new_armor = Item.get_armor(clothing=True)
    else:
        new_armor = Item.get_armor()
    if isinstance(new_armor, list):
        for new_armor_item_from_list in new_armor:
            GEAR_SHOPPING_LIST.append(new_armor_item_from_list)
    else:
        GEAR_SHOPPING_LIST.append(new_armor)
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

    ch.Gear = evaluate_gear_list(GEAR_SHOPPING_LIST)
    cost = sum([i.cost for i in GEAR_SHOPPING_LIST])
    ch.Nuyen = cost

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

    commlink_skills = ['Aeronautics Mechanic', 'Automotive Mechanic', 
                       'Biotechnology', 'Computer', 'Cybercombat', 
                       'Cybertechnology', 'Electronic Warfare', 'Hacking', 
                       'Hardware', 'Industrial Mechanic', 'Nautical  Mechanic', 
                       'Software']
    has_commlink = False
    for skill in commlink_skills:
        if has_commlink:
            continue
        elif skill in ch.Skills.keys():
            has_commlink = True
    if not has_commlink and random.randint(1, 100) >= 30:
            has_commlink = True
    if has_commlink:
        new_item = random.choice(
                [i for i in Core.Electronics.items if not hasattr(
                    i, "requires") 
                 and hasattr(i, "subtype") and 
                 i.subtype == "Commlink"])
        gear_essentials.append(Item.get_item(new_item))

    for gear in gear_essentials:
        if hasattr(gear, "subtype") and gear.subtype == "Commlink":
            if random.randint(1, 100) >= 50:
                gear_essentials.append(Item.get_item(Core.SIM_MODULE_HOT_SIM))
            else:
                gear_essentials.append(Item.get_item(Core.SIM_MODULE))
        else:
            continue
        

    return gear_essentials

        

def get_gear_skill_dependant(ch, skill, rating,
                             rating_roll=True) -> list[Core.Gear]:
    """
        skill: Core.Skill
        rating: Core.Skill.rating
        rating_roll: bool -> If a skill's rating should influence whether or 
            not an item is rolled.
            e.g. Someone mildly skilled at pistols might not own one right 
            now, but someone mildly skilled at piloting aircraft probably does
    """
    if rating_roll:
        if not check_rating(rating):
            return

    # Makes it more likely to have more than one weapon with a modification
    #   if skills are of higher rating
    sec_wpn_mod_chance = 40
    sec_wpn_mod_chance += sum(
            [ch.Skills[skill].rating for skill in ch.Skills if skill in [
                "Automatics", "Pistols", "Heavy Weapons"]]) * 5
    
    match skill:
        case "Automatics":
            # Roll second weapon without mods if a Firearm has already been 
            #   rolled with one
            if (Core.Firearm in [i.__class__ for i in GEAR_SHOPPING_LIST if 
                hasattr(i, "mods") and i.mods is not None]) and random.randint(
                        1, 100) <= sec_wpn_mod_chance:
                return Item.get_weapon(skill, no_mod=True)
            return Item.get_weapon(skill)
        case "Pistols":
            if (Core.Firearm in [i.__class__ for i in GEAR_SHOPPING_LIST if 
                hasattr(i, "mods") and i.mods is not None]) and random.randint(
                        1, 100) <= sec_wpn_mod_chance:
                return Item.get_weapon(skill, no_mod=True)
            return Item.get_weapon(skill)
        case "Heavy Weapons":
            if (Core.Firearm in [i.__class__ for i in GEAR_SHOPPING_LIST if 
                hasattr(i, "mods") and i.mods is not None]) and random.randint(
                        1, 100) <= sec_wpn_mod_chance:
                return Item.get_weapon(skill, no_mod=True)
            return Item.get_weapon(skill)
        case "Archery":
            if Core.ProjectileWeapon in [i.__class__ for i in GEAR_SHOPPING_LIST]:
                return
            projectile_weapon = Item.get_weapon(skill)
            try:
                projectile_ammo = Item.get_item(random.choice(
                        [i for i in Core.ProjectileWeapon.items if 
                         i.subtype == "Ammo" and projectile_weapon.name
                         in i.requires]))
            except IndexError:
                return projectile_weapon
            return [projectile_weapon, projectile_ammo]
        case "Blades":
            if Core.MeleeWeapon in [
                    i.__class__ for i in GEAR_SHOPPING_LIST
                    ] and random.randint(1, 100) >= 50:
                return
            return Item.get_weapon(skill)
        case "Clubs":
            if Core.MeleeWeapon in [
                    i.__class__ for i in GEAR_SHOPPING_LIST
                    ] and random.randint(1, 100) >= 50:
                return
            return Item.get_weapon(skill)
        case "Throwing Weapons":
            return Item.get_weapon(skill)
        case "Pilot Ground Craft" | "Pilot Aircraft":
            return Item.get_vehicle(skill)
        case "Pilot Watercraft" | "Pilot Walker":
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

    # If a character doesn't have a legal SIN, give them a fake license 
    #   to practise magic
    if len([q for q in ch.Qualities.keys() if q in [
        i.name for i in SINNER_QUALITIES]]) == 0:
        magic_items.append(Item.get_fake_license(
            license_type="to Practise Magic"))

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
            if new_license is None or new_license.name in [l.name for l in added_licenses]:
                continue
    # If item is a magic item and character alreaady has a fake license for 
    #   magic, continue
            elif isinstance(
                    gear, Core.MagicItem) and "Fake License ( \
            to Practise Magic)" in [
                    l.name for l in added_licenses] + [
                            g.name for g in gear_list]:
                continue

            else:
                added_licenses.append(new_license)
    return added_licenses
            

def evaluate_gear_list(gear_list) -> list[Core.Gear]:
    # exceptions = False
    evaluated_gear_list = []
    for gear in gear_list:
        if gear.name in [i.name for i in evaluated_gear_list]:
            continue
        # if hasattr(gear, "subtype") and gear.subtype == "Commlink_":
        evaluated_gear_list.append(gear)
    return evaluated_gear_list


    
