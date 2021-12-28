import yaml

annelid = yaml.safe_load(open('tbz_data/annelid.yaml'))

for i in annelid:
    print(annelid[i])
