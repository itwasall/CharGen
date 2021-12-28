import yaml
import random
from random import choice, choices, randint
from math import floor, ceil
from itertools import repeat


def expand(d):
    ret = {}
    for k in d:
        v = d[k]
        if isinstance(k, range):
            ret.update({i: v for i in k})
        else:
            ret[k] = v
    return ret


alignments = [
    "Lawful Good",
    "Lawful Evil",
    "Lawful Neutral",
    "Neutral Good",
    "Neutral Evil",
    "True Neutral",
    "Chaotic Good",
    "Chaotic Evil",
    "Chaotic Neutral",
]
# aa = Alignment Abbreviation
aa = {
    alignments[0]: "LG",
    alignments[1]: "LE",
    alignments[2]: "LN",
    alignments[3]: "NG",
    alignments[4]: "NE",
    alignments[5]: "TN",
    alignments[6]: "CG",
    alignments[7]: "CE",
    alignments[8]: "CN",
}
data = yaml.safe_load(
    open("/home/refrshrs/code/python/CharGen/dnd_3.5e_data/_core.yaml", "rt")
)
races = data["races"]
jobs = data["jobs"]
skills = data["skills"]


class Character:
    def __init__(self, name):
        self.name = name
        self.job = {}
        self.job["name"] = None
        self._ability_score_mods()

    def __dice_roll(self, diceroll):
        throws, sides = diceroll.split('d')
        total = 0
        for i in range(int(throws)):
            total += randint(1, int(sides))
        return total

    def _alignment(self, align="R"):
        if align == "R" or align not in alignments:
            self.alignment = choice(alignments)
        else:
            self.alignment = align

    def _race(self, race="R"):
        if race == "R" or race not in [r["name"] for r in races]:
            self.race = choice(races)
        else:
            for r in races:
                if race == r["name"]:
                    self.race = r
        self.base_speed = self.race['base_speed']

    def _job(self, job):
        abbr_align = aa[self.alignment]
        if job == "R" or job == "r" or job not in [j["name"] for j in jobs]:
            self.job = choice(jobs)
            while abbr_align not in self.job['alignment']:
                self.job = choice(jobs)
        else:
            for j in jobs:
                if job == j["name"]:
                    self.job = j
                    c = 0
                    while abbr_align not in self.job['alignment']:
                        if c == 0:
                            print("Alignment and job mismatch! Choosing new job")
                            c += 1
                        self.job = choice(jobs)
        self.hp = self._hit_points()

    def _hit_points(self):
        return self.__dice_roll(self.job['hitdice'])

    def _ability_scores(self):
        j_name = self.job["name"]
        rolls = []
        for _ in repeat(None, 6):
            dice_rolls = []
            for _ in repeat(None, 4):
                dice_rolls.append(self.__dice_roll('1d6'))
            dice_rolls.sort()
            dice_rolls.pop(0)
            rolls.append(sum(dice_rolls))
        rolls.sort()
        print(rolls)

    def _ability_score_mods(self):
        self.str_mod = expand(
            {
                1: -5,
                range(2, 4): -4,
                range(4, 6): -3,
                range(6, 8): -2,
                range(8, 10): -1,
                range(10, 12): 0,
                range(12, 14): 1,
                range(14, 16): 2,
                range(16, 18): 3,
                range(18, 20): 4,
            }
        )
        self.dex_mod = expand(
            {
                range(1, 4): -5,
                range(4, 6): -3,
                range(6, 8): -2,
                range(8, 10): -1,
                range(10, 12): 0,
                range(12, 14): 1,
                range(14, 16): 2,
                range(16, 18): 3,
                range(18, 20): 4,
            }
        )
        self.con_mod = expand(
            {
                range(1, 8): -2,
                range(8, 10): -1,
                range(10, 12): 0,
                range(12, 14): 1,
                range(14, 16): 2,
                range(16, 18): 3,
                range(18, 20): 4,
            }
        )
        self.int_mod = expand(
            {
                1: -5,
                range(2, 4): -4,
                range(4, 6): -3,
                range(6, 8): -2,
                range(8, 10): -1,
                range(10, 12): 0,
                range(12, 14): 1,
                range(14, 16): 2,
                range(16, 18): 3,
                range(18, 20): 4,
            }
        )
        self.wis_mod = expand(
            {
                1: -5,
                range(2, 6): -4,
                range(6, 8): -2,
                range(8, 10): -1,
                range(10, 12): 0,
                range(12, 14): 1,
                range(14, 16): 2,
                range(16, 18): 3,
                range(18, 20): 4,
            }
        )
        self.cha_mod = expand(
            {
                1: -5,
                range(2, 4): -4,
                range(4, 6): -3,
                range(6, 8): -2,
                range(8, 10): -1,
                range(10, 12): 0,
                range(12, 14): 1,
                range(14, 16): 2,
                range(16, 18): 3,
                range(18, 20): 4,
            }
        )

    def _ability_mods(self):
        pass

    def _skills(self):
        j_name = self.job["name"]
        if j_name == "Barbarian":
            pass

    def char_sheet(self, r_details=False, j_details=False):
        print(f"Name:      {self.name}")
        print(f'Race:      {self.race["name"]}')
        if r_details == True:
            self.char_sheet_race()
        print(f"Alignment: {self.alignment}")
        print(f'Class:     {self.job["name"]}')
        if j_details == True:
            self.char_sheet_job()
        print(f'HP:        {self.hp}')
        print(f'Speed:     {self.base_speed}ft')

    def char_sheet_race(self):
        pass

    def char_sheet_job(self):
        pass



def make_character(name, align="R", j="R"):
    c = Character(name)
    c._ability_scores()
    c._ability_mods()
    c._race()
    c._alignment(align)
    c._job(j)
    c.char_sheet()
    return c


char = make_character("B")
