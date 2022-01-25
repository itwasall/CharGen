import yaml

data = yaml.safe_load(open('ancestry_demo.yaml', 'rt'))

class BaseAncestoryClass:
    def __init__(self, *args):
        self.is_first_feat = None
        self.is_second_feat = None
        self.add_resistance = None
        [setattr(self, name, value) for name, value in args[0].items()]




demo = BaseAncestoryClass(data['test']['feats']['Second Feat'])
print(demo.is_first_feat)
print(demo.is_second_feat)
print(demo.add_resistance)
