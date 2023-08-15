import csv, random

csvfile = csv.DictReader(open('dndmonster.csv', 'tr'))

csv_contents = csvfile.reader

monsters = []
for i in csv_contents:
    monsters.append(i)

lawful_monsters = []
chaotic_monsters = []
neutral_monsters = []
good_monsters = []
evil_monsters = []
challenge_rating = {}
cr_ref = ['1/8', '1/4', '1/2', '0', '1', '2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19',
          '20','21','22','23','24','26','30']
for i in cr_ref:
    challenge_rating[i] = []

for it, i in enumerate(monsters):
    align = monsters[it][3]
    name = monsters[it][0]
    size = monsters[it][1]
    montype = monsters[it][2]
    cr = monsters[it][4]
    book = monsters[it][5]
    if cr == "CR":
        continue
    if align.find("Chaotic") == 0:
        chaotic_monsters.append([name, size, montype, cr])
        challenge_rating[cr].append(name)
    elif align.find("Lawful") == 0:
        lawful_monsters.append([name, size, montype, cr])
        challenge_rating[cr].append(name)
    elif align.find("Neutral") == 0:
        neutral_monsters.append([name, size, montype, cr])
        challenge_rating[cr].append(name)

    if align.find("Good") < 0:
        good_monsters.append([name, size, montype, cr])
        challenge_rating[cr].append(name)
    elif align.find("Evil") < 0:
        evil_monsters.append([name, size, montype, cr])
        challenge_rating[cr].append(name)

cr_input = 10

solo_monster_limit_four = {1:1, 2:2, 3:3, 4:4, 5:7, 6:8, 7:9, 8:10, 9:11, 10:12, 11:13, 12:15, 13:16, 14:17, 15:18, 16:19, 17:20, 18:20, 19:21, 20:22}
solo_monster_limit_five = {}
solo_monster_limit_six = {}
for k, d in solo_monster_limit_four.items():
    solo_monster_limit_five[k] = d+1
    solo_monster_limit_six[k] = d+2

def get_solo_monster_cr(party_size=4, level=1):
    if party_size == 4:
        x = solo_monster_limit_four[level]
        print(f'Recommended challenge rating for party of {party_size} at level {level}: CR{x}')
    elif party_size == 5:
        x = solo_monster_limit_five[level]
        print(f'Recommended challenge rating for party of {party_size} at level {level}: CR{x}')
    elif party_size == 6:
        x = solo_monster_limit_six[level]
        print(f'Recommended challenge rating for party of {party_size} at level {level}: CR{x}')
    print(f"Monsters of challenge rating {x}")
    print(challenge_rating[str(x)])

if __name__ == "__main__":
    get_solo_monster_cr(level=random.randint(1,20))
