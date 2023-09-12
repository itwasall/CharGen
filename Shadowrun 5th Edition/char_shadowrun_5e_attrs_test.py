from attrs import define, field
from dataclasses import dataclass

@define
class Skill:
    name: str
    attribute: str
    skill_type: str
    rating: int
    group: bool
    spec: list 

@dataclass
class Availability:
    name: str
    def __repr__(self):
        return self.name

RESTRICTED = Availability('Restricted')

@dataclass
class Item:
    name: str
    cost: int
    page_ref: str
    rating: int
    avail: int
    legality: Availability
    category: str


COMMERCIAL_EXPLOSIVES = Item("Commercial Explosives", cost=100, page_ref=436, rating=5, avail=8, legality=RESTRICTED, category="Explosives")

print(COMMERCIAL_EXPLOSIVES)
