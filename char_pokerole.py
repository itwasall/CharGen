from typing import List
from random import choice, choices
from yaml import safe_load

rank_data = safe_load(open('pokerole_data/rank.yml', 'rt'))
age_data = safe_load(open('pokerole_data/ages.yml', 'rt'))

class Character:
    def __init__(self, name):
        self.name = name
        # Starter, Beginner, Amateur, Ace, Professional
        self.rank = None
        # Kid, Teen (Default), Adult, Senior
        self.age = None
        # Strength, Vitality, Dexterity, Insight
        self.attributes = {
            'Strength': 1, 'Vitality': 1, 'Dexterity': 1, 'Insight': 1
        }
        # Tough, Beauty, Cool, Cute, Clever
        self.social_attributes = {
            'Tough': 1, 'Beauty': 1, 'Cool': 1, 'Cute': 1, 'Clever': 1
        }
        # The skills that are in the game.
        self.skills = {
            'Brawl': {'value': 0, 'type': 'Fight'},
            'Throw': {'value': 0, 'type': 'Fight'},
            'Weapons': {'value': 0, 'type': 'Fight'},
            'Evasion': {'value': 0, 'type': 'Fight'},
            'Alert': {'value': 0, 'type': 'Survival'},
            'Athletic': {'value': 0, 'type': 'Survival'},
            'Nature': {'value': 0, 'type': 'Survival'},
            'Stealth': {'value': 0, 'type': 'Survival'},
            'Allure': {'value': 0, 'type': 'Social'},
            'Etiquette': {'value': 0, 'type': 'Social'},
            'Intimidate': {'value': 0, 'type': 'Social'},
            'Perform': {'value': 0, 'type': 'Social'},
            'Crafts': {'value': 0, 'type': 'Knowledge'},
            'Lore': {'value': 0, 'type': 'Knowledge'},
            'Medicine': {'value': 0, 'type': 'Knowledge'},
            'Science': {'value': 0, 'type': 'Knowledge'},
        }
        # Always 150,000
        self.money = 150_000
        self.nature = None
        self.confidence = None
        # Initial max HP is equal to Vitality
        self.current_hp = None
        self.max_hp = None
        # Initial Will is equal to (Insight + 2)
        self.will = None
        # Can carry up to 6 of the critters with you at once. Just there names here.
        self.pokemon = []
        # Potions can be used a number of times. The 'Remaining' value refers only
        #   to the most recently used potion
        self.backpack = {
            'Potions': {'Owned': 0, 'Remaining': 0}, # Potion max 2
            'Super Potions': {'Owned': 0, 'Remaining': 0}, # Super Potion max 4
            'Hyper Potions': {'Owned': 0, 'Remaining': 0}, # Hyper Potion max 14
            'Small Pocket': List, # Items in the small pocket can be used in battle
            'Main Pocket': List, # All other items go here
            'Gym Badge Case': dict # {Gym Name: 0/1}
        }

    def character_info(self):
        print(f"Name: {self.name} | Age: {self.age} | Rank: {self.rank}")
        print(f"Nature: {self.nature} | Confidence: {self.confidence}")
        print(f"Attributes: {list((k, v) for k,v in self.attributes.items())}")
        print(f"Will: {self.will} | HP: {self.current_hp}")
        print(f"Social Attributes: {list((k, v) for k,v in self.social_attributes.items())}")
        print(f"Skills:\n{list((k, v['value']) for k, v in self.skills.items())}")
        print(f"Starter Pokemon: {self.pokemon}")


