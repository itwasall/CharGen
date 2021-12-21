import random
import click

npc_app_jewel = ["bracelet", "amulet", "pinky finger ring", "earrings"]
npc_app_pierce = ["Lip", "Ear", "Nose", "Cheek", "Eyebrow", "Forehead"]
npc_app_scar = ["Cheek", "Lip", "Eye", "Chest", "Arm", "Neck"]
npc_app_tattoo = ["Arm", "Hand", "Neck", "Chest", "Face", "Forehead", "Back", "Leg"]
npc_app_skincolour = ["amber", "silver", "reddish brown", "blue", "jet black", "lime"]
npc_app_posture = ["crooked", "wunched", "rigid", "limp", "relaxed"]
npc_app_missing = ["left eye", "right eye", "teeth", "fingers"]

def npc_appearance_gen():
    npc_appearance = [
            f"Distinctive {random.choice(npc_app_jewel)}", f"{random.choice(npc_app_pierce)} piercings", f"Pronounced scar on {random.choice(npc_app_scar)}", f"{random.choice(npc_app_tattoo)} tattoo", f"{random.choice(npc_app_tattoo)} birthmark", f"Unusual {random.choice(npc_app_skincolour)} skin color", f"Unusual {random.choice(npc_app_skincolour)} hair color", f"Distinctive {random.choice(npc_app_posture)} posture", f"Missing {random.choice(npc_app_missing)}", "Flamboyant or outlandish clothes", "Formal clean clothes", "Ragged dirty clothes", "Unusual or split eye color/s", "Bald", "Distinctive nose", "Exceptionally beautiful", "Exceptionally ugly"]
    return npc_appearance

npc_abilities = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

npc_talents_puzzles = ["sudoku", "crossword", "cypher", "riddle"]
npc_talents_musical = ["lute", "handdrum", "harmonica", "steel pan drum", "ucordian", "flute"]
npc_talents_languages = ["Dwarvish", "Elvish", "Giant", "Gnomish", "Goblin", "Halfling", "Ogre"]
npc_talents_elanguages = ["Abyssal", "Celestial", "Deep Speech", "Draconic", "Infernal", "Primordial", "Sylvan", "Undercommon"]
npc_talents_arts = ["Draws", "Paints", "Sings"]
npc_talents_expertise = ["carpenter", "cook", "dart thrower", "juggler", "blacksmith", "scholar"]
npc_talents_great = ["with children", "with animals", "at poker", "at backgammon", "at cards", "at impersonations", "at poetry"]

def npc_talent_gen():
            # This bastard of a list comprehension nestled in an f string executes the following logic: Select a random(1,3) number of languages from the languages list
    npc_talents = [f"Plays the {random.choice(list(npc_talents_musical))}", f"Speaks several languages: {', '.join([random.choice(npc_talents_languages) for y in range(random.randint(2,4))])}", f"Great at solving {random.choice(list(npc_talents_puzzles))} puzzles", f"{random.choice(npc_talents_arts)} beautifully", f"Expert {random.choice(npc_talents_expertise)}", f"Great {random.choice(npc_talents_great)}", f"Skilled speaker of the {random.choice(npc_talents_elanguages)} tongue", "Unbelievably lucky", "Perfect memory", "Drinks everyone under the table", "Skilled actor and master of disguise", "Skilled dancer"]
    return npc_talents

npc_mannerism_freq_nickname = ["nyaa", "desu", "bear", "beefcake", "boss", "buddy", "bucko", "buttercup", "brainiac", "chickpea", "cookie", "cupcake", "dearie", "dog", "dumpling", "genius", "kid", "kiddo", "lamb", "muscles", "olddog", "pal", "popstar", " shmoopy", " shorty", " skippy", "sweetie", "youngin"]
npc_mannerism_freq = ["uses the wrong word", "uses inappropriate language", "asks cryptic riddes", f"ends each sentence with {random.choice(npc_mannerism_freq_nickname)}", "tells jokes or puns", "tells of the end of the world", "slurs words", "whistles to themself"]
npc_mannerism_voice = ["high", "low", "deep", "raspy", "quiet", "loud"]
npc_mannerism_bodylang = ["figet", "squint", "stare into the distance", "tap their fingers", "bite their fingernails", "twirl their hair"]

def npc_mannerism_gen():
    npc_mannerism = [
            f"Frequently {random.choice(npc_mannerism_freq)}", f"Particularly {random.choice(npc_mannerism_voice)} voice", f"Tends to {random.choice(npc_mannerism_bodylang)} a lot"]
    return npc_mannerism

