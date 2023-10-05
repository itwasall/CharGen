import random
import char_shadowrun_5e_data as Core
import char_shadowrun_5e_gear as Gear
import char_shadowrun_5e_item as Item
import multiprocessing
import time
from collections import OrderedDict

KARMA_LOG = False


def generate_character() -> Core.Character:
    karma_log = Core.KarmaLogger()
    # STEP 1: CONCEPT
    character = Core.Character()
    priority_table = get_priorities(character)
    attribute_points = priority_table['Attributes']
    nuyen = priority_table['Resources']
    magic_reso = priority_table['MagicResonance']
    metatype = random.choice(priority_table['Metatype'])
    # STEP 2: METATYPE & ATTRIBUTES
    special_attribute_points = metatype[1]
    metatype = metatype[0]
    character.Metatype = metatype
    generate_attributes(character, character.Metatype)
    roll_stats(character, attribute_points)
    highest_attrs = get_highest_attr(character)
    # STEP 3: MAGIC/RESONANCE
    resolve_magic_resonance(character, magic_reso, priority_table)
    roll_special_stats(character, metatype, special_attribute_points)
    character.redo_attr()
    # STEP 3.5: DETERMING NON-MAGIC/RESONANCE CHAR BUILD CHOICES
    IS_DECKER = False
    IS_RIGGER = False
    IS_FACE = False
    alt_builds = ['Decker', 'Rigger', 'Face', None]
    if priority_table['MagicResonance'] is None:
        build = random.choices(alt_builds, [1, 1, 1, 5])
        if build == 'Decker':
            ch.IS_DECKER = True
            print('Character is decker')
        elif build == 'Rigger':
            ch.IS_RIGGER = True
            print('Character is rigger')
        elif build == 'Face':
            ch.IS_FACE = True
            print('Character is face')
    skill_builds = {'IS_DECKER': IS_DECKER,
                    'IS_RIGGER': IS_RIGGER, 'IS_FACE': IS_FACE}
    # STEP 4: QUALITIES
    get_qualities(character, karma_log)
    # STEP 5: SKILLS
    get_skills(character, priority_table, attr_influence=highest_attrs,
               skill_cap=20, builds=skill_builds)
    get_language_knowledge_skills(character)
    """
        dealing with this later
    """
    #if 'Exotic Melee Weapon' in character.Skills:
    #    character = resolve_specific_skill(character, Core.EXOTIC_MELEE_WEAPON)
    add_contacts(character, karma_log)
    get_gear(character, nuyen)
    leftover_karma(character, karma_log)
    print_shit(character, nuyen, karma_log)
    return character


def get_priorities(character: Core.Character) -> dict:
    """
        Chooses priorities from priority table.
        Returns choices as dict
    """
    table_choices = ['A', 'B', 'C', 'D', 'E']
    selected_items = {
        'Metatype': None,
        'Attributes': None,
        'MagicResonance': None,
        'Skills': None,
        'Resources': None
    }
    for category in selected_items.keys():
        new_priority = random.choice(table_choices)
        table_choices.pop(table_choices.index(new_priority))
        selected_items[category] = Core.PRIORITY_TABLE_FLIPPED[
            category][new_priority]
    return selected_items


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
    limits_hit = 0
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


def resolve_magic_resonance(ch: Core.Character, tbl, priority_table) -> None:
    """
        If a character weilds magic or is a technomancer,
            give them the relevant stats and abilities here.
    """
    if tbl is None:
        return
    _type = random.choice(list(tbl.keys()))
    ch.MagicResoUser = str(_type)
    print(f'Uh oh! Looks like you\'re a {ch.MagicResoUser}')

    def get_special_attribute(ch, tbl, attr):
        match attr:
            case 'Magic':
                ch.Magic = Core.Attribute("Magic")
                ch.Magic.value = tbl[ch.MagicResoUser][attr]
            case 'Resonance':
                ch.Resonance = Core.Attribute("Resonance")
                ch.Resonance.value = tbl[ch.MagicResoUser][attr]

    match ch.MagicResoUser:
        case 'Adept':
            get_special_attribute(ch, tbl, 'Magic')
            get_adept_powers(ch)
        case 'Magician':
            get_special_attribute(ch, tbl, 'Magic')
            ch.Spells = []
            for i in range(tbl[ch.MagicResoUser]['Spells']):
                add_spell(ch)
        case 'Aspected Magician':
            get_special_attribute(ch, tbl, 'Magic')

        case 'Mystic Adept':
            get_special_attribute(ch, tbl, 'Magic')
            try:
                if priority_table['Skills'][1] != 0:
                    pass
            except IndexError:
                return "We'll do it live" 
        case 'Technomancer':
            get_special_attribute(ch, tbl, 'Resonance')
            ch.ComplexForms = []
            for i in range(tbl[ch.MagicResoUser]['Complex Forms']):
                add_complex_form(ch)
    return "no"


def roll_special_stats(ch: Core.Character, metatype_tbl, points):
    """
        Rolls special stats.
            If a character doesn't use magic or resonance, then
            all the points are added to Edge
    """
    if "Edge" in ch.Metatype.stat_changes.keys():
        edge_value = ch.Metatype.stat_changes['Edge'][0]
        edge_limit = ch.Metatype.stat_changes['Edge'][1]
    else:
        edge_value = 1
        edge_limit = 6
    ch.Edge = Core.Attribute('Edge', edge_value, edge_limit)

    rollable_special_stats = [ch.Magic, ch.Resonance, ch.Edge]
    while points > 0:
        stat_roll = random.choice(rollable_special_stats)
        if stat_roll is not None:
            points -= 1
            if stat_roll.limit > stat_roll.value:
                stat_roll.value += 1


