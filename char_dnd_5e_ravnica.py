import random
import char_dnd_5e_core as Core

def dice_roll(dicestring):
    throws, sides = dicestring.split("d")
    return sum([random.randint(1, int(sides)) for _ in range(int(throws))])


class Guild:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self.name
DEFAULT_GUILD = Guild("Default Guild")


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

class AbilityScore:
    def __init__(self, name, value = 0):
        self.name = name
        self.value = value
        self.modifier = self.get_mod(value)

    def get_mod(self, value):
        if value == 1:
            return -5
        if (value + 1) % 2 == 0:
            value -= 1
        return int(value/2)-5

    def __repr__(self):
        return self.name

    def __add__(self, value):
        self.value += value
        return AbilityScore(self.name, self.value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __sub__(self, value):
        self.value -= value
        return AbilityScore(self.name, self.value)

    def __isub__(self, value):
        return self.__sub__(value)
DEFAULT_ABILITY_SCORE = AbilityScore("DEFAULT ABILITY_SCORE")

class Skill:
    def __init__(self, name, ab_score, prof, **kwargs):
        self.name = name
        self.ab_score = ab_score
        self.prof = prof
        for k, d in kwargs.items():
            self.__setattr__(k, d)

    def __repr__(self):
        return f"({self.ab_score}) {self.name}: +-{self.prof}"

"""
    ABILITY SCORES
"""
STR = AbilityScore("Strength")
DEX = AbilityScore("Dexterity")
CON = AbilityScore("Constitution")
INT = AbilityScore("Intelligence")
WIS = AbilityScore("Wisdom")
CHA = AbilityScore("Charisma")

STAT_BLOCK = {"STR": STR, "DEX": DEX, "CON": CON, "INT": INT, "WIS": WIS, "CHA": CHA}

"""
    SKILLS
"""
# ======= STR ======= 
ATHLETICS = Skill("Athletics", ab_score=STR, prof=0)
# ======= DEX ======= 
ACROBATICS = Skill("Acrobatics", ab_score=DEX, prof=0)
SLEIGHT_OF_HAND = Skill("Sleight_Of_Hand", ab_score=DEX, prof=0)
STEALTH = Skill("Stealth", ab_score=DEX, prof=0)
# ======= INT ======= 
ARCANA = Skill("Arcana", ab_score=INT, prof=0)
HISTORY = Skill("History", ab_score=INT, prof=0)
INVESTIGATION = Skill("Investigation", ab_score=INT, prof=0)
NATURE = Skill("Nature", ab_score=INT, prof=0)
RELIGION = Skill("Religion", ab_score=INT, prof=0)
# ======= WIS ======= 
ANIMAL_HANDLING = Skill("Animal_Handling", ab_score=WIS, prof=0)
INSIGHT = Skill("Insight", ab_score=WIS, prof=0)
MEDICINE = Skill("Medicine", ab_score=WIS, prof=0)
PERCEPTION = Skill("Perception", ab_score=WIS, prof=0)
SURVIVAL = Skill("Survival", ab_score=WIS, prof=0)
# ======= CHA ======= 
DECEPTION = Skill("Deception", ab_score=CHA, prof=0)
INTIMIDATION = Skill("Intimidation", ab_score=CHA, prof=0)
PERFORMANCE = Skill("Performance", ab_score=CHA, prof=0)
PERSUASION = Skill("Persuasion", ab_score=CHA, prof=0)

SKILLS = [ATHLETICS, ACROBATICS, SLEIGHT_OF_HAND, STEALTH, ARCANA, HISTORY, INVESTIGATION, NATURE, RELIGION, ANIMAL_HANDLING, INSIGHT, MEDICINE, PERCEPTION, SURVIVAL, DECEPTION, INTIMIDATION, PERFORMANCE, PERSUASION]

"""
    ALIGNMENT
"""
LAWFUL_GOOD = Core.Alignment("Lawful", "Good")
LAWFUL_NEUTRAL = Core.Alignment("Lawful", "Neutral")
LAWFUL_EVIL = Core.Alignment("Lawful", "Evil")
NEUTRAL_GOOD = Core.Alignment("Neutral", "Good")
NEUTRAL_EVIL = Core.Alignment("Neutral", "Evil")
NEUTRAL_NEUTRAL = Core.Alignment("Neutral", "Neutral")
CHAOTIC_GOOD = Core.Alignment("Chaotic", "Good")
CHAOTIC_NEUTRAL = Core.Alignment("Chaotic", "Neutral")
CHAOTIC_EVIL = Core.Alignment("Chaotic", "Evil")


"""
    GUILDS
"""
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



"""
    RACE CLASS CREATION STYLE GUIDE
    ab_score_bonus default
        [ (Ability_Score, Bonus), (Ability_Score, Bonus) ]
    ab_score_bonus choice
        [{
            "Choice": [Ability_Score_1, Ability_Score_2],
            "Amount": Bonus
        }, (Ability_Score, Bonus)]
    age
        [Lowest_Age, Highest Age]
    alignment default
        [Lawful/Chatoic/Neutral tendancy, Good/Evil/Neutral tendancy]
    alignment based on guild
        [
            {GUILD_1: Lawful/Chatoic/Neutral tendancy, GUILD_2: Lawful/Chaotic/Neutral tendandy},
            {GUILD_1: Good/Evil/Neutral tendancy, GUILD_3: Good/Evil/Neutral tendancy}
        ]
    alignment not x
        [(Lawful, Neutral) tendancy, (Good, Neutral) tendancy]
    size
        string
    speed
        int
    languages
        [Language_1, Language 2]
    languages, second is choice
        [Language_1, {'Choose': [ExLang_1, ExLang_2, ExLang_3]}]
"""

HUMAN = Core.Race("Human", ab_score_bonus=[(STR, 1), (DEX, 1), (CON, 1), (INT, 1), (WIS, 1), (CHA, 1)], age=[18,100], alignment=["None", "None"], size="Medium", speed=30, language=[COMMON, {'Choose': [ABYSSAL, CELESTIAL, DRACONIC, ELVISH, GIANT, GOBLIN_L, KRAUL, LOXODON_L, MERFOLK, MINOTAUR_L, SPHINX, SYLVAN, VEDALKEN_L]}]) 
ELF = Core.Race("Elf", ab_score_bonus=[(DEX, 2)], age=[100,750], alignment=["Chaos", "None"], size="Medium", speed=30, darkvision=60, language=[COMMON, ELVISH])
CENTAUR = Core.Race("Centaur", ab_score_bonus=[(STR, 2), (WIS, 1)], age=[18,100], alignment=["Neutral", "Neutral"], size="Medium", speed="40", language=[COMMON, SYLVAN])
GOBLIN = Core.Race("Goblin", ab_score_bonus=[(DEX, 2), (CON, 1)], age=[8, 60], alignment=["Chaotic","None"], size="Small", speed=30, darkvision=60, language=[COMMON, GOBLIN_L])
LOXODON = Core.Race("Loxodon", ab_score_bonus=[(CON, 2), (WIS, 1)], age=[20, 450], alignment=["Lawful","Good"], size="Medium", speed=30, language=[COMMON, LOXODON_L])
MINOTAUR = Core.Race("Minotaur", ab_score_bonus=[(STR, 2), (CON, 1)], age=[18,100], alignment=[{BOROS_LEGION: "Lawful", CULT_OF_RAKDOS: "Chatotic", GRUUL_CLANS:"Chatoic", DEFAULT_GUILD: "None"},""], size="", speed=0, language=[COMMON, MINOTAUR_L])
SIMIC_HYBRID = Core.Race("Simic_Hybrid", ab_score_bonus=[(CON, 2), {"Choice": [STR, DEX, INT, WIS, CHA], "Bonus": 1}], age=[1, 70], alignment=[{SIMIC_COMBINE: "Neutral", DEFAULT_GUILD: "None"}, {SIMIC_COMBINE: "Neutral", DEFAULT_GUILD: "None"}], size="Medium", speed=60, darkvision=60, language=[COMMON, {'Choose': [ELVISH, VEDALKEN_L]}])
VEDALKEN = Core.Race("Vedalken", ab_score_bonus=[(INT, 2), (WIS, 1)], age=[40, 350], alignment=["Lawful", ("Good", "Neutral")], size="Medium", speed=30, language=[COMMON, VEDALKEN_L, {'Choose': [ABYSSAL, CELESTIAL, DRACONIC, ELVISH, GIANT, GOBLIN_L, KRAUL, LOXODON_L, MERFOLK, MINOTAUR_L, SPHINX, SYLVAN]}])

BARBARIAN = Core.BARBARIAN
BARD = Core.BARD
CLERIC = Core.CLERIC
DRUID = Core.DRUID
FIGHTER = Core.FIGHTER
MONK = Core.MONK
PALADIN = Core.PALADIN
RANGER = Core.RANGER
ROGUE = Core.ROGUE
SORCERER = Core.SORCERER
WARLOCK = Core.WARLOCK
WIZARD = Core.WIZARD

GUILDS = [AZORIUS_SENATE, BOROS_LEGION, CULT_OF_RAKDOS, GOLGARI_SWARM, GRUUL_CLANS, HOUSE_DIMIR, IZZIT_LEAGUE, ORZHOV_SYNDICATE, SELESNYA_CONCLAVE, SIMIC_COMBINE]

class PartyMember:
    def __init__(
            self, 
            name = "", 
            guild = DEFAULT_GUILD,
            _class = DEFAULT_CLASS, 
            race = DEFAULT_RACE,
            alignment = DEFAULT_ALIGNMENT,
            stats = STAT_BLOCK,
            skills  = SKILLS,
            **kwargs,
        ):
        """ Character Overview """
        self.name = name
        self.alignment = alignment
        self.guild = guild
        self._class = _class
        self.race = race
        """ Cool Numbers """
        self.level = 1
        self.stats = stats
        self.age = random.randint(self.race.age[0], self.race.age[1])
        """ Height/ Weight """
        self.height = ""
        # Required for calculating weight as well
        self.height_modifier = 0
        self.weight = ""
        """ Languages & Skills """
        self.languages = []
        self.athletics = SKILLS[0]
        self.acrobatics = SKILLS[1] 
        self.sleight_of_hand = SKILLS[2]
        self.stealth = SKILLS[3]
        self.arcana = SKILLS[4]
        self.history = SKILLS[5]
        self.investigation = SKILLS[6]
        self.nature = SKILLS[7]
        self.religion = SKILLS[8]
        self.animal_handling = SKILLS[9]
        self.insight = SKILLS[10]
        self.medicine = SKILLS[11]
        self.perception = SKILLS[12]
        self.survival = SKILLS[13]
        self.deception = SKILLS[14]
        self.intimidation = SKILLS[15]
        self.performance = SKILLS[16]
        self.persuasion = SKILLS[17]

        for k, d in kwargs.items():
            self.__setattr__(k, d)

    def gen_height(self, base_height, dicestring):
        base_feet, base_inches = base_height.split("'")
        base_feet, base_inches = int(base_feet), int(base_inches)
        self.height_modifier = dice_roll(dicestring) 
        base_inches += self.height_modifier
        while base_inches >= 12:
            base_feet += 1
            base_inches -= 12
        return f"{base_feet}'{base_inches}\""
    
    def gen_weight(self, base_weight, dicestring):
        if self.height == "":
            raise ValueError("Please roll height first to get height mod")
        base_weight = int(base_weight)
        modifier = dice_roll(dicestring)
        return f"{base_weight + self.height_modifier * modifier}lbs"

    def set_ab_values(self, ab_values = [15,14,13,12,10,8]):
        random.shuffle(ab_values)
        for idx, stat in enumerate(self.stats.keys()):
            self.stats[stat] += ab_values[idx]
        print([{k:d.value} for k, d in self.stats.items()])


    def speaks(self):
        if isinstance(self.race.language) == list:
            for idx, lang in enumerate(self.race.language):
                if isinstance(lang) == dict and "Choose" in lang.keys():
                    self.languages.append(random.choice(lang["Choose"]))
                elif isinstance(lang) == Language:
                    self.languages.append(lang)
                else:
                    continue
                if idx == 0:
                    self.native_lang = lang
        elif isinstance(self.race.language) == Language:
            self.languages = [self.race.language]
            self.shitty_monolingual_cunt = True
        else:
            raise TypeError("I need a list of Language class items or a single Language class item. Daft cunt")

class Party:
    def __init__(self, name, party_comp, **kwargs):
        self.name = name
        self.party_comp = party_comp
        for k, d in kwargs.items():
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

def gen_extra_traits(partymember: PartyMember):
    match partymember.race.name:
        case "Centaur":
            partymember.race.extra_traits = {
                    'Fey': 'Your creature type is fey, rather than humanoid',
                    'Charge': 'If you move at least 30 feet straight toward a target and then hit it with a melee weapon attack on the same turn, you can immediately follow that attack with a bonus action, making one attack against the target with your hooves',
                    'Hooves': 'Your hooves are natural melee weapons, which you can use to make unarmed strikes. If you hit with them, you deal bludgeoning damage equal to 1d4 + your STR modifier, instead of the bludgeoning damage normal of an unarmed strike.',
                    'Equine Build': 'You count as one size larger when determining your carrying capacity and the weight you can push or drag. In addition, any climb that requires hands and feet is especially difficult for you because of your equine legs. When you make such a climb, each foot of movement costs 4 extra feet, instead of the 1 extra foot.',
                    }
            # race.proficiencies = 
        case "Minotaur":
            partymember.race.extra_traits = {
                'Horns': 'Your horns are natural melee weapons, which you can use to make unarmd stirkes. Ifyou hit with them, you deal piercing damage sequal to 1d6 + your STR modifier, instead of the bludgeoning damage normal for an unarmed strike',
                'Goring Rush': 'Immediately after you use the Dash action on your turn and move at least 20 feet you can make one melee attack with your horns as a bonus action',
                'Hammering Horns': 'Immediately after you hit a creature with a melee attack as parto fhte Attack action on your turn, you can use a bonus action to attempt to shove that target with your horns. The tartget must be no more than one size larger than you and within 5 feet of you. Unless it succeeds on a Strength saving throw against a DC equal to 8 + your proficiency bonus + your STR modifier, you push it up to 10 feet away from you.',
                'Imposing Presence': 'You have proficiencies in one of the following skills of your choice: Intimidation or Persuasion'
            }
            imposing_presence_roll = random.choice(['Intimidation', 'Persuasion'])
            if imposing_presence_roll == 'Intimidation':
                pass




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

def gen_character():
    guilds = GUILDS
    classes = [BARD, BARBARIAN, CLERIC, DRUID, FIGHTER, MONK, PALADIN, RANGER, ROGUE, SORCERER, WARLOCK, WIZARD]
    races = [HUMAN, ELF, CENTAUR, GOBLIN, LOXODON, MINOTAUR, SIMIC_HYBRID, VEDALKEN]
    NEW_CHARACTER = PartyMember(name="Jeff", guild=random.choice(guilds), _class=random.choice(classes), race=random.choice(races))
    return NEW_CHARACTER

def create_character():
    my_nu_leng = gen_character()
    my_nu_leng.set_ab_values()
    print("Name: ", my_nu_leng.name)
    print("Class: ", my_nu_leng._class.name)
    print("Race: ", my_nu_leng.race.name)
    print("Guild: ", my_nu_leng.guild.name)
    print("Age: ", my_nu_leng.age)
    print(my_nu_leng.acrobatics)

create_character()
print(CHAOTIC_GOOD)
print(NEUTRAL_NEUTRAL)
