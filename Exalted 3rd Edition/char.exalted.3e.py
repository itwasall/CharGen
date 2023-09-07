from typing import List
from chargen import *
from exalted_3e_data import data
from random import choice
# Character creation steps
#   1. Character concept & caste
#   2. Attributes
#   3. Abilities
#   4. Merits
#   5. Charms
#   6. Intimacies and Limit Trigger
#   7. Bonus Points
#   8. Finishing Touches

class ExaltedCharacter:
    def __init__(self):
        self.name = ""
        self.charms = []
    def roll_charms(self):
        for _ in range(15):
            self.charms = get_charm(self.charms)

def get_charm(charms = [], charm:str = None):
    charm_choice = data.get_charm()
    valid_charm = False
    while not valid_charm:
        prereq_charms = charm_choice.prerequisite_charms
        print(prereq_charms)
        for prereq_charm in prereq_charms:
            if (prereq_charm == "None"):
                valid_charm = True
            elif (prereq_charm in [charm.name for charm in charms]):
                prereq_charms.pop(prereq_charms.index(prereq_charm))
            if type(prereq_charms == bool):
                valid_charm = True
    charms.append(charm_choice)

# Character Concept & Caste

demo = ExaltedCharacter()
demo.roll_charms()