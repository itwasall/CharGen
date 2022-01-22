import parts, random
from chargen import roll


class Kijin:
    def __init__(self,
                 name: str = None,
                 attribute_budget: int = None
                 ):
        self.name = name
        self.mechanica = {
            'Sensor': None,
            'Torso': None,
            'Arm': None,
            'Leg': None,
            'Other': None
        }
        self.mechanica_slots = {
            'Name': None
        }
        self.attribute_budget = attribute_budget
        self.total_attribute_penalty = 0
        self.notice_bonus = 0


def generate_kijin(name: str):
    """

    Args:
        name:

    Returns:

    """
    budget_roll = roll("1d10")

    kijin = Kijin(name, budget_roll)

    number_of_parts = random.choices([1, 2, 3], weights=[10, 7, 3])[0]

    for i in range(number_of_parts):
        parts.part_chooser(kijin)

    return kijin

