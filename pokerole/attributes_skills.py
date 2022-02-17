from random import choice

from attr import attr

class PkAttribute:
    def __init__(self, name, value=1):
        self.name = name
        self.value = value

    def __add__(self, x):
        return PkAttribute(self.name, self.value + x)

    def __repr__(self):
        return f"{self.name}: {self.value}"


PokeAttribute_Strength = PkAttribute('Strength')
PokeAttribute_Vitality = PkAttribute('Vitality')
PokeAttribute_Dexterity =   PkAttribute('Dexterity')
PokeAttribute_Insight =     PkAttribute('Insight')
PokeSocialAttribute_Tough = PkAttribute('Tough')
PokeSocialAttribute_Beauty =PkAttribute('Beauty')
PokeSocialAttribute_Cool =  PkAttribute('Cool')
PokeSocialAttribute_Cute =  PkAttribute('Cute')
PokeSocialAttribute_Clever =PkAttribute('Clever')

class PkAttributes:
    def __init__(
        self,
        strength = PkAttribute('Strength'),
        vitality = PkAttribute('Vitality'),
        dexterity = PkAttribute('Dexterity'),
        insight = PkAttribute('Insight'),
        tough = PkAttribute('Tough'),
        beauty = PkAttribute('Beauty'),
        cool = PkAttribute('Cool'),
        cute = PkAttribute('Cute'),
        clever = PkAttribute('Clever'),
    ):
        self.strength = strength
        self.vitality = vitality
        self.dexterity = dexterity
        self.insight = insight
        self.tough = tough
        self.beauty = beauty
        self.cool = cool
        self.cute = cute
        self.clever = clever
        self.update_attribute_lists()

    def update_attribute_lists(self):
        self.core_attributes = [self.strength, self.vitality, self.dexterity, self.insight]
        self.social_attributes = [self.tough, self.beauty, self.cool, self.cute, self.clever]


    def rnd_add_core(self, attribute_type = 'Core'):
        if attribute_type == 'Core':
            a_choice = choice(self.core_attributes)
            a_choice.value += 1
            self.core_attributes[self.core_attributes.index(a_choice)] = a_choice
        elif attribute_type == 'Social':
            a_choice = choice(self.social_attributes)
            a_choice.value += 1
            self.social_attributes[self.social_attributes.index(a_choice)] = a_choice
        self.update_attribute_lists()

    def print_attributes(self, compact = False):
        self.update_attribute_lists()
        if compact:
            print("Core Attributes:")
            print(", ".join(a.__repr__() for a in self.core_attributes))
            print("Social Attributes:")
            print(", ".join(a.__repr__() for a in self.social_attributes))
        else:
            print("Core Attributes:")
            for a in self.core_attributes:
                print(f"  {a}")
            print("Social Attributes:")
            for a in self.social_attributes:
                print(f"  {a}")

class PkSkill(PkAttribute):
    def __init__(self, name, value = 0):
        super().__init__(name, value)

class PkSkills:
    def __init__(self):
        self.brawl = PkSkill('Brawl')
        self.throw = PkSkill('Throw')
        self.evasion = PkSkill('Evasion')
        self.weapons = PkSkill('Weapons')
        self.empathy = PkSkill('Empathy')
        self.intimidate = PkSkill('Intimidate')
        self.perform = PkSkill('Perform')
        self.alert = PkSkill('Alert')
        self.athletic = PkSkill('Athletic')
        self.nature = PkSkill('Nature')
        self.stealth = PkSkill('Stealth')
        self.crafts = PkSkill('Crafts')
        self.lore = PkSkill('Lore')
        self.medicine = PkSkill('Medicine')
        self.science = PkSkill('Science')
        self.update_skill_list()

    def update_skill_list(self):
        self.skills_list = [self.brawl, self.throw, self.evasion, self.weapons, self.empathy, self.intimidate, self.perform, self.alert,
                            self.athletic, self.nature, self.stealth, self.crafts, self.lore, self.medicine, self.science]

    def rnd_add_skill(self, limit):
        rnd_skill = choice(self.skills_list)
        rnd_skill.value += 1
        self.skill_limit_check(rnd_skill, limit)
        self.skills_list[self.skills_list.index(rnd_skill)] = rnd_skill
        self.update_skill_list()

    def skill_limit_check(self, skill, limit):
        if skill.value > limit:
            skill.value -= 1
            self.rnd_add_skill(limit)
        else:
            pass

    def __repr__(self):
        self.update_skill_list()
        return ", ".join(i.__repr__() for i in self.skills_list)

rank_bonuses = {
    'Starter': {'Extra Attribute': 0, 'Extra Social': 0, 'Skill Points': 5, 'Skill Limit': 1},
    'Beginner': {'Extra Attribute': 2, 'Extra Social': 2, 'Skill Points': 9, 'Skill Limit': 2},
    'Amateur': {'Extra Attribute': 4, 'Extra Social': 4, 'Skill Points': 12, 'Skill Limit': 3},
    'Ace': {'Extra Attribute': 6, 'Extra Social': 6, 'Skill Points': 15, 'Skill Limit': 4},
    'Professional': {'Extra Attribute': 8, 'Extra Social': 8, 'Skill Points': 16, 'Skill Limit': 5}
}
age_bonuses = {
    'Kid': {'Extra Attribute': 0, 'Extra Social': 0},
    'Teenager': {'Extra Attribute': 2, 'Extra Social': 2},
    'Adult': {'Extra Attribute': 4, 'Extra Social': 4},
    'Senior': {'Extra Attribute': 3, 'Extra Social': 6}
}

def gen_stats(rank, age):
    attribute_points = rank_bonuses[rank]['Extra Attribute'] + age_bonuses[age]['Extra Attribute']
    social_points = rank_bonuses[rank]['Extra Social'] + age_bonuses[age]['Extra Social']
    skill_points = rank_bonuses[rank]['Skill Points']
    skill_limit = rank_bonuses[rank]['Skill Limit']
    p = PkAttributes()
    for _ in  range(attribute_points):
        p.rnd_add_core('Core')
    for _ in range(social_points):
        p.rnd_add_core('Social')
    p.print_attributes(compact=True)

def gen_skills(s, rank):
    skill_points = rank_bonuses[rank]['Skill Points']
    skill_limit = rank_bonuses[rank]['Skill Limit']
    for _ in range(skill_points):
        s.rnd_add_skill(skill_limit)
    print(f"Skill points: {skill_points}\nSkill Limit: {skill_limit}")
    print([skill for skill in s.skills_list if skill.value > 0])


print("Teenage Starter")
gen_stats('Starter', 'Teenager')
print("Senior Ace")
gen_stats('Ace', 'Senior')
s = PkSkills()
gen_skills(s, 'Starter')
s1 = PkSkills()
gen_skills(s1, 'Starter')

