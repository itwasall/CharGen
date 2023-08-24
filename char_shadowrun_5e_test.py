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

def get_skills(c: Core.Character, add_back = False, add_back_plus = False, **kwargs):
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
        print(type(ROLL_GROUP))
        for skill in ROLL_GROUP:
            print(f"Roll group {ROLL_GROUP.name} processing {skill.name}")
            if skill.name not in character_skills.keys():
                character_skills[skill.name] = skill
                character_skills[skill.name].group = ROLL_GROUP.name
                character_skills[skill.name].rating += 1
            else:
                character_skills[skill.name].rating += 1
            log.append(f"skill {skill.name} has +1 rating to {character_skills[skill.name].rating}")
        if add_back:
            weight_groups[list_of_groups.index(ROLL_GROUP)] += random.randint(1, 5)
        group_points -= 1
            
    # Individual Skill Points spend
    # for _ in range(skill_points):
    log.append("\n\nbeing individual point spend\n")
    while skill_points > 0:
        ROLL_SKILL = random.choices(list_of_skills, weight_skills)[0]
        if ROLL_SKILL.name in character_skills.keys() and character_skills[ROLL_SKILL.name].group != False:
            log.append(f"{ROLL_SKILL.name} being ignored because it's group is {character_skills[ROLL_SKILL.name].group}")
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
                weight_skills[list_of_skills.index(ROLL_SKILL)] += random.randint(1,5)
                if add_back_plus:
                    if ROLL_SKILL.group != False:
                        for group in list_of_groups:
                            if ROLL_SKILL in group.skills:
                                for gskill in group.skills:
                                    weight_skills[list_of_skills.index(gskill)] += random.randint(1,3)
                    else:
                        pass

            skill_points -= 1
    
    # Getting debug output. Sorts skills by group first, then by ranking
    output = {'Non-Grouped': {}}
    for k, d in character_skills.items():
        if d.group != False:
            if d.group not in output.keys():
                output[d.group] = {}
                if d.rating not in output[d.group].keys():
                    output[d.group][d.rating] = [d.name]
                else:
                    output[d.group][d.rating].append(d.name)
            else:
                if d.rating not in output[d.group].keys():
                    output[d.group][d.rating] = [d.name]
                else:
                    output[d.group][d.rating].append(d.name)
        else:
            if d.rating not in output['Non-Grouped'].keys():
                output['Non-Grouped'][d.rating] = [d.name]
            else:
                output['Non-Grouped'][d.rating].append(d.name)

    for group in output.keys():
        output[group] = OrderedDict(sorted(output[group].items(), key=lambda t: t[0]))
        print(group)
        for rating in output[group].keys():
            print(rating, output[group][rating])




    f = open('shadowrun_5e_test_out', 'wt')
    for _ in log:
        f.write(f"\n{_}")
    f.close()


b = Core.Character()
b.debug_gen_attrs(magic=True)
c = Core.Character()
c.debug_gen_attrs(techo=True)
d = Core.Character()
d.debug_gen_attrs(magic=True, techo=True)
get_skills(b, add_back=False, add_back_plus=False)
# get_skills(c, add_back=True, add_back_plus=False)
# get_skills(d, add_back=True, add_back_plus=True)
