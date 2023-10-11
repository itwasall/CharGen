import data as Core
import random

def generate_attributes(ch: Core.Character, metatype: Core.Metatype):
    """
        Generates character attributes in line with their
            metatype's default values
    """
    if "Body" in metatype.stat_changes.keys():
        body_value = metatype.stat_changes['Body'][0]
        body_limit = metatype.stat_changes['Body'][1]
    else:
        body_value = 1
        body_limit = 6
    ch.Body = Core.Attribute('Body', body_value, body_limit)

    if "Agility" in metatype.stat_changes.keys():
        agility_value = metatype.stat_changes['Agility'][0]
        agility_limit = metatype.stat_changes['Agility'][1]
    else:
        agility_value = 1
        agility_limit = 6
    ch.Agility = Core.Attribute('Agility', agility_value, agility_limit)

    if "Reaction" in metatype.stat_changes.keys():
        reaction_value = metatype.stat_changes['Reaction'][0]
        reaction_limit = metatype.stat_changes['Reaction'][1]
    else:
        reaction_value = 1
        reaction_limit = 6
    ch.Reaction = Core.Attribute('Reaction', reaction_value, reaction_limit)

    if "Strength" in metatype.stat_changes.keys():
        strength_value = metatype.stat_changes['Strength'][0]
        strength_limit = metatype.stat_changes['Strength'][1]
    else:
        strength_value = 1
        strength_limit = 6
    ch.Strength = Core.Attribute("Strength", strength_value, strength_limit)

    if "Logic" in metatype.stat_changes.keys():
        logic_value = metatype.stat_changes['Logic'][0]
        logic_limit = metatype.stat_changes['Logic'][1]
    else:
        logic_value = 1
        logic_limit = 6
    ch.Logic = Core.Attribute("Logic", logic_value, logic_limit)

    if "Willpower" in metatype.stat_changes.keys():
        willpower_value = metatype.stat_changes['Willpower'][0]
        willpower_limit = metatype.stat_changes['Willpower'][1]
    else:
        willpower_value = 1
        willpower_limit = 6
    ch.Willpower = Core.Attribute("Willpower", willpower_value, willpower_limit)

    if "Intuition" in metatype.stat_changes.keys():
        intuition_value = metatype.stat_changes['Intuition'][0]
        intuition_limit = metatype.stat_changes['Intuition'][1]
    else:
        intuition_value = 1
        intuition_limit = 6
    ch.Intuition = Core.Attribute("Intuition", intuition_value, intuition_limit)

    if "Charisma" in metatype.stat_changes.keys():
        charisma_value = metatype.stat_changes['Charisma'][0]
        charisma_limit = metatype.stat_changes['Charisma'][1]
    else:
        charisma_value = 1
        charisma_limit = 6
    ch.Charisma = Core.Attribute("Charisma", charisma_value, charisma_limit)

    ch.Essence = Core.Attribute("Essence", 6, 6)



def roll_stats(ch: Core.Character, attr: int) -> None:
    """
        Rolls eligible stats
        Only one stat can be at max during character creation.
        Magic and resonance aren't rolled here as the character isn't eligible
            for either that at this point in generation
        Returns None as it mutes values in the Core.Attribute classes in the
            Core.Character class
    """
    rollable_stats = [ch.Body, ch.Agility, ch.Reaction, ch.Strength,
                      ch.Willpower, ch.Logic, ch.Intuition, ch.Charisma]
    limits_hit = 1
    while attr > 0:
        stat_roll = random.choice(rollable_stats)
        # Ensuring only one stat is at max
        if stat_roll.value + 1 == stat_roll.limit:
            if limits_hit == 0:
                limits_hit += 1
            else:
                continue
        if stat_roll.value + 1 <= stat_roll.limit:
            stat_roll.value += 1
            attr -= 1
        else:
            continue


def get_highest_attr(ch: Core.Character) -> list[Core.Attribute]:
    """
        Sorts all physical and mental attributes by value
        Returns list of the two highest attributes
        This is to influence the skill choices later on in character
        generation.
    """
    non_special_attrs = [ch.Body, ch.Agility, ch.Reaction, ch.Strength,
                         ch.Willpower, ch.Logic,ch.Charisma, ch.Intuition]
    # List is shuffled to avoid predictable results
    #   e.g. if unshuffled and Body is in a three way tie for highest stat,
    #       Body will *always* be picked
    random.shuffle(non_special_attrs)
    attr_values = list(set(sorted([i.value for i in non_special_attrs])))
    highest = []
    for i in attr_values[::-1]:
        for attr in non_special_attrs:
            if i == attr.value:
                highest.append(attr)
                break
        if len(highest) > 1:
            break
    # print("Highest attrs: ", highest)
    return highest
