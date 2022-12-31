import random
import char_dnd_5e_core as Core


def unpack_new(data):
    unpacked_items = []
    def roll_items(data, amount):
        items = []
        while len(items) < amount:
            roll = random.choice(data)
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
        elif isinstance(item, list):
            for i in item:
                if isinstance(i, dict) and len(i.keys()) == 1:
                    unpacked_dict_value = unpack_new(list(i.values())[0])
                    unpacked_items.append(key_process(list(i.keys())[0], unpacked_dict_value))
                else:
                    unpacked_items.append(i) 
        else:
            unpacked_items.append(item) 
    return unpacked_items

flatten = lambda *n: (e for a in n for e in (flatten(*a) if isinstance(a, (tuple, list)) else (a,)))    


c = Core.CLASSES

pal = Core.FIGHTER
for i in range(10):
    print(pal, list(flatten(unpack_new(pal.equipment))))
