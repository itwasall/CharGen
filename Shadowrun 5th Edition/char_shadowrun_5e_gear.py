import char_shadowrun_5e_data as Core
import char_shadowrun_5e_item as Item
import random

GEAR_SHOPPING_LIST = []

def get_gear(ch: Core.Character, budget: int) -> Core.Character:
    essentials_out = get_essentials(ch)
    for i in essentials_out:
        GEAR_SHOPPING_LIST.append(i)
    armor_roll = random.randint(1, 100)
    if armor_roll >= 10:
        if armor_roll % 2 == 0:
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
    ch.Gear = GEAR_SHOPPING_LIST
    return ch

######################################################################

def roll_new_item(req: list):
    ammended_requirements  = [i for i in req if avail <= 12]

def get_gear_skill_dependant(ch, skill, rating, rating_roll=True) -> list[Core.Gear]:
    """
        skill: Core.Skill
        rating: Core.Skill.rating
        rating_roll: bool -> If a skill's rating should influence whether or not an
            item is rolled.
            e.g. Someone mildly skilled at pistols might not own one right now, but
                someone mildly skilled at piloting aircraft probably does
    """
    # If flag argument is set, then the higher the rating the more likely it is an
    #   item is rolled.
    #   Rating 1: 16%, Rating 2: 33%, Rating 3: 50%
    #   Rating 4: 75%, Rating 5: 85%, Rating 6: 90% 
    #   Rating 7: 95%, Rating 8: 98% - Not sure how these is legal though
    rating_roll_ratio = {1: 83, 2: 66, 3: 50, 4: 25, 5: 15, 6: 10, 7: 5, 8: 2}
    if rating_roll:
        if random.randint(1, 100) >= rating_roll_ratio[rating]:
            return None

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