def get_adept_powers(ch: Core.Character, power_points=0) -> None:
    """
        Gets adept powers.
        Depending on the type of character, this will either be called during the
            magic/resonance part of character generation, or right at the end when spending
            extra karma.
        While both Adepts and Mystic Adepts use Adept Powers, only Adepts get their PP
            for free. Mystic Adepts must purchase their PP using karma much later into
            character generation.
    """
    if ch.MagicResoUser != 'Mystic Adept':
        power_points = ch.Magic.value
    max_buys = ch.Magic.value
    char_powers = []
    while power_points > 0:
        new_power = random.choice(Core.AdeptPower.items)
        if new_power.per_level:
            if len([i for i in char_powers if i.name == new_power.name]) >= max_buys:
                continue
        elif new_power.per_group:
            if len([i for i in char_powers if i.group == new_power.group]) >= max_buys:
                continue
        elif not new_power.per_level and not new_power.per_group:
            if new_power in char_powers:
                continue
        if new_power.cost > power_points:
            Core.AdeptPower.items.pop(Core.AdeptPower.items.index(new_power))
            continue
        char_powers.append(new_power)
        power_points -= new_power.cost
    ch.AdeptPowers = char_powers
    return


def add_spell(ch: Core.Character, category=None) -> None:
    if category is not None:
        spell_list = [i for i in Core.Spell.items if i.category == category]
    else:
        spell_list = [i for i in Core.Spell.items]
    ROLL_SPELL = random.choice(spell_list)
    spell_list.pop(spell_list.index(ROLL_SPELL))
    if ch.Spells is None:
        ch.Spells = [ROLL_SPELL]
    else:
        ch.Spells.append(ROLL_SPELL)
    return


def add_complex_form(ch: Core.Character) -> None:
    ROLL_COMPLEX = random.choice(Core.ComplexForm.items)
    while ch.ComplexForms is not None and ROLL_COMPLEX.name in [cf.name for cf in ch.ComplexForms]:
        ROLL_COMPLEX = random.choice(Core.ComplexForm.items)
    if ch.ComplexForms is None:
        ch.ComplexForms = [ROLL_COMPLEX]
    else:
        ch.ComplexForms.append(ROLL_COMPLEX)
    return


def get_qualities(ch: Core.Character, k: Core.KarmaLogger) -> None:
    """
        Randomly chooses qualities for character.
        Karma starts off at 25 points. Positive qualities cost karma whilst
            negative qualities grant karma.
        However the total sum of positive qualities cannot exceed 25, and
            the total sum of negative qualities cannot exceed -25
    """
    ch.Qualities = {}
    total_karma = 25
    positive_karma, negative_karma = 0, 0
    k.append(f'Beginning karma logging.\n   {total_karma} is Karma total')
    NEGATIVE_TOO_HIGH, POSITIVE_TOO_HIGH = False, False
    quality_weights = [1 for _ in Core.Quality.items]
    inc = 0
    while total_karma > 0 and inc < 100:
        inc += 1
        ch.Karma = total_karma
        # There's an infinite loop I can't be bothered to fix right now, this
        # will do
        if (total_karma < 10 and random.randint(0, 1) == 1) or \
                total_karma <= 0:
            break
        ROLL_QUALITY = random.choices(Core.Quality.items, quality_weights)[0]
        # If a quality in the same group has already been taken, continue
        # (SEE DATA)
        if hasattr(ROLL_QUALITY, "group"):
            if ROLL_QUALITY.group in [d.group for d in ch.Qualities.values() if
                                    hasattr(d, "group")]:
                continue
        # Negative qualities cannot total more than ABS(25)
        if hasattr(ROLL_QUALITY, "negative"):
            if negative_karma + ROLL_QUALITY.cost > 25:
                NEGATIVE_TOO_HIGH = True
                continue
                # continue
        # Positive qualities cannot total more than ABS(25)
        elif positive_karma + ROLL_QUALITY.cost > 25:
            POSITIVE_TOO_HIGH = True
            continue
            # continue
        if total_karma - ROLL_QUALITY.cost < 0 or (
                NEGATIVE_TOO_HIGH and not POSITIVE_TOO_HIGH) or (
                POSITIVE_TOO_HIGH and not NEGATIVE_TOO_HIGH):
            continue
        if hasattr(ROLL_QUALITY, "negative"):
            negative_karma += ROLL_QUALITY.cost
            total_karma += ROLL_QUALITY.cost
            k.append(f'(NEG) {ROLL_QUALITY.name} has been bought.' +
                     f'Costing {ROLL_QUALITY.cost}.' +
                     f'\n   {total_karma} is Karma total.' +
                     f'\nNegative Karma is at {negative_karma}')
        else:
            positive_karma += ROLL_QUALITY.cost
            total_karma -= ROLL_QUALITY.cost
            k.append(f'(POS) {ROLL_QUALITY.name} has been bought.' +
                     f'Costing {ROLL_QUALITY.cost}.' +
                     f'\n   {total_karma} is Karma total.' +
                     f'\nPositive Karma is at {positive_karma}')

        # Pretty output & roll for quality specific params here
        ROLL_QUALITY = resolve_quality(ROLL_QUALITY, ch)

        ch.Qualities[ROLL_QUALITY.name] = ROLL_QUALITY
        if hasattr(ROLL_QUALITY, "quantity"):
            if hasattr(ch.Qualities[ROLL_QUALITY.name], "level"):
                ch.Qualities[ROLL_QUALITY.name].level += 1
            else:
                ch.Qualities[ROLL_QUALITY.name].level = 1
            quality_weights[Core.Quality.items.index(ROLL_QUALITY)] += 10
        if NEGATIVE_TOO_HIGH and POSITIVE_TOO_HIGH:
            break
    # print(ch.Qualities)
    return


