from classSpecialDie import Die

class AngryDice:

    def __init__(self):
        """Angry Dice is a game of chance that involves rolling dice to ascend through stages and win the game."""
        #start the game off by initializing the cheating function with "False"
        self.cheating = False
        # the Die class allows possible values when creating a die
        self.possibleValues = ['1', '2', 'ANGRY', '4', '5', '6']
        #instantiate the two die that we'll be using for the game
        self.dice_a = Die(self.possibleValues)
        self.dice_b = Die(self.possibleValues)
        self.showing = []
        #Start the game in Stage 1.
        self.currentStage = 1
        self.main()

    def main(self):
        """This is the main function that runs the game. It begins play and calls the functions that control the three stages."""

        #Print the rules of the game
        print("""
--------------------------------------------------
Welcome to Angry Dice! Roll the two dice until you get thru the 3 Stages!
Stage 1 you need to roll 1 & 2
Stage 2 you need to roll ANGRY & 4
Stage 3 you need to roll 5 & 6
You can lock a die needed for your current stage
and just roll the other one, but beware!
If you ever get 2 ANGRY's at once, you have to restart to Stage 1!
Also, you can never lock a 6! That's cheating!

To roll the dice, simply input the name of the die you want to roll.
Their names are a and b.
Press ENTER to start!
--------------------------------------------------
            """)

        #receive a blank input in response to the call for the player to Press Enter. The player could enter anything here. 
        input("")

        #to start the game off, call the roll function from the Special Die Class on our two die
        self.dice_a.roll()
        self.dice_b.roll()

        while self.currentStage != 4:
            if self.currentStage == 1:
                self.stage_one()
            elif self.currentStage == 2:
                self.stage_two()
            elif self.currentStage == 3:
                self.stage_three()

    # the next three functions cycle through the 3 stages of the game, checking for cheating, evaluating the die and prompting the roll.

    def stage_one(self):
        self.you_rolled()
        self.player_roll()
        self.check_anger()
        if ("1" in self.showing and "2" in self.showing) and not self.cheating:
            self.currentStage = 2
        
    def stage_two(self):
        self.you_rolled()
        self.player_roll()
        self.check_anger()
        if ("ANGRY" in self.showing and "4" in self.showing) and not self.cheating:
            self.currentStage = 3

    def stage_three(self):
        self.you_rolled()
        self.player_roll()
        self.check_anger()
        if ("5" in self.showing and "6" in self.showing) and not self.cheating:
            print("You rolled:\n  a = [ {} ]\n  b = [ {} ]\n".format(self.dice_a.currentValue, self.dice_b.currentValue))
            print("You've won! Calm down!")
            self.currentStage = 4

    def you_rolled(self):
        """This function shows the player what they rolled by printing the currentValue of the die."""

        print("--------------------------------------\n")
        print("You rolled:\n  a = [ {} ]\n  b = [ {} ]\n".format(self.dice_a.currentValue, self.dice_b.currentValue))
        print("\nYou are in Stage {}\n".format(self.currentStage))

    def roll_parse(self, string):
        output = ""
        if "a" in string:
            output += "a"

        if "b" in string:
            output += "b"

        return output

    def player_roll(self):
        roll_value = input("Roll dice: ")
        roll_value = self.roll_parse(roll_value)
        self.check_cheating(roll_value)

        if not self.cheating:
            # roll the dice asked for
            if "a" in roll_value:
                self.dice_a.roll()
            if "b" in roll_value:
                self.dice_b.roll()
            self.showing = [self.dice_a.currentValue, self.dice_b.currentValue]

    #The purpose of this function is to perform a check to make sure the player is following the rules that were set out in the beginning of the game

    def check_cheating(self, roll_value):

        self.cheating = False
        if roll_value in ["ab", ""]:
            return

        if roll_value == "a":
            held_value = self.dice_b.currentValue
        else:
            held_value = self.dice_a.currentValue

        if self.currentStage == 1:
            if held_value in self.possibleValues[2:]:
                print("That's cheating!")
                self.cheating = True

        elif self.currentStage == 2:
            if held_value in (self.possibleValues[:2] + self.possibleValues[4:]):
                print("Hey cheater!")
                self.cheating = True

        elif self.currentStage == 3:
            if held_value in (self.possibleValues[:4]):
                print("That's cheating!")
                self.cheating = True
            elif held_value == "6":
                print("You're cheating! You cannot lock a 6! You cannot win until you reroll it!")
                self.cheating = True

    def check_anger(self):
        if (self.dice_a.currentValue == "ANGRY" and self.dice_b.currentValue == "ANGRY"):
            print("WOW, you're ANGRY! \nTime to go back to Stage 1!")
            self.currentStage = 1






