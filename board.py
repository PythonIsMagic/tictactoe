from __future__ import print_function

PLACEHOLDER = '.'


class Board():
    def __init__(self, size=3):
        self.board = [[PLACEHOLDER for x in range(size)] for y in range(size)]

    def __str__(self):
        _str = ''
        for row in self.board:
            for col in row:
                _str += str(col)
            _str += "\n"
        return _str

    def play(self, x, y, piece):
        if x < 0 or y < 0 or x >= len(self.board) or y >= len(self.board):
            print('x or y is out of bounds!')
            return -1

        if self.board[x][y] != PLACEHOLDER:
            print('({}, {}) is already played on!'.format(x, y))
            return -1

        self.board[x][y] = piece