def resolve_quality(q: Core.Quality, ch: Core.Character) -> Core.Quality:
    """
        For qualities that have multiple levels or are a generic title meant
            for something more specific, then those levels/specificities are
            dealt with here

        Returns Core.Quality
    """
    # Just a dump for all the quality-specific rolling options
    if "Allergy" in q.name:
        if "Common" in q.name:
            x = {5: 'Mild', 10: 'Moderate', 15: 'Severe', 20: 'Extreme'}
            common_allergies = ['Peanuts', 'Pollutants', 'Grass']
            q.name = f"{x[q.cost]} Allergy ({random.choice(common_allergies)})"
        if "Uncommon" in q.name:
            x = {10: 'Mild', 15: 'Moderate', 20: 'Severe', 25: 'Extreme'}
            uncom_allergies = ['Dogs', 'Grass', 'Seafood', 'Sunlight']
            q.name = f"{x[q.cost]} Allergy ({random.choice(uncom_allergies)})"
    if "Addiction" in q.name:
        x = {4: 'Mild', 9: 'Moderate', 20: 'Severe', 25: 'Burnout'}
        q.name = f"{x[q.cost]} Addiction ({random.choice(q.opts)})"
    if "Resistance to Pathogens or Toxins" in q.name:
        q.name = f"Resistance to {random.choice(q.opts)}"
    if "Mentor Spirit" in q.name:
        q.name = f"Mentor Spirit ({random.choice(q.opts)})"
    if "(Natural)" in q.name:
        q.name = "Natural Immunity (Organic)"
    if "Prejudiced" in q.name:
        if "Common" in q.name:
            x = {5: 'Bias', 7: 'Outspoken', 10: 'Radical'}
            common_prejudices = ['Human', 'Metahuman',
                                 'Troll', 'Ork', 'Elve', 'Dwarf']
            new_prejudice = random.choice([
                i for i in common_prejudices if i != ch.Metatype.name
            ])
            q.name = f"Prejudiced - {x[q.cost]} against {new_prejudice}"
        if "Specific" in q.name:
            x = {3: 'Bias', 5: 'Outspoken', 8: 'Radical'}
            specific_prejudices = [
                'The Awakened',
                'technomancers',
                'shapeshifters',
                'aspected magicians']
            new_prejudice = random.choice(specific_prejudices)
            q.name = f"Prejudiced - {x[q.cost]} against {new_prejudice}"
    return q


def get_skills(
        ch: Core.Character,
        tbl,
        skill_cap=50,
        attr_influence=None,
        **kwargs) -> None:
    """
        Generates skills for character.

        Returns a dict of {skill_name: Core.Skill}
    """
    ch.Skills = {}
    # character_specialisations = {}
    skill_points_table = tbl['Skills']
    if ch.MagicResoUser is not None:
        if 'Skills' in tbl['MagicResonance'][ch.MagicResoUser].keys():
            magic_reso_skills = skills_magic_resonance(
                ch, tbl['MagicResonance'][ch.MagicResoUser]['Skills'])
            for k, d in magic_reso_skills.items():
                ch.Skills[k] = d
        else:
            pass
    skills = [skill for skill in Core.Skill.items if
              skill.skill_type == "Active"]
    groups = [group for group in Core.SkillGroup.items]
    weight_skills = [1 for _ in skills]
    weight_groups = [1 for _ in groups]

    skill_list = {}
    group_list = {}
    for idx, i in enumerate(skills):
        skill_list[i] = weight_skills[idx]
    for idx, i in enumerate(groups):
        group_list[i] = weight_groups[idx]

    if "builds" in kwargs:
        if kwargs['builds']['IS_DECKER']:
            for _ in range(2):
                decker_skill = random.choice(Core.DECKER_SKILLS)
                ch.Skills[decker_skill.name] = decker_skill
                ch.Skills[decker_skill.name].rating += 1
                skill_list[decker_skill] += 3
            pass
        if kwargs['builds']['IS_RIGGER']:
            for _ in range(2):
                rigger_skill = random.choice(Core.RIGGER_SKILLS)
                ch.Skills[rigger_skill.name] = rigger_skill
                ch.Skills[rigger_skill.name].rating += 1
                skill_list[rigger_skill] += 3
            pass
        if kwargs['builds']['IS_FACE']:
            for _ in range(2):
                face_skill = random.choice(Core.FACE_SKILLS)
                ch.Skills[face_skill.name] = face_skill
                ch.Skills[face_skill.name].rating += 1
                skill_list[face_skill] += 3
            pass

    skill_points, group_points = skill_points_table

    # Non-magic users can't select magic skills/groups
    # Non-resonance users can't select resonance skills/group
    skill_list, group_list = skills_remove_magic_resonance(
        ch, skill_list, group_list)
    # Adjusting weights based on highest physical and mental attributes
    skill_list, group_list = skills_attribute_influence(
        ch, attr_influence, skill_list, group_list)
    # Group Skill Points spend
    skill_list, group_list = skills_roll_group(
        ch, group_points, group_list, skill_list)

    # Individual Skill Points spend
    skill_list = skills_roll_individual(
        ch, skill_points, skill_list, skill_cap)

    for skill in ch.Skills:
        if ch.Skills[skill].rating > 6:
            ch.Skills[skill].rating = 6
    return


