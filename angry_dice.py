from classSpecialDie import Die


class AngryDice:

    def __init__(self):

        self.cheating = False
        # creates a list populated with dice values - necessary to return to the player the current status of the game
        self.possibleValues = ['1', '2', 'ANGRY', '4', '5', '6']
        #these two variables establish the two separate die from the Die class.
        self.dice_a = Die(self.possibleValues)
        self.dice_b = Die(self.possibleValues)
        #Start the game in Stage 1. The nature of the game is this tripartite structure: roll a 1 & 2 to advance to the next stage, roll 'ANGRY' or 4 to advance to Stage 2, etc. 
        self.showing = []
        self.currentStage = 1
        self.start_game()
        #Initialize an empty list, which needs to be passed around in different functions in order to keep track of the two values of the die
        


  

    def start_game(self):

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

        #to start the game off, call the roll function from the Special Die Class on the two die 
        self.dice_a.roll()
        self.dice_b.roll()

        # the next three funtions cycle through the 3 stages of the game, checking for cheating, evaluating the die and prompting the roll.

        self.stage_one()
        self.stage_two()
        self.stage_three()


    def you_rolled(self):

        """This function shows the player what they rolled by printing the currentValue of the die.""" 

        print("--------------------------------------\n")
        print("You rolled:\n  a = [ {} ]\n  b = [ {} ]\n")
        print("\nYou are in Stage {}\n".format(self.dice_a.currentValue, self.dice_b.currentValue, self.currentStage))

        """The three stages of the die. A lot of repetition here. This could be cleaned up, perhaps with a Stage class. These functions control gameplay. They show the die and prompt input. They each contain a while loop which breaks upon the evaluation of the roll.""" 

    def stage_one(self):
        while self.currentStage == 1:
            self.you_rolled()
            self.player_roll()
            if ("1" in self.showing and "2" in self.showing) and not self.cheating: 
                self.currentStage = 2
        
    def stage_two(self):
        while self.currentStage == 2:
            self.you_rolled()
            self.player_roll()
            if ("ANGRY" in self.showing and "4" in self.showing) and not self.cheating:
                self.currentStage = 3
            # This section commented out as it is currently not workingg    
            # elif ("ANGRY" in self.showing and "ANGRY" in self.showing) and not self.cheating:
            #     print("Wow you're Angry!")
            #     self.currentStage = 1
            #     self.stage_one()

    def stage_three(self):
        while self.currentStage == 3:
            self.you_rolled()
            self.player_roll()
            if ("5" in self.showing and "6" in self.showing) and not self.cheating:
                print("Fortune and glory!")
                break
            # This section commented out as it is currently not working!    
            # elif ("ANGRY" in self.showing and "ANGRY" in self.showing) and not self.cheating:
            #     print("Wow you're Angry!")
            #     self.currentStage = 1
            #     self.stage_one()

        #  Anything can be input by the user, but only four values will cause the game to progress. These values are: 'ab', 'ba', 'a', 'b'. The purpose of this function is to roll the die according to the player's input, or to admonish them if they try to enter something that is not a valid roll. 
        
    def player_roll(self):
        roll_value = input("Roll dice: ")

        if "ab" in roll_value or "ba" in roll_value:
            self.dice_a.roll()
            self.dice_b.roll()
            print("ab")
        elif "b" in roll_value:
            self.check_cheating(self.dice_a)
            self.dice_b.roll()
            print("b")
        elif "a" in roll_value:
            self.dice_a.roll()
            print("a")
        else: 
            print("That is not a valid roll.")
        
        self.showing = [self.dice_a.currentValue, self.dice_b.currentValue]

        #The purpose of this function is to perform a check to make sure the player is following the rules that were set out in the beginning of the game. Die not in the sliced list should return a 'You're cheating!' string.

    def check_cheating(self, dice):
        if self.currentStage == 1:
            if dice in self.possibleValues[2:]:  
                print("That's cheating!")
                self.cheating = True
        
        if self.currentStage == 2:
            if dice in (self.possibleValues[:2] + self.possibleValues[4:]):
                print("Hey cheater!")
                self.cheating = True

        if self.currentStage == 3:
            if dice in (self.possibleValues[:4] + self.possibleValues[5]):
                print("That's cheating!")
                self.cheating = True 


