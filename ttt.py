#!/usr/bin/env python

"""
# Author: lunatunez
# Date Created: Mon Apr  4 20:28:29 2016
# Purpose: Tic Tac Toe Game
"""
import board
import random

HUMAN = 0
CPU = 1


class TicTacToe():
    def __init__(self, size=3, pick='x'):
        # Initialize a new tictactoe board
        self.b = board.Board(size)

        # Set the player symbols

        if pick.lower() == 'x':
            self.PLAYERS = ['x', 'o']
        else:
            self.PLAYERS = ['o', 'x']

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


def title():
    return 'Python Tic Tac Toe!'


def console():
    print(title())
    print('~'*40)
    print('select your symbol: (x/o)')
    while True:
        s = input(':>')
        if s == 'x' or s == 'o':
            break

    ttt = TicTacToe(size=3, pick=s)
    print('Player {} goes first'.format(ttt.player))
    print('~'*40)

    # Game loop
    while ttt.playing:
        if ttt.player == HUMAN:
            print('Go human...')
            print(ttt.b)

            while True:
                move = input('>')
                if ttt.b.play(int(move), ttt.PLAYERS[HUMAN]):
                    break
                else:
                    print('invalid move, try again')

        # If it is the computer's turn, let them compute the best move
        elif ttt.player == CPU:
            # Run computer turn
            print('CPU is thinking...')
            cpu_move = ttt.cpu_turn()
            print('The CPU played on spot {}'.format(cpu_move))

        else:
            print('Player selection error! Aborting!!!!!')
            exit()

        state = ttt.check_state()
        if state:
            print(state)
            input()

        ttt.next_player()


if __name__ == "__main__":
    console()
