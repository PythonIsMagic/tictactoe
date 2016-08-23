from __future__ import print_function
import math

PLACEHOLDER = '.'
SYMBOLS = {'o': 1, 'x': -1}


class Board():
    def __init__(self, size=3):
        self.board = [x for x in range(size ** 2)]
        self.length = int(math.sqrt(len(self.board)))

    def __str__(self):
        _str = ''
        for i in range(len(self)):
            if i % self.length == 0:
                _str += '\n'
            _str += format(self.board[i], '^3')
        _str += '\n'
        return _str

    def __len__(self):
        return len(self.board)

    def play(self, i, piece):
        if i < 0 or i >= len(self.board):
            print('The index  is out of bounds!')
            return False

        if self.board[i] in ['x', 'o']:
            print('Spot #{} is already played on!'.format(i))
            return False

        self.board[i] = piece
        return True

    def find_win(self):
        # Searches for a complete winning row, column, or diagonal.
        # If one is found, it returns the symbol with the win.
        # using a counting method: 'o' = +1, 'x' = -1
        length = int(math.sqrt(len(self.board)))
        dndg_ct, updg_ct = 0, 0

        # Columns and rows
        for x in range(length):
            col_ct, row_ct = 0, 0

            for y in range(length):
                # Check column
                col = x + length * y
                col_ct += SYMBOLS.get(self.board[col], 0)

                # Check row
                row = length * x + y
                row_ct += SYMBOLS.get(self.board[row], 0)

            # Search diagonals
            # Check downward diagnonal
            dndg = x * (length + 1)
            dndg_ct += SYMBOLS.get(self.board[dndg], 0)

            # Check upward diagnonal
            start = length * (length - 1)
            updg = start - x * (length - 1)
            updg_ct += SYMBOLS.get(self.board[updg], 0)

            # Check row/col counts
            if row_ct == length or col_ct == length:
                return 'o'
            elif row_ct == -length or col_ct == -length:
                return 'x'

        if dndg_ct == length or updg_ct == length:
            return 'o'
        elif dndg_ct == -length or updg_ct == -length:
            return 'x'

        # If none are found, it returns None.
        return None
