import random
import char_shadowrun_5e_data as Core
from decimal import getcontext, Decimal

getcontext().prec = 2

DEFAULT_MAX_AVAILABILITY = 12
DEFAULT_MAX_RATING = 6
DEFAULT_AUG_GRADES = ["standard", "alphaware"]

RATING_ALREADY_ROLLED = False
AVAIL_ALREADY_ROLLED = False
COST_ALREADY_ROLLED = False


def attrAsDict(_class):
    return {i: _class.__getattribute__(i) for i in dir(_class) if not i.startswith("__") and i != 'items'}


def get_item_rating(item: Core.Gear, max_rating=DEFAULT_MAX_RATING, **kwargs):
    if "rating" in kwargs:
        return kwargs['rating']
    elif "rating" not in attrAsDict(item).keys():
        return 1
    elif isinstance(item.rating, int) or isinstance(item.rating, str):
        return item.rating
    elif isinstance(item.rating, list):
        if item.rating[2] > max_rating:
            item.rating[2] == max_rating
        return list_handler(item.rating, item, max_rating)
    else:
        raise ValueError(f'{item.name} has bad rating data\n{item.rating}\n{type(item.rating)}')


def get_item_avail(item: Core.Gear, max_avail=DEFAULT_MAX_AVAILABILITY, **kwargs):
    if not hasattr(item, "avail"):
        return 0
    if isinstance(item.avail, int):
        return item.avail
    elif isinstance(item.avail, str):
        return 0
    elif isinstance(item.avail, list):
        return list_handler(item.avail, item, max_avail, **kwargs)
    else:
        raise ValueError(f'{item.name} has bad avail data\n{item.avail}\n{type(item.avail)}')


def get_item_force(item: Core.Gear, ch: Core.Character) -> Core.Gear:
    if not hasattr(item, "force"):
        return

    # An items "Force" value can be within a range of values relative to the characters
    #   'Magic' attribute value. However some values (typically that equal to the magic
    #   attribute value) are more common than others so the horrible bit of math here
    #   is just that.
    ranges = [i for i in range(1, ch.Magic.value * 2 + 1)]
    range_probs = [abs(i-len(ranges)+1) if abs(i) > (len(ranges)/2)-1 else 0 for i in ranges]

    return random.choices(ranges, range_probs)[0]


def get_item_cost(item: Core.Gear, arg=-1, **kwargs):
    if not hasattr(item, "cost"):
        return 0
    if isinstance(item.cost, int):
        return item.cost
    elif isinstance(item.cost, list):
        if arg != -1:
            return list_handler(item.cost, item, arg, **kwargs)
        return list_handler(item.cost, item, **kwargs)
    else:
        raise ValueError(f'{item.name} has bad cost data\n{item.cost}\n{type(item.cost)}')


def get_item_essence(item: Core.Gear, arg=-1, **kwargs):
    if not hasattr(item, "essence"):
        return 0
    if isinstance(item.essence, int): 
        return item.essence
    elif isinstance(item.essence, float):
        getcontext().prec = 2
        return Decimal(item.essence) * Decimal(1)
    if isinstance(item.essence, str):
        return 0
    elif isinstance(item.essence, list):
        if arg != -1:
            x = list_handler(item.essence, item, arg, **kwargs)
        else:
            x = list_handler(item.essence, item, **kwargs)
        return Decimal(x) * Decimal(1)

    else:
        raise ValueError(f'{item.name} has bad essence data\n{item.essence}\n{type(item.essence)}')


def get_item_capacity(item: Core.Gear, arg=-1, **kwargs):
    """
        If item has capacity (e.g. Cybereyes), then calculate it here if it's a variance
    """
    if not hasattr(item, "capacity"):
        return 1
    if isinstance(item.capacity, int) or isinstance(item.capacity, str):
        if item.capacity == "-":
            return 1
        return int(item.capacity)
    elif isinstance(item.capacity, list):
        if arg != -1:
            return list_handler(item.capacity, item, arg, **kwargs)
        return list_handler(item.capacity, item, **kwargs)
    else:
        raise ValueError(f'{item.name} has bad capacity data\n{item.capacity}\n{type(item.capacity)}')


