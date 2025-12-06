from unittest import TestCase, main
from project.star_system import StarSystem


class TestStarSystem(TestCase):
    def setUp(self):
        self.star_system = StarSystem("Test name", "Red giant", "Single", 3)

    def test_init(self):
        self.assertEqual("Test name", self.star_system.name)
        self.assertEqual("Red giant", self.star_system.star_type)
        self.assertEqual("Single", self.star_system.system_type)
        self.assertEqual(3, self.star_system.num_planets)
        self.assertEqual(None, self.star_system.habitable_zone_range)

    def test_is_habitable(self):
        self.assertFalse(self.star_system.is_habitable)
        self.star_system.habitable_zone_range = (2, 3)
        self.assertTrue(self.star_system.is_habitable)
        self.star_system.num_planets = 0
        self.assertFalse(self.star_system.is_habitable)

    def test_name_error(self):
        with self.assertRaises(ValueError) as e:
            self.star_system.name = " "
        self.assertEqual("Name must be a non-empty string.", str(e.exception))

    def test_name_success(self):
        self.star_system.name = "test 2"
        self.assertEqual("test 2", self.star_system.name)

    def test_star_type_error(self):
        with self.assertRaises(ValueError) as e:
            self.star_system.star_type = " "
        self.assertEqual("Star type must be one of ['Blue giant', 'Brown dwarf', 'Red dwarf', 'Red giant', 'Yellow dwarf'].", str(e.exception))

    def test_star_type_success(self):
        self.star_system.star_type = "Red dwarf"
        self.assertEqual("Red dwarf", self.star_system.star_type)

    def test_system_type_error(self):
        with self.assertRaises(ValueError) as e:
            self.star_system.system_type = " "
        self.assertEqual("System type must be one of ['Binary', 'Multiple', 'Single', 'Triple'].", str(e.exception))

    def test_system_type_success(self):
        self.star_system.system_type = "Binary"
        self.assertEqual("Binary", self.star_system.system_type)

    def test_num_planets_error(self):
        with self.assertRaises(ValueError) as e:
            self.star_system.num_planets = -1
        self.assertEqual("Number of planets must be a non-negative integer.", str(e.exception))

    def test_num_planets_success(self):
        self.star_system.num_planets = 0
        self.assertEqual(0, self.star_system.num_planets)

    def test_habitable_zone_range_error_len(self):
        with self.assertRaises(ValueError) as e:
            self.star_system.habitable_zone_range = (23, 12, 12)
        self.assertEqual("Habitable zone range must be a tuple of two numbers (start, end) where start < end.", str(e.exception))

    def test_habitable_zone_range_error_values(self):
        with self.assertRaises(ValueError) as e:
            self.star_system.habitable_zone_range = (23, 12)
        self.assertEqual("Habitable zone range must be a tuple of two numbers (start, end) where start < end.", str(e.exception))

    def test_habitable_zone_range_success_none(self):
        self.star_system.habitable_zone_range = None
        self.assertEqual(None, self.star_system.habitable_zone_range)

    def test_habitable_zone_range_success_not_none(self):
        self.star_system.habitable_zone_range = (13, 15)
        self.assertEqual((13, 15), self.star_system.habitable_zone_range)

    def test_gt_error_my(self):
        other_system = StarSystem("Test name2", "Red giant", "Single", 3, (12, 16))
        with self.assertRaises(ValueError) as e:
            self.star_system > other_system
        self.assertEqual("Comparison not possible: One or both systems lack a defined habitable zone or planets.",
                         str(e.exception))

    def test_gt_error_other(self):
        self.star_system.habitable_zone_range = (12, 15)
        other_system = StarSystem("Test name2", "Red giant", "Single", 3)
        with self.assertRaises(ValueError) as e:
            self.star_system > other_system
        self.assertEqual("Comparison not possible: One or both systems lack a defined habitable zone or planets.", str(e.exception))

    def test_gt_success_true(self):
        self.star_system.habitable_zone_range = (12, 15)
        other_system = StarSystem("Test name2", "Red giant", "Single", 3, (12, 13))
        self.assertTrue(self.star_system > other_system)

    def test_gt_success_false(self):
        self.star_system.habitable_zone_range = (12, 15)
        other_system = StarSystem("Test name2", "Red giant", "Single", 3, (12, 17))
        self.assertFalse(self.star_system > other_system)

    def test_compare_sys_error(self):
        other_system = StarSystem("Test name2", "Red giant", "Single", 3)
        error = self.star_system.compare_star_systems(self.star_system, other_system)
        self.assertEqual("Comparison not possible: One or both systems lack a defined habitable zone or planets.", error)

    def test_compare_sys_success(self):
        self.star_system.habitable_zone_range = (12, 15)
        other_system = StarSystem("Test name2", "Red giant", "Single", 3, (12, 13))
        result = self.star_system.compare_star_systems(self.star_system, other_system)
        self.assertEqual(result, "Test name has a wider habitable zone than Test name2.")

    def test_compare_sys_success_2(self):
        self.star_system.habitable_zone_range = (12, 15)
        other_system = StarSystem("Test name2", "Red giant", "Single", 3, (12, 17))
        result = self.star_system.compare_star_systems(self.star_system, other_system)
        self.assertEqual(result, "Test name2 has a wider or equal habitable zone compared to Test name.")


if __name__ == '__main__':
    main()