npc_interaction_trait = ["Argumentative", "Arrogant", "Blustering", "Rude", "Curious", "Friendly", "Honest", "Hot-tempered", "Irritable", "Ponderous", "Quiet", "Suspicious"]

npc_alignment = [["Lawful", "Neutral", "Chaotic"], ["Good", "Neutral", "Evil"]]

npc_bonds = ["Dedicated to fulfilling a personal life goal", "Protective of close family members",  "Protective of colleagues or compatriots ", "Loyal to a benefactor, patron, or employer",  "Captivated by a romantic interest",  "Drawn to a special place",  "Protective of a sentimental keepsake",  "Protective of a valuable possession",  "Out for revenge"]

npc_flaw_phobia = ["the outdoors", "the indoors", "arachnids", "insects", "the dark", "the light", "butterflies", "love"]

npc_flaw_secret = ["Forbidden love or susceptibility to romance", "Enjoys decadent pleasures",  "Arrogance", "Envies another creature's possessions or station",  "Overpowering greed", "Prone to rage", "Has a powerful enemy",  f"Phobia of {random.choice(npc_flaw_phobia)}", "Shameful or scandalous history",  "Secret crime or misdeed",  "Possession of forbidden lore",  "Fool hardy bravery"]

def get_flaw():
    return random.choice(list(npc_flaw_secret))

def get_bonds():
    return random.choice(list(npc_bonds))

def get_mannerism(n=1):
    mannerisms = []
    for i in range(n):
        m = random.choice(list(npc_mannerism_gen()))
        while m[:14] in (x[:14] for x in mannerisms):
            m = random.choice(list(npc_mannerism_gen()))
        mannerisms.append(m)
    try:
        mannerisms[1]
        mannerisms.sort()
        return mannerisms
    except IndexError:
        mannerisms = mannerisms[0]
        return mannerisms

def get_interaction():
    return random.choice(list(npc_interaction_trait))

def get_talents(n=1):
    talents = []
    for i in range(n):
        t = random.choice(list(npc_talent_gen()))
        # Checks the first 24 characters of each item in talents.
        #   Specifically to stop the repeated use of the "Speaks several languages" option
        while t[:24] in (x[:24] for x in talents):
            t = random.choice(list(npc_talent_gen()))
        talents.append(t)
    try:
        talents[1]
        talents.sort()
        return talents
    except IndexError:
        talents = talents[0]
        return talents


def get_alignment():
    a1 = random.choice(list(npc_alignment[0]))
    a2 = random.choice(list(npc_alignment[1]))
    if a1 == a2:
        return "True Neutral"
    else:
        return f"{a1} {a2}"

def get_apperance(ap):
    appearance = random.choice(list(npc_appearance_gen()))
    return appearance

def get_high_low_ability(npc):
    low_stat = random.choice(list(npc))
    high_stat = low_stat
    while high_stat == low_stat:
        high_stat = random.choice(list(npc))
    return low_stat, high_stat

@click.command()
#@click.argument('name', default='Default Name')
@click.option('-n','--name', default='Default Name', help='Name of NPC')
@click.option('-t','--talents', default=1, help='Number of talents')
@click.option('-m','--mannerisms', default=1, help='Number of mannerisms')
#@click.argument('talent_no', default = 1)
def make_npc(name, talents=1, mannerisms=1):
    newpc_name = name
    newpc_app = get_apperance(npc_appearance_gen())
    newpc_low_stat, newpc_high_stat = get_high_low_ability(npc_abilities)
    newpc_alignment = get_alignment()
    newpc_flaw = get_flaw()
    newpc_talents = get_talents(talents)
    newpc_interaction = get_interaction()
    newpc_mannerism = get_mannerism(mannerisms)
    newpc_bond = get_bonds()
    newpc = {'Name': newpc_name, 'Appearance': newpc_app, 'Alignment': newpc_alignment, 'High/Low Stat': f"{newpc_high_stat}/{newpc_low_stat}",
            'Talents': newpc_talents, 'Mannerisms':newpc_mannerism, 'Flaw': newpc_flaw, 'Interaction Trait': newpc_interaction, 'Bond': newpc_bond}
    for k, d in newpc.items():
        if d.__class__ == list:
            print(f'{k}:')
            for i in d:
                print(f'    {i}')
        else:
            print(f'{k}: {newpc[k]}')

if __name__ == "__main__":
    make_npc()
