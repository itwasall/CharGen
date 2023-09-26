import yaml

stream = open('classes.yaml', 'r')
data = yaml.safe_load(stream)

jobs = data['classes']
races = data['races']
race_names = races[3]
for i,_ in enumerate(races):
    print(races[i]['name'])


