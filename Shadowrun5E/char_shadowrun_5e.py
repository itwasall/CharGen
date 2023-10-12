import random
import data as Core
import gear as Gear
import item as Item
import skills as Skills
import attributes as Attributes
import multiprocessing
import time
from collections import OrderedDict

KARMA_LOG = False


def generate_character(karma_logging = True) -> Core.Character:
    out = []
    if karma_logging:
        karma_log = Core.KarmaLogger()
    # STEP 1: CONCEPT
    character = Core.Character()
    # TEST FOR NON-MAGIC CHARACTERS
    # priority_table = get_priorities(character, defaults={'MagicResonance': 'E'})
    priority_table = get_priorities(character)
    attribute_points = priority_table['Attributes']
    nuyen = priority_table['Resources']
    magic_reso = priority_table['MagicResonance']
    metatype = random.choice(priority_table['Metatype'])
    # STEP 2: METATYPE & ATTRIBUTES
    special_attribute_points = metatype[1]
    metatype = metatype[0]
    character.Metatype = metatype
    Attributes.generate_attributes(character, character.Metatype)
    Attributes.roll_stats(character, attribute_points)
    highest_attrs = Attributes.get_highest_attr(character)
    # STEP 3: MAGIC/RESONANCE
    resolve_magic_resonance(out, character, magic_reso, priority_table)
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
            out.append('Character is decker')
        elif build == 'Rigger':
            ch.IS_RIGGER = True
            out.append('Character is rigger')
        elif build == 'Face':
            ch.IS_FACE = True
            out.append('Character is face')
    skill_builds = {'IS_DECKER': IS_DECKER,
                    'IS_RIGGER': IS_RIGGER, 'IS_FACE': IS_FACE}
    # STEP 4: QUALITIES
    get_qualities(character, karma_log)
    # STEP 5: SKILLS
    get_skills(character, priority_table, attr_influence=highest_attrs,
               skill_cap=20, builds=skill_builds)
    Skills.get_language_knowledge_skills(character)
    if character.MagicResoUser == "Adept":
        get_adept_powers(character, character.Magic.value)

            

    """
        dealing with this later
    """
    #if 'Exotic Melee Weapon' in character.Skills:
    #    character = resolve_specific_skill(character, Core.EXOTIC_MELEE_WEAPON)
    add_contacts(character, karma_log)
    get_gear(character, nuyen)
    leftover_karma(out, character, karma_log)
    #out.append(karma_log)
    calculate_remaining_stats(character)
    return out, character, nuyen, karma_log


def get_priorities(character: Core.Character, defaults=None) -> dict:
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
    if defaults is not None:
        for key in defaults.keys():
            selected_items[key] = Core.PRIORITY_TABLE_FLIPPED[key][defaults[key]]
            table_choices.pop(table_choices.index(defaults[key]))
        categories = [k for k in selected_items.keys() if k not in defaults.keys()]
    else:
        categories = [k for k in selected_items.keys()]
    for category in categories:
        if selected_items[category] is not None:
            continue
        new_priority = random.choice(table_choices)
        table_choices.pop(table_choices.index(new_priority))
        selected_items[category] = Core.PRIORITY_TABLE_FLIPPED[
            category][new_priority]
    return selected_items


