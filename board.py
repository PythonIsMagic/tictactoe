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

    def occupied(self, index):
        return self.board[index] in ['x', 'o']

    def play(self, i, piece):
        if i < 0 or i >= len(self.board):
            print('The index  is out of bounds!')
            return False

        if self.occupied(i):
            print('Spot #{} is already played on!'.format(i))
            return False

        self.board[i] = piece
        return True

    def find_win(self):
        # Searches for a complete winning row, column, or diagonal.
        # If one is found, it returns the symbol with the win.
        # using a counting method: 'o' = +1, 'x' = -1

        dndg_ct, updg_ct = 0, 0
        counts = []

        for x in range(self.length):
            col_ct, row_ct = 0, 0

            for y in range(self.length):
                # Check column
                col = x + self.length * y
                col_ct += SYMBOLS.get(self.board[col], 0)

                # Check row
                row = self.length * x + y
                row_ct += SYMBOLS.get(self.board[row], 0)
            counts.append(row_ct)
            counts.append(col_ct)

            # Check downward diagnonal
            dndg = x * (self.length + 1)
            dndg_ct += SYMBOLS.get(self.board[dndg], 0)

            # Check upward diagnonal
            start = self.length * (self.length - 1)
            updg = start - x * (self.length - 1)
            updg_ct += SYMBOLS.get(self.board[updg], 0)
            counts.append(updg_ct)
            counts.append(dndg_ct)

        if self.length in counts:
            return 'o'
        elif -self.length in counts:
            return 'x'

        return None

    def get_available_spaces(self):
        return [i for i in range(len(self)) if not self.occupied(i)]

    def what_row(self, index):
        return index / self.length

    def what_col(self, index):
        return index % self.length

    def get_col(self, spot):
        x = self.what_row(spot)
        return [(x + self.length * i) for i in range(self.length)]

    def get_row(self, spot):
        y = self.what_row(spot)
        return [(self.length * y + i) for i in range(self.length)]

    def get_up_diagonal(self):
        return [(x * (self.length + 1)) for x in range(self.length)]

    def get_dn_diagonal(self):
        start = self.length * (self.length - 1)
        return [(start - x * (self.length - 1)) for x in range(self.length)]

    def get_diagonal_spots(self):
        diag_nums = []
        return diag_nums

    def get_diagonal(self, spot):
        if spot in self.get_up_diagonal():
            return self.get_up_diagonal()
        if spot in self.get_dn_diagonal():
            return self.get_dn_diagonal()

            return None

    def score_move(self, move):
        pass
