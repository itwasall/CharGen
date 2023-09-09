from attrs import define, feild

@define
class Skill:
    attribute: str
    skill_type: str
    rating: int
    group: bool
    spec: list 


class AbstractBaseClass():
    def __init__(self, name, **kwargs):
        
