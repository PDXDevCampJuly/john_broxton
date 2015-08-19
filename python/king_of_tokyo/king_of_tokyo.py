__author__ = 'jbroxton'

class Monster:

    def __init__(self):

        self.name = "Bojangles the Howling Leviathan"
        self.status = "Out of Tokyo"
        self.health = 10
        self.victory_points = 0

    def reset(self):
        self.status = "Out of Tokyo"
        self.health = 10
        self.victory_points = 0

    def in_tokyo(self):
        if self.status == "In Tokyo":
            return True
        elif self.status == "Out of Tokyo":
            return False

    def flee(self):
        answer = input("Do you want to flee Tokyo? >>> ")
        answer = answer.lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False

    def heal(self, balm):
        if self.health + balm <= 10:
            self.health = self.health + balm
        elif self.health + balm >= 10:
            self.health = 10

    def attack(self, damage):
        if self.health - damage > 0:
            self.health = self.health - damage
        elif self.health - damage <= 0:
            self.health = "K.O.'d"

    def score(self, wins):
        if self.victory_points + wins < 20:
            self.victory_points = self.victory_points + wins
        elif self.victory_points + wins >= 20:
            self.victory_points = "WINNING"


