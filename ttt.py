#!/usr/bin/env python

"""
# Author: lunatunez
# Date Created: Mon Apr  4 20:28:29 2016
# Purpose: Tic Tac Toe Game
"""

import board
import random


def main():
    print('Python Tic Tac Toe!')
    print('~'*40)
    print('CPU = \'o\' and human =\'x\'')

    # Initialize a new tictactoe board
    b = board.Board()

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
            print(b)

            while True:
                move = input('>')
                if b.play(int(move), 'x'):
                    break
                else:
                    print('invalid move, try again')

        # If it is the computer's turn, let them compute the best move
        elif player == 1:
            print('CPU is thinking...')

            while True:
                move = random.randint(0, len(b) - 1)
                if b.play(move, 'o'):
                    print('The CPU played on spot {}'.format(move))
                    break
        else:
            print('Player selection error! Aborting!!!!!')
            exit()

        # Check the state of board
        state = b.find_win()

        # CPU wins, Human wins, Tie, or in progress.
        if state == 'o' or state == 'x':
            print('{} wins!'.format(state))
            exit()

        # Change players
        player = (player + 1) % 2


if __name__ == "__main__":
    main()
