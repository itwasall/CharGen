import yaml
import random

NAMES = yaml.safe_load(open('chargen_names.yml', 'rt'))

NATIONALITIES = list(NAMES.keys())

def gen_name():
    names = []
    name_out = {}
    yaml_out = """"""
    for nation in list(NAMES.keys()):
        if 'family' in NAMES[nation].keys():
            names = [" ".join(
                [random.choice(NAMES[nation][random.choice(['male', 'female'])]), random.choice(NAMES[nation]['family']
                    )
                ]) for _ in range(100)]
        name_out[nation] = f'{nation} - {names}'
    for nation in list(NAMES.keys()):
        yaml_out += f"\n-- '{nation}':\n    [{[i for i in names]}]"
    return yaml_out




y = yaml.safe_load(gen_name())

with open('names.yml', 'a') as file:
    yaml.dump(y, file)

print(open('names.yml').read())
