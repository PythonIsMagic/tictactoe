from __future__ import print_function
import math

PLACEHOLDER = '.'


class Board():
    def __init__(self, size=3):
        #  self.board = [[PLACEHOLDER for x in range(size)] for y in range(size)]
        self.board = [x for x in range(size ** 2)]

    def __str__(self):
        _str = ''

        for i in self.board:
            if i % math.sqrt(len(self.board)) == 0:
                _str += '\n'
            _str += '{:3}'.format(i)
        return _str

    def play(self, i, piece):
        if i < 0 or i >= len(self.board):
            print('The index  is out of bounds!')
            return -1

        if self.board[i] != PLACEHOLDER:
            print('(Spot #{} is already played on!'.format(i))
            return -1

        self.board[i] = piece
