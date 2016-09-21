#!/usr/bin/env python

"""
# Author: lunatunez
# Date Created: Mon Apr  4 20:28:29 2016
# Purpose: Tic Tac Toe Game
"""
import board
import random

SYMBOLS = {0: 'x', 1: 'o'}


class TicTacToe():
    def __init__(self, size):
        # Initialize a new tictactoe board
        self.b = board.Board(size)
        self.get_first()
        self.playing = True

    def get_first(self):
        # HUMAN = 0, CPU = 1
        self.player = random.randint(0, 1)

    def sym(self):
        return SYMBOLS[self.player]

    def cpu_turn(self):
        #  move = random.choice(b.get_available_spaces())
        move = self.b.best_move('o')

        if self.b.play(move, 'o'):
            return move

    def check_state(self):
        # Check the state of board
        state = self.b.find_win()

        # CPU wins, Human wins, Tie, or in progress.
        if state == 'o' or state == 'x':
            self.playing = False
            return '{} wins!'.format(state)
        elif len(self.b.get_available_spaces()) == 0:
            self.playing = False
            return 'Game is tied! Ending.'

    def next_player(self):
        self.player = (self.player + 1) % 2


def title():
    return 'Python Tic Tac Toe!'


def console():
    print(title())
    print('~'*40)
    print('CPU = \'o\' and human =\'x\'')

    ttt = TicTacToe(size=3)
    print('Player {} goes first'.format(ttt.player))
    print('~'*40)

    # Game loop
    while ttt.playing:
        if ttt.player == 0:
            print('Go human...')
            print(ttt.b)

            while True:
                move = input('>')
                if ttt.b.play(int(move), 'x'):
                    break
                else:
                    print('invalid move, try again')

        # If it is the computer's turn, let them compute the best move
        elif ttt.player == 1:
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


def gui():
    pass


if __name__ == "__main__":
    console()