def skills_remove_magic_resonance(ch: Core.Character,
                                  skill_list, group_list) -> (dict, dict):
    """
        If a character is not magically or resonancly inclined, remove those
            skills from the pool of potential skill picks
    """
    if ch.Magic is None or ch.MagicResoUser == 'Adept':
        for sk in Core.MAGIC_SKILLS:
            skill_list[sk] = 0
        for sk in Core.MAGIC_SKILL_GROUPS:
            group_list[sk] = 0

    if ch.MagicResoUser == 'Aspected Magician':
        usable_magic_group = random.choice(Core.MAGIC_SKILL_GROUPS)
        for magic_skill_group in Core.MAGIC_SKILL_GROUPS:
            if magic_skill_group != usable_magic_group:
                for sk in magic_skill_group.skills:
                    skill_list[sk] = 0
        # for sk in [magic_skill_group.skills for magic_skill_group in Core.MAGIC_SKILL_GROUPS if 
        # magic_skill_group != usable_magic_group]:
        #    skill_list[sk] = 0
            # pass
        for magic_skill_group in Core.MAGIC_SKILL_GROUPS:
            if magic_skill_group != usable_magic_group:
                group_list[magic_skill_group] = 0
                pass


    if ch.Resonance is None:
        for sk in Core.RESONANCE_SKILLS:
            skill_list[sk] = 0
        group_list[Core.TASKING] = 0
    return skill_list, group_list


def skills_attribute_influence(ch: Core.Character, attr_influence, skill_list,
                               group_list) -> (dict, dict):
    """
        Adjusts the probabilities of skills being randomly selected based
            on the two highest stats (randomly chosen from ties) of the
            character
    """

    if attr_influence is not None:
        for attr in attr_influence:
            skills_attr_influcence = [
                s for s in skill_list.keys() if s.attribute.name == attr.name]
            for i in skills_attr_influcence:
                skill_list[i] += 3
            for group in group_list:
                if group.skills[0].attribute == attr.name:
                    group_list[group] += 3
    return skill_list, group_list


def skills_roll_group(ch: Core.Character, group_points, group_list,
                      skill_list) -> (dict, dict):
    """
        If called for by skill point priority, rolls skills based on group.

        Skills rolled this way cannot be rolled for individually later on
    """
    while group_points > 0:
        ROLL_GROUP = random.choices(
            list(group_list.keys()), list(group_list.values()))[0]
        for skill in ROLL_GROUP.skills:
            if skill.name not in ch.Skills.keys():
                ch.Skills[skill.name] = skill
                ch.Skills[skill.name].group = ROLL_GROUP.name
                ch.Skills[skill.name].rating += 1
            else:
                ch.Skills[skill.name].rating += 1
        # Adjusting weights based on groups already selected
        group_list[ROLL_GROUP] += random.randint(1, 4)
        skills_of_same_attr = [s for s in skill_list.keys(
        ) if s.attribute == skill.attribute and s.name != skill.name]
        for skill in skills_of_same_attr:
            skill_list[skill] += random.randint(1, 3)
        group_points -= 1
    return skill_list, group_list


def skills_roll_individual(ch: Core.Character, skill_points, skill_list,
                           skill_cap) -> dict:
    """
        Rolls for individual skill point allocation.
    """
    while skill_points > 0:
        # Rolling for skill specialisations
        specialisations = [d for k, d in ch.Skills.items(
        ) if d.rating > 4 and d.group is False and d.spec is not None]
        if len(specialisations) > 1 and random.randint(1, 100) > 80:
            ROLL_SPEC = random.choice(specialisations)
            inc = 0
            while len(ROLL_SPEC.spec) < 1 or inc < 100:
                inc += 1
                ROLL_SPEC = random.choice(specialisations)
            ROLL_SPECIALISATION = random.choice(ROLL_SPEC.spec)
            if isinstance(ch.Skills[ROLL_SPEC.name].spec, list):
                ch.Skills[ROLL_SPEC.name].spec = ROLL_SPECIALISATION
                skill_points -= 1
            else:
                pass

        ROLL_SKILL = random.choices(
            list(skill_list.keys()), list(skill_list.values()))[0]
        non_grouped_skills_count = len(
            [i for i in ch.Skills.keys() if
             ch.Skills[i].group is False])
        # If skill is in group, ignore
        #   In this context, skills are only assigned to their group if the
        #   skill group has been previously chosen.
        if ROLL_SKILL.name in ch.Skills.keys() \
                and ROLL_SKILL.group is not False:
            pass
        elif ROLL_SKILL.name not in ch.Skills.keys() and \
                non_grouped_skills_count >= skill_cap:
            pass
        else:
            if ROLL_SKILL.name not in ch.Skills.keys():
                ch.Skills[ROLL_SKILL.name] = ROLL_SKILL
            elif ch.Skills[ROLL_SKILL.name].rating >= 6:
                if ch.Skills[ROLL_SKILL.name].rating > 6:
                    skill_points += ch.Skills[ROLL_SKILL.name].rating - 6
                    ch.Skills[ROLL_SKILL.name].rating = 6
                continue
            skill_rating_increase = random.choices([1, 2, 3, 4], [4, 3, 3, 1])[0]
            ch.Skills[ROLL_SKILL.name].rating += skill_rating_increase
            # Adjusting weights based on skills already selected
            match skill_list[ROLL_SKILL]:
                case 1, 2, 3:
                    skill_list[ROLL_SKILL] += random.randint(1, 5)
                case _:
                    skill_list[ROLL_SKILL] += random.randint(1, 2)
            skills_of_same_attr = [skill for skill in skill_list if
                                   skill.attribute == ROLL_SKILL.attribute and
                                   skill.name != ROLL_SKILL.name]
            for skill in skills_of_same_attr:
                skill_list[skill] += random.randint(1, 3)
            else:
                pass
            skill_points -= skill_rating_increase
    return skill_list


