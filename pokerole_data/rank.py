from yaml import safe_load

rank_data = safe_load(open('pokerole/rank.yml', 'rt'))

class PkRank:
    def __init__(self, name, data):
        self.name = name
        self.core_attribute_points = data['core_attribute_points']
        self.social_attribute_points = data['social_attribute_points']
        self.skill_points = data['skill_points']
        self.skill_limit = data['skill_limit']
        self.extra_benefits = data['extra_benefits']
        self.max_targets = data['max_targets']
        self.next_rank_reqs = data['next_rank_reqs']

    def __repr__(self):
        return self.name

def get_rank(rank_name):
    if rank_name in ['Starter', 'Beginner', 'Amateur', 'Ace', 'Pro', 'Master', 'Champion']:
        return PkRank(rank_name, rank_data[rank_name])
    else:
        return ValueError
