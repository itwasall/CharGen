import random


# This code allows us to use range values for item tables that, when passed through this function, creates a dictionary that has a separate entry for each item within the range.
#   For example: expand({range(1,4): "Dick"}, range(4,6): "Pennis", 6: "Balls")
#   Would give: {1: "Dick", 2: "Dick", 3: "Dick", 4: "Pennis", 5: "Pennis", 6: "Balls"}
def expand(d):
    ret = {}
    for k in d:
        v = d[k]
        if isinstance(k, range):
            ret.update({i: v for i in k})
        else:
            ret[k] = v
    return ret

def dice(throws, verbose=False):
    y = throws.split("d")
    total = 0
    for i in range(int(y[0])):
        x = random.randint(1,int(y[1]))
        if verbose == True:
            print(f'Rolled a {x}')
        total += x
    return total

encounter_artic_1_4 = expand({
             1: "1 Giant Owl",
    range(2,5):   f"{dice('1d6') + 3} Kobolds",
    range(6,8):   f"{dice('1d4') + 3} Trappers",
    range(9,10):   "1 Owl",
    range(11,12): f"{dice('2d4')} Blood hawks",
    range(13,17): f"{dice('2d6')} Bandits",
    range(18,20): f"{dice('1d3')} winged kobolds with {dice('1d6')} kobolds",
    range(21,25): f"The partially eaten carcass of a mammoth, from which f{dice('1d6')} weeks of rations can be harvested",
    range(26,29): f"{dice('2d8')} hunters (tribal warriors)",
    range(30,35):  "1 half ogre",
    range(36,40):  "Single-file tracks in the snow that stop abruptly",
    range(41,45): f"{dice('1d3')} ice mephits",
    range(46,50):  "1 brown bear",
    range(51,53): f"{dice('1d6') + 1} orcs",
    range(54,55):  "1 polar bear ",
    range(56,57): f"{dice('1d6')} scouts ",
    range(58,60):  "1 saber-toothed tiger",
    range(61,65):  "A frozen pond with a jagged hole in the ice that appears recently made",
    range(66,68):  "1 berserker",
    range(69,70):  "1 ogre",
    range(71,72):  "1 griffon",
    range(73,75):  "1 druid",
    range(76,80): f"{dice('3d4')} refugees (commoners) fleeing from ores",
              81: f"{dice('1d3')} veterans", 82: f"{dice('1d4')} orogs", 83:  "2 brown bears",
              84: f"1 ore Eye ofGruumsh with {dice('2d8')} ores",  85: f"{dice('1d3')} winter wolves",
    range(86,88): f"{dice('1d4')} yetis",
              88:  "1 half-ogre", 89: f"{dice('1d3')} manticores", 90: f"1 bandit captain with {dice('2d6')} bandits",
              91:  "1 revenant",
    range(92,93):  "1 troll",
    range(94,95):  "1 werebear",
    range(96,97):  "1 young remorhaz",
              98:  "1 mammoth", 99:  "1 young white dragon", 100:  "1 frost giant"
})

encounter_artic_5_10 = expand({
    range(1,5): "2 saber-toothed tigers" ,
    range(6,7): f"{dice('1d4')} half.ogres ",
    range(8,10): f"{dice('1d3') + 1} brown bears ",
    range(11,15): f"{dice('1d3')} polar bears ",
    range(16,20): f"{dice('2d4')} berserkers",
    range(21,25): "A half-ore druid tending to an injured polar bear. If the characters assist the druid, she gives them a vial of antitoxin.",
    range(26,30): f"{dice('2d8')} scouts ",
    range(31,35): f"{dice('2d4')} ice mephits",
    range(36,40): f"{dice('2d6') + 1} zombies aboard a galleon trapped in the ice. Searching the ship yields {dice('2d20')} days of rations.",
    range(41,45): "1 manticore",
    range(46,50): f"{dice('2d6') + 3} ores",
    range(51,53): f"{dice('1d6') + 2} ogres",
    range(54,55): f"{dice('2d4')} griffons ",
    range(56,57): f"{dice('1d4')} veterans ",
    range(58,60): f"1 bandit captain with 1 druid, {dice('1d3')} berserkers, and {dice('2d10') + 5} bandits ",
    range(61,65): f"{dice('1d4')} hours of extreme cold ",
    range(66,68): "1 young remorhaz ",
    range(69,72): f"1 ore Eye ofGruumsh with {dice('1d6')} orogs and {dice('2d8') + 6} ores ",
    range(73,75): "1 revenant ",
    range(76,80): f"A howl that echoes over the land for {dice('1d3')} minutes ",
    range(81,82): f"{dice('1d3')} mammoths ",
    range(83,84): "1 young white dragon ",
    range(85,86): f"{dice('2d4')} winter wolves ",
    range(87,88): f"{dice('1d6') + 2} yetis ",
    range(89,90): f"{dice('1d2')} frost giants ",
    range(91,92): f"{dice('1d3')} werebears ",
    range(93,94): f"{dice('1d4')} trolls ",
    range(95,96): "1 abominable yeti ",
    range(97,98): "1 remorhaz ",
              99: "1 roe ",
             100: f"{dice('2d4')} young remorhazes"
    })
