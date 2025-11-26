from project.hero import Hero
from unittest import TestCase, main

class HeroTests(TestCase):
    username = "Test hero"
    level = 5
    health = 16.8
    damage = 9.4

    def setUp(self):
        self.hero = Hero(self.username, self.level, self.health, self.damage)

    def test_init(self):
        self.assertEqual(self.username, self.hero.username)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(self.health, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

    def test_attr_types(self):
        self.assertIsInstance(self.hero.username, str)
        self.assertIsInstance(self.hero.level, int)
        self.assertIsInstance(self.hero.health, float)
        self.assertIsInstance(self.hero.damage, float)

    def test_battle_same_name(self):
        self.enemy = Hero(self.username, self.level, self.health, self.damage)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_low_health_raises(self):
        self.enemy = Hero("Enemy", self.level, self.health, self.damage)
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

        self.hero.health = -2
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_enemy_low_health_raises(self):
        self.enemy = Hero("Enemy", self.level, 0, self.damage)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ex.exception))

        self.enemy.health = -5
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ex.exception))

    def test_draw_battle(self):
        self.enemy = Hero("Enemy", self.level, self.health, self.damage)
        result = self.hero.battle(self.enemy)
        self.assertEqual("Draw", result)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(-30.2, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

    def test_hero_wins(self):
        self.enemy = Hero("Enemy", 1, 1, 1)
        result = self.hero.battle(self.enemy)

        self.assertEqual("You win", result)
        self.assertEqual(6, self.hero.level)
        self.assertEqual(20.8, self.hero.health)
        self.assertEqual(14.4, self.hero.damage)

    def test_hero_losses(self):
        self.hero.health = 10
        self.hero.damage = 10
        self.enemy = Hero("Enemy", 100, 100, 100)
        result = self.hero.battle(self.enemy)

        self.assertEqual("You lose", result)
        self.assertEqual(101, self.enemy.level)
        self.assertEqual(55, self.enemy.health)
        self.assertEqual(105, self.enemy.damage)

    def test_str(self):
        expected = f"Hero {self.username}: {self.level} lvl\nHealth: {self.health}\nDamage: {self.damage}\n"
        self.assertEqual(expected, str(self.hero))

if __name__ == "__main__":
    main()