def resolve_magic_resonance(out, ch: Core.Character, tbl, priority_table) -> None:
    """
        If a character weilds magic or is a technomancer,
            give them the relevant stats and abilities here.
    """
    if tbl is None:
        return
    _type = random.choice(list(tbl.keys()))
    ch.MagicResoUser = str(_type)
    #out.append(f'Uh oh! Looks like you\'re a {ch.MagicResoUser}')

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
        if hasattr(new_power, "requires"):
            if new_power.requires.__class__ == Core.Skill:
                if not new_power.requires.name in ch.Skills.keys():
                    continue
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
    def make_karma_message(polarity, quality, total_karma, polarity_karma):
        karma_message = [
                f'{polarity} {quality.name} has been bought. ', 
                f'Costing {quality.cost}\n   {total_karma} is Karma total',
                f'\n{polarity} karma is at {polarity_karma}']
        return karma_message

    ch.Qualities = {}
    ch.Qualities['Incompetent'] = Core.INCOMPETENT
    total_karma = 25
    positive_karma, negative_karma = 0, 0
    k.append(f'Beginning karma logging.\n   {total_karma} is Karma total')
    NEGATIVE_CAP, POSITIVE_CAP = False, False
    quality_list = [i for i in Core.Quality.items]
    resolve_quality_list(ch, quality_list)
    quality_weights = [1 for _ in quality_list]
    inc = 0
    while total_karma > 0 and inc < 100:
        inc += 1
        ch.Karma = total_karma
        # There's an infinite loop I can't be bothered to fix right now, this
        # will do
        if (total_karma < 10 and random.randint(0, 1) == 1) or \
                total_karma <= 0:
            break
        ROLL_QUALITY = random.choices(quality_list, quality_weights)[0]
        # If a quality in the same group has already been taken, continue
        # (SEE DATA)
        if hasattr(ROLL_QUALITY, "group") and ROLL_QUALITY.group in [
                d.group for d in ch.Qualities.values() if hasattr(d, "group")]:
            continue
        # Negative qualities cannot total more than ABS(25)
        if hasattr(ROLL_QUALITY, "negative"
                   ) and negative_karma + ROLL_QUALITY.cost > 25:
            NEGATIVE_CAP = True
            continue
            # continue
        # Positive qualities cannot total more than ABS(25)
        elif positive_karma + ROLL_QUALITY.cost > 25:
            POSITIVE_CAP = True
            continue
            # continue
        if (total_karma - ROLL_QUALITY.cost < 0) or  (
                NEGATIVE_CAP != POSITIVE_CAP):
            continue
        if hasattr(ROLL_QUALITY, "negative"):
            negative_karma += ROLL_QUALITY.cost
            total_karma += ROLL_QUALITY.cost
            k.append(make_karma_message(
                'NEG', ROLL_QUALITY, total_karma, negative_karma))
        else:
            positive_karma += ROLL_QUALITY.cost
            total_karma -= ROLL_QUALITY.cost
            k.append(make_karma_message(
                'POS', ROLL_QUALITY, total_karma, positive_karma))

        # Pretty output & roll for quality specific params here
        ROLL_QUALITY = resolve_quality_level(ROLL_QUALITY, ch)

        ch.Qualities[ROLL_QUALITY.name] = ROLL_QUALITY
        if hasattr(ROLL_QUALITY, "quantity"):
            if hasattr(ch.Qualities[ROLL_QUALITY.name], "level"):
                ch.Qualities[ROLL_QUALITY.name].level += 1
            else:
                ch.Qualities[ROLL_QUALITY.name].level = 1
            quality_weights[quality_list.index(ROLL_QUALITY)] += 10
        if NEGATIVE_CAP and POSITIVE_CAP:
            break
    #out.append(ch.Qualities)
    return


def resolve_quality_list(ch: Core.Character, quality_list) -> list[Core.Quality]:
    if ch.Metatype.name == 'Human':
        quality_list.pop(quality_list.index(Core.HUMAN_LOOKING))
    elif ch.Metatype.name == 'Elf':
        quality_list.pop(quality_list.index(Core.ELF_POSER))
    elif ch.Metatype.name == 'Ork':
        quality_list.pop(quality_list.index(Core.ORK_POSER))



def resolve_quality_level(q: Core.Quality, ch: Core.Character) -> Core.Quality:
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


def get_skills(ch: Core.Character, tbl, skill_cap=10, attr_influence=None, **kwargs) -> None:
    return Skills.get_skills(ch, tbl, skill_cap, attr_influence, **kwargs)



def get_gear(ch: Core.Character, nuyen: int) -> None:
    ch = Gear.get_gear(ch, nuyen)
    licences = Gear.check_legality(ch, gear_list=ch.Gear)
    for i in licences:
        ch.Gear.append(i)
    for i in ch.Gear:
        if hasattr(i, "armor_rating"):
            ch.Armor += i.armor_rating
    return