def list_handler(l: list, item, arg=-1, **kwargs):
    """
        list_handler

        Handles parameters for which isinstance(param, list) is True

        ["Rating", "*", 2] -> Roll for rating, multiply by 2, return


    """
    r1 = 1

    if isinstance(l[0], int) and l[1] == "to":
        if arg != -1 and isinstance(arg, int) and arg < l[2]:
            l[2] == arg
        else:
            return random.choice(range(l[0], l[2]))

    if l[0] == "Rating":
        # Catches if item doesn't have rating attribute
        if not hasattr(item, "rating"):
            if hasattr(item, "requires") and item.requires[0] == 'Category':
                rand_req = random.choice([i for i in Core.Gear.items if i.category == item.requires[1]])
                r1 = get_item_rating(rand_req, **kwargs)
            elif hasattr(item, "requires") and item.requires[0] == 'Subtype':
                random_req = random.choice([i for i in Core.Gear.items if i.subtype == item.requires[1]])
                r1 = get_item_rating(random_req, **kwargs)
            else:
                raise AttributeError(f"{item.name} has no 'rating' attribute despite mention in {l}")
        # If item.rating is an integar, pass that on
        elif isinstance(item.rating, int):
            r1 = item.rating
        elif arg != -1:
            if arg in [DEFAULT_MAX_AVAILABILITY, DEFAULT_MAX_RATING]:
                item.rating = get_item_rating(item, **kwargs)
                r1 = item.rating
            else:
                pass
        else:
            item.rating = get_item_rating(item, **kwargs)
            r1 = item.rating
        if len(l) == 1:
            return r1


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
        elif "random" in kwargs:
            if hasattr(item, "requires") and item.requires[0] == 'Category':
                r1 = get_item_cost([i for i in Core.Gear.items if i.category == item.requires[1]])
            elif hasattr(item, "requires") and item.requires[0] == 'Subtype':
                r1 = get_item_cost([i for i in Core.Gear.items if i.subtype == item.requires[1]])
        else:
            raise ValueError("WeaponCost fuckery")

    elif l[0] == "ArmorRating":
        if not hasattr(item, "requires"):
            raise AttributeError(f"{item.name} has a dependant cost variable but nothing to depend on!")
        if arg != -1 and isinstance(arg, Core.Armor):
            r1 = arg.armor_rating
        else:
            return "TODO: FIX ARMORRATING COST"
            # raise ValueError("ArmorRating fuckery")

    elif l[0] == "CommlinkCost":
        if not hasattr(item, "requires"):
            raise AttributeError(f"{item.name} has a dependant cost vairable but nothing to depend on!")
        if arg != -1 and isinstance(arg, Core.Electronics):
            if arg.subtype == "Commlink":
                r1 = arg.cost

    elif l[0] == "DeckCost":
        if not hasattr(item, "requires"):
            raise AttributeError(f"{item.name} has a dependant cost vairable but nothing to depend on!")
        if arg != -1 and isinstance(arg, Core.Electronics):
            if arg.subtype == "Cyberdeck":
                r1 = arg.cost

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


    elif l[0] == "Force":
        if not hasattr(item, "force"):
            raise AttributeError(f"Item {item} has a 'Force' list handler with no 'Force' attribute")
        r1 = item.force

        
        
    else:
        print("TODO")
        print(f"    {l[0]} logic for {item}")

    match l[1]:
        case "+":
            if (isinstance(r1, int) or isinstance(r1, float)) and (isinstance(l[2], int) or isinstance(l[2], float)):
                return r1 + l[2]
        case "*":
            if (isinstance(r1, int) or isinstance(r1, float)) and (isinstance(l[2], int) or isinstance(l[2], float)):
                return r1 * l[2]


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
            if hasattr(item, "legality") and hasattr(weapon_mod, "legality"):
                if weapon_mod.legality == Core.FORBIDDEN or item.legality == Core.FORBIDDEN:
                    item.legality = Core.FORBIDDEN
                elif weapon_mod.legality == Core.RESTRICTED or item.legaliy == Core.RESTRICTED:
                    item.legality = Core.RESTRICTED
            if not hasattr(item, "legality") and hasattr(weapon_mod, "legality"):
                item.legality = weapon_mod.legality
            item.name = f"{item.name} /w {weapon_mod.name}"

    if isinstance(item, Core.Armor):
        if hasattr(item, "mods"):
            if m is not None:
                armor_mod = m
            else:
                armor_mod = random.choice([i for i in Core.ArmorModification.items if hasattr(i, "requires") and i.requires[1] == "Armor"])
            item.mods = armor_mod
            if isinstance(armor_mod.cost, list):
                item.cost = get_item_cost(item) + get_item_cost(armor_mod, item)
            else:
                item.cost = item.cost + armor_mod.cost

    if isinstance(item, Core.Augmentation):
        if hasattr(item, "mods"):
            if m is not None:
                aug_mod = m
            else:
                aug_mod = random.choice([i for i in Core.Augmentation.items if not hasattr(i, "base") and i.subtype == item.subtype])
            while aug_mod.name in [i.name for i in item.mods]:
                aug_mod = random.choice([i for i in Core.Augmentation.items if not hasattr(i, "base") and i.subtype == item.subtype])
            aug_mod.rating = get_item_rating(aug_mod)
            aug_mod.capacity = get_item_capacity(aug_mod)
            aug_mod.cost = get_item_cost(aug_mod)
            aug_mod.essence = get_item_essence(aug_mod)
            if item.capacity >= aug_mod.capacity:
                item.capacity -= aug_mod.capacity
                item.mods.append(aug_mod)
                item.cost += aug_mod.cost
            else:
                return item
                pass

    return item

