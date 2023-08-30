import random
import char_shadowrun_5e_data as Core

def attrAsDict(_class):
    return {i: _class.__getattribute__(i) for i in dir(_class) if not i.startswith("__") and i != 'items'}

def get_rating(item: Core.Gear):
    if "rating" not in attrAsDict(item).keys():
        return 1
    if isinstance(item.rating, int):
        return item.rating
    elif isinstance(item.rating, str):
        return 0
    elif isinstance(item.rating, list):
        return random.choice(range(item.rating[0], item.rating[2]))
    else:
        raise ValueError(f'{item.name} has bad rating data')

def get_item_cost(item: Core.Gear, arg=-1):
    if not hasattr(item, "cost"):
        raise AttributeError("Item has not 'cost' attribute")

    if isinstance(item.cost, int):
        return item.cost
    elif isinstance(item.cost, list):
        if arg != -1:
            return list_handler(item.cost, item, arg)
        return list_handler(item.cost, item)


def list_handler(l: list, item, arg=-1):
    if item.name in [
            'Gas Vent System',
            'Chemical Protection',
            'Fire Resistance',
            'Insulation',
            'Nonconductivity',
            'Thermal Damping'
        ]:
        return 0
    r1 = 1
        
    if l[0] == "Rating":
        if not hasattr(item, "rating"):
            raise AttributeError(f"{item.name} has no 'rating' attribute despite mention in {l}")
        if arg != -1 and arg <= item.rating[2] and arg >= item.rating[0]:
            r1 = arg
        elif arg != -1:
            raise ValueError(f"{arg} is outside the range of {item.rating[0]} - {item.rating[2]}")
        else:
            r1 = get_rating(item)

    elif l[0] == "Capacity":
        if not hasattr(item, "capacity"):
            raise AttributeError(f"Item has no 'capacity' attribute despite mention in {l}")
        if arg != -1 and arg < item.capacity[2] and arg > item.capacity[0]:
            r1 = arg
        elif arg != -1:
            raise ValueError(f"{arg} is outside the capacity of {item.capacity[0]} - {item.capacity[2]}")
        else:
            r1 = random.choice(range(item.capacity[0], item.capacity[2]))

    elif l[0] == "WeaponCost":
        if not hasattr(item, "requires"):
            raise AttributeError(f"{item.name} has a dependant cost variable but nothing to depend on!")
        if arg != -1 and isinstance(arg, Core.Firearm):
            r1 = get_item_cost(arg)
        else:
            raise ValueError("WeaponCost fuckery")

    elif l[0] == "ArmorRating":
        if not hasattr(item, "requires"):
            raise AttributeError(f"{item.name} has a dependant cost variable but nothing to depend on!")
        if arg != -1 and isinstance(arg, Core.Armor):
            r1 = arg.armor_rating
        else:
            raise ValueError("ArmorRating fuckery")


    elif l[0] == "Category":
        cond_list = [i for i in Core.Gear.items if hasattr(i, "category") and i.category == l[1]]
        if arg != -1 and arg in cond_list:
            return arg
        else:
            return random.choice(cond_list)

    elif l[0] == "Subtype":
        cond_list = [i for i in Core.Gear.items if hasattr(i, "subtype") and i.subtype == l[1]]
        if arg != -1 and arg in cond_list:
            return arg
        else:
            return random.choice(cond_list)
        
        
    else:
        print("TODO")
        print(f"    {l[0]} logic for {item}")

    match l[1]:
        case "+":
            if isinstance(r1, int) and isinstance(l[2], int):
                return r1 + l[2]
        case "*":
            if isinstance(r1, int) and isinstance(l[2], int):
                return r1 * l[2]
"""
    match l[0]:
        case "Rating":
            if not hasattr(item, "rating"):
                raise AttributeError(f"Item has no 'rating' attribute despite mention in {l}")
            if arg != -1 and arg < item.rating[2] and arg > item.rating[0]:
                l[0] = arg
            else:
                l[0] = get_rating(item)
        case "Quantity":
        case _:
            print(f"TODO LIST HANDLER FOR {l[0]} in {l} for {item.name}")
"""

def get_mod(item: Core.Gear, m=None):
    if isinstance(item, Core.Firearm):
        if hasattr(item, "mods"):
            if m is not None:
                weapon_mod = m
            else:
                weapon_mod = random.choice([i for i in Core.FirearmAccessory.items if hasattr(i, "requires") and i.requires[1] == "Firearm"])
            item.mods = weapon_mod
            if isinstance(weapon_mod.cost, list):
                item.cost = get_item_cost(item) + get_item_cost(weapon_mod, item)
            else:
                item.cost = item.cost + weapon_mod.cost
            item.name = f"{item.name} /w {weapon_mod.name}"
    if isinstance(item, Core.Armor):
        if hasattr(item, "mods"):
            if m is not None:
                armor_mod = m
            else:
                armor_mod = random-choice([i for i in Core.ArmorModification.items if hasattr(i, "requires") and i.requires[1] == "Armor"])
            item.mods = armor_mod
            if isinstance(armor_mod.cost, list):
                item.cost = get_item_cost(item) + get_item_cost(armor_mod, item)
            else:
                item.cost = item.cost + armor_mod.cost
            item.name = f"{item.name} /w {armor_mod.name}"

