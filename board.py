from __future__ import print_function
import math
import operator

PLACEHOLDER = '.'
SYMBOLS = {'o': 1, 'x': -1}


class Board():
    def __init__(self, size=3):
        self.board = [x for x in range(size ** 2)]
        self.length = int(math.sqrt(len(self.board)))

        self.up_diag = [(x * (self.length + 1)) for x in range(self.length)]
        start = self.length * (self.length - 1)
        self.dn_diag = [(start - x * (self.length - 1)) for x in range(self.length)]

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
            #  print('The index  is out of bounds!')
            return False

        if self.occupied(i):
            #  print('Spot #{} is already played on!'.format(i))
            return False

        self.board[i] = piece
        return True

    def find_win(self):
        # Searches for a complete winning row, column, or diagonal.
        # If one is found, it returns the symbol with the win.
        L = self.length
        lines = []

        # Columns and Rows
        for x in range(L):
            lines.append([self.board[self.length * x + y] for y in range(L)])
            lines.append([self.board[x + self.length * y] for y in range(L)])

        lines.append([self.board[i] for i in self.dn_diag])
        lines.append([self.board[i] for i in self.up_diag])

        for l in lines:
            if l.count('x') == L:
                return 'x'
            elif l.count('o') == L:
                return 'o'
        return None

    def get_available_spaces(self):
        return [i for i in range(len(self)) if not self.occupied(i)]

    def get_col(self, move):
        x = move % self.length
        col = [(x + self.length * i) for i in range(self.length)]
        return [self.board[i] for i in col]

    def get_row(self, move):
        y = move // self.length
        row = [(self.length * y + i) for i in range(self.length)]
        return [self.board[i] for i in row]

    def get_up_diag(self):
        return [self.board[i] for i in self.up_diag]

    def get_dn_diag(self):
        return [self.board[i] for i in self.dn_diag]

    def associated_lines(self, move):
        lines = []
        lines.append(self.get_row(move))
        lines.append(self.get_col(move))

        if move in self.up_diag:
            lines.append(self.get_up_diag())

        if move in self.dn_diag:
            lines.append(self.get_dn_diag())

        return lines

    def score_move(self, move, symbol):
        # Get all the lines associated with a move
        # Check that the move isn't already occupied

        if self.occupied(move):
            print('Spot #{} is already played on!'.format(move))
            return -1

        lines = self.associated_lines(move)
        scores = [self.score_line(l, symbol) for l in lines]

        #  print('Move {} is worth: {}'.format(move, sum(scores)))
        # We sum the values to account for opportunity value, and other values as well.
        return sum(scores)

    def score_line(self, line, symbol):
        if symbol == 'o':
            opp = line.count('x')
        else:
            opp = line.count('o')

        like = line.count(symbol)

        if like == 2:
            # Win value
            return 125
        elif opp == 2:
            # Block value
            return 100
        elif opp == 1 and like == 1:
            # No value
            return 0
        elif like == 1:
            # Building value
            return 45
        elif opp == 1:
            # Blocking value
            return 40
        else:
            # Opportunity value
            return 30

    def best_move(self, symbol):
        moves = {}
        for m in self.get_available_spaces():
            moves[m] = self.score_move(m, symbol)

        # Return the move that corresponds to the highest value.
        return max(moves.items(), key=operator.itemgetter(1))[0]
