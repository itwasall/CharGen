import random
import json

def d4(rolls=1):
    total = 0
    for i in range(rolls):
        total += random.randint(1,4)
    return total

def d6(rolls=1):
    total = 0
    for i in range(rolls):
        total += random.randint(1,6)
    return total

def d8(rolls=1):
    total = 0
    for i in range(rolls):
        total += random.randint(1,8)
    return total

def d10(rolls=1):
    total = 0
    for i in range(rolls):
        total += random.randint(1,10)
    return total

def d20(rolls=1):
    total = 0
    for i in range(rolls):
        total += random.randint(1,20)
    return total

names = []
sizes = []
types = []
subtypes = []
alignments = []
armor_classes = []
hit_points = []
hit_dices = []
speeds = []
str_scores = []
dex_scores = []
con_scores = []
int_scores = []
wis_scores = []
cha_scores = []
str_saves = []
dex_saves = []
con_saves = []
int_saves = []
wis_saves = []
cha_saves = []
histories = []
perceptions = []
damage_vulnerabilities = []
damage_resistances = []
condition_immunitites = []
senses = []
languages = []
challenge_ratings = []
special_abilitites = []
actions = []
legendary_actions = []

with open('F:\\Chargen\\monsters.json','r',encoding='cp932', errors='ignore') as file:
    monster_data = json.load(file)
    for entry in monster_data:
        names.append(entry['name'])
        sizes.append(entry['size'])
        types.append(entry['type'])
        subtypes.append(entry['subtype'])
        alignments.append(entry['alignment'])
        armor_classes.append(entry['armor_class'])
        hit_points.append(entry['hit_points'])
        hit_dices.append(entry['hit_dice'])
        speeds.append(entry['speed'])
        str_scores.append(entry['strength'])
        dex_scores.append(entry['dexterity'])
        con_scores.append(entry['constitution'])
        int_scores.append(entry['intelligence'])
        wis_scores.append(entry['wisdom'])
        cha_scores.append(entry['charisma'])
        try:
            str_saves.append(entry['strength_save'])
        except:
            str_saves.append(0)
        try:
            dex_saves.append(entry['dexterity_save'])
        except:
            dex_saves.append(0)
        try:
            con_saves.append(entry['constitution_save'])
        except:
            con_saves.append(0)
        try:
            int_saves.append(entry['intelligence_save'])
        except:
            int_saves.append(0)
        try:
            wis_saves.append(entry['wisdom_save'])
        except:
            wis_saves.append(0)
        try:
            cha_saves.append(entry['charisma_save'])
        except:
            cha_saves.append(0)
        damage_vulnerabilities.append(entry['damage_vulnerabilities'])
        damage_resistances.append(entry['damage_resistances'])
        condition_immunitites.append(entry['condition_immunities'])
        senses.append(entry['senses'])
        languages.append(entry['languages'])
        challenge_ratings.append(entry['challenge_rating'])
        try:
            special_abilitites.append(entry['special_abilities'])
        except:
            special_abilitites.append('None')
        try:
            actions.append(entry['actions'])
        except:
            actions.append('None')

for item in monster_data:
    if item['type'] == 'aberration':
        print(item)

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.name_label = QLabel('Name')
        self.type_label = QLabel('Type')
        self.subtype_label = QLabel('Subtype')
        self.name_choose = QComboBox()
        self.item_names = (item['name'] for item in monster_data)
        self.name_choose.addItems(self.item_names)

        self.layout = QGridLayout()
        self.layout.addWidget(self.name_choose, 0,0)
        self.layout.addWidget(self.name_label, 1, 0)
        self.layout.addWidget(self.type_label, 2, 0)
        self.layout.addWidget(self.subtype_label, 3, 0)
        self.setLayout(self.layout)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    run = MainWindow()
    run.show()
    sys.exit(app.exec_())