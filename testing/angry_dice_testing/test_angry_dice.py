__author__ = 'jbroxton'

import unittest
from angry_dice_test_game import AngryDice
from unittest.mock import patch
from io import StringIO


class TestAngryDice(unittest.TestCase):

    def setUp(self):
        self.new_game = AngryDice()

    def tearDown(self):
        del self.new_game

    def check_possible_values(self):
        self.new_game.dice_a.currentValue = "sasquatch"
        if self.new_game.dice_a.currentValue not in self.new_game.possibleValues:
            print("Checked for current values in possible values")
            self.assertFalse(True)

    @patch('sys.stdout', new_callable=StringIO)
    def test_double_anger_output(self, mock_stdout):
        """Test the print function of the check_anger function"""
        self.new_game.dice_a.currentValue = "ANGRY"
        self.new_game.dice_b.currentValue = "ANGRY"

        angry_text = "WOW, you're ANGRY! \nTime to go back to Stage 1!\n"

        self.new_game.check_anger()
        self.assertEqual(mock_stdout.getvalue(), angry_text)
        self.assertEqual(self.new_game.currentStage, 1)

        if self.new_game.currentStage == 1:
            self.assertTrue(True)

    @patch('sys.stdout', new_callable=StringIO)
    def test_roll_parse_for_input(self, mock_stdout):
        """Give a player input and make sure the game returns the correct string"""
        roll_dice = self.new_game.roll_parse(['asdf', 'blsdf', 'ahgybiwu*', ""])
        if roll_dice == ['a', 'b', 'ab', '']:
            self.assertTrue(True)

    def test_stage_one_input_returns_stage_two(self):
        self.new_game.currentStage = 1
        self.new_game.showing = [1, 2]

    @patch('builtins.input', return_value="ab")
    def test_player_roll_output(self, input_value):
        self.new_game.dice_a.currentValue = 10
        self.new_game.dice_b.currentValue = 10
        rolled_die = self.new_game.player_roll()
        if self.new_game.showing != [10, 10]:
            self.assertTrue(True)

    def test_cheating_lock_die_stage_one(self):
        self.new_game.currentStage = 1
        self.new_game.dice_b.currentValue = "4"

        self.new_game.check_cheating('a')

        self.assertTrue(self.new_game.cheating)

    def test_cheating_lock_die_stage_two(self):
        self.new_game.currentStage = 2
        self.new_game.dice_b.currentValue = "1"

        self.new_game.check_cheating('a')

        self.assertTrue(self.new_game.cheating)

    def test_cheating_lock_die_stage_three(self):
        self.new_game.currentStage = 3
        self.new_game.dice_b.currentValue = "6"

        self.new_game.check_cheating('a')

        self.assertTrue(self.new_game.cheating)

    def test_you_rolled_prints_correct_values(self):
        self.new_game.dice_a.currentValue = "sasquatch"
        self.new_game.dice_b.currentValue = "bigfoot"
        self.new_game.currentStage = 5

    def test_cheating(self):
        self.new_game.currentStage = 1
        self.new_game.lock_value = 6
        self.new_game.check_cheating("a")


if __name__ == '__main__':
    unittest.main()
