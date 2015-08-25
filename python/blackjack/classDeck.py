## importing since we have different files
from classCard import Card
from random import shuffle
from itertools import product

class Deck:

    def __init__(self):
        self.cards = []
        self.make_deck()

    def make_deck(self):
        suits = ["\u2660", "\u2665", "\u2666", "\u2663"]
        faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        for suit, face in product(suits, faces):
            # creating a deck out of suits and faces
            self.cards.append(Card(suit, face))
            # populate each suit and face together into a list called card
        shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


class Player:

    def __init__(self, player_name):
        self.hand = []
        self.player_name = player_name
        self.score = 0
        self.status = False

    def decision(self):
        """ Make a choice whether to hit or to stay """
        ### input Hit or stay via decision function
        player_decision = ""
        while player_decision == "":
            player_decision = input("\nWe're waiting {}... (Hit or Stay) >>> ".format(self.player_name)).lower()
            if player_decision not in ["hit", "stay"]:
                print("What is wrong with you? Do you want to hit or stay??")
                player_decision = ""
        return player_decision


    def print_hand(self):
        print("\nPay attention {}, I gave you: {}".format(self.player_name, self.hand))


    def score_hand(self):
        count = 0
        for card in self.hand:
            count += card.value
        if count > 21:
            for card in self.hand:
                card.demote()
                count = 0
                for card in self.hand:
                    count += card.value 
                if count <= 21:
                    break             



        self.score = count
        #check for Aces later!
        if self.score >= 21:
            return True
        else:
            return False




