import random
import char_shadowrun_5e_data as Core
from statistics import mean

c = Core.Character()
m = Core.Character()
m.Magic = 5
r = Core.Character()
r.Resonance = 4

"""
def get_skills(ch: Core.Character, add_back, add_back_plus):
    print("===========")
    print("===========")
    print("===========")
    print("===========")
    Core.refresh_priority_table()
    table = Core.PRIORITY_TABLE_FLIPPED

    skill_points = table['Skills']['A']
    print(skill_points)
    # skill_points = [10, 0]
    char_skills = [_ for _ in Core.Skill.items if _.skill_type == "Active"]
    for skill in char_skills:
        skill.rating = 0

    book_skills = [_ for _ in Core.Skill.items if _.skill_type == "Active"]
    book_sg = [_ for _ in Core.SkillGroup.items]
    book_sg_2 = [_ for _ in Core.SkillGroup.items]
    if ch.Magic is None:
        print("magic is none")
        book_skills = [s for s in book_skills if s not in Core.MAGIC_SKILLS]
        book_sg = [sg for sg in book_sg if sg not in Core.MAGIC_SKILL_GROUPS]
    if ch.Resonance is None:
        print("resonance is none")
        book_skills = [s for s in book_skills if s not in Core.RESONANCE_SKILLS]
    


    print(skill_points[1])
    # Choosing skill groups
    # If applicable, skill group points are allocated here. Those skills then have their
    #   'group' value changed to the group they're in. This is to prevent skill group
    #   point allocation breaking when individual points are given to skill group skills
    while skill_points[1] > 0:
        chosen_sg = random.choice(book_sg)
        if add_back:
            book_sg.append(chosen_sg)
            # if add_back_plus:
            #    for skill_list in book_sg_2:
            #            if skills[skills.index()].rating > 0:
            #                print(f"appending {chosen_sg} due to {skills[skills.index(sk)]} being greater than 0")
            #                book_sg.append(chosen_sg)
        for new_group_skill in chosen_sg.skills:
            for skill in char_skills:
                if skill.name == new_group_skill.name:
                    skill.group = chosen_sg.name
                    skill.rating += 1
                # print(f'Skill "{skill.name}" has rating "{char_skills[char_skills.index(skill)].rating}"')
        skill_points[1] -= 1

    book_skills = [s for s in book_skills if char_skills[char_skills.index(s)].group == False]

    print(skill_points[0])
    # Choosing individual skills
    while skill_points[0] > 0:
        the_new_skill = random.choice(book_skills)
        
        if add_back:
            book_skills.append(the_new_skill)
            if add_back_plus:
                if the_new_skill.group != False:
                    print(f"wait no what {the_new_skill.name} shouldn't have triggered here")
                            # print(f"appending {chosen_sg.name} due to {s.name} being greater than 0 {s.rating}")
                            # book_skills.append(the_new_skill)
        # skills[skills.index(the_new_skill)].rating += 1
        for idx, s in enumerate(char_skills):
            if s.name == the_new_skill.name:
                char_skills[idx].rating += 1
        skill_points[0] -= 1
    print("pre")
    print(len(char_skills))
    for s in char_skills:
        if s.rating <= 0:
            char_skills.pop(char_skills.index(s))
    print("post")
    print(len(char_skills))

    skills_output = {'Non-Grouped':[]}
    skills_output_ratings = []
    for char_skill in char_skills:
        # S = skills[skills.index(s)]
        skills_output_ratings.append(char_skill.rating)
        if char_skill.group != False and char_skill.group not in skills_output.keys():
            skills_output[char_skill.group] = [char_skill]
        elif char_skill.group != False:
            skills_output[char_skill.group].append(char_skill)
        else:
            skills_output['Non-Grouped'].append(char_skill)
    for k in skills_output.keys():
        print(k, skills_output[k])

        pass
    print(f'Mean rating: {mean(skills_output_ratings)}')
    print(f'Total unique skills: {len(char_skills)}')
    f = open('shadowrun_5e_test_out', 'wt')
    for skill in char_skills:
        f.write("\n")
        f.write("".join([str(skill.name), str(skill.rating)]))
    f.close()
"""
def init_shit():
    for s in Core.Skill.items:
        if hasattr(s, 'group'):
            s.group = False
        s.rating = 0
    Core.refresh_priority_table()

def get_skills(c: Core.Character, add_back = False, **kwargs):
    print("\n\n\nInit gen\n")
    init_shit()
    table = Core.PRIORITY_TABLE_FLIPPED
    skill_points, group_points = table['Skills']['A']

    character_skills = {}

    list_of_skills = [skill for skill in Core.Skill.items if skill.skill_type == "Active"]
    weight_skills = [1 for skill in list_of_skills]
    list_of_groups = [group for group in Core.SKILL_GROUPS]
    weight_groups = [1 for group in list_of_groups]

    if c.Magic is None:
        for _ in Core.MAGIC_SKILLS:
            list_of_skills.pop(list_of_skills.index(_))
        for _ in Core.MAGIC_SKILL_GROUPS:
            list_of_groups.pop(list_of_groups.index(_))

    if c.Resonance is None:
        for _ in Core.RESONANCE_SKILLS:
            list_of_skills.pop(list_of_skills.index(_))
        list_of_groups.pop(list_of_groups.index(Core.TASKING))

    log = []

    # Group Skill Points spend
    # for _ in range(group_points):
    log.append("\n\nbeing group point spend\n")
    while group_points > 0:
        ROLL_GROUP = random.choices(list_of_groups, weight_groups)[0]
        for skill in ROLL_GROUP:
            print(f"Roll group {ROLL_GROUP.name} processing {skill.name}")
            if skill.name not in character_skills.keys():
                character_skills[skill.name] = skill
                log.append(f"skill {skill.name} added to character skills")
                character_skills[skill.name].group = ROLL_GROUP.name
                log.append(f"skill {skill.name} assigned group {ROLL_GROUP.name}")
            character_skills[skill.name].rating += 1
            log.append(f"skill {skill.name} has +1 rating to {character_skills[skill.name].rating}")
        if add_back:
            weight_groups[list_of_groups.index(ROLL_GROUP)] += 5
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

    for key in output.keys():
        print(key)
        for k in output[key].keys(): 
            print(k, output[key][k])


    f = open('shadowrun_5e_test_out', 'wt')
    for _ in log:
        f.write(f"\n{_}")
    f.close()


b = Core.Character()
b.debug_gen_attrs()
c = Core.Character()
c.debug_gen_attrs()
d = Core.Character()
d.debug_gen_attrs()
get_skills(b, add_back=False, add_back_plus=False)
get_skills(c, add_back=True, add_back_plus=False)
get_skills(d, add_back=True, add_back_plus=True)
