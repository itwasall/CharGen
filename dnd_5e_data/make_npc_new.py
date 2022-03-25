import random
from random import choice
import click
import yaml
from os import getcwd

print(getcwd())
names = yaml.safe_load(open('./npc_new_namelist.yaml', 'rt'))
aligncombine = ['Chaotic Evil', 'Chaotic Good', 'Chaotic Neutral', 'Lawful Good', 'Lawful Evil', 'Lawful Neutral', 'Neutral Good', 'Neutral Evil', 'True Neutral']
abilities = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
race = ['Human', 'Elf', 'Dwarf', 'Halfing', 'Orc', 'Dragonborn', 'Tiefling', 'Half-Elf', 'Half-Orc']
traits = []

def get_race(overrides=None):
    if overrides == None or overrides not in race:
        return choice(race)
    else: return race


def get_gender(overrides=None, inclusive=False):
    if overrides == None:
        if inclusive == False:
            return choice(['Male', 'Female'])
        else:
            return choice(['Male', 'Female', 'Trans-Male', 'Trans-Female', 'Non-Binary'])
    else:
        return overrides


def get_name(gender, race, overrides=None, genderOverride=False):
    if overrides == None:
        if genderOverride == False:
            if race == "Half-Orc":
                name = choice(names['Half-Orc'][gender])
            else:
                name = choice(names[race][gender]) + " " + choice(names[race]['surname'])
        if genderOverride == True:
            allnames = []
            allnames.extend(names[race]['Male'])
            allnames.extend(names[race]['Female'])
            if race == "Half-Orc":
                name = choice(allnames)
            else:
                name = choice(allnames) + " " + choice(names[race]['surname'])
        return name
    else: return overrides



def get_alignment(overrides=None):
    if overrides == None or overrides not in aligncombine:
        return choice(aligncombine)
    else: return overrides

def get_high_low(overrides=None):
    if overrides == None or overrides.__class__ is not list:
        high_stat = choice(abilities)
        low_stat = high_stat
        while low_stat == high_stat:
            low_stat = choice(abilities)
    elif overrides.__class__ is list:
        high_stat = overrides[0]
        low_stat = overrides[1]
    return high_stat, low_stat

@click.command()
@click.option('-n','--name',default=None,help="Character Name")
@click.option('-ng', '--namegendered',default=False,help="Character Name based on Character gender")
@click.option('-r', '--race',default=None,help="Character Race")
@click.option('-g', '--gender',default=None,help="Character Gender")
@click.option('-eg', '--extendedgender',default=False,help="More gender options")
@click.option('-a','--alignment',default=None,help="Character alignment")
@click.option('-hs', '--high_stat',default=None,help="Character high stat")
@click.option('-ls','--low_stat',default=None,help="Character low stat")
def get_npc(name, namegendered, race, gender, extendedgender, alignment, high_stat, low_stat):
    name_override = name
    namegender_override = namegendered
    race_override = race
    gender_override = gender
    extended_genders = extendedgender
    alignment_override = alignment
    high_stat_override = high_stat
    low_stat_override = low_stat
    if high_stat_override == low_stat_override and low_stat_override == None:
        high_low_override = None
    else:
        high_low_override = [high_stat_override, low_stat_override]
    npc_race = get_race(race_override)
    print(npc_race)
    npc_gender = get_gender(gender_override)
    npc_name = get_name(npc_gender, npc_race, name_override, namegender_override)
    npc_alignment = get_alignment(alignment_override)
    npc_high_stat, npc_low_stat = get_high_low(high_low_override)
    npc = {'Name':npc_name, 'Race':npc_race,'Gender':npc_gender,'Alignment':npc_alignment,'High/Low Stat':f'{npc_high_stat}/{npc_low_stat}'}
    for k, d in npc.items():
        print(k, npc[k])

if __name__ == "__main__":
    get_npc()

