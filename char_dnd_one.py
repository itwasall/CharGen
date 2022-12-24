from chargen import yaml_importer
expert_classes = yaml_importer("dnd_one_data/PLAYTEST_expert_classes.yml")

print([expert_classes['class'][c] for c in expert_classes['class'].keys()])



