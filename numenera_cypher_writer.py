import yaml

cyphers = open('numenera_data\\numnera_cyphers.txt', 'r')

count_boi = 5
cypher_list = []
for line in cyphers:
    cypher_list.append(line)

cypher_name = []
cypher_level = []
cypher_usable = []
cypher_effect = []
cypher_internal = []
cypher_wearable = []
cypher_line_no = []
for it, line in enumerate(cypher_list):
    if line.startswith('Level:'):
        line = line.rstrip('\n')
        cypher_level.append(line)
        cypher_line_no.append('Level')
    elif line.startswith('Usable'):
        line = line.rstrip('\n')
        cypher_usable.append(line)
        cypher_line_no.append('Usable')
    elif line.startswith('Effect'):
        line = line.rstrip('\n')
        cypher_effect.append(line)
        cypher_line_no.append('Effect')
    elif line.startswith('Wearable'):
        line = line.rstrip('\n')
        cypher_wearable.append(line)
        cypher_line_no.append('Wearable')
    elif line.startswith('Internal'):
        line = line.rstrip('\n')
        cypher_internal.append(line)
        cypher_line_no.append('Internal')
    else:
        line = line.rstrip('\n')
        cypher_name.append(line)
        cypher_line_no.append('Name')
cyphers_dict = {}

for line in cypher_line_no:
    if line == 'Name':
        current_name = cypher_name[0]
        cyphers_dict[cypher_name[0]] = {}
        cypher_name.pop(0)
    elif line == 'Level':
        cyphers_dict[current_name]['Level'] = cypher_level[0][7:]
        cypher_level.pop(0)
    elif line == 'Wearable':
        cyphers_dict[current_name]['Wearable'] = cypher_wearable[0][10:]
        cypher_wearable.pop(0)
    elif line == 'Internal':
        cyphers_dict[current_name]['Internal'] = cypher_internal[0][10:]
        cypher_internal.pop(0)
    elif line == 'Usable':
        cyphers_dict[current_name]['Usable'] = cypher_usable[0][8:]
        cypher_usable.pop(0)
    elif line == 'Effect':
        cyphers_dict[current_name]['Effect'] = cypher_effect[0][8:]
        cypher_effect.pop(0)

print(cyphers_dict)

stream = open('numenera_cyphers_redone.yaml', 'w')

yaml.dump(cyphers_dict, stream)