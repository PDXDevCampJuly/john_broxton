__author__ = 'jbroxton'

import unittest
from classSpecialDie import Die


class DieRollTest(unittest.TestCase):
    """Test the functionality of the Die Class Roll function"""

    def setUp(self): #setUp function will run before every function when called
        self.possible_values = [1,2,3,"Wolverine", "Cyclops", "Storm"]
        self.new_die = Die(self.possible_values)

        print(self.shortDescription()) #this insures that all the tests ran

    def tearDown(self):
        print("Just ran test:")
        print(self._testMethodName)
        del self.possible_values


    def test_roll_once(self):
        """Roll the die once and insure the value is in possibleValues"""

        self.assertIn(self.new_die.roll(), self.possible_values, "Rolled value was not in possible die values")


    def test_roll_value_changes(self):
        """Roll the die a number of times to make sure it changes value"""

        holding_value = self.new_die.roll()
        for i in range(10):
            if self.new_die.roll() != holding_value:
                print("Rolled die value {} is different from Holding Value {}".format(self.new_die.currentValue, holding_value))
                self.assertTrue(True)
                return

        self.assertTrue(False, "Die value did not change from Holding Value for 10 rolls")

    def test_currentValue_is_updated_to_roll_value(self):
        """Make sure the Die's currentValue is updated to match what is rolled"""
        rolled_value = self.new_die.roll()
        if rolled_value == self.new_die.currentValue:
            self.assertTrue(True, "currentValue {} matches the rolled value".format(self.new_die.currentValue))
            return


if __name__ == '__main__':
    unittest.main()
