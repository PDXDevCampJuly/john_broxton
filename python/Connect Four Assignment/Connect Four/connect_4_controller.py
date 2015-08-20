__author__ = 'jbroxton'

from connect_4_model import Connect_Four_Model
from connect_4_view import Connect_Four_View

class Connect_Four_Controller:
    """This object controls game play for the Connect 4 game"""

    def __init__(self):
        """Initializes a new game of Connect 4"""

        #This holds the game's model
        self.game_state = Connect_Four_Model()

        #This is the current display
        self.game_display = Connect_Four_View()

    def handoff_board(self):
        """Hands off the board to the current player """

        return self.game_state.get_board()

    def play_turn(self):
        """This is where the player plays a turn"""
        pass

    def check_game_status(self):
        """Verifies if a player has won or the game has ended in a tie"""
        pass

    def switch_player(self):
        """Tells the model to switch the current player"""
        pass

    def close_game(self):
        """Closes and exits the game"""
        pass

    def check_move_validity(self, board):
        """Verifies if a move is valid or invalid"""
        pass

    def check_play_again(self):
        """Asks the player if they would like to play again"""
        pass

    def reset_game(self):
        """Resets game to initial conditions"""
        pass