def get_sensor(arg=-1):
    if arg != -1:
        pass
    else:
        sensor_housing = random.choice([Core.HANDHELD_HOUSING, Core.WALL_MOUNTED_HOUSING])
        if isinstance(sensor_housing.capacity, list):
            sensor_housing.capacity = list_handler(sensor_housing.capacity, sensor_housing)
        sensor_type = random.choice([Core.SENSOR_ARRAY, Core.SENSOR_SINGLE])
        sensor_type.rating = list_handler(sensor_type.rating, sensor_type)

        sensor_functions = []
        if sensor_type == Core.SENSOR_ARRAY:
            for i in range(sensor_type.rating):
                if random.randint(0, i) < sensor_type.rating / 2:
                    x = random.choice([f"{k}: (Range: {d})" if d != 0 else f"{k}" for k, d in Core.SENSOR_FUNCTIONS.items()])
                    while x in sensor_functions:
                        x = random.choice([f"{k}: (Range: {d})" if d != 0 else f"{k}" for k, d in Core.SENSOR_FUNCTIONS.items()])
                    sensor_functions.append(x)
                else:
                    pass
        else:
            x = random.choice([f"{k}: (Range: {d})" if d != 0 else f"{k}" for k, d in Core.SENSOR_FUNCTIONS.items()])
            sensor_functions.append(x)
    sensor = Core.Sensor(sensor_type, sensor_housing, sensor_functions)
    
    return sensor


def get_cyberdeck(item: Core.Electronics = None):
    if item is None or (hasattr(item, "category") and item.subtype != "Cyberdeck"):
        item = random.choice([i for i in Core.Electronics.items if hasattr(i, "category") and i.subtype == "Cyberdeck"])
    program_count = int(item.programs)
    item.programs = []
    for idx in range(program_count):
        if idx == 0:
            new_program = random.choice([i for i in Core.Software.items if i.category == 'Common'])
            item.programs.append(new_program)
            continue
        else:
            while True:
                new_program = random.choice([i for i in Core.Software.items])
                if new_program not in item.programs:
                    item.programs.append(new_program)
                    break
    item.attack = Core.Attribute("Attack", item.attributes[0], matrix=True)
    item.sleaze = Core.Attribute("Sleaze", item.attributes[1], matrix=True)
    item.data_processing = Core.Attribute("Data Processing", item.attributes[2], matrix=True)
    item.firewall = Core.Attribute("Firewall", item.attributes[3], matrix=True)
    return item


