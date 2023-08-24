import random
import char_shadowrun_5e_data as Core
from statistics import mean
from collections import OrderedDict

c = Core.Character()
m = Core.Character()
m.Magic = 5
r = Core.Character()
r.Resonance = 4

def init_shit():
    for s in Core.Skill.items:
        if hasattr(s, 'group'):
            s.group = False
        s.rating = 0
    Core.refresh_priority_table()

def get_skills(c: Core.Character, add_back = False, add_back_plus = False, skill_cap = 50, **kwargs):
    log = []
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

    # Group Skill Points spend
    # for _ in range(group_points):
    log.append("\n\nbeing group point spend\n")
    while group_points > 0:
        ROLL_GROUP = random.choices(list_of_groups, weight_groups)[0]
        for skill in ROLL_GROUP.skills:
            # print(f"Roll group {ROLL_GROUP.name} processing {skill.name}")
            if skill.name not in character_skills.keys():
                character_skills[skill.name] = skill
                character_skills[skill.name].group = ROLL_GROUP.name
                character_skills[skill.name].rating += 1
            else:
                character_skills[skill.name].rating += 1
            log.append(f"skill {skill.name} has +1 rating to {character_skills[skill.name].rating}")
        if add_back:
            weight_groups[list_of_groups.index(ROLL_GROUP)] += random.randint(1, 2)
            if add_back_plus:
                same_attribute_list = [s for s in list_of_skills if s.attribute == skill.attribute and s.name != skill.name]
                for same_attr in same_attribute_list:
                    weight_skills[list_of_skills.index(same_attr)] += random.randint(1, 3)
                
        group_points -= 1
            
    # Individual Skill Points spend
    # for _ in range(skill_points):
    log.append("\n\nbeing individual point spend\n")
    while skill_points > 0:
        ROLL_SKILL = random.choices(list_of_skills, weight_skills)[0]
        non_grouped_skills_count = len([i for i in character_skills.keys() if character_skills[i].group == False])
        if ROLL_SKILL.name in character_skills.keys() and character_skills[ROLL_SKILL.name].group != False:
            log.append(f"{ROLL_SKILL.name} being ignored because it's group is {character_skills[ROLL_SKILL.name].group}")
            pass
        elif ROLL_SKILL.name not in character_skills.keys() and non_grouped_skills_count >= skill_cap:
            pass
        else:
            if ROLL_SKILL.name not in character_skills.keys():
                log.append(f"{ROLL_SKILL.name} not in character_skills, creating")
                character_skills[ROLL_SKILL.name] = ROLL_SKILL
            elif character_skills[ROLL_SKILL.name].rating >= 12:
                log.append(f"{ROLL_SKILL.name}'s rating ({character_skills[ROLL_SKILL.name].rating}) is too high!")
                continue
            character_skills[ROLL_SKILL.name].rating += 1
            log.append(f"skill {ROLL_SKILL.name} has +1 rating to {character_skills[ROLL_SKILL.name].rating}")
            log.append(f"SHOULD BE FALSE: {character_skills[ROLL_SKILL.name].group}")
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
    
    # Getting debug output_by_group. Sorts skills by group first, then by ranking
    output_by_group = {'Non-Grouped': {}}
    output_by_attr = {}
    for k, d in character_skills.items():
        if d.attribute.name not in output_by_attr.keys():
            output_by_attr[d.attribute.name] = [d.name]
        else:
            output_by_attr[d.attribute.name].append(d.name)
        if d.group != False:
            if d.group not in output_by_group.keys():
                output_by_group[d.group] = {}
                if d.rating not in output_by_group[d.group].keys():
                    output_by_group[d.group][d.rating] = [d.name]
                else:
                    output_by_group[d.group][d.rating].append(d.name)
            else:
                if d.rating not in output_by_group[d.group].keys():
                    output_by_group[d.group][d.rating] = [d.name]
                else:
                    output_by_group[d.group][d.rating].append(d.name)
        else:
            if d.rating not in output_by_group['Non-Grouped'].keys():
                output_by_group['Non-Grouped'][d.rating] = [d.name]
            else:
                output_by_group['Non-Grouped'][d.rating].append(d.name)

    for group in output_by_group.keys():
        output_by_group[group] = OrderedDict(sorted(output_by_group[group].items(), key=lambda t: t[0]))
        print(group)
        for rating in output_by_group[group].keys():
            print(rating, output_by_group[group][rating])
    
    print("====")
    for attr in output_by_attr.keys():
        print(f'    {attr}')
        print(" ".join([skill for skill in output_by_attr[attr]]))





    f = open('shadowrun_5e_test_out', 'wt')
    for _ in log:
        f.write(f"\n{_}")
    f.close()


b = Core.Character()
b.debug_gen_attrs(magic=True)
c = Core.Character()
c.debug_gen_attrs(magic=True)
d = Core.Character()
d.debug_gen_attrs(magic=True, techo=True)
# get_skills(c, add_back=True, add_back_plus=True, skill_cap=13)
# get_skills(c, add_back=True, add_back_plus=False)
# get_skills(d, add_back=True, add_back_plus=True)
