import yaml
data = yaml.safe_load(
    open("/home/refrshrs/code/python/CharGen/dnd_3.5e_data/_core.yaml", "rt")
)
races = data["races"]
jobs = data["jobs"]
skills = data["skills"]

for j in jobs:
    print(j['name'])
    print(j['alignment'])