def skills_magic_resonance(ch: Core.Character, tbl) -> dict:
    """
        If a character weilds magic or is a technomancer, the relevant skills
            to those archetypes are rolled for here

        Returns dict {skill_name: Core.Skill}
    """
    skills = {}
    match tbl['Type']:
        case 'Magic':
            for _ in range(tbl['Quantity']):
                while True:
                    new_skill = random.choice(Core.MAGIC_SKILLS)
                    if new_skill not in skills.keys():
                        break
                skills[new_skill.name] = new_skill
                skills[new_skill.name].rating = tbl['Rating']
        case 'Resonance':
            for _ in range(tbl['Quantity']):
                while True:
                    new_skill = random.choice(Core.RESONANCE_SKILLS)
                    if new_skill not in skills.keys():
                        break
                skills[new_skill.name] = new_skill
                skills[new_skill.name].rating = tbl['Rating']
        case 'Magic Group':
            groups_chosen = []
            for _ in range(tbl['Quantity']):
                while True:
                    new_group = random.choice(Core.MAGIC_SKILL_GROUPS)
                    if new_group not in groups_chosen:
                        break
                groups_chosen.append(new_group)
            for group in groups_chosen:
                for skill in group.skills:
                    skills[skill.name] = skill
                    skills[skill.name].rating = tbl['Rating']
                    skills[skill.name].group = group.name
        case 'Active':
            for _ in range(tbl['Quantity']):
                while True:
                    new_skill = random.choice(Core.ACTIVE_SKILLS)
                    if new_skill not in skills.keys():
                        break
                skills[new_skill.name] = new_skill
                skills[new_skill.name].rating = tbl['Rating']
    return skills


def get_language_knowledge_skills(ch: Core.Character) -> None:
    """
        Sets default language skill

        Rolls for other language + knowledge skills

        returns void
    """
    knowledge_points = (ch.Logic.value + ch.Intuition.value) * 2
    # Roll native language
    language = [i for i in Core.LANGUAGE_SKILLS if i.category == 'Tongue']
    knowl_skills = [i for i in Core.Skill.items if i.skill_type == 'Knowledge']

    native_roll = random.choice(language)
    ch.SkillsLanguages[native_roll] = "N"
    language.pop(language.index(native_roll))

    if 'Bilingual' in ch.Qualities.keys():
        bilingual_roll = random.choice(language)
        ch.SkillsLanguages[bilingual_roll] = "N"
        language.pop(language.index(bilingual_roll))

    if 'Language' in ch.Skills.keys():
        language_roll = random.choice(language)
        ch.SkillsLanguages[language_roll] = ch.Skills['Language'].rating
        knowledge_points -= ch.Skills['Language'].rating

    extra_language_roll = random.randint(0, 1)
    if extra_language_roll:
        language_roll = random.choice(language)
        ch.SkillsLanguages[language_roll] = random.randint(1, 4)
        knowledge_points -= ch.SkillsLanguages[language_roll]

    while knowledge_points > 1:
        knowl_skill_roll = random.choice(knowl_skills)
        knowl_skill_amt = random.randint(1, 4)
        while knowledge_points - knowl_skill_amt < 0:
            knowl_skill_amt = random.randint(1, 4)
        ch.SkillsKnowledge[knowl_skill_roll] = knowl_skill_amt
        knowl_skills.pop(knowl_skills.index(knowl_skill_roll))
        knowledge_points -= knowl_skill_amt
    return


def get_gear(ch: Core.Character, nuyen: int) -> None:
    """
        Get's gear
        Given the expected complexity of this function I (for now) am using 
            a separate file just for gear generation. Which is funny because I 
            already have a separate file for item management. So this tiny part 
            of character creation is the only part to have dedicated files

        TODO:
        - Chars with one of the SINner qualities will not be given a fake SIN
        - Chars with piloting skills should have an appropriate vehicle, 
            maybe one or more depending on which skills are more prominant, and at
            what ratings
        - Chars with skills relating to hacking should have a cyberdeck. This will
            almost certainly require it's own separate generate function
        - Chars with skills relating to firearms should have more weapons, with a 
            slight/heavy lean towards weaponary they are skilled in. Slight lean for
            stuff like heavy weapons (e.g. they probably wont be without a pistol).
            Heavy lean for stuff like melee weapons (You studied the blade, not the 
            gun afterall)
        - Chars with more nuyen are more likely to have bio augs if they are going to
            have augmentations at all. Poorer characters likely to have cyberwear
        - Chars of magic tendancies must have some magic items
        - Chars most likely will have a commlink. Skills + nuyen to influence what kind
            (e.g. techy/rich folk likely to have a better commlink)
        - Chars without arcana skill won't get magic formulae, chars with arcana will
            be likely to possess it
    """
    ch = Gear.get_gear(ch, nuyen)
    licences = Gear.check_legality(ch, gear_list=ch.Gear)
    for i in licences:
        ch.Gear.append(i)
    return


