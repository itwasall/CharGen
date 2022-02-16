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
PokeAttribute_Dexterity = PkAttribute('Dexterity')
PokeAttribute_Insight = PkAttribute('Insight')

PokeSocialAttribute_Tough = PkAttribute('Tough')
PokeSocialAttribute_Beauty = PkAttribute('Beauty')
PokeSocialAttribute_Cool = PkAttribute('Cool')
PokeSocialAttribute_Cute = PkAttribute('Cute')
PokeSocialAttribute_Clever = PkAttribute('Clever')

class PkAttributes:
    def __init__(
        self,
        strength = PokeAttribute_Strength,
        vitality = PokeAttribute_Vitality,
        dexterity = PokeAttribute_Dexterity,
        insight = PokeAttribute_Insight,
        tough = PokeSocialAttribute_Tough,
        beauty = PokeSocialAttribute_Beauty,
        cool = PokeSocialAttribute_Cool,
        cute = PokeSocialAttribute_Cute,
        clever = PokeSocialAttribute_Clever
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
        self.core_attributes = [self.strength, self.vitality, self.dexterity, self.insight]
        self.social_attributes = [self.tough, self.beauty, self.cool, self.cute, self.clever]

    def rnd_add_core(self, attribute_type = 'Core'):
        if attribute_type == 'Core':
            a_choice = choice(self.core_attributes)
        elif attribute_type == 'Social':
            a_choice = choice(self.social_attributes)
        # options = {'Strength': self.strength, 'Vitality': self.vitality, 'Insight':self.insight, 'Dexterity': self.dexterity,
        #           'Tough': self.tough, 'Beauty': self.beauty, 'Cool': self.cool, 'Cute': self.cute, 'Clever': self.clever}
        # options[a_choice.name] += 1
        if a_choice.name == 'Strength':
            self.strength += 1
        elif a_choice.name == 'Vitality':
            self.vitality += 1
        elif a_choice.name == 'Insight':
            self.insight += 1
        elif a_choice.name == 'Dexterity':
            self.dexterity += 1
        elif a_choice.name == 'Tough':
            self.tough += 1
        elif a_choice.name == 'Beauty':
            self.beauty += 1
        elif a_choice.name == 'Cool':
            self.cool += 1
        elif a_choice.name == 'Cute':
            self.cute += 1
        elif a_choice.name == 'Clever':
            self.clever += 1

    def print_attributes(self):
        self.core_attributes = [self.strength, self.vitality, self.dexterity, self.insight]
        self.social_attributes = [self.tough, self.beauty, self.cool, self.cute, self.clever]
        print("Core Attributes:")
        for a in self.core_attributes:
            print(f"  {a}")
        for a in self.social_attributes:
            print(f"  {a}")



class PkSkill(PkAttribute):
    def __init__(self, name, value = 0):
        super().__init__(name, value)

PokeSkill_Brawl = PkSkill('Brawl')
PokeSkill_Throw = PkSkill('Throw')
PokeSkill_Evasion = PkSkill('Evasion')
PokeSkill_Weapons = PkSkill('Weapons')
PokeSkill_Empathy = PkSkill('Empathy')
PokeSkill_Intimidate = PkSkill('Intimidate')
PokeSkill_Perform = PkSkill('Perform')
PokeSkill_Alert = PkSkill('Alert')
PokeSkill_Athletic = PkSkill('Athletic')
PokeSkill_Nature = PkSkill('Nature')
PokeSkill_Stealth = PkSkill('Stealth')
PokeSkill_Crafts = PkSkill('Crafts')
PokeSkill_Lore = PkSkill('Lore')
PokeSkill_Medicine = PkSkill('Medicine')
PokeSkill_Science = PkSkill('Science')

class PkSkills:
    def __init__(self):
        self.brawl = PokeSkill_Brawl
        self.throw = PokeSkill_Throw
        self.evasion = PokeSkill_Evasion
        self.weapons = PokeSkill_Weapons
        self.empathy = PokeSkill_Empathy
        self.intimidate = PokeSkill_Intimidate
        self.perform = PokeSkill_Perform
        self.alert = PokeSkill_Alert
        self.athletic = PokeSkill_Athletic
        self.nature = PokeSkill_Nature
        self.stealth = PokeSkill_Stealth
        self.crafts = PokeSkill_Crafts
        self.lore = PokeSkill_Lore
        self.medicine = PokeSkill_Medicine
        self.science = PokeSkill_Science
        
        self.update_skill_list()

    def update_skill_list(self):
        self.skills_list = [self.brawl, self.throw, self.evasion, self.weapons, self.empathy, self.intimidate, self.perform, self.alert,
                            self.athletic, self.nature, self.stealth, self.crafts, self.lore, self.medicine, self.science]

    def rnd_add_skill(self, limit):
        rnd_skill = choice(self.skills_list)
        while rnd_skill.value < limit: 
            rnd_skill = choice(self.skills_list)
            rnd_skill.value += 1
        self.skills_list[self.skills_list.index(rnd_skill)] = rnd_skill
        self.update_skill_list()

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
    p.print_attributes()

def gen_skills(rank):
    skill_points = rank_bonuses[rank]['Skill Points']
    skill_limit = rank_bonuses[rank]['Skill Limit']
    s = PkSkills()
    for _ in range(skill_points):
        s.rnd_add_skill(skill_limit)
    print(f"Skill points: {skill_points}\nSkill Limit: {skill_limit}")
    print(s)


print("Teenage Starter")
gen_stats('Starter', 'Teenager')
print("Senior Ace")
gen_stats('Ace', 'Senior')
gen_skills('Starter')

