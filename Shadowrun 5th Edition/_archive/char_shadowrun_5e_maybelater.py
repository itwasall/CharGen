
LOYALTY_RATINGS = {
    1: 'Just Biz. The relationship is purely mercenary, based solely on economics The people involved may not even like each other, and they won’t offer any sort of preferential treatment',
    2: 'Regular. The relationship is still all business, but the parties treat each other with a modicum of mutual respect',
    3: 'Acquaintance. The people in the relationship are friendly, but calling them actual friends might be stretching it The contact is willing to be inconvenienced in small ways for the character but won’t take a fall for him',
    4: 'Buddy. There’s actual friendship here, or at least solid mutual respect The contact will go out of his way for the character if needed',
    5: 'Got Your Back. The parties know and trust each other, and have for some time The contact will back the character even in risky situations',
    6: 'Friend for Life. The contact and character will go to the wall for each other, if that’s what it takes'
    }
CONNECTION_RATINGS = {
    1: 'Virtually no social influence; useful only for their Knowledge skills',
    2: 'Has one or two friends with some Knowledge skills, or some minor social influence',
    3: 'Has a few friends, but not a lot of social influence',
    4: 'Knows several people in a neighborhood; a borough mayor or a gang leader',
    5: 'Knows several people and has a moderate degree of social influence; a city councilman or a low-level executive it a small-to-medium corporation',
    6: 'Known and connected across his state; a city/sprawl mayor or governor, notable fixer, or a mid-level executive in a medium-sized corporation',
    7: 'Knows a lot of people over a large area, and has considerable social influence; often holds a leadership position in a national corporation',
    8: 'Well-connected across a multi-state region; an executive in a state government or a national corporation',
    9: 'Well-connected on his own continent, with considerable social influence; a mid-level executive in a small national government or AA megacorporation',
    10: 'Well-connected worldwide, with significant social influence; a senior executive in a small national government or a AA megacorporation',
    11: 'Extremely well-connected worldwide, with significant social influence; mid-level executive position in a major national government or AAA megacorporation',
    12: 'Global power-player with extensive social influence; holds a key executive position in a major national government or AAA megacorporation'
    }


def format_skills():
    def format_skills_specialisations():
        longest_key = 0
        for i in spec_skills:
            for k, d in i.items():
               if len(k) > longest_key:
                longest_key = len(k)
        for i in spec_skills:
            for k, d in i.items():
                spaces = "".join([" " for _ in range(longest_key - len(k))])
                print(f'Skill: {k}' + spaces + f' Spec: {d}')