encounter_artic_11_16 = expand ({
    1: "1 abominable yeti",
    range(2,4): f"{dice('1d6')} revenants", 
    range(5,10): f"{dice('1d4') + 1} werebears", 
    range(11,20): f"{dice('1d3')} young white dragons", 
    range(21,25): f"A blizzard that reduces visibility to 5 feet for {dice('1d6')} hours", 
    range(26,35): "1 roe ",
    range(36,40): f"A herd of {dice('3d20') + 60} caribou (deer) moving through the snow", 
    range(41,50): f"{dice('1d4')} mammoths ",
    range(51,60): f"{dice('1d8') + 1} trolls ",
    range(61,65): "A mile-wide frozen lake in which the preserved corpses of strange creatures can be seen ",
    range(66,75): f"{dice('2d4')} young remorhazes ",
    range(76,80): "A crumbling ice castle littered with the frozen bodies of blue-skinned humanoids ",
    range(81,90): "1 adult white dragon ",
    range(91,96): f"{dice('1d8') + 1} frost giants ",
    range(97,99): f"{dice('1d4')} remorhazes ",
    100: "1 ancient white dragon"
})
encounter_artic_17_20 = expand ({
    range(1,2): f"{dice('2d10')} revenants",
    range(3,4): f"{dice('2d8')} trolls",
    range(5,6): f"{dice('2d10')} werebears ",
    range(7,8): f"1 frost giant",
    range(9,10): f"{dice('2d4')} young remorhazes ",
    range(11,20): f"{dice('1d4')} frost giants",
    range(21,25): f"A circular patch of black ice on the ground. The air temperature around the patch is warmer than in the surrounding area, and characters who inspect the ice find bits of machinery frozen within.",
    range(26,35): f"1 ancient white dragon ",
    range(36,40): f"An adventurer frozen 6 feet under the ice; 50% chance the corpse has a rare magic item of the DM's choice ",
    range(41,50): f"{dice('1d3')} abominable yetis ",
    range(51,60): f"{dice('1d4')} remorhazes ",
    range(61,65): f"A 500-foot-high wall of ice that is 300 feet thick and spread across {dice('1d4')} miles ",
    range(66,75): f"{dice('1d4')} roes ",
    range(76,80): f"The likeness of a stern woman with long, flowing hair, carved into the side of a mountain ",
    range(81,90): f"{dice('1d10')} frost giants with {dice('2d4')} polar bears ",
    range(91,96): f"{dice('1d3')} adult white dragons ",
    range(97,99): f"{dice('2d4')} abominable yetis ",
    100: f"1 ancient white dragon with {dice('1d3')} young white dragons"
})
encounter_coastal_1_4 = expand({
    1: f"1 pseudodragon",
    range(2,5): f"{dice('2d8')} crabs",
    range(6,10): f"{dice('2d6')} fishers (commoners)",
    11: f"{dice('1d3')} poisonous snakes",
    range(12,13): f"{dice('1d6')} guards protecting a stranded noble ",
    range(14,15): f"{dice('2d4')} scouts ",
    range(16,18): f"{dice('2d10')} merfolk ",
    range(19,20): f"{dice('1d6') + 2} sahuagin ",
    range(21,25): f"{dice('1d4')} ghouls feeding on corpses aboard the wreckage of a merchant ship. A search uncovers {dice('2d6')} bolts of ruined silk, a 50-foot length of rope, and a barrel of salted herring. ",
    range(26,27): f"{dice('1d4')} winged kobolds with {dice('1d6') + 1} kobolds ",
    range(28,29): f"{dice('2d6')} tribal warriors ",
    range(30,31): f"{dice('3d4')} kobolds ",
    range(32,33): f"{dice('2d4') + 5} blood hawks ",
    range(34,35): f"{dice('1d8') + 1} pteranodons ",
    range(36,40): f"A few dozen baby turtles struggling to make their way to the sea ",
    range(41,42): f"{dice('1d6') + 2} giant lizards",
    range(43,44): f"{dice('1d6') + 4} giant crabs ",
    range(45,46): f"{dice('2d4')} stirges",
    range(47,48): f"{dice('2d6') + 3} bandits ",
    range(49,53): f"{dice('2d4')} sahuagin ",
    range(54,55): f"{dice('1d6') + 2} scouts",
    range(56,60): f"1 sea hag ",
    range(61,65): f"A momentary formation in the waves that looks like an enormous humanoid face ",
    range(66,70): f"1 druid ",
    range(71,75): f"{dice('1d4')} harpies ",
    range(76,80): f"A lone hermit (acolyte) sitting on the beach, contemplating the meaning of the multiverse ",
    81: f"{dice('1d4')} berserkers ",
    82: f"{dice('1d6')} giant eagles ",
    83: f"{dice('2d4')} giant toads ",
    84: f"{dice('1d4')} ogres or {dice('1d4')} merrow ",
    85: f"{dice('3d6')} sahuagin ",
    86: f"{dice('1d4')} veterans ",
    87: f"{dice('1d2')} plesiosauruses ",
    88: f"1 bandit captain with {dice('2d6')} bandits ",
    89: f"{dice('1d3')} manticores ",
    90: f"1 banshee ",
    range(91,92): f"{dice('1d4') + 3} griffons ",
    range(93,94): f"1 sahuagin priestess with {dice('1d3')} merrow and {dice('2d6')} sahuagin ",
    range(95,96): f"1 sahuagin baron ",
    range(97,98): f"1 water elemental ",
    99: f"1 cyclops ",
    00: f"1 young bronze dragon"
})

item_loot = []
item_n = random.randint(1,4)
for n in range(item_n):
    item = random.choice(list(encounter_artic_1_4))
    item = encounter_artic_1_4[item]
    item_loot.append(item)
print([i for i in item_loot])
