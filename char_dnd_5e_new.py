import random

from char_dnd_5e_core import *

class PartyMember:
    def __init__(
            self,
            name: str = None,
            race: Race = None,
            subRace: SubRace = None,
            _class: _Class = None,
            _subClass: _SubClass = None,
            STR: STR = None,
            DEX: DEX = None,
            CON: CON = None,
            INT: INT = None,
            WIS: WIS = None,
            CHA: CHA = None,
            athletics: ATHLETICS= None,
            acrobatics: ACROBATICS= None,
            sleight_of_Hand: SLEIGHT_OF_HAND = None,
            stealth: STEALTH = None,
            arcana: ARCANA = None,
            history: HISTORY = None,
            investigation: INVESTIGATION = None,
            nature: NATURE = None,
            religion: RELIGION = None,
            animal_Handling: ANIMAL_HANDLING = None,
            insight: INSIGHT = None,
            medicine: MEDICINE = None,
            perception: PERCEPTION = None,
            survival: SURVIVAL = None,
            deception: DECEPTION = None,
            intimidation: INTIMIDATION = None,
            performance: PERFORMANCE = None,
            persuasion: PERSUASION = None,
            money = None,
            languages = None,
            weapon_Proficiences = None,
            armor_Proficiences = None,
            tool_Proficiences = None,
            equipment = None,
            **kwargs
            ):
        """ Macro Character Stuff """
        self.name = name
        self.race = race
        self.subrace = subRace
        self._class = _class
        self._subclass = _subClass
        self.languages = languages
        """ Ability Scores """
        self.STR = STR
        self.DEX = DEX
        self.CON = CON
        self.INT = INT
        self.WIS = WIS
        self.CHA = CHA
        """ Skills """
        # STR
        self.athletics = athletics
        # DEX
        self.acrobatics = acrobatics
        self.sleight_of_hand = sleight_of_Hand
        self.stealth = stealth
        # INT
        self.arcana = arcana
        self.history = history
        self.investigation = investigation
        self.nature = nature
        self.religion = religion
        # WIS
        self.animal_handling = animal_Handling
        self.insight = insight
        self.medicine = medicine
        self.perception = perception
        self.survival = survival
        # CHA
        self.deception = deception
        self.intimidation = intimidation
        self.performance = performance
        self.persuasion = persuasion
        """ Equipment & Proficiencies """
        self.weapon_proficiences = weapon_Proficiences
        self.armor_proficiences = armor_Proficiences
        self.tool_proficiences = tool_Proficiences
        """ Combat Stats """
        self.AC = 0
        self.initiative = 0
        self.speed = 0
        self.hit_points = 0
        self.current_hit_points = 0
        """ Possessions """
        self.money = money
        self.equipment = equipment


        for k, d in kwargs.items():
            self.__setattr__(k, d)
    
    def __repr__(self):
        return self.__format__()

    def __format__(self):
        return self.name

def dice_roll(dicestring, summed=True):
    throws, sides = dicestring.split("d")
    if summed:
        return sum([random.randint(int(sides)) for _ in range(int(throws))])
    else:
        return [random.randint(int(sides)) for _ in range(int(throws))]

def gen_character():
    CHOSEN_RACE = random.choice(RACES)
    potential_subraces = [subrace for subrace in SUBRACES if subrace.parent_race == chosen_race]
    if len(potential_subraces) != 0:
        CHOSEN_SUBRACE = random.choice(potential_subraces)
    else:
        CHOSEN_SUBRACE = None
    CHOSEN_CLASS = random.choice(CLASSES)

    EQUIPMENT = GenerateEquipment(CHOSEN_CLASS.equipment)
    if isinstance(CHOSEN_CLASS.equipment_pack, dict):
        EQUIPMENT += random.choice(CHOSEN_CLASS.equipment_pack['Choose 1'])
    else:
        EQUIPMENT += CHOSEN_CLASS.equipment_pack




    

