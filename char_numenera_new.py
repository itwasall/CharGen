import yaml

class job_class(yaml.YAMLObject):
    yaml_tag = u'!job'
    def __init__(self, name, stats, stats_pool, stat_pool_weights, effort, edge, background, player_intrusions,
                connection, equipment, money, abilities, skills, actions, defaults):
        self.name = name
        self.stats = stats
        self.stats_pool = stats_pool
        self.stat_pool_weights = stat_pool_weights
        self.effort = effort
        self.edge = edge
        self.background = background
        self.player_intrusions = player_intrusions
        self.connection = connection
        self.equipment = equipment
        self.money = money
        self.abilities = abilities
        self.skills = skills
        self.actions = actions
        self.defaults = defaults
        pass

data_jobs = open('numenera_data/classes.yaml', 'r')
jobs = {}
for job in yaml.load_all(data_jobs, Loader=yaml.FullLoader):
    jobs[job.name] = job.stats, job.stats_pool, job.stat_pool_weights, job.effort, job.edge, job.background, job.player_intrusions, job.connection, job.equipment, job.money, job.abilities, job.skills, job.actions, job.defaults

print(jobs)