def leftover_karma(ch: Core.Character, k: Core.KarmaLogger) -> None:
    """
        If there is any leftover karma points after spending on qualities,
            spent it here
    """
    karma_budget = ch.Karma
    karma_options = [
        'Raise Attribute',
        'Raise Skill',
        'Raise Skill Group',
        'New Contact',
        'New Skill',
        'New Skill Specialisation',
        'New Spell',
        'New Complex Form',
        'New Sprite',
    ]
    if ch.MagicResoUser == 'Mystic Adept':
        magic_value = ch.Magic.value
        # Ensuring at least some, but not all karma is spent on adept powers.
        # Your fault for picking Mystic Adept anyway. He says several hundred lines
        #   into a character generator
        while karma_budget < ((magic_value * 5) + 10):
            magic_value -= 1
        power_points = random.randint(1, ch.Magic.value) 
        karma_budget -= power_points * 5
        print(f'{ch.MagicResoUser} has {power_points} to spend on powers\nCosts {power_points*5}')
        get_adept_powers(ch, power_points)

    while karma_budget > 7:
        item = random.choice(karma_options)
        # item = 'New Skill Specialisation'
        # print(item)
        match item:
            case 'Raise Attribute':
                try:
                    raised_attr = random.choice([
                        i for i in ch.AttributesCore if
                        hasattr(i, 'value') and i.value > 0 and
                        i.value != i.limit])
                    karma_attr_raise = Core.KARMA_ATTRIBUTE_COSTS[
                        raised_attr.value][raised_attr.value + 1]
                    raised_attr.value += 1
                    if karma_attr_raise >= karma_budget:
                        continue
                    else:
                        karma_budget -= karma_attr_raise
                    # print(karma_attr_raise)
                    r = raised_attr.value
                    k.append(
                        f'(EX) {raised_attr.name} has been increased to {r}.' +
                        f' Costing {karma_attr_raise}.' +
                        f'\n   {karma_budget} is Karma total.')
                except IndexError:
                    continue
                pass
            case 'Raise Skill':
                try:
                    skill_to_raise = random.choice(
                        [i for i in ch.Skills if
                         ch.Skills[i].rating < 6])
                    karma_cost_skill_raise = Core.KARMA_SKILL_COSTS['Active'][
                        ch.Skills[skill_to_raise].rating + 1]
                    # print(Core.KARMA_SKILL_COSTS['Active'][ch.Skills[
                    # 'Active'][skill_to_raise].rating + 1])
                    if karma_cost_skill_raise > karma_budget:
                        continue
                    else:
                        ch.Skills[skill_to_raise].rating += 1
                        karma_budget -= karma_cost_skill_raise
                        s1 = ch.Skills[skill_to_raise].name
                        s2 = ch.Skills[skill_to_raise].rating
                        k.append(
                            f'(EX) {s1} has been increased to {s2}.' +
                            f'Costing {karma_cost_skill_raise}.' +
                            f'\n   {karma_budget} is Karma total.')
                except IndexError:
                    continue
                pass
            case 'Raise Skill Group':
                try:
                    skill_group_to_raise = random.choice(list(set([ch.Skills[
                        s].group for s in ch.Skills if
                        hasattr(ch.Skills[s], 'group') and
                        ch.Skills[s].group is not False])))
                    skills_in_skill_group = [
                        s for s in ch.Skills if ch.Skills[
                            s].group == skill_group_to_raise]
                    karma_cost_skill_group_raise = Core.KARMA_SKILL_COSTS[
                        'Active Group'][ch.Skills[
                            skills_in_skill_group[0]].rating+1]
                    if karma_cost_skill_group_raise > karma_budget:
                        continue
                    else:
                        for skill in skills_in_skill_group:
                            ch.Skills[skill].rating += 1
                        karma_budget -= karma_cost_skill_group_raise
                        s1 = skill_group_to_raise
                        s2 = ch.Skills[
                            skills_in_skill_group[0]].rating
                        k.append(
                            f'(EX) {s1} skills have been increased to {s2}.' +
                            f'Costing {karma_cost_skill_group_raise}.' +
                            f'\n   {karma_budget} is Karma total.')
                except IndexError:
                    continue
                pass
            case 'New Contact':
                pass
            case 'New Skill':
                unskilled = [s for s in Core.ACTIVE_SKILLS if
                             s.name not in list(ch.Skills.keys())]
                new_skill = random.choice(unskilled)
                ch.Skills[new_skill.name] = new_skill
                ch.Skills[new_skill.name].rating += 1
                karma_budget -= 1
                k.append(
                    f'(EX) {new_skill.name} has been acquired as new skill.' +
                    f'Costing 1\n   {karma_budget} is Karma Total')
                pass
            case 'New Skill Specialisation':
                skills_for_spec = [s for s in ch.Skills.keys() if ch.Skills[s].rating > 3 and
                                   isinstance(ch.Skills[s].spec, list)]
                if len(skills_for_spec) == 0:
                    skills_for_spec = [s for s in ch.Skills.keys() if ch.Skills[s].rating > 2 and
                                   isinstance(ch.Skills[s].spec, list)]
                if len(skills_for_spec) == 0:
                    continue
                skill_for_spec = random.choice(skills_for_spec)
                try:
                    new_spec = random.choice(ch.Skills[skill_for_spec].spec)
                except IndexError:
                    continue
                ch.Skills[skill_for_spec].spec = new_spec
                karma_budget -= 1
                k.append(
                    f'EX \'{new_spec}\' specialisation chosen for ' +
                    f'{skill_for_spec}. Costing 1\n   {karma_budget} ' +
                    f'is Karama Total')
            case 'New Spell':
                if ch.MagicResoUser in ['Magician', 'Aspected Magician'] and karma_budget >= 5:
                    add_spell(ch)
                    karma_budget -= 5
                    new_spell = ch.Spells[len(ch.Spells)-1]
                    k.append(
                        f'(EX) {new_spell.name} has been added to spell list. ' +
                        f'Costing 5.\n   {karma_budget} is Karma Total')
                else:
                    pass
            case 'New Complex Form':
                if ch.MagicResoUser == 'Technomancer' and karma_budget >= 4:
                    add_complex_form(ch)
                    karma_budget -= 5
                    new_cf = ch.ComplexForms[len(ch.ComplexForms)-1]
                    k.append(
                        f'(EX) {new_cf.name} has been added to spell list. ' +
                        f'Costing 5.\n   {karma_budget} is Karma Total')
                else:
                    pass
            case 'New Sprite':
                pass
    return


