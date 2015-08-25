__author__ = 'jbroxton'

import unittest
from king_of_tokyo import Monster
from unittest.mock import patch


class TestMonster(unittest.TestCase):
    """Unittests for the Monster Class. A 'tonster' is a test monster."""

    def setUp(self):
        self.tonster = Monster()

    def tearDown(self):
        del self.tonster

    def test_reset_function(self):
        """Test to reset values to initial values"""
        self.tonster.status = "In Tokyo"
        self.tonster.health = 1
        self.tonster.victory_points = 5

        self.tonster.reset()

        self.assertEqual(self.tonster.health, 10)
        self.assertEqual(self.tonster.victory_points, 0)

    def test_in_tokyo_yes_function(self):
        """Test to determine if the in_tokyo function returns the correct
         value when the Monster is In Tokyo """
        self.tonster.status = "In Tokyo"
        self.tonster.in_tokyo()
        self.assertTrue(self.tonster.status)

    def test_in_tokyo_no_function(self):
        """Test to determine if in_tokyo return the correct value when the
        Monster is Out of Tokyo"""
        self.tonster.status = "Out of Tokyo"
        self.tonster.in_tokyo()
        self.assertTrue(self.tonster.status)

    @patch('builtins.input', return_value= "n")
    def test_flee_function(self, input_value):
        """This test takes a no value and tests to see if the monster flees Tokyo"""
        response = self.tonster.flee()
        self.assertFalse(response)

    @patch('builtins.input', return_value= "y")
    def test_flee_function(self, input_value):
        """This test takes a yes value and tests to see if the
        monster flees Tokyo"""
        response = self.tonster.flee()
        self.assertTrue(response)

    def test_healing_function(self):
        """Set the health to one, pass in 4 healing points and compare the
        returned value to 5"""

        self.tonster.health = 1
        self.tonster.heal(4)

        self.assertEqual(self.tonster.health, 5)

    def test_healing_function_greater_than_ten(self):
        """Set the health to nine, pass in 4 healing points and compare the
        returned value to 10 (the Monster cannot have a health greater
        than 10)"""

        self.tonster.health = 9
        self.tonster.heal(4)

        self.assertEqual(self.tonster.health, 10)

    def test_attack_function(self):
        """Set the monster's health to 5, drop it by 5 points and see if the
         monster is K.O.'d """

        self.tonster.health = 5
        self.tonster.attack(5)

        self.assertEqual(self.tonster.health, "K.O.'d")


    def test_score_function(self):
        """Set the monster's victory points to 15, increase by 6 and expect
         'Winning' returned value """

        self.tonster.victory_points = 15
        self.tonster.score(6)

        self.assertEqual(self.tonster.victory_points, "WINNING")














if __name__ == '__main__':
    unittest.main()
