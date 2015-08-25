__author__ = 'jbroxton'

class Monster:

    def __init__(self):
        """The Monster Class controls the parameters for a giant, city-smashing
        monster. The Monster initializes with a name, a status of 'Out of
        Tokyo', health = 10, and 0 victory points."""

        self.name = "Bojangles the Howling Leviathan"
        self.status = "Out of Tokyo"
        self.health = 10
        self.victory_points = 0

    def reset(self):
        """The reset function sets the Monster's status, health and victory
        points to their original values"""

        self.status = "Out of Tokyo"
        self.health = 10
        self.victory_points = 0

    def in_tokyo(self):
        """The in_tokyo function returns a bool, True for 'In Tokyo', False
        for 'Out of Tokyo' """

        if self.status == "In Tokyo":
            return True
        else:
            return False

    def flee(self):
        """Return True if the monster would like to flee Tokyo, False for
        anything else. """

        answer = input("Do you want to flee Tokyo? (y or n) >>> ")
        answer = answer.lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False

    def heal(self, balm):
        """The heal function passes in a balm integer and adds it to the
        Monster's health. The health cannot exceed 10 """

        balm = int(balm)
        if self.health + balm < 10:
            self.health = self.health + balm
        elif self.health + balm >= 10:
            self.health = 10

    def attack(self, damage):
        """The attack function takes a damage integer and subtracts it from
         the Monster's health. If the health is less than or equal to zero,
         the health is 'K.O.'d' """

        damage = int(damage)
        if self.health - damage > 0:
            self.health = self.health - damage
        elif self.health - damage <= 0:
            self.health = "K.O.'d"
        return self.health

    def score(self, wins):
        if self.victory_points + wins < 20:
            self.victory_points = self.victory_points + wins
        elif self.victory_points + wins >= 20:
            self.victory_points = "WINNING"
        return self.victory_points