def get_augmentation_grade(item: Core.Augmentation, grade=None, grades=DEFAULT_AUG_GRADES, **kwargs):
    if "rating" in kwargs:
        item.rating = kwargs['rating']
    if grade is None:
        grade = random.choice([g for g in Core.AUG_GRADES if hasattr(g, "default")])
    item.grade = grade
    return item


def get_augmentation(bioware=False, cyberlimb=False, **kwargs):
    if bioware:
        item = random.choice([i for i in Core.Augmentation.items if i.subtype in ['Bioware', 'Cultured Bioware']])
    elif cyberlimb:
        item = random.choice([i for i in Core.Augmentation.items if i.subtype == 'Cyberlimbs'])
        item.rating = 1
    else:
        cyberware_location = random.choice(['Headware', 'Earware', 'Eyeware', 'Bodyware'])
        if cyberware_location in ['Bodyware', 'Headware']:
            item = random.choice([i for i in Core.Augmentation.items if i.subtype == cyberware_location])
        else:
            item = random.choice([i for i in Core.Augmentation.items if i.subtype == cyberware_location and hasattr(i, 'base')])
    item.grade = get_augmentation_grade(item)
    item.rating = get_item_rating(item)
    item.cost = get_item_cost(item)
    item.capacity = get_item_capacity(item)
    item.essence = get_item_essence(item)
    mod_attempts = 0
    if item.subtype not in ['Bodyware', 'Headware']:
        while item.capacity > 0 and mod_attempts < 4:
            mod_attempts += 1
            item = get_mod(item)
    return item


def get_weapon(skill=None, no_mod=False, **kwargs):
    if skill is None:
        # Generate random weapon from all weapons
        pass
    match skill:
        case "Automatics":
            pool = [p for p in Core.Firearm.items if p.subtype in [
                'Assault Rifle', 'Machine Pistol', 'Submachine Gun'
                ]]
        case "Pistols":
            pool = [p for p in Core.Firearm.items if p.subtype in [
                'Light Pistol', 'Heavy Pistol', 'Machine Pistol',
                'Hold-Out', 'Taser']]
        case "Heavy Weapons":
            pool = [p for p in Core.Firearm.items if p.subtype in [
                'Sniper Rifle', 'Shotgun', 'Machine Gun', 'Cannon/Launcher'
                ]]
        case "Archery":
            pool = [p for p in Core.ProjectileWeapon.items if p.subtype in ["Bows", "Crossbow"]]
            no_mod = True
        case "Blades":
            pool = [p for p in Core.MeleeWeapon.items if p.subtype == "Blade"]
            no_mod = True
        case "Clubs":
            pool = [p for p in Core.MeleeWeapon.items if p.subtype == "Club"]
            no_mod = True
        case "Throwing Weapons":
            pool = [p for p in Core.ProjectileWeapon.items if p.subtype == "Throwing Weapons"]
            no_mod = True
    for pool_item in pool:
        pool_item.avail = get_item_avail(pool_item)
    new_weapon = random.choice([i for i in pool if i.avail <= DEFAULT_MAX_AVAILABILITY])
    if not no_mod and random.randint(1, 100) >= 40:
        new_weapon = get_mod(new_weapon)
    return get_item(new_weapon)

