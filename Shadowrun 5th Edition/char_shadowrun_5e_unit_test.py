import char_shadowrun_5e_item as Item
import char_shadowrun_5e_data as Core

import unittest


class TestItemGeneration(unittest.TestCase):
    wpn = None

    def test_weapon(self, wpn=None):
        Item.get_item(wpn)

    def test_all_weapons(self):
        ALL_WEAPONS = Core.MeleeWeapon.items + Core.ProjectileWeapon.items + Core.Firearm.items
        for weapon in ALL_WEAPONS:
            self.test_weapon(wpn=weapon)


if __name__ == "__main__":
    unittest.main()
