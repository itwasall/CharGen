import random
import char_dnd_5e_core as Core

def dice_roll(dicestring):
    throws, sides = dicestring.split("d")
    return sum([random.randint(1, int(sides)) for _ in range(int(throws))])


class Guild:
    def __init__(self, name, classes: list, subclasses: list, races: list, alignment: list, **kwargs):
        self.name = name
        self.classes = classes
        self.subclasses = subclasses
        self.races = races
        """
            Alignments are shown in the book as, for example, "Usually Good, Often Lawful"
            This will be split up into a four part list: ['Usually', 'Good', 'Often', 'Lawful'], then
            properly assembled in the list below to give:
                self.alignment = [('Usually', 'Good'), ('Often', 'Lawful')]
            This structure was chosen because it doesn't matter which order the items are in on a tuple level, it does
            matter which order the items are in from the list level. As both Good/Evil & Chaotic/Lawful dichotomys have
            a "neutral" option, it should be clear which of the two any given "netural" is referring to, with only so much
            as its position on the list to indicate it's value
        """
        self.alignment = [ (alignment[0], alignment[1]), (alignment[2], alignment[3]) ]
        for k, d in kwargs.items():
            self.__setattr(k, d)
    
    def __repr__(self):
        return self.name
DEFAULT_GUILD = Guild("Default Guild")


DEFAULT_ABILITY_SCORE = Core.AbilityScore("DEFAULT ABILITY_SCORE")

# ABILITY SCORES
STR = Core.STR
DEX = Core.DEX
CON = Core.CON
INT = Core.INT
WIS = Core.WIS
CHA = Core.CHA
STAT_BLOCK = Core.STAT_BLOCK
# SKILLS
SKILLS = [
    # STR
    Core.ATHLETICS,
    # DEX
    Core.ACROBATICS, Core.SLEIGHT_OF_HAND, Core.STEALTH,
    # INT 
    Core.ARCANA, Core.HISTORY, Core.INVESTIGATION, Core.NATURE, Core.RELIGION, 
    # WIS
    Core.ANIMAL_HANDLING, Core.INSIGHT, Core.MEDICINE, Core.PERCEPTION, Core.SURVIVAL,
    # CHA
    Core.DECEPTION, Core.INTIMIDATION, Core.PERFORMANCE, Core.PERSUASION
]
# ALIGNMENT
LAWFUL_GOOD = Core.Alignment("Lawful", "Good")
LAWFUL_NEUTRAL = Core.Alignment("Lawful", "Neutral")
LAWFUL_EVIL = Core.Alignment("Lawful", "Evil")
NEUTRAL_GOOD = Core.Alignment("Neutral", "Good")
NEUTRAL_EVIL = Core.Alignment("Neutral", "Evil")
NEUTRAL_NEUTRAL = Core.Alignment("Neutral", "Neutral")
CHAOTIC_GOOD = Core.Alignment("Chaotic", "Good")
CHAOTIC_NEUTRAL = Core.Alignment("Chaotic", "Neutral")
CHAOTIC_EVIL = Core.Alignment("Chaotic", "Evil")
# CLASS
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
# GUILDS
AZORIUS_SENATE = Guild("Azorius Senate", classes=[BARD, CLERIC, FIGHTER, PALADIN, WIZARD], subclasses=[])
BOROS_LEGION = Guild("Boros Legion", classes=[CLERIC, FIGHTER, PALADIN, RANGER, WIZARD], subclasses=[])
CULT_OF_RAKDOS = Guild("Cult of Rakdos", classes=[BARBARIAN, BARD, FIGHTER, WARLOCK], subclasses=[])
GOLGARI_SWARM = Guild("Golgari Swarm", classes=[DRUID, FIGHTER, RANGER, ROGUE, WIZARD], subclasses=[])
GRUUL_CLANS = Guild("Gruul Clans", classes=[BARBARIAN, CLERIC, DRUID, FIGHTER, RANGER], subclasses=[])
HOUSE_DIMIR = Guild("House Dimir", classes=[MONK, ROGUE, WIZARD], subclasses=[])
IZZIT_LEAGUE = Guild("Izzit League", classes=[FIGHTER, SORCERER, WIZARD], subclasses=[])
ORZHOV_SYNDICATE = Guild("Orzhov Syndicate", classes=[CLERIC, FIGHTER, ROGUE, WIZARD], subclasses=[])
SIMIC_COMBINE = Guild("Simic Combine", classes=[DRUID, FIGHTER, MONK, WIZARD], subclasses=[])
SELESNYA_CONCLAVE = Guild("Selesnya Conclave", classes=[BARD, CLERIC, DRUID, FIGHTER, MONK, PALADIN, RANGER, WARLOCK], subclasses=[])
GUILDS = [AZORIUS_SENATE, BOROS_LEGION, CULT_OF_RAKDOS, GOLGARI_SWARM, GRUUL_CLANS, HOUSE_DIMIR, IZZIT_LEAGUE, ORZHOV_SYNDICATE, SELESNYA_CONCLAVE, SIMIC_COMBINE]
# LANGUAGES
ABYSSAL = Core.Language("Abyssal", speakers=["Demons", "Devils"], script="Infernal")
CELESTIAL = Core.Language("Celestial", speakers="Angels", script="Celestial")
COMMON = Core.Language("Common", speakers="Humans", script="Common")
DRACONIC = Core.Language("Draconic", speakers="Dragons", script="Draconic")
ELVISH = Core.Language("Elvish", speakers="Elves", script="Elvish")
GIANT = Core.Language("Giant", speakers=["Ogres", "Giants"], script="Minotaur")
GOBLIN_L = Core.Language("Goblin", speakers="Goblins", script="Common")
KRAUL = Core.Language("Kraul", speakers="Kraul", script="Kraul")
LOXODON_L = Core.Language("Loxodon", speakers="Loxodons", script="Elvish")
MERFOLK = Core.Language("Merfolk", speakers="Merfolk", script="Merfolk")
MINOTAUR_L = Core.Language("Minotaur", speakers="Minotaurs", script="Minotaur")
SPHINX = Core.Language("Sphinx", speakers="Sphinxes", script="-")
SYLVAN = Core.Language("Sylvan", speakers=["Centaurs", "Dryads"], script="Elvish")
VEDALKEN_L = Core.Language("Vedalken", speakers="Vedalken", script="Vedalken")

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
        [Language_1, {'Choose 1': [ExLang_1, ExLang_2, ExLang_3]}]
