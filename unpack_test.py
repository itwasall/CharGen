import char_dnd_5e_core as Core
import random

test_data = Core.BARBARIAN.equipment

def unpack(data):
    unpacked = []

    def resolve_choice(value, amt):
        print("\n", value)
        return_list = []
        for item in value:
            if isinstance(item, dict):
                return_list.append(resolve_dict(item))
        while len(return_list) < amt:
            roll = random.choice(value)
            if roll in return_list:
                return_list.pop(return_list.index(roll))
            return_list.append(roll)
        return return_list
    def resolve_dict(d: dict):
        print("\n", d)
        keys = list(d.keys())
        for key in keys:
            match key:
                case 'Choose 1':
                    resolved_dict = resolve_choice(d[key], 1)
                case 'Choose 2':
                    resolved_dict = resolve_choice(d[key], 2)
                case 'Choose 3':
                    resolved_dict = resolve_choice(d[key], 3)
        return resolved_dict
    def resolve_list(d: data):
        for item in data:
            # e.g. [{'Chooose 1': [MARTIAL WEAPONS]}, SHIELD]
            if isinstance(item, list):
                unpacked.append(resolve_list(item))
            elif isinstance(item, dict):
                unpacked.append(resolve_dict(item))
            else:
                unpacked.append(item)
        return
    if not isinstance(data, list):
        return unpacked
    else:
        unpacked.append(resolve_list(data))
        return unpacked





def unpack_new(data):
    unpacked_items = []
    def roll_items(data, amount):
        items = []
        roll = random.choice(data)
        while len(items) < amount:
            if roll in items:
                items.pop(items.index(roll))
            items.append(roll)
        return items

    def key_process(key, data):
        match key:
            case 'Choose 1':
                return roll_items(data, 1)
            case 'Choose 2':
                return roll_items(data, 2)

    for item in data:
        if isinstance(item, dict) and len(item.keys()) == 1:
            unpacked_dict_value = unpack_new(list(item.values())[0])
            unpacked_items.append(key_process(list(item.keys())[0], unpacked_dict_value))
        else:
            unpacked_items.append(item) 
    return unpacked_items

flatten = lambda *n: (e for a in n for e in (flatten(*a) if isinstance(a, (tuple, list)) else (a,)))    
print(list(flatten(unpack_new(test_data))))