class Pokemon:
    def __init__(self, name):
        self.name = name
        self.nickname = None
        self.dex_number = 0
        # Size is [Feet, Inches], Weight is lbs
        self.size = [0, 0]
        self.weight = 0
        self.type = None
        # Pokemon attributes, on top of having the 'Special' attribute PC's don't,
        #   also have a max value that attribute can be raised to. PC's technically
        #   have this as well, but all PC's stats can be raised up to 5, whereas a
        #   Pokemon's base + potential max stat vary by attribute by pokemon
        self.attributes = {
            'Strength': [0, 0],
            'Dexterity': [0, 0],
            'Vitality': [0, 0],
            'Special': [0, 0],
            'Insight': [0, 0]
        }
        self.social_attributes = {
            'Tough': 1, 'Beauty': 1, 'Cool': 1, 'Cute': 1, 'Clever': 1
        }
        self.suggested_rank = None
        self.base_hp = 0
        self.hp = 0 # base hp as in pokedex + 1 for each vitality
        self.will = 0 # Insight + 2
        self.held_item = "None"
        self.status = "Healthy"
        self.initiative = 0 # Dexterity + Alert
        self.accuracy = 0
        self.damage = 0
        self.evasion = 0
        self.clash = 0
        self.defences = [0, 0] # [DEF, SDEF] == [VITALITY, INSIGHT]
        self.moves = [
            {'name': None, 'power': None, 'dice_pool': 0 },
            {'name': None, 'power': None, 'dice_pool': 0 },
            {'name': None, 'power': None, 'dice_pool': 0 },
            {'name': None, 'power': None, 'dice_pool': 0 },
        ]
        self.skills = {
            'Brawl': {'value': 0, 'type': 'Fight'},
            'Channel': {'value': 0, 'type': 'Fight'},
            'Clash': {'value': 0, 'type': 'Fight'},
            'Evasion': {'value': 0, 'type': 'Fight'},
            'Alert': {'value': 0, 'type': 'Survival'},
            'Athletic': {'value': 0, 'type': 'Survival'},
            'Nature': {'value': 0, 'type': 'Survival'},
            'Stealth': {'value': 0, 'type': 'Survival'},
            'Allure': {'value': 0, 'type': 'Contest'},
            'Etiquette': {'value': 0, 'type': 'Contest'},
            'Intimidate': {'value': 0, 'type': 'Contest'},
            'Perform': {'value': 0, 'type': 'Contest'},
        }
        self.nature = None
        self.confidence = 0


class Rank:
    def __init__(self, name, data):
        self.name = name
        self.skill_points = data['skill_points']
        self.skill_limit = data['skill_limit']
        self.extra_benefits = data['extra_benefits']
        self.max_targets = data['max_targets']
        self.next_rank_reqs = data['next_rank_reqs']

    def __repr__(self):
        return self.name

RANKS = {
    # Rank : Statistical Weight
    'Starter': 50,
    'Beginner': 30,
    'Amateur': 10,
    'Ace': 5,
    'Pro': 3,
    'Master': 1,
    'Champion': 1
}

AGES = {
    # Age : Statistical Weight (for randomisation lmao)
    'Kid': 20,
    'Teen': 50,
    'Adult': 25,
    'Senior': 5
}

NATURES = {
    # Nature : Confidence
    'Adamant': 4, 'Bashful': 6,
    'Bold': 9,    'Brave': 9,
    'Calm': 8,    'Careful': 5,
    'Docile': 7,  'Gentle': 10,
    'Hardy': 9,   'Hasty': 7,
    'Impish': 7,  'Jolly': 10,
    'Lax': 8,     'Lonely': 5,
    'Mild': 8,    'Modest': 10,
    'Naive': 7,   'Naughty': 6,
    'Quiet': 5,   'Quirky': 9,
    'Rash': 6,    'Relaxed': 8,
    'Sassy': 7,   'Serious': 4,
    'Timid': 4
}