def leftover_karma(out, ch: Core.Character, k: Core.KarmaLogger) -> None:
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
        out.append(f'{ch.MagicResoUser} has {power_points} to spend on powers\nCosts {power_points*5}')
        get_adept_powers(ch, power_points)

    while karma_budget > 7:
        item = random.choice(karma_options)
        # item = 'New Skill Specialisation'
        #out.append(item)
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
                    #out.append(karma_attr_raise)
                    r = raised_attr.value
                    k.append(
                        f'(EX) {raised_attr.name} has been increased to {r}.' +
                        f' Costing {karma_attr_raise}.' +
                        f'\n   {karma_budget} is Karma total.')
                except IndexError:
                    continue
                pass
            case 'Raise Skill':
                ch, k, karma_budget = Skills.karma_spend_raise_skill(ch, k, karma_budget)
                pass
            case 'Raise Skill Group':
                ch, k, karma_budget = Skills.karma_spend_raise_skill_group(ch, k, karma_budget)
            case 'New Contact':
                pass
            case 'New Skill':
                ch, k, karma_budget = Skills.karma_spend_new_skill(ch, k, karma_budget)
            case 'New Skill Specialisation':
                ch, k, karma_budget = Skills.karma_spend_new_skill_specialisation(ch, k, karma_budget)
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
        ch.Contacts[CONTACT_ROLL.name] = {'Contact': CONTACT_ROLL, 'Connection': CONTACT_ROLL.connection, 'Loyalty': loyalty_cost}
    return


def buy_gear(out, ch: Core.Character, nuyen: int) -> None:
    vehicle_skill_ratings = [
        i.rating for i in ch.Skills.values() if
        i in Core.VEHICLE_SKILLS]
    out.append(vehicle_skill_ratings)
    return


def roll_dice(dicestring) -> int:
    throws, sides = dicestring.split('d')
    return sum([random.randint(1, int(sides)) for _ in range(int(throws))])


def calculate_remaining_stats(ch: Core.Character) -> None:
    ch.LivingPersonaAttack = Core.Attribute(
            'Living Persona: Attack', value=ch.Charisma.value)
    ch.LivingPersonaDataProcessing = Core.Attribute(
            'Living Persona: Data Processing', value=ch.Logic.value)
    if ch.Resonance is not None:
        ch.LivingPersonaDeviceRating = Core.Attribute(
                'Living Persona: Device Rating', value=ch.Resonance.value)
    else:
        ch.LivingPersonaDeviceRating = None
    ch.LivingPersonaFirewall = Core.Attribute(
            'Living Persona: Firewall', value=ch.Willpower.value)
    ch.LivingPersonaSleaze = Core.Attribute(
            'Living Persona: Sleaze', value=ch.Intuition.value)

    ch.Initiative = ch.Intuition.value + ch.Reaction.value + roll_dice('1d6')
    ch.InitiativeAstral = (ch.Intuition.value * 2) + roll_dice('3d6')
    ch.InitiativeMatrixAR = ch.Intuition.value + ch.Reaction.value + roll_dice('1d6')
    ch.InitiativeMatrixVRCold = (ch.LivingPersonaDataProcessing.value + ch.Intuition.value) + roll_dice('3d6')
    ch.InitiativeMatrixVRHot = (ch.LivingPersonaDataProcessing.value + ch.Intuition.value) + roll_dice('4d6')

    ch.LimitMental = round(((ch.Logic.value * 2) + ch.Intuition.value + ch.Willpower.value) / 3)
    ch.LimitPhysical = round(((ch.Strength.value * 2) + ch.Body.value + ch.Essence.value) / 3)
    ch.LimitSocial = round(((ch.Charisma.value * 2) + ch.Willpower.value + ch.Essence.value) / 3)

    ch.ConditionalMonitorPhysical = round(ch.Body.value / 2) + 8
    ch.ConditionalMonitorStun =  round(ch.Willpower.value / 2) + 8
    ch.ConditionalMonitorOverflow = ch.Body.value


def alt_generate_character():
    out = []
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
    out.append(character_focus)
    out.append(selected_items['MagicResonance'])


