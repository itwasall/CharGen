import random

import char_dnd_5e_core as Core


class PartyMember:
    def __init__(
            self,
            name: str = None,
            race: Core.Race = None,
            subRace: Core.SubRace = None,
            _class: Core._Class = None,
            _subClass: Core._SubClass = None,
            STR: Core.STR = None,
            DEX: Core.DEX = None,
            CON: Core.CON = None,
            INT: Core.INT = None,
            WIS: Core.WIS = None,
            CHA: Core.CHA = None,
            athletics: Core.ATHLETICS= None,
            acrobatics: Core.ACROBATICS= None,
            sleight_of_Hand: Core.SLEIGHT_OF_HAND = None,
            stealth: Core.STEALTH = None,
            arcana: Core.ARCANA = None,
            history: Core.HISTORY = None,
            investigation: Core.INVESTIGATION = None,
            nature: Core.NATURE = None,
            religion: Core.RELIGION = None,
            animal_Handling: Core.ANIMAL_HANDLING = None,
            insight: Core.INSIGHT = None,
            medicine: Core.MEDICINE = None,
            perception: Core.PERCEPTION = None,
            survival: Core.SURVIVAL = None,
            deception: Core.DECEPTION = None,
            intimidation: Core.INTIMIDATION = None,
            performance: Core.PERFORMANCE = None,
            persuasion: Core.PERSUASION = None,
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
        return sum([random.randint(1, int(sides)) for _ in range(int(throws))])
    else:
        rolls = [random.randint(1, int(sides)) for _ in range(int(throws))]
        rolls.sort()
        return rolls

def gen_character():
    AbilityScore_Rolls = []
    for _ in range(6):
        rolls = dice_roll("4d6", summed=False)
        rolls.sort()
        rolls.reverse()
        rolls.pop()
        AbilityScore_Rolls.append(rolls)
    
    AbilityScore_Rolls.sort()
    CHAR_CLASS = random.choice(Core.CLASSES)
    print(CHAR_CLASS)
    CHAR_STR, CHAR_DEX, CHAR_CON, CHAR_INT, CHAR_WIS, CHAR_CHA = Core.STR, Core.DEX, Core.CON, Core.INT, Core.WIS, Core.CHA
    ABILITY_SCORES = [CHAR_STR, CHAR_DEX, CHAR_CON, CHAR_INT, CHAR_WIS, CHAR_CHA]
    CHAR_ABILITY_SCORES = []
    for abilityScore in ABILITY_SCORES:
        if abilityScore in CHAR_CLASS.saving_throws:
            ABILITY_SCORES.pop(ABILITY_SCORES.index(abilityScore))
            CHAR_ABILITY_SCORES.append(abilityScore)
    random.shuffle(CHAR_ABILITY_SCORES)
    random.shuffle(ABILITY_SCORES)
    for abilityScore in ABILITY_SCORES:
        CHAR_ABILITY_SCORES.append(abilityScore)
    for idx, value in enumerate(AbilityScore_Rolls):
        CHAR_ABILITY_SCORES[idx] = value

            
    print(CHAR_ABILITY_SCORES)

print(gen_character())