import random

def dice_roll(dicestring):
    throws, sides = dicestring.split("d")
    return sum([random.randint(1, int(sides)) for _ in range(int(throws))])


class Guild:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self.name
DEFAULT_GUILD = Guild("Default Guild")

class _Class:
    def __init__(self, name, **kwargs):
        self.name = name
        for k, d in self.kwargs.items():
            self.__setattr__(k, d)
DEFAULT_CLASS = _Class("Default Class")

class Race:
    def __init__(self, name, **kwargs):
        self.name = name
        for k, d in self.kwargs.items():
            self.__setattr__(k, d)
DEFAULT_RACE = Race("Default Race")

class Alignment:
    def __init__(self, law_chaos, good_evil):
        self.law_chaos = law_chaos 
        self.good_evil = good_evil
    def __repr__(self):
        return f"{self.law_chaos} {self.good_evil}"
DEFAULT_ALIGNMENT = Alignment("DEFAULT", "ALIGNMENT")

class Language:
    def __init__(self, name, speakers: None, script: None):
        self.name = name
        if type(speakers) == str:
            self.speakers = [speakers]
        elif type(speakers) != list:
            raise TypeError
        self.speakers = speakers
        self.script = script
    def __repr__(self):
        return self.name
DEFAULT_LANGUAGE = Language("DEFAULT LANGUAGE", "DEFAULT SPEAKERS", "DEFAULT SCRIPT")