def add_contacts(ch: Core.Character, k: Core.KarmaLogger) -> None:
    """
        Chooses contacts for character.
        The karma points used for this is separate from the karma points
            spent on qualities and later other misc bonuses.
    """
    karma = ch.Charisma.value * 3
    c = ch.Charisma.value
    k.append(
        f'[CONTACT GENERATION]. Awarding {karma} karma due to Charisma of {c}')
    while True:
        if karma <= 1:
            break
        CONTACT_ROLL = random.choice(Core.CONTACTS)
        while CONTACT_ROLL in ch.Contacts:
            CONTACT_ROLL = random.choice(Core.CONTACTS)
        contact_cost = CONTACT_ROLL.connection
        if karma - contact_cost < 4:
            if karma - contact_cost <= 0:
                break
            try:
                loyalty_cost = random.randint(1, karma - contact_cost)
            except ValueError:
                loyalty_cost = 1

        else:
            loyalty_cost = random.randint(1, 4)
        contact_cost += loyalty_cost
        karma -= contact_cost
        k.append(f'[CON]\nAdding {CONTACT_ROLL.name} as contact.' +
                 f'Conn: {CONTACT_ROLL.connection} | ' +
                 f'Loyalty: {loyalty_cost} | ' +
                 f'Total: {CONTACT_ROLL.connection + loyalty_cost}' +
                 f'\n   {karma} is remaining bonus karma')
    return


def format_skills(character_skills) -> None:
    """
        Print skills in different ways.
        First way is to group them by their group, then their rank (the latter
        only used for ungrouped skills)

        The second way is to group skills by their primary attribute
    """
    output_by_group = {'Non-Grouped': {}}

    def format_skills_specialisations():
        spec_skills = [{character_skills[s].name: character_skills[s].spec} for
                       s in character_skills.keys() if isinstance(
                           character_skills[s].spec, str)]
        if len(spec_skills) == 0:
            return 
        print("====")
        print("SPECIALISATIONS")
        for i in spec_skills:
            for k, d in i.items():
                print(f'{d}   ({k})')

    def format_skills_group_rating():
        print("====")
        print("ACTIVE SKILLS")
        print("    by Group/Rating:")

        non_grouped_skills = {}
        groups = {}
        for k, d in character_skills.items():
            if d.group is not False:
                if d.group not in groups.keys():
                    groups[d.group] = d.rating
                else:
                    continue
            d.group = "Non-Grouped"

            if isinstance(d.spec, str):
                skill_name_formatted = f'{d.name} ({d.spec})'
            else:
                skill_name_formatted = d.name

            if d.rating not in non_grouped_skills.keys():
                non_grouped_skills[d.rating] = [skill_name_formatted]
            else:
                non_grouped_skills[d.rating].append(skill_name_formatted)

        non_grouped_skills = OrderedDict(sorted(non_grouped_skills.items(), key=lambda t: t[0]))
        print("--> Non-Grouped Skills")
        for rating in non_grouped_skills.keys():
            print(f'{rating}: ', ", ".join(non_grouped_skills[rating]))

        for group in groups.keys():
            print(f"--> {group} Skill Group: {groups[group]}")




    def format_skills_attribute():
        output_by_attr = {
            'Body': None, 'Agility': None, 'Strength': None, 'Reaction': None,
            'Logic': None, 'Willpower': None, 'Intuition': None,
            'Charisma': None, 'Magic': None, 'Resonance': None
        }
        for key in list(output_by_attr.keys()):
            attribute_skills = [s for s in character_skills.keys(
            ) if character_skills[s].attribute.name == key]
            if len(attribute_skills) == 0:
                output_by_attr.pop(key)
            else:
                output_by_attr[key] = attribute_skills

        # output_by_attr = {attr: [s for s in character_skills.keys() if
        #                   character_skills[s].attribute.name == attr] for
        #                   attr in character_skill_attributes}
        # print("===")
        # print("    by Attribute:")
        # print("===")
        sorted(output_by_attr)

        for attr in output_by_attr.keys():
            # else:
            # print(f'---> {attr}')
            # print(", ".join(
            #    [f'{skill} ({character_skills[skill].rating})' for
            #     skill in output_by_attr[attr]]))
            pass

    format_skills_group_rating()
    format_skills_attribute()
    format_skills_specialisations()
    return


def buy_gear(ch: Core.Character, nuyen: int) -> None:
    vehicle_skill_ratings = [
        i.rating for i in ch.Skills.values() if
        i in Core.VEHICLE_SKILLS]
    print(vehicle_skill_ratings)
    return