def get_vehicle(skill = None, **kwargs):
    if skill is not None:
        match skill:
            case "Pilot Ground Craft":
                valid_vehicles = [i for i in Core.Vehicle.items if i.skill_req == Core.PILOT_GROUND_CRAFT]
            case "Pilot Aircraft":
                valid_vehicles = [i for i in Core.Vehicle.items if i.skill_req == Core.PILOT_AIRCRAFT]
            case "Pilot Walker":
                valid_vehicles = [i for i in Core.Vehicle.items if i.skill_req == Core.PILOT_WALKER]
            case "Pilot Watercraft":
                valid_vehicles = [i for i in Core.Vehicle.items if i.skill_req == Core.PILOT_WATERCRAFT]
            case _:
                print("invalid 'skill_req' arg, choosing all vehicles")
                valid_vehicles = [i for i in Core.Vehicle.items]
    else:
        valid_vehicles = [i for i in Core.Vehicle.items]

    if "veh_type" in kwargs:
        match kwargs['veh_type']:
            case "road":
                veh_types = list(dict.fromkeys([i.subtype for i in Core.ROAD_VEHICLES]))
            case "water":
                veh_types = list(dict.fromkeys([i.subtype for i in Core.WATER_VEHICLES]))
            case "air":
                veh_types = list(dict.fromkeys([i.subtype for i in Core.AIR_VEHICLES]))
            case "drone":
                veh_types = list(dict.fromkeys([i.subtype for i in Core.DRONE_VEHICLES]))
            case _:
                print("invalid 'veh_type' arg, choosing all vehicles")
                veh_types = list(dict.fromkeys([i.subtype for i in Core.Vehicle.items]))
    else:
        return random.choice([i for i in valid_vehicles])

    if "any" in kwargs:
        vehicle = random.choice(valid_vehicles)
    else:
        vehicle = random.choice([i for i in valid_vehicles if i.subtype==random.choice(veh_types)])
    return vehicle

def get_fake_license(item=None, license_type=None) -> Core.Electronics:
    if item is not None:
        if hasattr(item, "subtype"):
            license_type = item.subtype
        elif hasattr(item, "category"):
            license_type = item.category
        else:
            license_type = item.name
    license_rating = random.choices([1, 2, 3, 4, 5, 6], [2, 3, 3, 5, 3, 1])[0]
    return Core.Electronics(f"Fake License ({license_type})", cost=(license_rating * 200), page_ref=443, rating=license_rating, avail=[license_rating * 3], legality=Core.FORBIDDEN, subtype="Identification")


def get_item_pool(item_pool_id: str) -> list[Core.Gear]:
    match item_pool_id:
        case "Locksmith":
            item_pool = [i for i in Core.Electronics.items if hasattr(i, "subtype") and
                         i.subtype == "B&E Gear"]
            return item_pool
        case "Hardware":
            item_pool = [i for i in Core.Electronics.items if hasattr(i, "subtype") and
                         i.subtype in ["Commlink", "Cyberdeck", "Accessories", "RFID Tags"]]
            return item_pool


def get_item_force(item: Core.Gear, ch: Core.Character) -> Core.Gear:
    if not hasattr(item, "force") or not hasattr(item, "category"):
        return item

    # An items "Force" value can be within a range of values relative to the characters
    #   'Magic' attribute value. However some values (typically that equal to the magic
    #   attribute value) are more common than others so the horrible bit of math here
    #   is just that.
    match item.category:
        case "Spell":
            try:
                ranges = [i for i in range(1, ch.Magic.value * 2 + 1)]
                range_probs = [abs(i-len(ranges)+1) if abs(i) > (len(ranges)/2)-1 else 0 for i in ranges]
            except AttributeError:
                return item
            item.force = random.choices(ranges, range_probs)[0]
        case "Foci":
            upper_bound = max(ch.Skills[item.skill.name], ch.Magic.value)
            try:
                ranges = [i for i in range(1, upper_bound + 1)]
                range_probs = [i+1 if idx < len(ranges) - 1 else i-1 for idx, i in enumerate(ranges)]
            except AttributeError:
                return item
            item.force = random.choices(ranges, range_probs)[0]
            
    return item