def format_skills(out, character_skills, compact=False) -> None:
    """
        Print skills in different ways.
        First way is to group them by their group, then their rank (the latter
        only used for ungrouped skills)

        The second way is to group skills by their primary attribute
    """
    output_by_group = {'Non-Grouped': {}}

    def format_skills_specialisations(out, compact = False):
        if compact:
            out.append(f"===\nSPECIALISATIONS\n{[{character_skills[s].name: character_skills[s].spec} for s in character_skills.keys() if isinstance( character_skills[s].spec, str)]}")
            return
        spec_skills = [{character_skills[s].name: character_skills[s].spec} for
                       s in character_skills.keys() if isinstance(
                           character_skills[s].spec, str)]
        if len(spec_skills) == 0:
            return 
        out.append("====")
        out.append("SPECIALISATIONS")
        for i in spec_skills:
            for k, d in i.items():
                out.append(f'{d}   ({k})')

    def format_skills_group_rating(out, compact=False):
        out.append("====")
        out.append("ACTIVE SKILLS")

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
        out.append("--> Non-Grouped Skills")
        for rating in non_grouped_skills.keys():
            if rating == -1:
               out.append(f'Unaware: {", ".join(non_grouped_skills[rating])}')
            else:
               out.append(f'{rating}: {", ".join(non_grouped_skills[rating])}')

        for group in groups.keys():
            if groups[group] < 0:
               out.append(f"--> {group} Skill Group: Unaware")
            else:
               out.append(f"--> {group} Skill Group: {groups[group]}")




    def format_skills_attribute(out):
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

        output_by_attr = {attr: [s for s in character_skills.keys() if
                          character_skills[s].attribute.name == attr] for
                          attr in character_skill_attributes}
        out.append("===")
        out.append("    by Attribute:")
        out.append("===")
        sorted(output_by_attr)

        for attr in output_by_attr.keys():
            out.append(f'---> {attr}')
            out_list = (", ".join(
               [f'{skill} ({character_skills[skill].rating})' for
                skill in output_by_attr[attr]]))
            out.append(out_list)

    format_skills_group_rating(out)
    format_skills_specialisations(out)
    return


def format_qualities(out, ch: Core.Character, compact=False) -> None:
    qual = ch.Qualities
    good_quals = ", ".join([i for i in qual.keys() if not hasattr(qual[i], 'negative')])
    bad_quals = ", ".join([i for i in qual.keys() if hasattr(qual[i], 'negative')])
    out.append("====")
    out.append('QUALITIES:')
    if compact:
        if len(good_quals) > 0:
            out.append(f'--->  Positive: {[i for i in good_quals]}')
        if len(bad_quals) > 0:
            out.append(f'--->  Negative: {[i for i in bad_quals]}')
        return
    if len(good_quals) > 0:
        out.append(f'--->  Positive:\n {good_quals}')
    if len(bad_quals) > 0:
        out.append(f'--->  Negative:\n {bad_quals}')


def format_attributes(out, ch: Core.Character, compact=False) -> None:
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
    out.append("====")
    out.append("ATTRIBUTES:")
    if compact:
        if ch.Magic is not None:
            out.append(f"{apv['Body']}, {apv['Agility']}, {apv['Reaction']}, {apv['Strength']}, {apv['Willpower']}, {apv['Logic']}, {apv['Intuition']}, {apv['Charisma']}, {apv['Edge']}, {apv['Essence']}, {apv['Magic']}")
        elif ch.Resonance is not None:
            out.append(f"{apv['Body']}, {apv['Agility']}, {apv['Reaction']}, {apv['Strength']}, {apv['Willpower']}, {apv['Logic']}, {apv['Intuition']}, {apv['Charisma']}, {apv['Edge']}, {apv['Essence']}, {apv['Resonance']}")
        else:
            out.append(f"{apv['Body']}, {apv['Agility']}, {apv['Reaction']}, {apv['Strength']}, {apv['Willpower']}, {apv['Logic']}, {apv['Intuition']}, {apv['Charisma']}, {apv['Edge']}, apv['Essence']")
        return
    out.append(" Physical     | Mental       | Special ")
    out.append("--------------|--------------|------------")
    out.append(f" {apv['Body']} | {apv['Willpower']} | {apv['Edge']}")
    out.append(f" {apv['Agility']} | {apv['Logic']} | {apv['Essence']}")
    if ch.Magic is not None:
        out.append(f" {apv['Reaction']} | {apv['Intuition']} | {apv['Magic']}")
    elif ch.Resonance is not None:
        out.append(f" {apv['Reaction']} | {apv['Intuition']} | {apv['Resonance']}")
    else:
        out.append(f" {apv['Reaction']} | {apv['Intuition']} | ")
    out.append(f" {apv['Strength']} | {apv['Charisma']} | ")


def format_table(out, list_name, l: list, compact=False):
    out.append(f"===\n{list_name}")
    if compact:
        out.append([i for i in l])
        return
    l = [i.__repr__() for i in l]
    longest_item = 0
    for i in l:
        if len(i) > longest_item:
            longest_item = len(i)
    out.append("".join(["-" for _ in range(2*longest_item+1)]))
    spaces = lambda x: " ".join(["" for i in range((longest_item+1)-len(x))])
    for i in range(len(l)):
        if i % 2 == 0:
            try:
                out.append(f" {l[i]}{spaces(l[i])}  |  {l[i+1]}{spaces(l[i+1])}")
            except IndexError:
                out.append(f" {l[i]}{spaces(l[i])}  |")
        else:
            pass


