from random import choice

ABILITY_SCORES = {
        'STR': [],
        'DEX': [],
        'CON': [],
        'INT': [],
        'WIS': [],
        'CHA': []
}

RACES = ['Android', 'Human', 'Kasatha', 'Lashunta', 'Shirren', 'Vesk', 'Ysoki']
THEMES = ['Ace Pilot', 'Bounty Hunter', 'Icon', 'Mercenary', 'Outlaw', 'Priest', 'Scholar', 'Spacefarer', 'Xenoseeker', 'Themeless']
CLASSES = ['Envoy', 'Mechanic', 'Mystic', 'Operative', 'Solarian', 'Soldier', 'Technomancer']



def ab_score_mod(ab_scores):
    for ab in ab_scores.keys():
        print(ab_scores[ab])
        ab_scores[ab][1] = (ab_scores[ab][0] // 2 ) - 5
    return ab_scores

def generate_character():
    char = {}
    char['Ability Scores'] = ABILITY_SCORES
    for score in char['Ability Scores'].keys():
        char['Ability Scores'][score] = [10,0]
    char['Ability Scores'] = ab_score_mod(char['Ability Scores'])
    char['Race'] = choice(RACES)
    char['Theme'] = choice(THEMES)
    char['Class'] = choice(CLASSES)
    return char

char = generate_character()

print(char)

