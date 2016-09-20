#!/usr/bin/env python

"""
# Author: lunatunez
# Date Created: Mon Apr  4 20:28:29 2016
# Purpose: Tic Tac Toe Game
"""
import board
import random


class TicTacToe():
    def __init__(self, size):
        # Initialize a new tictactoe board
        self.b = board.Board(size)


def consolerun():
    print('Python Tic Tac Toe!')
    print('~'*40)
    print('CPU = \'o\' and human =\'x\'')

    ttt = TicTacToe(size=3)

    # Determine which player goes first
    # HUMAN = 0, CPU = 1
    player = random.randint(0, 1)

    print('Flipping the coin for first go....')
    if player == 0:
        print('The HUMAN goes first!')
    else:
        print('The CPU goes first!')
    print('~'*40)

    playing = True

    # Game loop
    while playing:
        if player == 0:
            print('Go human...')
            print(ttt.b)

            while True:
                move = input('>')
                if ttt.b.play(int(move), 'x'):
                    break
                else:
                    print('invalid move, try again')

        # If it is the computer's turn, let them compute the best move
        elif player == 1:
            print('CPU is thinking...')

            #  move = random.choice(b.get_available_spaces())
            move = ttt.b.best_move('o')
            if ttt.b.play(move, 'o'):
                print('The CPU played on spot {}'.format(move))
        else:
            print('Player selection error! Aborting!!!!!')
            exit()

        # Check the state of board
        state = ttt.b.find_win()

        # CPU wins, Human wins, Tie, or in progress.
        if state == 'o' or state == 'x':
            print('{} wins!'.format(state))
            exit()
        elif len(ttt.b.get_available_spaces()) == 0:
            print('Sorry the game is tied! Ending.')
            exit()

        # Change players
        player = (player + 1) % 2


if __name__ == "__main__":
    consolerun()
