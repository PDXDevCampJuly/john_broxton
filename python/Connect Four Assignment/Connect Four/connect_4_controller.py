__author__ = 'jbroxton'

import sys
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

        return self.game_state.flip_current_player()


    def close_game(self):
        """Exits the game with a fond farewell """

        self.game_display.print_goodbye()
        exit()


    def check_move_validity(self, board, move):
        """Verifies if a move is valid or invalid"""
        try:
            if len(board[move][:]) < 6:
                return True
            else:
                return False
        except IndexError:
            return False

    def check_play_again(self):
        """Asks the player if they would like to play again"""

        self.game_display.prompt_play_again()

        play_again_prompt = input()

        if play_again_prompt == 'y':
            self.game_state.reset_state()
        else:
            self.close_game()












