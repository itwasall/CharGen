from chargen import *
from typing import Tuple, List

class ExaltedAttributeClass(BaseAttributeClass):
    def __init__(self, name):
        super().__init__(name, 0, 0)

AttributeStrength = ExaltedAttributeClass('Strength')
AttributeDexterity = ExaltedAttributeClass('Dexterity')
AttributeStamina = ExaltedAttributeClass('Stamina')
AttributeCharisma = ExaltedAttributeClass('Charisma')
AttributeManipulation = ExaltedAttributeClass('Manipulation')
AttributeAppearance = ExaltedAttributeClass('Appearance')
AttributePerception = ExaltedAttributeClass('Perception')
AttributeIntelligence = ExaltedAttributeClass('Intelligence')
AttributeWits = ExaltedAttributeClass('Wits')

class ExaltedCasteClass:
    def __init__(self, name: str, abilities: List[str]):
        self.name = name
        self.abilities = abilities
    def __repr__(self):
        return self.name

CasteDawn = ExaltedCasteClass('Dawn', ['Archery', 'Awareness', 'Brawl/Martial Arts', 'Dodge', 'Melee', 'Resistance', 'Thrown', 'War'])
CasteZenith = ExaltedCasteClass('Zenith', ['Athletics', 'Integrity', 'Performance', 'Lore', 'Presense', 'Resistance', 'Survival', 'War'])
CasteTwilight = ExaltedCasteClass('Twilight', ['Bureaucracy', 'Craft', 'Integrity', 'Investigation', 'Linguistics', 'Lore', 'Medicine', 'Occult'])
CasteNight = ExaltedCasteClass('Night', ['Athletics', 'Awareness', 'Dodge', 'Investigation', 'Larceny', 'Ride', 'Stealth', 'Socialize'])
CasteEclipse = ExaltedCasteClass('Eclipse', ['Bureaucracy', 'Larceny', 'Linguistics', 'Occult', 'Presence', 'Ride', 'Sail', 'Socialize'])

class ExaltedSkillClass:
    def __init__(self, name: str, level: int = 0):
        self.name = name
        self.level = level
        self.is_favored: bool = False
        self.is_caste: bool = False
        self.is_supernal: bool = False
        self.is_specialty: bool = False
    def __repr__(self):
        return self.name
    def __add__(self, amt):
        self.level += amt
    def __iadd__(self, amt):
        self.__add__(amt)

class ExaltedCharmKeywordClass:
    def __init__(self, name: str, desc: str):
        self.name = name
        self.desc = desc

    def __repr__(self):
        return self.name

KeywordAggravated = ExaltedCharmKeywordClass("Aggravated", "The Health Track damage inflicted by this Charm cannot be healed magically, nor can magic be used to speed up the natural process of healing it.")
KeywordBridge = ExaltedCharmKeywordClass("Bridge",  "A Charm with this keyword can be purchased with alternate prerequisites from another Ability. If all the prerequisites used to buy a Bridge Charm enjoy a Caste/Favored cost discount, so does the Bridge Charm. No non-Integrity Charm can act as a prerequisite for more than one Bridge Charm, and Integrity Charms can never serve as an alternate Bridge prerequisite. If Integrity is Caste or Favored, the character may buy in via half the listed number of Bridge prerequisites (round up, or round down if Supernal).")
KeywordClash = ExaltedCharmKeywordClass("Clash", "Cannot be used simultaneously with or in response to a Charm with the Counterattack keyword.")
KeywordCounterattack = ExaltedCharmKeywordClass("Counterattack", "Cannot be used in reaction to a Charm with the Counterattack or Clash keyword")
KeywordDecisiveOnly = ExaltedCharmKeywordClass("Decisive-only", "If it’s an attack Charm, the Charm can only be used with a decisive attack. If it is a defensive Charm, it can only be used to defend against a decisive attack.")
KeywordDual = ExaltedCharmKeywordClass("Dual", "This Charm has two different functions, one for withering and one for decisive.")
KeywordMute = ExaltedCharmKeywordClass("Mute", "This Charm’s cost will not add to the Exalt’s anima level unless she wants it to.")
KeywordPilot = ExaltedCharmKeywordClass("Pilot" "The character must be the captain or the helmsman of the sailing vessel to use this Charm.")
KeywordPsyche = ExaltedCharmKeywordClass("Psyche", "A power with this keyword is an unnatural, hypnotic, or sorcerous power that magically influences, controls, or cripples an opponent’s thoughts or feelings.")
KeywordPerilous = ExaltedCharmKeywordClass("Perilous", "Be cautious about your reliance on this Charm! Charms with this keyword cannot be used in Initiative Crash.")
KeywordSalient = ExaltedCharmKeywordClass("Salient", "This keyword indicates that the Charm’s cost requires silver, gold, and white points for major, superior, and legendary craft projects, respectively.")
KeywordStackable = ExaltedCharmKeywordClass("Stackable", "This Charm’s effects can stack. • Uniform: This Charm has the same function for both withering and decisive attacks or defenses.")
KeywordWitheringOnly = ExaltedCharmKeywordClass("Withering-only", "If it’s an attack Charm, the Charm can only be used with a withering attack. If it is a defensive Charm, it can only be used to defend against a withering attack.")
KeywordWrittenOnly = ExaltedCharmKeywordClass("Written-only", "A Charm with this keyword can only be used to enhance, supplement, or create written social influence.")

CHARM_TYPES = ['Simple', 'Supplemental', 'Reflexive', 'Permanent']

class ExaltedCharmClass:
    def __init__(
        self,
        name: str,
        cost: str,
        mins: List[Tuple(str, int)],
        charm_type: str,
        keywords: ExaltedCharmKeywordClass,
        duration: str,
        prerequisite_charms: List,
        desc: str
    ):
        self.name = name
        self.cost = cost
        self.mins = mins
        if charm_type not in CHARM_TYPES:
            raise ValueError
        self.charm_type = charm_type
        self.keywords = keywords
        self.duration = duration
        self.prerequisite_charms = prerequisite_charms
        self.desc = desc

    def __repr__(self):
        return self.name

LIST_CASTE = [CasteDawn, CasteZenith, CasteTwilight, CasteNight, CasteEclipse]
LIST_ATTRIBUTE = [AttributeStrength, AttributeDexterity, AttributeStamina, AttributeCharisma, AttributeManipulation, AttributeAppearance, AttributePerception, AttributeWits]
LIST_CHARM_KEYWORDS = [KeywordAggravated, KeywordBridge, KeywordClash, KeywordCounterattack, KeywordDecisiveOnly, KeywordDual, KeywordMute, KeywordPilot, KeywordPsyche, KeywordPerilous, KeywordSalient, KeywordWitheringOnly, KeywordWrittenOnly]
