from dataclasses import dataclass, field

@dataclass
class Attribute:
    name: str
    value: int

@dataclass
class Skill:
    name: str
    value: int

@dataclass
class Tribe:
    name: str
    _: KW_ONLY
    patorn: str
    archetype: list[str]

BLACK_FURIES = Tribe('Black Furies', patron='Gorgon', archetype=['Most Wanted', 'EMT', 'Musician', 'Outrider'])
BONE_GNAWERS = Tribe('Bone Gnawers', patron='Rat', archetype=['Zine Racounteur', 'Sound Tech', 'Friend of Ours', 'Gig Wheelman'])
CHILDREN_OF_GAIA = Tribe('Children of Gaia', patron='Unicorn', archetype=['Sawbones', 'Dealer', 'Wayfarer', 'Miner'])
GALESTALKERS = Tribe('Galestalkers', patron='North Wind', archetype=['Drifter', 'Spiritwalker', 'Gaucho', 'Leechtalker'])
GHOST_COUNCIL = Tribe('Ghost Council', patron='Horned Serpent', archetype=['Contemplative', 'Saboteur', 'Witch', 'Shepherd'])
GLASS_WALKERS = Tribe('Glass Walkers', patron='Spider', archetype=['Urban Planner', 'Car Liberator', 'Detective', 'Tattoo Artist'])
HART_WARDENS = Tribe('Hart Wardens', patron='Stag', archetype=['Huntsman', 'Digital Caern Strategist', 'Emcee', 'Local Legend'])
RED_TALONS = Tribe('Red Talons', patron='Griffin', archetype=['Bounty Hunter', 'Maneater', 'Prepper', 'Plague Dog'])
SHADOW_LORDS = Tribe('Shadow Lords', patron='Thunder', archetype=['Boyar', 'Hacktivist', 'Midnight Terror', 'Assassin'])
SILENT_STRIDERS = Tribe('Silent Striders', patron='Owl', archetype=['Kinseeker', 'Ambassador', 'Revivalist', 'Long-Haul Trucker'])
SILVER_FANGS = Tribe('Silver Fangs', patron='Falcon', archetype=['Local Celebrity', 'Hetman', 'Glory-Days QB', 'Nobile-in-Exile'])

TRIBES = [BLACK_FURIES, BONE_GNAWERS, CHILDREN_OF_GAIA, GALESTALKERS, GHOST_COUNCIL, GLASS_WALKERS, 
          HART_WARDENS, RED_TALONS, SHADOW_LORDS, SILENT_STRIDER, SILVER_FANGS]


class Character():
    def __init__(self, **kwargs):
        for k, d in kwargs:
            self.__setattr__(k, d)


def generate_character():
    AUSPICES = ['Ragabash', 'THEURGE', 'PHILDOX', 'GALLIAD', 'AHROUN']
    c = Character()
    c.strength = Attribute("Strength", 1)
    c.dexterity = Attribute("Dexterity", 1)
    c.stamina = Attribute("Stamina", 1)
    c.charisma = Attribute("Charisma", 1)
    c.manipulation = Attribute("Manipulation", 1)
    c.composure = Attribute("Composure", 1)
    c.intelligence = Attribute("Intelligence", 1)
    c.wits = Attribute("Wits", 1)
    c.resolve = Attribute("Resolve", 1)
    c.physical_attrs = [c.strength, c.dexterity, c.stamina]
    c.social_attrs = [c.charisma, c.manipulation, c.composure]
    c.mental_attrs = [c.intelligence, c.wits, c.resolve]
    c.all_attrs = c.physical_attrs + c.social_attrs + c.mental_attrs
    print(c.all_attrs)


if __name__ == "__main__":
    generate_character()