def alt_generate_character():
    character = Core.Character()
    if not character:
        pass
    table_choices = ['A', 'B', 'C', 'D', 'E']
    table_categories = ['Metatype', 'Attributes',
                        'MagicResonance', 'Skills', 'Resources']
    if not table_categories:
        pass
    selected_items = {'Metatype': None, 'Attributes': None,
                      'MagicResonance': None, 'Skills': None,
                      'Resources': None}
    character_focus = random.choice(Core.Archetype.items)
    if character_focus in [archetype for archetype in Core.Archetype.items if
                           (hasattr(archetype, "magic") and
                            archetype.magic is True) or
                           (hasattr(archetype, "resonance") and
                            archetype.resonance is True)]:
        is_awakened = True
    else:
        is_awakened = False
    if is_awakened:
        awakened_table_value = random.choice(['A', 'B', 'C'])
        table_choices.pop(table_choices.index(awakened_table_value))
        selected_items['MagicResonance'] = Core.PRIORITY_TABLE_FLIPPED[
            'MagicResonance'][awakened_table_value]
    else:
        selected_items['MagicResonance'] = Core.PRIORITY_TABLE_FLIPPED[
            'MagicResonance']['E']
        table_choices.pop(table_choices.index('E'))
    print(character_focus)
    print(selected_items['MagicResonance'])


def format_qualities(ch: Core.Character) -> None:
    qual = ch.Qualities
    good_quals = ", ".join([i for i in qual.keys() if not hasattr(qual[i], 'negative')])
    bad_quals = ", ".join([i for i in qual.keys() if hasattr(qual[i], 'negative')])
    print("====")
    print('QUALITIES:')
    if len(good_quals) > 0:
        print('--->  Positive:\n', good_quals)
    if len(bad_quals) > 0:
        print('--->  Negative:\n', bad_quals)


def format_attributes(ch: Core.Character) -> None:
    attr = ch.AttributesCore
    apv = {} # apv == attr_print_values
    for attr in ch.AttributesPhysical:
        if attr is None:
            pass
        else:
            spaces = " ".join(["" for i in range(11-len(attr.name))])
            apv[attr.name] = f"{attr.name}{spaces}{attr.value} "
    for attr in ch.AttributesMental:
        if attr is None:
            pass
        else:
            spaces = " ".join(["" for i in range(11-len(attr.name))])
            apv[attr.name] = f"{attr.name}{spaces}{attr.value} "
    for attr in ch.AttributesSpecial:
        if attr is None:
            pass
        else:
            spaces = " ".join(["" for i in range(11-len(attr.name))])
            apv[attr.name] = f"{attr.name}{spaces}{attr.value} "
    print("====")
    print("ATTRIBUTES:")
    print(" Physical     | Mental       | Special ")
    print("--------------|--------------|------------")
    print("", apv['Body'], "|", apv['Willpower'], "|", apv["Edge"])
    print("", apv['Agility'], "|", apv['Logic'], "|", apv["Essence"])
    if ch.Magic is not None:
        print("", apv['Reaction'], "|", apv['Intuition'], "|", apv["Magic"])
    elif ch.Resonance is not None:
        print("", apv['Reaction'], "|", apv['Intuition'], "|", apv["Resonance"])
    else:
        print("", apv['Reaction'], "|", apv['Intuition'])
    print("", apv['Strength'], "|", apv['Charisma'], "|")


def format_table(list_name, l: list):
    print(f"===\n{list_name}")
    l = [i.__repr__() for i in l]
    longest_item = 0
    for i in l:
        if len(i) > longest_item:
            longest_item = len(i)
    print("".join(["-" for _ in range(2*longest_item+1)]))
    spaces = lambda x: " ".join(["" for i in range((longest_item+1)-len(x))])
    for i in range(len(l)):
        if i % 2 == 0:
            try:
                print("", f"{l[i]}{spaces(l[i])}", "|", f"{l[i+1]}{spaces(l[i+1])}")
            except IndexError:
                print("", f"{l[i]}{spaces(l[i])}", "|")
        else:
            pass
        


def print_shit(ch: Core.Character, nuyen, karma_log, attr_format=True):
    print('Metatype  : ', ch.Metatype.name)
    if attr_format:
        format_attributes(ch)
    else:
        print('Attributes: ')
        print('  Physical: ', ch.AttributesPhysical)
        print('    Mental: ', ch.AttributesMental)
        print('   Special: ', [i for i in ch.AttributesSpecial if i is not None])
    format_qualities(ch)
    if ch.MagicResoUser is not None and ch.MagicResoUser != 'Technomancer':
        print('Awakened:', ch.MagicResoUser)
    if ch.Spells is not None:
        format_table("SPELLS", ch.Spells)
    if ch.AdeptPowers is not None:
        format_table("ADEPT POWERS", ch.AdeptPowers)
    if ch.ComplexForms is not None:
        format_table("COMPLEX FORMS", ch.ComplexForms)
        print(0)
    # print("character karma is ", ch.Karma)
    # print(nuyen)
    # print('Karma logs:')
    # if KARMA_LOG:
    #    print(karma_log)
    format_skills(ch.Skills)
    print("===\nGEAR: \n")
    # sorted(ch.Gear)
    for item in ch.Gear:
        Item.item_format(item, compact=True)

if __name__ == "__main__":
    # Kills process if charater generation takes too long
    # In like 1% of cases the program hangs, this is to temporarily tackle that
    #   before I find and fix the issue
    p = multiprocessing.Process(target=generate_character)
    p.start()
    p.join(5)
    if p.is_alive():
        print("running too long, killing process")
        p.terminate()
        p.join()

