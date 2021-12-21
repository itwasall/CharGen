import yaml
from random import randint, choice, choices

job = yaml.safe_load(open('numenera_data//classes.yaml'))
cypher = yaml.safe_load(open('numenera_data//cyphers.yaml'))


def stats(job):
    stats = {'might':0, 'speed':0, 'int':0}
    stat_weights = job['stat_pool_weights']
    for stat_name, stat_value in job['stats'].items():
        stats[stat_name] = stat_value
    for i in range(job['stat_pool']):
        stat_boost = choices(list(stats.keys()), stat_weights)
        stats[stat_boost[0]] += 1
    return stats


def cypher_gen(job):
    items = job['equipment']
    pop_list = []
    for it, item in enumerate(items):
        if item == 'rnd_cypher':
            pop_list.append(it)
            cyphergen = choice(list(cypher.keys()))
            items.append(cyphergen)
    pop_list.reverse()
    for it in pop_list:
        items.pop(it)
    return items

def char_gen():
    char_job = choice(job['name'])
    print(char_job[char_job['name']].keys())
    char_stats = stats(char_job)
    char_job['equipment'] = cypher_gen(char_job)


    print(char_stats)
    print(char_job['equipment'])

char_gen()