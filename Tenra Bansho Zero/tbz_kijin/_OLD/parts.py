import yaml, random

mechanica_parts = yaml.safe_load(open('../tbz_data/mechanica.yaml'))['mechanica']


class Mechanica:
    def __init__(
            self,
            body_part: str,
            mechanica_class: str,
            notice_bonus: int = 0,
            attribute_penalty: int = 0,
            mechanica_slots: int = 0,
            damage_bonus: int = 0,
            wound_level: str = None,
            damage_red: int = 0
    ):
        self.body_part = body_part
        self.mechanica_class = mechanica_class
        self.notice_bonus = notice_bonus
        self.attribute_penalty = attribute_penalty
        self.mechanica_slots = mechanica_slots
        self.damage_bonus = damage_bonus
        self.wound_level = wound_level
        self.damage_red = damage_red

    def __repr__(self):
        return f"{self.body_part} {self.mechanica_class}"


sensor_kou = Mechanica('Sensor', 'Kou', 8, 3, 3)
sensor_otsu = Mechanica('Sensor', 'Otsu', 5, 2, 1)
sensor_hei = Mechanica('Sensor', 'Hei', 4, 3, 6)
sensor_visor = Mechanica('Sensor', 'Rotating Visor', 4, 3, 6)
arm_kou = Mechanica('Arm', 'Kou', 8, 4, 4)
arm_otsu = Mechanica('Arm', 'Otsu', 5, 2, 2)
arm_hei = Mechanica('Arm', 'Hei', 3, 1, 1)
torso_kou = Mechanica('Torso', 'Kou', 20, 4, 4)
torso_otsu = Mechanica('Torso', 'Otsu', 10, 2, 2)
torso_hei = Mechanica('Torso', 'Hei', 5, 1, 1)
leg_kou = Mechanica('Leg', 'Kou', 8, 4, 4)
leg_otsu = Mechanica('Leg', 'Otsu', 5, 2, 2)
leg_hei = Mechanica('Leg', 'Hei', 3, 1, 1)
weaponinterface_kou = Mechanica('weapon_interface', 'Kou', damage_bonus=4, attribute_penalty=2)
weaponinterface_otsu = Mechanica('weapon_interface', 'Otsu', damage_bonus=2, attribute_penalty=1)
bulletskin_kou = Mechanica('homeopathic_bullet_skin', 'Kou', damage_red=30, attribute_penalty=4, wound_level='Light')
bulletskin_otsu = Mechanica('homeopathic_bullet_skin', 'Otsu', damage_red=20, attribute_penalty=2, wound_level='Heavy')
bulletskin_hei = Mechanica('homeopathic_bullet_skin', 'Hei', damage_red=10, attribute_penalty=1, wound_level='Critical')

sensor_parts = [sensor_kou, sensor_otsu, sensor_hei, sensor_visor]
arm_parts = [arm_kou, arm_otsu, arm_hei]
torso_parts = [torso_kou, torso_otsu, torso_hei]
leg_parts = [leg_kou, leg_otsu, leg_hei]
dick_part = {'Arm': arm_parts, 'Leg': leg_parts, 'Torso': torso_parts, 'Sensor': sensor_parts}
body_parts = [sensor_kou, sensor_otsu, sensor_hei, sensor_visor,arm_kou, arm_otsu, arm_hei, torso_kou, torso_otsu,
              torso_hei, leg_kou, leg_otsu, leg_hei]
special_parts = [weaponinterface_otsu, weaponinterface_kou, bulletskin_otsu, bulletskin_hei, bulletskin_kou]


def part_chooser(kijin):
    """
    Assigns a part to kijin. Chooses body-part & class based on what's already been selected (if
        not the first run), and also on the attribute_budget variable in the kijin.Kijin object.

    Args:
        kijin: kijin.Kijin object

    Returns: kijin.Kijin object

    """
    def inner_part_chooser():
        if len([x for x in kijin.mechanica.values() if x is None]) == 4:
            inner_part_choice = random.choice(body_parts)
        else:
            b = random.choice(['Arm', 'Leg', 'Torso', 'Sensor'])
            while kijin.mechanica[b] is not None:
                b = random.choice(['Arm', 'Leg', 'Torso', 'Sensor'])
            inner_part_choice = random.choice(dick_part[b])
        return inner_part_choice
    part_choice = inner_part_chooser()

    while kijin.attribute_budget - part_choice.attribute_penalty < 0:
        part_choice = inner_part_chooser()
    kijin.mechanica[part_choice.body_part] = part_choice
    kijin.total_attribute_penalty += part_choice.attribute_penalty
    return 0


class kij:
    def __init__(self, attribute_budget):
        self.mechanica = {
            'Arm': None,
            'Leg': None,
            'Torso': None,
            'Sensor': None
        }
        self.total_attribute_penalty = 0
        self.attribute_budget = attribute_budget

    def __repr__(self):
        return f"{self.mechanica}\n{self.total_attribute_penalty}\n{self.attribute_budget}"

k = kij(9)

part_chooser(k)
part_chooser(k)