class Attribute:
    # Fuck you I don't care if this looks awful
    modifier_table = {
            1: -5, 2: -4, 3: -4, 4: -3, 5: -3, 6: -2, 7: -2, 8: -1, 9: -1, 10: 0, 11: 0, 12: 1, 13: 1, 14: 2, 15: 2,
            16: 3, 17: 3, 18: 4, 19: 4, 20: 5, 21: 5, 22: 6, 23: 6, 24: 7, 25: 7, 26: 8, 27: 8, 28: 9, 29: 9, 30: 10
            }
    def __init__(self, name, value = 0):
        self.name = name
        self.value = value
        self.modifier = modifier_table[value]

    def __add__(self, value):
        self.value += value
        return Attribute(self.name, self.value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __sub__(self, value):
        self.value -= value
        return Attribute(self.name, self.value)

    def __isub__(self, value):
        return self.__sub__(value)

DEFAULT_ATTRIBUTE = Attribute("DEFAULT ATTRIBUTE")

STR = Attribute("Strength")
DEX = Attribute("Dexterity")
CON = Attribute("Constitution")
INT = Attribute("Intelligence")
WIS = Attribute("Wisdom")
CHA = Attribute("Charisma")

class Attribute_Block:
    def __init__(self):
        self.attributes = [STR, DEX, CON, INT, WIS, CHA]

class PartyMember:
    def __init__(
            self, 
            name = "", 
            guild = DEFAULT_GUILD,
            _class = DEFAULT_CLASS, 
            race = DEFAULT_RACE,
            alignment = DEFAULT_ALIGNMENT,
            stats = None,
        ):
        self.name = name
        self.guild = guild
        self.level = 1
        self.stats = stats
        self._class = _class
        self.age = 0
        self.alignment = alignment
        for k, d in self.kwargs.items():
            self.__setattr__(k, d)

HUMAN = Race("Human")
ELF = Race("Elf")
CENTAUR = Race("Centaur")
GOBLIN = Race("Goblin")
SIMIC_HYBRID = Race("Simic_Hybrid")
LOXODON = Race("Loxodon")
MINOTAUR = Race("Minotaur")
VEDALKEN = Race("Vedalken")

BARBARIAN = _Class("Barbarian")
BARD = _Class("Bard")
CLERIC = _Class("Cleric")
DRUID = _Class("Druid")
FIGHTER = _Class("Fighter")
MONK = _Class("Monk")
PALADIN = _Class("Paladin")
RANGER = _Class("Ranger")
ROGUE = _Class("Rogue")
SORCERER = _Class("Sorcerer")
WARLOCK = _Class("Warlock")
WIZARD = _Class("Wizard")

AZORIUS_SENATE = Guild("Azorius Senate")
HOUSE_DIMIR = Guild("House Dimir")
SIMIC_COMBINE = Guild("Simic Combine")
IZZIT_LEAGUE = Guild("Izzit League")
SELESNYA_CONCLAVE = Guild("Selesnya Conclave")
GOLGARI_SWARM = Guild("Golgari Swarm")
GRUUL_CLANS = Guild("Gruul Clans")
CULT_OF_RAKDOS = Guild("Cult of Rakdos")
BOROS_LEGION = Guild("Boros Legion")
ORZHOV_SYNDICATE = Guild("Orzhov Syndicate")

GUILDS = [AZORIUS_SENATE, BOROS_LEGION, CULT_OF_RAKDOS, GOLGARI_SWARM, GRUUL_CLANS, HOUSE_DIMIR, IZZIT_LEAGUE, ORZHOV_SYNDICATE, SELESNYA_CONCLAVE, SIMIC_COMBINE]

class Party:
    def __init__(self, name, party_comp, **kawrgs):
        self.name = name
        self.party_comp = party_comp
        for k, d in self.kwargs.items():
            self.__setattr__(k, d)


def gen_party_makeup(party_name = "Default"):
    roll = dice_roll("1d8")
    match roll:
        case 1:
            template = "One-Guild Party"
            party_guild = random.choice(GUILDS)
            party_makeup = Party(party_name, gen_one_guild_party_makeup(party_guild))
        case 2:
            party_members = [
                random.choice([
                    PartyMember(guild=BOROS_LEGION, _class=CLERIC),
                    PartyMember(guild=SELESNYA_CONCLAVE, _class=CLERIC)
                ]),
                random.choice([
                    PartyMember(guild=BOROS_LEGION, _class=FIGHTER),
                    PartyMember(guild=AZORIUS_SENATE, _class=FIGHTER)
                ]),
                random.choice([
                    PartyMember(guild=HOUSE_DIMIR, _class=ROGUE),
                    PartyMember(guild=GOLGARI_SWARM, _class=ROGUE)
                ]),
                random.choice([
                    PartyMember(guild=BOROS_LEGION, _class=WIZARD),
                    PartyMember(guild=IZZIT_LEAGUE, _class=WIZARD)
                ]),
            ]
        case 3:
            party_members = [
                PartyMember(guild=BOROS_LEGION, _class=CLERIC),
                PartyMember(guild=BOROS_LEGION, _class=RANGER),
                PartyMember(guild=AZORIUS_SENATE, _class=FIGHTER),
                PartyMember(guild=AZORIUS_SENATE, _class=WIZARD),
            ]
            return Party("Law and Order", party_members)
        case 4:
            party_members = [
                PartyMember(guild=SIMIC_COMBINE, _class=DRUID),
                PartyMember(guild=SIMIC_COMBINE, _class=MONK),
                PartyMember(guild=IZZIT_LEAGUE, _class=FIGHTER),
                PartyMember(guild=IZZIT_LEAGUE, _class=WIZARD),
            ]
            return Party("Mad Science", party_members)
        case 5:
            party_members = [
                PartyMember(guild=GOLGARI_SWARM, _class=DRUID),
                random.choice([
                    PartyMember(guild=GOLGARI_SWARM, _class=FIGHTER),
                    PartyMember(guild=GOLGARI_SWARM, _class=RANGER)
                ]),
                random.choice([
                    PartyMember(guild=HOUSE_DIMIR, _class=ROGUE),
                    PartyMember(guild=HOUSE_DIMIR, _class=MONK)
                ]),
                PartyMember(guild=HOUSE_DIMIR, _class=WIZARD),
            ]
            return Party("Skulkers", party_members)
        case 6:
            party_members = [
                PartyMember(guild=GRUUL_CLANS, _class=DRUID),
                PartyMember(guild=GRUUL_CLANS, _class=BARBARIAN),
                PartyMember(guild=CULT_OF_RAKDOS, _class=WARLOCK),
                PartyMember(guild=CULT_OF_RAKDOS, _class=ROGUE),
            ]
            return Party("Chaos", party_members)
        case 7:
            party_members = [
                PartyMember(guild=SELESNYA_CONCLAVE, _class=DRUID),
                PartyMember(guild=GRUUL_CLANS, _class=BARBARIAN),
                random.choice([
                    PartyMember(guild=SIMIC_COMBINE, _class=WIZARD),
                    PartyMember(guild=SELESNYA_CONCLAVE, _class=BARD)
                ]),
                PartyMember(guild=GOLGARI_SWARM, _class=ROGUE),
            ]
            return Party("Nature", party_members)
        case 8:
            party_members = [
                PartyMember(guild=SELESNYA_CONCLAVE, _class=CLERIC),
                PartyMember(guild=BOROS_LEGION, _class=PALADIN),
                PartyMember(guild=AZORIUS_SENATE, _class=WIZARD),
                PartyMember(guild=SELESNYA_CONCLAVE, _class=BARD),
            ]
            return Party("Benevolent", party_members)

def gen_common_cause():
    match dice_roll("1d8"):
        case 1:
            prison = random.choice(["an Azorius prison", "a Gruul camp", "a Rakados cage"])
            return ["Cellmates", f"The characters are prisoners in {prison}"]
        case 2:
            return ["Greater Threat", "The characters are fighting each other when a rampaging wurm attacks"]
        case 3:
            trapped = random.choice(["a sinkhole opening", "a building collapsing", "a laboratory exploding"])
            return ["Sudden Danger", f"The characters are trapped together by {trapped}"]
        case 4:
            return ["Dream Team", "A strange dream lands each character to the same destination"]
        case 5:
            return ["Lost Together", "The characters are hopelessly lose in an unfamiliar part of the city"]
        case 6:
            return ["Detente", "By order of their guilds' leaders, the characters must cooperate to complete a secret mission"]
        case 7:
            return ["Common Foe", "A villain is a common enemy to all the characters"]
        case 8:
            return ["Do or Die", "The characters are all trying to avert the catastrophe of an all-out war amoung the guilds"]




def gen_one_guild_party_makeup(guild: Guild):
    match guild.name:
        case "Azorius Senate":
            print("Azorius Senate")
            pass
        case "Boros Legion":
            print("Boros Legion")
            pass
        case "Cult of Rakdos":
            print("Cult of Rakdos")
            pass
        case "Golgari Swarm":
            print("Golgari Swarm")
            pass 
        case "Gruul Clans":
            print("Gruul Clans")
            pass
        case "House Dimir":
            print("House Dimir")
            pass
        case "Izzit League":
            print("Izzit League")
            pass
        case "Orzhov Syndicate":
            print("Orzhov Syndicate")
            pass
        case "Selesnya Conclave":
            print("Selesnya Conclave")
            pass
        case "Simic Combine":
            print("Simic Combine")
            pass
        case _:
            print(f"{guild.name} is wrong")
            pass
