#!/usr/bin/env python

"""
# Author: lunatunez
# Date Created: Mon Apr  4 20:28:29 2016
# Purpose: Tic Tac Toe Game
"""

import board
import random


def main():
    pass

    # Initialize a new tictactoe board
    b = board.Board()
    print(b)

    # Determine which player goes first
    coin = random.randint(0, 1)
    print(coin)

    # Set gamestate to PLAYING
    playing = True

    exit()
    # Game loop
    while playing:

        # Display the board
        print(b)
        # If it is the computer's turn, let them compute the best move
        # If it is the human's turn, let them choose a move.

        # Execute the chosen move

        # Check the state of board
            # CPU wins, Human wins, Tie, or in progress.
        # If the game is still in progress:
            # Change the active player
        #

if __name__ == "__main__":
	main()
