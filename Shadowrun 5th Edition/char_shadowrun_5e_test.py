import random
import char_shadowrun_5e_data as Core
from statistics import mean
from collections import OrderedDict

c = Core.Character()
m = Core.Character()
m.Magic = 5
r = Core.Character()
r.Resonance = 4
log = []

def roll_stats(ch: Core.Character, attr: int) -> None:
    rollable_stats = [
            ch.Body, ch.Agility, ch.Reaction, ch.Strength, ch.Willpower,
            ch.Logic, ch.Intuition, ch.Charisma, ch.Edge
            ]
    while attr > 0:
        stat_roll = random.choice(rollable_stats)
        if stat_roll.value + 1 <= stat_roll.limit:
            stat_roll.value += 1
            attr -= 1
    return ch

c.Metatype = Core.HUMAN 
for attribute in Core.HUMAN.attributes.List:
    match attribute.name:
        case 'Body':
            c.Body = Core.HUMAN.attributes.Body
        case 'Agility':
            c.Agility = Core.HUMAN.attributes.Agility
        case 'Reaction':
            c.Reaction = Core.HUMAN.attributes.Reaction
        case 'Strength':
            c.Strength = Core.HUMAN.attributes.Strength
        case 'Willpower':
            c.Willpower = Core.HUMAN.attributes.Willpower
        case 'Logic':
            c.Logic = Core.HUMAN.attributes.Logic
        case 'Intuition':
            c.Intuition = Core.HUMAN.attributes.Intuition
        case 'Charisma':
            c.Charisma = Core.HUMAN.attributes.Charisma
        case 'Edge':
            c.Edge = Core.HUMAN.attributes.Edge
        case 'Essence':
            c.Essence = Core.HUMAN.attributes.Essence
c.redo_attr()
c = roll_stats(c, 24)
print(c.CoreAttributes)

def get_highest_attr(ch: Core.Character):
    non_special_attrs = ch.PhysicalAttributes + ch.MentalAttributes
    attr_values = list(set(sorted([i.value for i in non_special_attrs])))
    highest = []
    for v in attr_values[::-1]:
        for attr in non_special_attrs:
            if attr.value == v:
                highest.append(attr)
                break
        if len(highest) > 1:
            break
    print(highest)


get_highest_attr(c)

def init_shit():
    for s in Core.Skill.items:
        if hasattr(s, 'group'):
            s.group = False
        s.rating = 0
    Core.refresh_priority_table()

def get_skills(c: Core.Character, add_back = False, add_back_plus = False, skill_cap = 50, **kwargs):
    log.append("\n\n\n\n\BEGIN SEQUENCE\n\n")
    print("\n\n\nInit gen\n")
    init_shit()
    table = Core.PRIORITY_TABLE_FLIPPED
    skill_points, group_points = table['Skills']['A']
    character_skills = {}
    list_of_skills = [skill for skill in Core.Skill.items if skill.skill_type == "Active"]
    list_of_groups = [group for group in Core.SkillGroup.items]
    if c.Magic is None:
        for _ in Core.MAGIC_SKILLS:
            list_of_skills.pop(list_of_skills.index(_))
        for _ in Core.MAGIC_SKILL_GROUPS:
            list_of_groups.pop(list_of_groups.index(_))
    if c.Resonance is None:
        for _ in Core.RESONANCE_SKILLS:
            list_of_skills.pop(list_of_skills.index(_))
        list_of_groups.pop(list_of_groups.index(Core.TASKING))
    weight_skills = [1 for _ in list_of_skills]
    weight_groups = [1 for _ in list_of_groups]
    while group_points > 0:
        ROLL_GROUP = random.choices(list_of_groups, weight_groups)[0]
        for skill in ROLL_GROUP.skills:
            if skill.name not in character_skills.keys():
                character_skills[skill.name] = skill
                character_skills[skill.name].group = ROLL_GROUP.name
                character_skills[skill.name].rating += 1
            else:
                character_skills[skill.name].rating += 1
        if add_back:
            weight_groups[list_of_groups.index(ROLL_GROUP)] += random.randint(1, 2)
            if add_back_plus:
                same_attribute_list = [s for s in list_of_skills if s.attribute == skill.attribute and s.name != skill.name]
                for same_attr in same_attribute_list:
                    weight_skills[list_of_skills.index(same_attr)] += random.randint(1, 3)
        group_points -= 1
    while skill_points > 0:
        ROLL_SKILL = random.choices(list_of_skills, weight_skills)[0]
        non_grouped_skills_count = len([i for i in character_skills.keys() if character_skills[i].group == False])
        if ROLL_SKILL.name in character_skills.keys() and character_skills[ROLL_SKILL.name].group != False:
            pass
        elif ROLL_SKILL.name not in character_skills.keys() and non_grouped_skills_count >= skill_cap:
            pass
        else:
            if ROLL_SKILL.name not in character_skills.keys():
                character_skills[ROLL_SKILL.name] = ROLL_SKILL
            elif character_skills[ROLL_SKILL.name].rating >= 12:
                continue
            character_skills[ROLL_SKILL.name].rating += 1
            if add_back:
                match weight_skills[list_of_skills.index(ROLL_SKILL)]:
                    case 1,2,3:
                        weight_skills[list_of_skills.index(ROLL_SKILL)] += random.randint(1,5)
                    case _:
                        weight_skills[list_of_skills.index(ROLL_SKILL)] += random.randint(1,2)
                if add_back_plus:
                    if ROLL_SKILL.group != False:
                        for group in list_of_groups:
                            if ROLL_SKILL in group.skills:
                                for gskill in group.skills:
                                    weight_skills[list_of_skills.index(gskill)] += random.randint(1,3)
                    same_attribute_list = [skill for skill in list_of_skills if skill.attribute == ROLL_SKILL.attribute and skill.name != ROLL_SKILL.name]
                    for same_attr in same_attribute_list:
                        weight_skills[list_of_skills.index(same_attr)] += random.randint(1, 3)
                    else:
                        pass
            skill_points -= 1
    return character_skills
    
