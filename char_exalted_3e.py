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


# Character Concept & Caste
print(choice(data.LIST_CASTE))
print(list(data.LIST_ATTRIBUTE))