"""
HUMAN = Core.Race("Human", ab_score_bonus=[(STR, 1), (DEX, 1), (CON, 1), (INT, 1), (WIS, 1), (CHA, 1)], age=[18,100], alignment=["None", "None"], size="Medium", speed=30, language=[COMMON, {'Choose 1': [ABYSSAL, CELESTIAL, DRACONIC, ELVISH, GIANT, GOBLIN_L, KRAUL, LOXODON_L, MERFOLK, MINOTAUR_L, SPHINX, SYLVAN, VEDALKEN_L]}]) 
ELF = Core.Race("Elf", ab_score_bonus=[(DEX, 2)], age=[100,750], alignment=["Chaos", "None"], size="Medium", speed=30, darkvision=60, language=[COMMON, ELVISH])
CENTAUR = Core.Race("Centaur", ab_score_bonus=[(STR, 2), (WIS, 1)], age=[18,100], alignment=["Neutral", "Neutral"], size="Medium", speed="40", language=[COMMON, SYLVAN])
GOBLIN = Core.Race("Goblin", ab_score_bonus=[(DEX, 2), (CON, 1)], age=[8, 60], alignment=["Chaotic","None"], size="Small", speed=30, darkvision=60, language=[COMMON, GOBLIN_L])
LOXODON = Core.Race("Loxodon", ab_score_bonus=[(CON, 2), (WIS, 1)], age=[20, 450], alignment=["Lawful","Good"], size="Medium", speed=30, language=[COMMON, LOXODON_L])
MINOTAUR = Core.Race("Minotaur", ab_score_bonus=[(STR, 2), (CON, 1)], age=[18,100], alignment=[{BOROS_LEGION: "Lawful", CULT_OF_RAKDOS: "Chatotic", GRUUL_CLANS:"Chatoic", DEFAULT_GUILD: "None"},""], size="", speed=0, language=[COMMON, MINOTAUR_L])
SIMIC_HYBRID = Core.Race("Simic_Hybrid", ab_score_bonus=[(CON, 2), {"Choose 1": [STR, DEX, INT, WIS, CHA], "Bonus": 1}], age=[1, 70], alignment=[{SIMIC_COMBINE: "Neutral", DEFAULT_GUILD: "None"}, {SIMIC_COMBINE: "Neutral", DEFAULT_GUILD: "None"}], size="Medium", speed=60, darkvision=60, language=[COMMON, {'Choose 1': [ELVISH, VEDALKEN_L]}])
VEDALKEN = Core.Race("Vedalken", ab_score_bonus=[(INT, 2), (WIS, 1)], age=[40, 350], alignment=["Lawful", ("Good", "Neutral")], size="Medium", speed=30, language=[COMMON, VEDALKEN_L, {'Choose 1': [ABYSSAL, CELESTIAL, DRACONIC, ELVISH, GIANT, GOBLIN_L, KRAUL, LOXODON_L, MERFOLK, MINOTAUR_L, SPHINX, SYLVAN]}])

class PartyMember:
    def __init__(
            self, 
            name = "", 
            guild = DEFAULT_GUILD,
            _class = Core.DEFAULT_CLASS, 
            race = Core.DEFAULT_RACE,
            alignment = Core.DEFAULT_ALIGNMENT,
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
        self.athletics = skills[0]
        self.acrobatics = skills[1] 
        self.sleight_of_hand = skills[2]
        self.stealth = skills[3]
        self.arcana = skills[4]
        self.history = skills[5]
        self.investigation = skills[6]
        self.nature = skills[7]
        self.religion = skills[8]
        self.animal_handling = skills[9]
        self.insight = skills[10]
        self.medicine = skills[11]
        self.perception = skills[12]
        self.survival = skills[13]
        self.deception = skills[14]
        self.intimidation = skills[15]
        self.performance = skills[16]
        self.persuasion = skills[17]
        """ Calculatables """
        self.ac = 0
        self.hit_die = ""
        self.hit_points = 0
        self.current_hit_points = 0

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
                if isinstance(lang) == dict and "Choose 1" in lang.keys():
                    self.languages.append(random.choice(lang["Choose 1"]))
                elif isinstance(lang) == Core.Language:
                    self.languages.append(lang)
                else:
                    continue
                if idx == 0:
                    self.native_lang = lang
        elif isinstance(self.race.language) == Core.Language:
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
            party_guild = random.choice(GUILDS)
            return Party("One Guild Party", gen_one_guild_party_makeup(party_guild))
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
            return Party("Ordinary", party_members)
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

def gen_extra_traits(Character: PartyMember):
    match Character.race.name:
        case "Centaur":
            survivor_roll = random.choice(['Animal Handling', 'Medicine', 'Nature', 'Survival'])
            match survivor_roll:
                case 'Animal Handling':
                    Character.animal_handling.set_proficiency_bonus(Character.level)
                case 'Medicine':
                    Character.medicine.set_proficiency_bonus(Character.level)
                case 'Nature':
                    Character.nature.set_proficiency_bonus(Character.level)
                case 'Survival':
                    Character.survival.set_proficiency_bonus(Character.level)
            Character.extra_traits = {
                'Fey': 'Your creature type is fey, rather than humanoid',
                'Charge': 'If you move at least 30 feet straight toward a target and then hit it with a melee weapon attack on the same turn, you can immediately follow that attack with a bonus action, making one attack against the target with your hooves',
                'Hooves': 'Your hooves are natural melee weapons, which you can use to make unarmed strikes. If you hit with them, you deal bludgeoning damage equal to 1d4 + your STR modifier, instead of the bludgeoning damage normal of an unarmed strike.',
                'Equine Build': 'You count as one size larger when determining your carrying capacity and the weight you can push or drag. In addition, any climb that requires hands and feet is especially difficult for you because of your equine legs. When you make such a climb, each foot of movement costs 4 extra feet, instead of the 1 extra foot.',
                'Survivor': f"You have proficiency in one of the following skills of your choice: Animal Handling, Medicine, Nature or Survival. DEBUG: {survivor_roll} was chosen"
            }
        case "Goblin":
            Character.extra_traits = {
                'Fury of the Small': "When you damage a creature with an attack or spell and the creature's size is greater than yours, you can cause the attack or spell to deal extra damage to the creature. The extra damage equals your level. This can only be used once per short rest",
                'Nimble Escape': "You can take a Disengage or Hide action as a bonus action on each of your turns"
            }
        case "Loxodon":
            Character.extra_traits = {
                'Powerful Build': "You count as one size larger when determing your carrying capacity and the weight you can push or drag",
                'Loxodon Serenity': "You have advantage on saving throws against being charmed or frightened",
                'Natural Armor': "You have thick, leathery skin. When you aren't wearing any armour, your AC is 12 + your CON modifier. You can use your natural armor to determine your AC if the armor you wear would leave you with a lower AC. A shield's benefits apply as normal when you are using your natural armor.",
                'Trunk': "You can grasp things with your trunk, and you can use it as a snorkel. It has a reach of 5 feet, and it can lift a number of pounds equal to five times your STR score. You can use it to do the following simple tasks: lift, drop, hold, push or pull an object or creature; open or close a door or container; grapple someone; or make an unarmed strike. Your trunk can't wield weapons or shields or do anything that requires manual prescision, such as using tools or magic items or performing the somantic components of a spell.",
                'Keen Smell': "Thanks to your sensitive trunk, you have advantage on Wisdom (Perception), Wisdom (Survival), and Intelligence (Investigation) checks with an involve smell"
            }
        case "Minotaur":
            imposing_presence_roll = random.choice(['Intimidation', 'Persuasion'])
            if imposing_presence_roll == 'Intimidation':
                Character.intimidation.set_proficiency_bonus(Character.level)
            elif imposing_presence_roll == 'Persuasion':
                Character.persuasion.set_proficiency_bonus(Character.level)
            Character.extra_traits = {
                'Horns': 'Your horns are natural melee weapons, which you can use to make unarmd stirkes. Ifyou hit with them, you deal piercing damage sequal to 1d6 + your STR modifier, instead of the bludgeoning damage normal for an unarmed strike',
                'Goring Rush': 'Immediately after you use the Dash action on your turn and move at least 20 feet you can make one melee attack with your horns as a bonus action',
                'Hammering Horns': 'Immediately after you hit a creature with a melee attack as parto fhte Attack action on your turn, you can use a bonus action to attempt to shove that target with your horns. The tartget must be no more than one size larger than you and within 5 feet of you. Unless it succeeds on a Strength saving throw against a DC equal to 8 + your proficiency bonus + your STR modifier, you push it up to 10 feet away from you.',
                'Imposing Presence': f'You have proficiencies in one of the following skills of your choice: Intimidation or Persuasion. DEBUG: {imposing_presence_roll} was chosen'
            }
        case "Simic Hybrid":
            animal_enhancement_first_roll = random.choice(['Manta Glide', 'Nimble Climber', 'Underwater Adaption'])
            animal_enhancement_fifth_roll = random.choice(['Grappling Appendages', 'Carapace', 'Acid Spit'])
            match animal_enhancement_first_roll:
                case 'Manta Glide':
                    first_animal_en_key, first_animal_en_value = {'Manta Glide', "You have ray-like fins that you can use as wings to slow your fall or allow you to glide. When you fall and aren't incapacitated, you can subtract up to 100 feet from the fall when calculating falling damage, and you can move up to 2 feet horizontally for every 1 foot you descend"}
                case 'Nimble Climber':
                    first_animal_en_key, first_animal_en_value= {'Nimble Climber': "You have a climbing speed equal to your walking speed."}
                case 'Underwater Adaptation':
                    first_animal_en_key, first_animal_en_value= {'Underwater Adaptation': "You can breathe air and water, and you have a swimming speed equal to your walking speed"}
            match animal_enhancement_fifth_roll:
                case 'Grappling Appendages':
                    fifth_animal_en_key, fifth_animal_en_value = {'Grappling Appendages': "You have two special appendages growing alongside your arms. Choose whether they're both claws or tentacles. As an action, you can use one of them to try to grapple a creature. Each one is also a natural weapon, which you can use to make an unarmed strike. Ifyou hit with it, the target takes bludgeoning damage equal to 1d6 + your STR modifier, instead of the bludgeoning damage normal for an unarmed strike. Immediately after hitting, you can try to grapple the target as a bonus action. These appendages can't precisely manipulate anything and can't wield weapons, magic items, or other specialised equipment."}
                case 'Carapace':
                    fifth_animal_en_key, fifth_animal_en_value = {'Carapace': "Your skin in places is covered by a thick shell. You gain +1 bonus to AC when you're not wearing heavy armor"}
                case 'Acid Spit':
                    fifth_animal_en_key, fifth_animal_en_value = {'Acid Spit': "As an action, you can spracy acid from glands in your mouth, targeting one creature or object you can see within 30 feet of you. The targettakes 2d10 acid damage unless it succeeds on a DEX saving throw against a DC equal to 8 + your CON modifier + your proficiency bonus. This damage increases by 1d10 when you reach 11th level (3d10) and 17th level (4d10). You can use this trait a number of times equal to your CON modifier (minimum of once), and you regain all expended uses of it when you finish a long rest."}
            if Character.level >= 5:
                Character.extra_traits = {
                'Animal Enhancement': f"Your body has been altered to incorporate certain animal characteristics. You choose one animal enhancement now and a second enhancement at 5th level. DEBUG: {animal_enhancement_first_roll} & {animal_enhancement_fifth_roll} was chosen",
                first_animal_en_key: first_animal_en_value,
                fifth_animal_en_key: fifth_animal_en_value
                }
            else:
                Character.extra_traits = {
                'Animal Enhancement': f"Your body has been altered to incorporate certain animal characteristics. You choose one animal enhancement now and a second enhancement at 5th level. DEBUG: {animal_enhancement_first_roll} was chosen",
                first_animal_en_key: first_animal_en_value,
                }
        case "Vedalken":
            tireless_precision_roll = random.choice(['Arcana', 'History', 'Investigation', 'Medicine', 'Performance', 'Sleight of Hand'])
            match tireless_precision_roll:
                case 'Arcana':
                    Character.arcana.set_proficiency_bonus(Character.level)
                case 'History':
                    Character.history.set_proficiency_bonus(Character.level)
                case 'Investigation':
                    Character.investigation.set_proficiency_bonus(Character.level)
                case 'Medicine':
                    Character.medicine.set_proficiency_bonus(Character.level)
                case 'Performance':
                    Character.performance.set_proficiency_bonus(Character.level)
                case 'Sleight of Hand':
                    Character.sleight_of_hand.set_proficiency_bonus(Character.level)
            Character.extra_traits = {
                'Vedalken Dispassion': "You have advantage on all Intelligence, Wisdom and Charisma saving throws.",
                'Tireless Precision': f"You are proficient in one of the following skills: Arcana, History, Investigation, Medicine, Performance, or Sleight of Hand. You are also proficient with one tool of your choice. Whenever you make an ability check with the chosen skill or tool, roll 1d4 and add the number rolled to the check's total. DEBUG: {tireless_precision_roll} was chosen.",
                'Partially Amphibious': "By absorbing oxygen through your skin, you can breathe underwater for up to 1 hour. Once you've reached that limit, you can't use this trait again until you finish a long rest"
            }

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