def format_gear(out, ch: Core.Character, item_compact=True, compact=False):
    if compact:
        out.append(f"===\nGEAR\n{[(type(i), i.name) for i in ch.Gear]}")
        return
    gear_licenses = []
    out.append("===\nGEAR")
    for item in ch.Gear:
        if "Fake License" in item.name:
            gear_licenses.append(item)
        else:
            out = Item.item_format(out, item, compact=item_compact)
    if len(gear_licenses) > 0:
        out.append(f"Fake licenses: {[i.name.split('Fake License (')[1][:-1] for i in gear_licenses if i.name != 'Fake License (None)']}")


def format_contacts(out, ch: Core.Character, compact=True):
    out.append("===\nCONTACTS")
    if len(ch.Contacts.keys()) > 0:
        if compact:
            for i in ch.Contacts:
                x = ch.Contacts[i]
                y = ch.Contacts[i]['Contact']
                out.append(f'{y.name}  Connection: {x["Connection"]} Loyalty: {x["Loyalty"]}')
        else:
            raise NotImplemented
    else:
        out.append("NONE")


def format_other_stats(out, ch: Core.Character) -> None:
    other_stat_list = [ch.Initiative, 
                 ch.InitiativeAstral,
                 ch.InitiativeMatrixAR, 
                 ch.InitiativeMatrixVRHot, 
                 ch.InitiativeMatrixVRCold, 
                 ch.ConditionalMonitorStun, 
                 ch.ConditionalMonitorOverflow, 
                 ch.ConditionalMonitorPhysical]
    for attr in other_stat_list:
        if attr < 10:
               other_stat_list[other_stat_list.index(attr)] = f"0{attr}"
        else:
            pass

#    ch.Initiative = zero_fill(ch.Initiative)
 #   ch.InitiativeAstral = zero_fill(ch.InitiativeAstral)
 #   ch.InitiativeMatrixAR = zero_fill(ch.InitiativeMatrixAR)
 #   ch.InitiativeMatrixVRHot = zero_fill(ch.InitiativeMatrixVRHot)
 #   ch.InitiativeMatrixVRCold = zero_fill(ch.InitiativeMatrixVRCold)
 #   ch.ConditionalMonitorPhysical= zero_fill(ch.ConditionalMonitorPhysical)
 #   ch.ConditionalMonitorStun = zero_fill(ch.ConditionalMonitorStun)
 #   ch.ConditionalMonitorOverflow = zero_fill(ch.ConditionalMonitorOverflow)

    out.append(f"---------------------------------------------")
    out.append(f"    Initiative")
    out.append(f"---------------------------------------------")
    out.append(f"       Initiative   | {ch.Initiative}")
    out.append(f"        Matrix AR   | {ch.InitiativeMatrixAR}")
    out.append(f"  Matrix VR (Hot)   | {ch.InitiativeMatrixVRHot}")
    out.append(f" Matrix VR (Cold)   | {ch.InitiativeMatrixVRCold}")
    out.append(f"           Astral   | {ch.InitiativeAstral}")
    out.append("")
    out.append(f"------------------------------------------")
    out.append(f" Inherent  Limits   | Condition Monitor ")
    out.append(f"--------------------|---------------------")
    out.append(f"    Mental Limit: {ch.LimitMental} | Physical: {ch.ConditionalMonitorPhysical}")
    out.append(f"  Physical Limit: {ch.LimitPhysical} |     Stun: {ch.ConditionalMonitorStun}")
    out.append(f"    Social Limit: {ch.LimitSocial} | Overflow: {ch.ConditionalMonitorOverflow}")




