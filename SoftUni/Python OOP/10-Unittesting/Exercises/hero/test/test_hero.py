from project.hero import Hero
import unittest


class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero('a', 1, 100.0, 10.0)
        self.enemy = Hero('b', 1, 100.0, 10.0)

    def test_constructor(self):
        self.assertEqual(self.hero.username, 'a')
        self.assertEqual(self.hero.health, 100.0)
        self.assertEqual(self.hero.level, 1)
        self.assertEqual(self.hero.damage, 10.0)

    def test_battle_cannot_fight_yourself(self):
        self.enemy.username = 'a'
        with self.assertRaises(Exception) as exc:
            self.hero.battle(self.enemy)
        self.assertEqual('You cannot fight yourself', str(exc.exception))

    def test_battle_health_is_too_low_need_to_rest_below_0(self):
        self.hero.health = 0
        with self.assertRaises(Exception) as exc:
            self.hero.battle(self.enemy)
        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(exc.exception))
        self.hero.health = -10
        with self.assertRaises(Exception) as exc:
            self.hero.battle(self.enemy)
        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(exc.exception))

    def test_battle_enemy_hero_below_zero_cannot_fight(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as exc:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(exc.exception))
        self.enemy.health = -10
        with self.assertRaises(ValueError) as exc:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(exc.exception))

    def test_battle_no_exceptions_draw(self):
        self.hero.health = 10.0
        self.enemy.health = 10.0
        self.assertEqual('Draw', self.hero.battle(self.enemy))

    def test_battle_no_exception_win(self):
        self.enemy.health = 1
        self.assertEqual('You win', self.hero.battle(self.enemy))
        self.assertEqual(2, self.hero.level)
        self.assertEqual(95.0, self.hero.health)
        self.assertEqual(15.0, self.hero.damage)

    def test_battle_no_exception_loss(self):
        self.hero.health = 1
        self.assertEqual('You lose', self.hero.battle(self.enemy))
        self.assertEqual(2, self.enemy.level)
        self.assertEqual(95.0, self.enemy.health)
        self.assertEqual(15.0, self.enemy.damage)

    def test__str__returns_correct(self):
        expected = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"
        self.assertEqual(expected, str(self.hero))

if __name__ == '__main__':
    unittest.main()

