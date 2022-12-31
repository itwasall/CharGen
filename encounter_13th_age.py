class ABC:
    def __init__(self, name, **kwargs):
        self.name = name
        for k, d in kwargs.items():
            self.__setattr__(k, d)

    def __repr__(self):
        return self.__format__()

    def __format__(self):
        return self.name

class Monster(ABC):
    items = []
    def __init__(
            self,
            name,
            armor_class = 0,
            phy_defence = 0,
            men_defence = 0,
            hit_points = 0,
            category = None,
            **kwargs
            ):
        super().__init__(name, **kwargs)
        self.armor_class = armor_class
        self.phy_defence = phy_defence
        self.men_defence = men_defence
        self.hit_points = hit_points
        self.category = category
        Monster.items.append(self)

    def __format__(self):
        return f"{self.name} ({self.category})"

Giant_Ant = Monster("Giant Ant", 14, 13, 9, 20, category="Beast")
Dire_Wolf = Monster("Dire Wolf", 18, 17, 13, 80, category="Beast")
Imp = Monster("Imp", 20, 13, 16, 40, category="Demon")

print([monster for monster in Monster.items])
print([monster for monster in Monster.items if monster.category == "Beast"])

