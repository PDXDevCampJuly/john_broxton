class Card:
    ### DENOM_VALUE is a constant dictionary that assigns a value to the face "key"
    DENOM_VALUE = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        "Queen": 10,
        "King": 10,
        "Ace": 11
    }

    def __init__(self, suit, face):
        self.face = face
        self.suit = suit
        self.value = Card.DENOM_VALUE[face]
        self.is_hidden = False

    def __repr__(self):
        """tells python how to print a card."""
        return "{} {}".format(self.face, self.suit)

    def demote(self):
        if self.value == 11:
            self.value = 1
            print("Your Ace is now = 1")