import yaml
import random

NAMES = yaml.safe_load(open('chargen_names.yml', 'rt'))

NATIONALITIES = list(NAMES.keys())

for nation in NATIONALITIES:
    print(nation)
    print(NAMES[nation].keys())
    print(len(NAMES[nation]['family']))

def gen_name():
    nationality = random.choice(NATIONALITIES)
    name = " ".join([random.choice(NAMES[nationality][random.choice(['male', 'female'])]), random.choice(NAMES[nationality]['family'])])
    return f'({nationality}) - {name}'

for i in range(10):
    gen_name()