def get_magic_item(item_type, ch: Core.Character) -> Core.Gear:
    if item_type == 'Alchemy':
        new_item = Core.ALCHEMICAL_FOCUS
        new_item = get_item_force(new_item, ch)
    return new_item



def get_item(item: Core.Gear=None, item_pool_id=None, ch: Core.Character = None):
    item_pool = get_item_pool(item_pool_id)
    if not item_pool is None:
        item = random.choice(item_pool)
        if item.__class__ == Core.Cyberdeck:
            item = get_cyberdeck(item)

    if item is None:
        return AttributeError("Both args cannot be None.\n",
                              f"They are currently {item} and {item_pool}")
    if hasattr(item, "force"):
        item.force = get_item_force(item, ch)
    if hasattr(item, "cost"):
        item.cost = get_item_cost(item)
    if hasattr(item, "rating"):
        item.rating = get_item_rating(item)
    if hasattr(item, "avail"):
        item.avail = get_item_avail(item)
    return item


def item_format(item: Core.Gear=None, compact=False):
    if item.__class__ == Core.Cyberdeck:
        software = item.programs
        name = item.name
        attributes   = f' {item.attack} | {item.data_processing.value} {item.data_processing.name}'
        attributes_2 = f' {item.sleaze} | {item.firewall.value} {item.firewall.name}'
        if not compact:
            print("--- Cyberdeck ---")
            print(name)
            print("--> Attributes    ")
            print(attributes)
            print(attributes_2)
            print("--> Software")
            print(", ".join([i.name for i in software]))
        else:
            print(f"[Cyberdeck] {item.name} -> A:{item.attack.value}, S:{item.sleaze.value}, DP:{item.data_processing.value}, F:{item.firewall.value}")

    elif item.__class__ in [Core.Firearm, Core.MeleeWeapon, Core.ProjectileWeapon]:
        if item.__class__ == Core.Firearm:
            wpn_type = "Firearm"
        elif item.__class__ == Core.MeleeWeapon:
            wpn_type = "Melee"
        elif item.__class__ == Core.ProjectileWeapon:
            wpn_type = "Projectile"
        print(f"[Weapon/{wpn_type}] {item.name} (p.{item.page_ref})")


    elif item.__class__ == Core.Electronics:
        if "license" in item.name:
            print(f'{item.name} - {item.rating}')
        elif hasattr(item, "subtype") and item.subtype == "Identification":
            print(f'[Elec/ID] {item.name} (p.{item.page_ref})')
        else:
            print(f'[Elec/{item.subtype}] {item.name} (p.{item.page_ref})')


    else:
        print(item)


if __name__ == "__main__":
    def test_vehs():
        print(f"Random vehicle: {get_vehicle(any=True)}")
        print(f"Groundcraft vehicle: {get_vehicle(skill_req='Pilot Ground Craft', any=True)}")
        print(f"Groundcraft road vehicle: {get_vehicle(skill_req='Pilot Ground Craft', any=True, veh_type='road')}")
        print(f"Aircraft vehicle: {get_vehicle(skill_req=Core.PILOT_AIRCRAFT.name, any=True)}")
        print(f"Walker vehicle: {get_vehicle(skill_req=Core.PILOT_WALKER.name, any=True)}")
        print(f"Watercraft vehicle: {get_vehicle(skill_req=Core.PILOT_WATERCRAFT.name, any=True)}")

    def run_through_gear(**kwargs):
        for idx, gear in enumerate(Core.Gear.items):
            print(f'[{idx}/{len(Core.Gear.items)}] {gear}')
            print('Cost:', get_item_cost(gear, **kwargs))
            print('Availabilty:', get_item_avail(gear, **kwargs))
            # print('Rating:', get_item_rating(gear, **kwargs))

    x = get_augmentation(bioware=False)
    y = get_cyberdeck()
    print("=== FULL FORMAT ===\n")
    item_format(y)
    print("\n=== COMPACT FORMAT ===\n")
    item_format(y, compact=True)
    

