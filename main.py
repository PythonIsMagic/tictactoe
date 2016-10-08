#!/usr/bin/env python
"""
# Author: lunatunez
# Date Created: Mon Apr  4 20:28:29 2016
# Purpose: Tic Tac Toe Game
"""
import sys
import console
import gui


def usage(runfile):
    print('Incorrect number of arguments.')
    print('usage: $ python3 {} mode'.format(runfile))
    print('mode can be "console" or "gui"')


if __name__ == "__main__":
    # Check arguments
    if len(sys.argv) != 2:
        usage(sys.argv[0])
    elif sys.argv[1] == 'console':
        console.console()

    elif sys.argv[1] == 'gui':
        gui.run()
    else:
        usage(sys.argv[0])
