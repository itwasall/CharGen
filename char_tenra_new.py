class ABC:
    def __init__(self, name, **kwargs):
        self.name = name
        for k, d in kwargs.items():
            self.__setattr__(k, d)

    def __repr__(self):
        return self.__format__()

    def __format__(self):
        return self.name

class Skill(ABC):
    items = []
    def __init__(self, name, property, **kwargs):
        self.property = property
        super().__init__(name, **kwargs)
        Skill.items.append(self)

class Attribute(ABC):
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)

AGILITY = Attribute("Agility")
BODY = Attribute("Body")
SENSES = Attribute("Senses")
KNOWLEDGE = Attribute("Knowledge")
SPIRIT = Attribute("Spirit")
EMPATHY = Attribute("Empathy")
STATION = Attribute("Station")

UNARMED_COMBAT = Skill("Unarmed_Combat", property='General', primary=BODY, attributes=[BODY, SENSES, KNOWLEDGE, SPIRIT, STATION])
WORMCHARM = Skill("Wormcharm", property='Specialist', primary=BODY, attributes=[BODY, AGILITY, SENSES, KNOWLEDGE, EMPATHY, STATION])
MOVEMENT = Skill("Movement", property='General', primary=AGILITY, attributes=[BODY, AGILITY, STATION])
MELEE_WEAPONS = Skill("Melee_Weapons", property='General', primary=AGILITY, attributes=[AGILITY, SENSES, KNOWLEDGE, SPIRIT, STATION])
EVASION = Skill("Evasion", property='General', primary=AGILITY, attributes=[AGILITY, SPIRIT, STATION])
STEALTH = Skill("Stealth", property='General', primary=AGILITY, attributes=[AGILITY, SENSES, SPIRIT])
NINJUTSU = Skill("Ninjutsu", property='Elite', primary=AGILITY, attributes=[AGILITY])
CRIMINAL_ARTS = Skill("Criminal_Arts", property='Specialist', primary=AGILITY, attributes=[AGILITY, SENSES, KNOWLEDGE, SPIRIT, EMPATHY, STATION])
FIRST_AID = Skill("First_Aid", property='General', primary=SENSES, attributes=[SENSES, KNOWLEDGE])
NOTICE = Skill("Notice", property='General', primary=SENSES, attributes=[SENSES, SPIRIT])
MARKSMAN = Skill("Marksman", property='General', primary=SENSES, attributes=[SENSES, KNOWLEDGE, SPIRIT])
FORGERY = Skill("Forgery", property='Specialist', primary=SENSES, attributes=[AGILITY, SENSES, KNOWLEDGE, EMPATHY, STATION])
INFORMATION = Skill("Information", property='General', primary=KNOWLEDGE, attributes=[KNOWLEDGE, STATION])
ONMYOJUTSU = Skill("Onmyojutsu", property='Specialist', primary=KNOWLEDGE, attributes=[KNOWLEDGE, STATION])
ART_OF_WAR = Skill("Art_of_War", property='Specialist', primary=KNOWLEDGE, attributes=[KNOWLEDGE])
WILLPOWER = Skill("Willpower", property='General', primary=SPIRIT, attributes=[BODY, SENSES, KNOWLEDGE, SPIRIT, EMPATHY, STATION])
RESONANCE = Skill("Resonance", property='Elite', primary=SPIRIT, attributes=[BODY, SPIRIT, EMPATHY, STATION])
INTERFACE = Skill("Interface", property='Elite', primary=SPIRIT, attributes=[SPIRIT])
BUDDHIST_MAGIC = Skill("Buddhist_Magic", property='Specialist', primary=SPIRIT, attributes=[SPIRIT])
PERSUASION = Skill("Persuasion", property='General', primary=EMPATHY, attributes=[BODY, AGILITY, SENSES, KNOWLEDGE, SPIRIT, EMPATHY, STATION])
PILLOW_ARTS = Skill("Pillow_Arts", property='General', primary=EMPATHY, attributes=[SENSES, KNOWLEDGE, SPIRIT, EMPATHY, STATION])
PERFORM = Skill("Perform", property='Specialist', primary=EMPATHY, attributes=[BODY, AGILITY, SENSES, KNOWLEDGE, EMPATHY, STATION])
ETIQUETTE = Skill("Etiquette", property='Specialist', primary=STATION, attributes=[AGILITY, SENSES, KNOWLEDGE, EMPATHY, STATION])
SHINTO = Skill("Shinto", property='Specialist', primary=STATION, attributes=[STATION])
ART_OF_RULE = Skill("Art_of_Rule", property='Elite', primary=STATION, attributes=[STATION, KNOWLEDGE, EMPATHY, STATION])
STRATEGY = Skill("Strategy", property='Specialist', primary=STATION, attributes=[KNOWLEDGE, EMPATHY, STATION])

SKILLS_GENERAL = [skill for skill in Skill.items if skill.property == 'General']
SKILLS_SPECIALIST = [skill for skill in Skill.items if skill.property == 'Specialist']
SKILLS_ELITE = [skill for skill in Skill.items if skill.property == 'Elite']
