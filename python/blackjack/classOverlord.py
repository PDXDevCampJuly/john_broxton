from classCard import *
from classDeck import *

class Overlord:

    def __init__(self, num_players):
        self.num_players = num_players
        self.players = []
        self.deck = Deck()
        self.dealer = Dealer()
        self.start_game()

    def make_player(self, player_name):
        new_player = Player(player_name)
        self.players.append(new_player) 


    def start_game(self):
        """ determine number of players, deals cards, starts turn  """
        still_playing = True

        ### make players
        for x in range(self.num_players):
            input_name = input("\n Welcome to my Blackjack game! \n Think you're good enough to beat me?? \n Okay then, what's your name? ")
            self.make_player(input_name)

        while still_playing:

            ### deal 2 cards into hand
            for player in self.players:
                player.hand.append(self.deck.deal_card())
                player.hand.append(self.deck.deal_card())
                print("\n{} here are your cards: {}.".format(player.player_name, player.hand))
                player.status = player.score_hand()
                if player.score == 21:
                    print("\nYou've achieved Blackjack, {}.".format(player.player_name))
                elif player.score > 21: 
                    print("\nYou've busted, {}. The House always wins!".format(player.player_name))
            self.dealer.hand.append(self.deck.deal_card())
            self.dealer.hand.append(self.deck.deal_card())
            print("\nDealer is showing: {}, {}".format('\U0001F0A0',self.dealer.hand[1]))
            ### check score_hand
                
            self.dealer.status = self.dealer.score_hand()


            # This loop gives each player a full turn
            for player in self.players:
                print("\nYour turn, {}. You've got: {}".format(player.player_name, player.hand))
                while player.status == False: #change to player.finished for cleaner code?
                    self.turn(player)
                    if player.score == 21:
                        print("Blackjack for you, {}.".format(player.player_name))
                    elif player.score > 21:
                        print("You've busted, {}. The House wins again! ".format(player.player_name))
            while self.dealer.status == False:
                self.turn(self.dealer)

            print("Here are my cards: {}".format(self.dealer.hand))

            for cardshark in self.players:     
                self.determine_winner(cardshark)

            still_playing = self.play_again()

    def turn(self, player):

        """ A decision to hit or stay until you reach a value of 21 or as close to it without busting."""

        input_decision = player.decision()
         ###  If player requests a hit

        if input_decision == "hit":
            player.hand.append(self.deck.deal_card())
            player.print_hand()
            # Dealer deals a card
            player.status = player.score_hand()

        else:
            player.status = True




    def determine_winner(self, player):
        """ Compare value of players hand and then crown winner. """
        # get each score_hand and
        if player.score == 21: 
            print("You've won, {}. Don't let it go to your head.".format(player.player_name))
        elif player.score > 21:
            print("You've busted, {}. Your cash is mine! ".format(player.player_name))
        else:
            if player.score > self.dealer.score:
                print("You beat me, {}. This displeases me.".format(player.player_name))
            elif self.dealer.score > 21: 
                print("I've gone over, {}. You've won - this time.".format(player.player_name))
            else: 
                print("I've beaten you, {}. Get used to it. ".format(player.player_name))

        # find highest - crown that playah!

    def play_again(self):
        """ Asks the players if they want to play again and then starts the game over with players."""
        another_game = input("Would you care to play again -- if you're not afraid of losing? Yes or No >>>" )
        another_game = another_game.lower()

        if another_game == "yes":
            for player in self.players:
                player.hand = []
                player.score = 0
                player.status = False
            self.dealer.hand = []
            self.dealer.score = 0
            self.dealer.status = False
            if len(self.deck.cards) < (self.num_players + 1) * 6:
                self.deck.make_deck()
            
            return True
        else: 
            return False 



        
