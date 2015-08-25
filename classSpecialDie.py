from random import choice

class Die: #(Card)
    ### FACE_VALUE is a dictionary that assigns a value to the face "key"

    def __init__(self, possibleValues):
        self.possibleValues = possibleValues    
        self.currentValue = self.roll()

    def roll(self):
        self.currentValue = choice(self.possibleValues)
        return self.currentValue #possible to leave this line out? 

    def __repr__(self):
        return str(self.currentValue)

#new_die = Die(["apples", "oranges", "pears", "grapes"])
#print(new_die.roll())











