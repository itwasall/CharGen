import random
import data as Core


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
    ch, skills, groups, weight_skills, weight_groups = resolve_skills_qualities(
            ch, skills, groups, weight_skills, weight_groups
            )
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
        for skill in ch.Skills.keys():
            if skill in Core.MAGIC_SKILLS:
                return skills_remove_aspected_magician(ch, skill_list, group_list, skill)
            else:
                pass
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


def skills_remove_aspected_magician(ch: Core.Character, skill_list, group_list, skill) -> (dict, dict):
    """
        If priority 'B' or 'C' is chosen for Magic or Resonance, and 'Aspected Magician' is selected,
            at this point in execution the character will have already rolled their magic skills, but
            no more can be added, so they'll need to be removed here
    """
    for group in Core.MAGIC_SKILL_GROUPS:
        if skill not in group:
            group_list[group] = 0
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


def karma_spend_raise_skill(ch: Core.Character,
                            k: Core.KarmaLogger,
                            karma_budget: int
                            ) -> (Core.Character, Core.KarmaLogger, int):
    try:
        skill_to_raise = random.choice(
            [i for i in ch.Skills if
             ch.Skills[i].rating < 6 and ch.Skills[i].rating > 1])
        karma_cost_skill_raise = Core.KARMA_SKILL_COSTS['Active'][ch.Skills[skill_to_raise].rating + 1]
        # print(Core.KARMA_SKILL_COSTS['Active'][ch.Skills[
        # 'Active'][skill_to_raise].rating + 1])
        if karma_cost_skill_raise > karma_budget:
            return (ch, k, karma_budget)
        else:
            ch.Skills[skill_to_raise].rating += 1
            karma_budget -= karma_cost_skill_raise
            s1 = ch.Skills[skill_to_raise].name
            s2 = ch.Skills[skill_to_raise].rating
            k.append(
                f'(EX) {s1} has been increased to {s2}.' +
                f'Costing {karma_cost_skill_raise}.' +
                f'\n   {karma_budget} is Karma total.')
    except IndexError | KeyError:
        return (ch, k, karma_budget)
    return (ch, k, karma_budget)


def karma_spend_raise_skill_group(ch: Core.Character,
                                  k: Core.KarmaLogger,
                                  karma_budget: int
                                  ) -> (Core.Character, Core.KarmaLogger, int):
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
            pass
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
    except:
        return (ch, k, karma_budget)
    return (ch, k, karma_budget)

def karma_spend_new_skill(ch: Core.Character,
                          k: Core.KarmaLogger,
                          karma_budget: int
                          ) -> (Core.Character, Core.KarmaLogger, int):
        unskilled = [s for s in Core.ACTIVE_SKILLS if
                     s.name not in list(ch.Skills.keys())]
        new_skill = random.choice(unskilled)
        ch.Skills[new_skill.name] = new_skill
        ch.Skills[new_skill.name].rating += 1
        karma_budget -= 1
        k.append(
            f'(EX) {new_skill.name} has been acquired as new skill.' +
            f'Costing 1\n   {karma_budget} is Karma Total')
        return (ch, k, karma_budget)


def karma_spend_new_skill_specialisation(
        ch: Core.Character,
        k: Core.KarmaLogger,
        karma_budget: int
        ) -> (Core.Character, Core.KarmaLogger, int):
        skills_for_spec = [s for s in ch.Skills.keys() if ch.Skills[s].rating > 3 and
                           isinstance(ch.Skills[s].spec, list)]
        if len(skills_for_spec) == 0:
            skills_for_spec = [s for s in ch.Skills.keys() if ch.Skills[s].rating > 2 and
                           isinstance(ch.Skills[s].spec, list)]
        if len(skills_for_spec) == 0:
            pass
        try:
            skill_for_spec = random.choice(skills_for_spec)
            new_spec = random.choice(ch.Skills[skill_for_spec].spec)
        except IndexError:
            return(ch, k, karma_budget)
        ch.Skills[skill_for_spec].spec = new_spec
        karma_budget -= 1
        k.append(
            f'EX \'{new_spec}\' specialisation chosen for ' +
            f'{skill_for_spec}. Costing 1\n   {karma_budget} ' +
            f'is Karama Total')
        return (ch, k, karma_budget)


def resolve_skills_qualities(ch: Core.Character, 
                             skill_list: list,
                             group_list: list,
                             weight_skills: list,
                             weight_groups: list):
    if 'Juryrigger' in ch.Qualities:
        for idx, skill in enumerate(skill_list):
            if "Mechanic" in skill.name:
                weight_skills[idx] += 10
    if 'Incompetent' in ch.Qualities:
        incompetent_skill_group = random.choice(group_list)
        for skill in incompetent_skill_group.skills:
            ch.Skills[skill.name] = skill
            ch.Skills[skill.name].rating = -1
            ch.Skills[skill.name].group = incompetent_skill_group.name
            weight_skills.pop(skill_list.index(skill))
            skill_list.pop(skill_list.index(skill))
        weight_groups.pop(group_list.index(incompetent_skill_group))
        group_list.pop(group_list.index(incompetent_skill_group))
        skill

    return ch, skill_list, group_list, weight_skills, weight_groups




if __name__ == "__main__":
    x = Core.Character
    x.MagicResoUser = None
    x.Magic, x.Resonance = None, None
    tbl = {'Skills': [28, 2]}
    get_skills(x, tbl)
    print(x.Skills)
    