POTENTIAL_STARTERS = [
    # Gen 8 + Some regionals
    'Cufant', 'Snom', 'Milcery', 'Yamask', 'Darumaka', 'Meowth', 'Zigzagoon',
    'Impidimp', 'Hatenna', 'Sinistea', 'Clobbopus', 'Sizzlipede', 'Toxel', 'Arrokuda',
    'Silicobra', 'Applin', 'Rolycoly', 'Yamper', 'Chewtle', 'Wooloo', 'Gossifleur',
    'Nickit', 'Blipbug', 'Rookidee', 'Skwovet', 'Sobble', 'Scorbunny', 'Grookey',
    # Gen 7
    'Jangmo-o', 'Sandygast', 'Wimpod', 'Bounsweet', 'Stufful', 'Salandit', 'Morelull',
    'Fomantis', 'Dewpider', 'Mudbury', 'Mareanie', 'Rockruff', 'Cutiefly', 'Crabbrawler',
    'Grubbin', 'Yungoos', 'Pikipek', 'Popplio', 'Litten', 'Rowlet',
    # Gen 6
    'Noibat', 'Bergmite', 'Pumpkaboo', 'Phantump', 'Goomy', 'Helioptile', 'Clauncher',
    'Skrelp', 'Binacle', 'Inkay', 'Swirlix', 'Spritzee', 'Honedge', 'Espurr', 'Pancham',
    'Skiddo', 'Flabebe', 'Litleo', 'Spewpa', 'Scatterbug', 'Fletchling', 'Bunnelby',
    'Froakie', 'Fennekin', 'Chespin',
    # Gen 5
    'Larvesta', 'Deino', 'Vullaby', 'Rufflet', 'Pawniard', 'Golett', 'Mienfoo', 'Shelmet',
    'Cubchoo', 'Axew', 'Litwick', 'Elgyem', 'Tynamo', 'Ferroseed', 'Joltik', 'Frillish',
    'Foongus', 'Karrablast', 'Deerling', 'Vanillite', 'Ducklett', 'Solosis', 'Gothita',
    'Minccino', 'Zorua', 'Trubbish', 'Scraggy', 'Dwebble', 'Sandile', 'Petilil', 'Cottenee',
    'Venipede', 'Swadloon', 'Sewaddle', 'Tympole', 'Timburr', 'Drilbur', 'Woobat', 'Roggenrola',
    'Blitzle', 'Pidove', 'Munna', 'Panpour', 'Pansear', 'Pansage', 'Purrloin', 'Lilipup',
    'Patrat', 'Oshawott', 'Tepig', 'Snivy',
    # Gen 4
    'Snover', 'Mantyke', 'Finneon', 'Croagunk', 'Skorupi', 'Hippopotas', 'Riolu', 'Munchlax',
    'Gible', 'Happiny', 'Mime Jr.', 'Bonsly', 'Bronzor', 'Stunky', 'Chingling', 'Glameow',
    'Buneary', 'Drifloon', 'Shellos', 'Cherubi', 'Buizel', 'Combee', 'Burmy', 'Budew',
    'Shinx', 'Kricketot', 'Bidoof', 'Starly', 'Piplup', 'Chimchar', 'Turtwig',
    # Gen 3
    'Beldum', 'Bagon', 'Clamperl', 'Spheal', 'Snorunt', 'Wynaut', 'Chimecho', 'Duskull',
    'Shuppet', 'Feebas', 'Baltoy', 'Corphish', 'Barboach', 'Swablu', 'Cacnea', 'Trapinch',
    'Spoink', 'Numel', 'Wailmer', 'Carvanha', 'Gulpin', 'Roselia', 'Electrike', 'Meditite',
    'Aron', 'Skitty', 'Nosepass', 'Azurill', 'Makuhita', 'Whismur', 'Nincada', 'Slakoth',
    'Shroomish', 'Surskit', 'Ralts', 'Wingull', 'Tailow', 'Seedot', 'Lotad', 'Cascoon',
    'Silicoon', 'Wurmple', 'Poochyena', 'Mudkip', 'Torchic', 'Treecko',
    # Gen 2
    'Larvitar', 'Magby', 'Elekid', 'Smoochum', 'Tyrogue', 'Phanpy', 'Houndour', 'Remoraid',
    'Swinub', 'Slugma', 'Teddiursa', 'Sneasel', 'Snubbull', 'Gligar', 'Pineco',
    'Misdreavus', 'Murkrow', 'Wooper', 'Yanma', 'Sunkern', 'Aipom', 'Hoppip', 'Marill',
    'Mareep', 'Natu', 'Togepi', 'Igglybuff', 'Cleffa', 'Pichu', 'Chinchou', 'Spinarak',
    'Ledyba', 'Hoothoot', 'Sentret', 'Totodile', 'Cyndaquil', 'Chikorita',
    # Gen 1
    'Dratini', 'Porygon', 'Eevee', 'Magikarp', 'Scyther', 'Staryu', 'Goldeen', 'Horsea',
    'Tangela', 'Chansey', 'Rhyhorn', 'Koffing', 'Lickitung', 'Cubone', 'Exeggcute',
    'Voltorb', 'Krabby', 'Drowzee', 'Gastly', 'Shellder', 'Grimer', 'Seel', 'Doduo',
    'Magnemite', 'Slowpoke', 'Ponyta', 'Geodude', 'Tentacool', 'Bellsprout', 'Machop',
    'Abra', 'Poliwag', 'Growlithe', 'Mankey', 'Psyduck', 'Diglett', 'Paras', 'Oddish',
    'Zubat', 'Jigglypuff', 'Vulpix', 'Clefairy', 'Nidoran', 'Sandshrew', 'Pikachu',
    'Ekans', 'Spearow', 'Rattata', 'Pidgey', 'Kakuna', 'Weedle', 'Metapod', 'Caterpie',
    'Squirtle', 'Charmander', 'Bulbasaur'
]
# I couldn't be bothered to write out all the stuff that's already been
#   spelled out in the class definition so fuck it, here's a dummy class
#   I can use to make list comprehensions out of.
d = Character("fuck oop")

