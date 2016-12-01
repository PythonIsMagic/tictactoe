"""
  " Manages the details of a Tic Tac Toe game.
  """
import board
import random

HUMAN = 0
CPU = 1


class TicTacToe(object):
    """ Keeps track of the players, pieces, board, and status of the game. """
    def __init__(self, size=3, pick='x'):
        # Initialize a new tictactoe board
        self.b = board.Board(size)

        # Set the player symbols

        if pick.lower() == 'x':
            self.PLAYERS = ['x', 'o']
        else:
            self.PLAYERS = ['o', 'x']

        self.player = -1
        self.get_first()
        self.playing = True
        self.winner = None

    def get_first(self):
        self.player = random.randint(0, 1)

    def sym(self):
        return self.PLAYERS[self.player]

    def cpu_turn(self):
        #  move = random.choice(b.get_available_spaces())
        move = self.b.best_move(self.PLAYERS[CPU])

        if self.b.play(move, self.PLAYERS[CPU]):
            return move

    def check_state(self):
        # Check the state of board
        winner, line = self.b.find_win()

        # CPU wins, Human wins, Tie, or in progress.
        if winner in self.PLAYERS:
            self.playing = False
            self.winner = '{} wins!'.format(winner)
            return line  # Return the line that won, if we want to process it.
        elif len(self.b.get_available_spaces()) == 0:
            self.playing = False
            self.winner = 'Game is tied! Ending.'

    def next_player(self):
        self.player = (self.player + 1) % 2