def get_highest_attr(ch: Core.Character):
    log.append("Starting Sequence\n")
    non_special_attrs = [ch.Body, ch.Agility, ch.Reaction, ch.Strength,
                         ch.Willpower, ch.Logic, ch.Intuition, ch.Charisma]
    highest = 0
    highest_attrs = []
    second_highest = 0
    second_attrs = []
    for idx, i in enumerate(non_special_attrs):
        log.append(f"On {i} iteration of {idx} index")
        if non_special_attrs[idx].value > highest:
            second_highest = highest
            highest = non_special_attrs[idx].value
            log.append(f"new {highest} is more than the old {second_highest}")
    if second_highest == 0:
        second_highest = highest - 1 
        while len([attr for attr in non_special_attrs if attr.value == second_highest]) < 1:
            second_highest -= 1

    highest_attrs = [attr for attr in non_special_attrs if attr.value == highest]
    if len(highest_attrs) > 1:
        log.append('Length of values at max is greater than one')
        return highest_attrs
    else:
        second_attrs = [attr for attr in non_special_attrs if attr.value == second_highest]
        if len(second_attrs) < 1:
            print(non_special_attrs)
            print(highest)
            print(highest_attrs)
            print(second_highest)
            print(second_attrs)
            raise IndexError("Fuck")

        return [highest_attrs[0], second_attrs[0]]
    print("====")
    for attr in output_by_attr.keys():
        print(f'    {attr}')
        print(" ".join([skill for skill in output_by_attr[attr]]))

def leftover_karma(ch: Core.Character, k: Core.KarmaLogger):
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
            'New Sprite'
            ]
    while karma_budget > 7:
        item = random.choice(karma_options)
        match item:
            case 'Raise Attribute':
                try:
                    raised_attr = random.choice([i for i in ch.CoreAttributes if i.value > 0 and i.value != i.limit])
                    raised_attr.value += 1
                    karma_budget -= 1
                    k.append(f'(EX) {raised_attr.name} has been increased to {raised_attr.value}. Costing 1.\n   {karma_budget} is Karma total.')
                    print(f'(EX) {raised_attr.name} has been increased to {raised_attr.value}. Costing 1.\n   {karma_budget} is Karma total.')
                except IndexError:
                    continue
                pass
            case 'Raise Skill':
                try:
                    skill_to_raise = random.choice([i for i in ch.Skills if ch.Skills[i].rating < 6])
                    karma_cost_skill_raise = Core.KARMA_SKILL_COSTS['Active'][ch.Skills[skill_to_raise].rating + 1]
                    if karma_cost_skill_raise > karma_budget:
                        continue
                    else:
                        ch.Skills[skill_to_raise].rating += 1
                        karma_budget -= karma_cost_skill_raise
                        k.append(f'(EX) {ch.Skills[skill_to_raise].name} has been increased to {ch.Skills[skill_to_raise].rating}. Costing {karma_cost_skill_raise}.\n   {karma_budget} is Karma total.')
                        print(f'(EX) {ch.Skills[skill_to_raise].name} has been increased to {ch.Skills[skill_to_raise].rating}. Costing {karma_cost_skill_raise}.\n   {karma_budget} is Karma total.')
                except IndexError:
                    continue
                pass
            case 'Raise Skill Group':
                try:
                    skill_group_to_raise = random.choice(list(set([ch.Skills[s].group for s in ch.Skills if ch.Skills[s].group != False])))
                    skills_in_skill_group = [s for s in ch.Skills if ch.Skills[s].group == skill_group_to_raise]
                    karma_cost_skill_group_raise = Core.KARMA_SKILL_COSTS['Active Group'][ch.Skills[skills_in_skill_group[0]].rating+1]
                    if karma_cost_skill_group_raise > karma_budget:
                        continue
                    else:
                        for skill in skills_in_skill_group:
                            ch.Skills[skill].rating += 1
                        karma_budget -= karma_cost_skill_group_raise
                        k.append(f'(EX) {skill_group_to_raise} skills have been increased to {ch.Skills[skills_in_skill_group[0]].rating}. Costing {karma_cost_skill_group_raise}.\n   {karma_budget} is Karma total.')
                        print(f'(EX) {skill_group_to_raise} skill group {[i for i in ch.Skills if ch.Skills[i].group == skill_group_to_raise]} have been increased to {ch.Skills[skills_in_skill_group[0]].rating}. Costing {karma_cost_skill_group_raise}.\n   {karma_budget} is Karma total.')
                except IndexError:
                    continue
                pass
            case 'New Contact':
                pass
            case 'New Skill':
                pass
            case 'New Skill Specialisation':
                pass
            case 'New Spell':
                pass
            case 'New Complex Form':
                pass
            case 'New Sprite':
                pass

def get_knowledge_language_skills(ch: Core.Character):
    kl_skill_points = 2*(ch.Intuition.value + ch.Logic.value)
    print(f"character gets {kl_skill_points} knowledge/skill points")
    native_language = random.choice([l for l in Core.Skill.items if l.skill_type == "Language" and l.category == "Tongue"])
    native_language.rating = "N"
    print(native_language)

