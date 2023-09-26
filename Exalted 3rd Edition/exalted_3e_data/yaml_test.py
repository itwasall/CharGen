import yaml
from random import choice

data = yaml.safe_load(open('exalted_3e_data/charms.yaml', 'rt'))

def choose_charm():
    charm_key = choice(list(data.keys()))
    charm = {charm_key: data[charm_key]}
    return charm

def print_charm_names():
    outfile = open('charm_names.txt', 'wt')
    for charm in list(data.keys()):
        charm_og = charm
        outfile.write(f"{charm_og}\n")
    outfile.close

print(choose_charm())
print_charm_names()