def print_shit(out, ch: Core.Character, nuyen, karma_log, attr_format=True, compact=False):
    out.append(f'Metatype  : {ch.Metatype.name}')
    if attr_format:
        format_attributes(out, ch, compact)
    else:
        out.append('Attributes:out,  ')
        out.append(f'  Physical: {ch.AttributesPhysical}')
        out.append(f'    Mental: {ch.AttributesMental}')
        out.append(f'   Special: {[i for i in ch.AttributesSpecial if i is not None]}')
    format_qualities(out, ch)
    if ch.MagicResoUser is not None and ch.MagicResoUser != 'Technomancer':
        out.append(f'Awakened: {ch.MagicResoUser}')
    if ch.Spells is not None:
        format_table(out, "SPELLS", ch.Spells, compact)
    if ch.AdeptPowers is not None:
        format_table(out, "ADEPT POWERS", ch.AdeptPowers, compact)
    if ch.ComplexForms is not None:
        format_table(out, "COMPLEX FORMS", ch.ComplexForms, compact)
    #out.append("character karma is ", ch.Karma)
    #out.append(nuyen)
    #out.append('Karma logs:')
    # if KARMA_LOG:
    #   out.append(karma_log)
    format_skills(out, ch.Skills, compact)
    format_gear(out, ch, compact=False)
    format_contacts(out, ch)
    out.append("===\nOTHER STATS:")
    out.append(f'Armor Rating: {ch.Armor}')
    format_other_stats(out, ch)
    out.append("===\nNUYEN: ")
    out.append(ch.Nuyen)
    return out

if __name__ == "__main__":
    import sys, time
    def quick_exec(filename):
        out, x, nuyen, karma_log = generate_character()
        out = print_shit(out, x, nuyen, karma_log, compact=False)
        with open(filename, "wt") as f:
            for line in out:
                f.write(f"{line}\n")
        f.close()

    def quick_exec_print():
        out, x, nuyen, karma_log = generate_character()
        out = print_shit(out, x, nuyen, karma_log, compact=False)
        for i in out:
            print(i)


    def main_routine(filename):
        print("\n")
        print(" ^-~*~-* WELCOME TO THE SHADOWRUN 5TH EDITION *-~*~-^ ")
        print(" ^-~*~.~*~-^  RANDOM CHARACTER GENERATOR  ^-~*~.~*~-^ ")
        print("")
        time.sleep(1)
        print("    ######## THIS TOOL IS INCOMPLETE ########    ")
        time.sleep(1)
        i = input("!!!== Press {Enter} to Begin Character Generation ==!!!")
        if i in ["", "y", "Y"]:
            print("--> Beginning Charcter Generation...")
            time.sleep(2)
            # Kills process if charater generation takes too long
            # In like 1% of cases the program hangs, this is to temporarily tackle that
            #   before I find and fix the issue
            out, x, nuyen, karma_log = generate_character()
            print("--> Charcter Generation Completed...")
            time.sleep(2)
            out = print_shit(out, x, nuyen, karma_log, compact=False)
            print("--> Text Formatting Completed...\n")
            print(f"--> Writing Character Data to {filename}...")
            print("")
            with open(filename, "wt") as f:
                for line in out:
                    f.write(f"{line}\n")
            f.close()
            time.sleep(2)
            print(f"--> Written Character to {filename}!")
            print("")
            print(" <.*~-*.> TOOL MADE BY github.com/itwasall <.*-~*.> ")
            # p = multiprocessing.Process(target=generate_character)
            # p.start()
            # p.join(5)
            # if p.is_alive():
            #    out.append("running too long, killing process")
            #     p.terminate()
            #    p.join()
        elif i in ["q", "Q", "n", "N", "exit", "no", "No", "NO"]:
            print(" _*~^~*~^~*:  Today's not the day choomer :*~^~*~^~*_ ")
            print(" <.*~-*.> TOOL MADE BY github.com/itwasall <.*-~*.> ")


    def argument_parse():
        if len(sys.argv) <= 1 or sys.argv[1] in ['-h', '--help']:
            print("char_shadowrun_5e.py\n    USAGE: python3 char_shadowrun_5e.py [options] -f [filename]")
            print("        OPTIONS:")
            print("                 -q --quick: Skips all my cool ascii text I whipped up and writes to file as quickly as possible")
            print("                 -p --print: Prints all data to console. If no -f --filename argument is provided, nothing is written to disk")
            return
        elif '--print' in sys.argv or '-p' in sys.argv:
            if '-f' not in sys.argv:
                quick_exec_print()
                return
            else:
                quick_exec(sys.argv[sys.argv.index('-f') + 1])
                return
        if '-f' not in sys.argv:
            raise IndexError("Please give a filename with the '-f' argument!")
        if '-q' in sys.argv or '--quick' in sys.argv:
            quick_exec(sys.argv[sys.argv.index('-f') + 1])
        main_routine(sys.argv[sys.argv.index('-f') + 1])

    argument_parse()


