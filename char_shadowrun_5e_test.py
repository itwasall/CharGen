import random
import char_shadowrun_5e_data as Core
from statistics import mean

c = Core.Character()
m = Core.Character()
m.Magic = 4
r = Core.Character()
r.Resonance = 4

def get_skills(ch: Core.Character, add_back, add_back_plus):
    print("get_skills called")
    table = Core.PRIORITY_TABLE_FLIPPED

    skill_points = table['Skills']['A']
    skills = []
    for skill in Core.Skill.items:
        skills.append(skill)
        skills[skills.index(skill)].rating = 0

    book_skills = [_ for _ in Core.Skill.items if _.skill_type == "Active"]
    book_sg = [_ for _ in Core.SkillGroup.items]
    if ch.Magic is None:
        print("magic is none")
        book_skills = [s for s in book_skills if s not in Core.MAGIC_SKILLS]
        book_sg = [sg for sg in book_sg if sg not in Core.MAGIC_SKILL_GROUPS]
    if ch.Resonance is None:
        print("resonance is none")
        book_skills = [s for s in book_skills if s not in Core.RESONANCE_SKILLS]
    


    print(skill_points[1])
    while skill_points[1] > 0:
        print(skill_points[1])
        chosen_sg = random.choice(book_sg)
        if add_back:
            book_sg.append(chosen_sg)
            print("add back initiated")
            if add_back_plus:
                print("add back plus initiated")
                for skill_list in book_sg:
                    for sk in skill_list:
                        if skills[skills.index(sk)].rating > 0:
                            print(f"appending {chosen_sg} due to {skills[skills.index(sk)]} being greater than 0")
                            book_sg.append(chosen_sg)
        for skill in chosen_sg.skills:
            skills[skills.index(skill)].group = chosen_sg.name
            skills[skills.index(skill)].rating += 1
        skill_points[1] -= 1

    book_skills = [s for s in book_skills if skills[skills.index(s)].group == False]

    for i in range(skill_points[0]):
        chosen_skill = random.choice(book_skills)
        
        if add_back:
            book_skills.append(chosen_skill)
        skills[skills.index(chosen_skill)].rating += 1

    for s in skills:
        if skills[skills.index(s)].rating == 0:
            skills.remove(s)

    skills_output = {'Non-Grouped':[]}
    skills_output_ratings = []
    for s in skills:
        S = skills[skills.index(s)]
        if S.rating >= 1:
            skills_output_ratings.append(S.rating)
            if S.group != False and S.group not in skills_output.keys():
                skills_output[S.group] = [S]
            elif S.group != False:
                skills_output[S.group].append(S)
            else:
                skills_output['Non-Grouped'].append(s)
    for k in skills_output.keys():
        # print(k, skills_output[k])
        pass
    print(f'Mean rating: {mean(skills_output_ratings)}')
    print(f'Total unique skills: {len(skills)}')
    Core.PRIORITY_TABLE_FLIPPED['Skills'] = { 'A': [46, 10], 'B': [36, 5], 'C': [28, 2], 'D': [22, 0], 'E': [18, 0] }

b = Core.Character()
b.debug_gen_attrs()
c = Core.Character()
c.debug_gen_attrs()
d = Core.Character()
d.debug_gen_attrs()
get_skills(b, add_back=False, add_back_plus=False)
get_skills(c, add_back=True, add_back_plus=False)
get_skills(d, add_back=True, add_back_plus=True)