ATTRIBUTES = [a for a in d.attributes]
SOCIAL_ATTRIBUTES = [s for s in d.social_attributes]
SKILLS = [skill for skill in d.skills]

def gen_character():
    """
    <summary>
    Stylistic Guide:
    gen_x = lambda function that generates sub component 'x'
    _y = variable of name 'y' used to assit in character generation

    Generates character by generating each sub component.
    Rank - Can be any of the ranks in the corebook, with
        weights to make lower ranks more probable.
    </summary>
    """
    _attribute_points, _social_attribute_points = 0, 0
    _skill_points, _skill_limit = 0, 0
    Char = Character('Jerry')
    # Just a way to declutter a choices call with a dictionary as an argument
    gen_chooser = lambda _dict: choices(list(_dict), list(_dict.values()))[0]

    # Generating a characters rank
    gen_rank = lambda _rankname: Rank(_rankname, rank_data[_rankname])
    Char.rank = gen_rank(gen_chooser(RANKS))

    _rank = rank_data[Char.rank.name]
    _attribute_points += _rank['core_attribute_points']
    _social_attribute_points += _rank['social_attribute_points']
    _skill_limit = _rank['skill_limit']
    _skill_points += _rank['skill_points']

    # Generating a characters age
    Char.age = gen_chooser(AGES)

    _age = age_data[Char.age]
    _attribute_points += _age['bonus_attribute']
    _social_attribute_points += _age['bonus_social']

    # Generating attributes & social attributes
    for _ in range(_attribute_points):
        Char.attributes[choice(ATTRIBUTES)] += 1
    for _ in range(_social_attribute_points):
        Char.social_attributes[choice(SOCIAL_ATTRIBUTES)] += 1

    # Generating skills
    #   The logic below adds 1 to a random skill, checks if that skill
    #   is now above the skill limit, reversing the change if it is and
    #   continuing, otherwise the remaining skill points is subtracted by 1
    #   until all skill points are spent
    while _skill_points > 0:
        _skill = choice(SKILLS)
        Char.skills[_skill]['value'] += 1
        if Char.skills[_skill]['value'] > _skill_limit:
            Char.skills[_skill]['value'] -= 1
            continue
        else:
            _skill_points -= 1

    # Calculate other values
    Char.current_hp = 4 + Char.attributes['Vitality']
    Char.max_hp = Char.current_hp
    Char.will = 2 + Char.attributes['Insight']

    # Generate nature + confidence
    Char.nature = choice(list(NATURES.keys()))
    Char.confidence = NATURES[Char.nature]

    # Get Starter pokemon
    Char.pokemon.append(choice(POTENTIAL_STARTERS))
    return Char


x = gen_character()
x.character_info()
