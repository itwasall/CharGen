import random
import char_shadowrun_5e_data as Core

DEFAULT_MAX_AVAILABILITY = 12
DEFAULT_MAX_RATING = 6
DEFAULT_AUG_GRADES = ["standard", "alphaware"]


def attrAsDict(_class):
    return {i: _class.__getattribute__(i) for i in dir(_class) if not i.startswith("__") and i != 'items'}


def get_rating(item: Core.Gear, max_rating=DEFAULT_MAX_RATING, **kwargs):
    if "rating" in kwargs:
        return kwargs['rating']
    elif "rating" not in attrAsDict(item).keys():
        return 0
    elif isinstance(item.rating, int):
        return item.rating
    elif isinstance(item.rating, str):
        return 0
    elif isinstance(item.rating, list):
        return list_handler(item.rating, item, max_rating)
    else:
        raise ValueError(f'{item.name} has bad rating data')


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
        raise ValueError


def get_item_cost(item: Core.Gear, arg=-1, **kwargs):
    if not hasattr(item, "cost"):
        return 0
    if isinstance(item.cost, int):
        return item.cost
    elif isinstance(item.cost, list):
        if arg != -1:
            return list_handler(item.cost, item, arg, **kwargs)
        return list_handler(item.cost, item, **kwargs)

def get_item_essence(item: Core.Gear, arg=-1, **kwargs):
    if not hasattr(item, "essence"):
        return 0
    if isinstance(item.essence, int) or isinstance(item.essence, float):
        return item.essence
    if isinstance(item.essence, str):
        return 0
    elif isinstance(item.essence, list):
        if arg != -1:
            return list_handler(item.essence, item, arg, **kwargs)
        return list_handler(item.essence, item, **kwargs)



def list_handler(l: list, item, arg=-1, **kwargs):

    # if item.name in [ 'Gas Vent System', 'Chemical Protection', 'Fire Resistance', 'Insulation', 'Nonconductivity', 'Thermal Damping' ]:
    #    return 0
    r1 = 1

    if isinstance(l[0], int) and l[1] == "to":
        if arg != -1 and isinstance(arg, int) and arg < l[2]:
            l[2] == arg
        else:
            return random.choice(range(l[0], l[2]))
        
    if l[0] == "Rating":
        # Catches if item doesn't have rating attribute
        if not hasattr(item, "rating"):
            raise AttributeError(f"{item.name} has no 'rating' attribute despite mention in {l}")
        # If item.rating is an integar, pass that on
        if isinstance(item.rating, int):
            r1 = item.rating
        elif arg != -1:
            if arg in [DEFAULT_MAX_AVAILABILITY, DEFAULT_MAX_RATING]:
                item.rating = get_rating(item, **kwargs)
                r1 = item.rating
            else:
                pass
        else:
            item.rating = get_rating(item, **kwargs)
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
        else:
            raise ValueError("WeaponCost fuckery")

    elif l[0] == "ArmorRating":
        if not hasattr(item, "requires"):
            raise AttributeError(f"{item.name} has a dependant cost variable but nothing to depend on!")
        if arg != -1 and isinstance(arg, Core.Armor):
            r1 = arg.armor_rating
        else:
            raise ValueError("ArmorRating fuckery")

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

def build_sensor(arg=-1):
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


def get_augmentation_grade(item: Core.Augmentation, grade=None, grades=DEFAULT_AUG_GRADES, **kwargs):
    if "rating" in kwargs:
        item.rating = kwargs['rating']
    if grade is None:
        grade = random.choice([g for g in Core.AUG_GRADES if hasattr(g, "default")])
    item.grade = grade
    x_i = get_item_cost(item, **kwargs)
    if x_i is None:
        raise TypeError()
    item.cost = int(round(get_item_cost(item, **kwargs) * grade.cost))
    item.avail = get_item_avail(item, **kwargs) + grade.avail
    item.essence = get_item_essence(item, **kwargs) * grade.essence
    return item

def get_augmentation(**kwargs):
    for i in Core.Augmentation.items:
        if i.subtype == "Headware":
            i.location = "Head"
        elif i.subtype == "Earware":
            i.location = "Ears"
        elif i.subtype == "Eyeware":
            i.location = "Eyes"
        elif i.subtype == "Bodyware":
            i.location = "Body"
    # is_cyberlimb = random.randint(0, 1)
    is_cyberlimb = True
    if is_cyberlimb:
        body_part = random.choice(["Full Arm", "Full Leg", "Lower Arm", "Lower Leg", "Hand", "Foot", "Torso", "Skull"])
        cyberlimb = random.choice([i for i in Core.Augmentation.items if hasattr(i, 'location') and i.location == body_part])
        print(cyberlimb)
        poss_aug = [i for i in Core.Augmentation.items if hasattr(i, "cyberlimbs") and i.cyberlimbs == True]
        x = get_augmentation_grade(random.choice(poss_aug))
        print(x.grade)
    else:
        aug_wares = ["Head", "Eyes", "Ears", "Body"]
        body_part = random.choice(aug_wares)

def get_vehicle(**kwargs):
    if "skill_req" in kwargs:
        match kwargs['skill_req']:
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
        veh_types = list(dict.fromkeys([i.subtype for i in Core.Vehicle.items]))

    if "any" in kwargs:
        vehicle = random.choice(valid_vehicles)
    else:
        vehicle = random.choice([i for i in valid_vehicles if i.subtype==random.choice(veh_types)])
    return vehicle

print(f"Random vehicle: {get_vehicle(any=True)}")
print(f"Groundcraft vehicle: {get_vehicle(skill_req='Pilot Ground Craft', any=True)}")
print(f"Groundcraft road vehicle: {get_vehicle(skill_req='Pilot Ground Craft', any=True, veh_type='road')}")
print(f"Aircraft vehicle: {get_vehicle(skill_req=Core.PILOT_AIRCRAFT.name, any=True)}")
print(f"Walker vehicle: {get_vehicle(skill_req=Core.PILOT_WALKER.name, any=True)}")
print(f"Watercraft vehicle: {get_vehicle(skill_req=Core.PILOT_WATERCRAFT.name, any=True)}")
