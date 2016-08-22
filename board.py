from __future__ import print_function


class Board():
    def __init__(self, size=3):
        self.board = [['.' for x in range(size)] for y in range(size)]

    def __str__(self):
        _str = ''
        for row in self.board:
            for col in row:
                _str += str(col)
            _str += "\n"
        return _str
