from random import choice

class Die: 
    """A generic die class that takes possible values for the number of sides"""

    def __init__(self, possibleValues):
        self.possibleValues = possibleValues    
        self.currentValue = self.roll()

    def roll(self):
        self.currentValue = choice(self.possibleValues)
        return self.currentValue #possible to leave this line out? 

    def __repr__(self):
        return str(self.currentValue)













