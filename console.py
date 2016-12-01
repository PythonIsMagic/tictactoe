"""
  " Console interface for Tic Tac Toe.
  """
import game


def title():
    return 'Python Tic Tac Toe!'


def console():
    """ Game loop interface for console. """
    print(title())
    print('~'*40)
    print('select your symbol: (x/o)')
    while True:
        s = input(':>')
        if s == 'x' or s == 'o':
            break

    ttt = game.TicTacToe(size=3, pick=s)
    print('Player {} goes first'.format(ttt.player))
    print('~'*40)

    # Game loop
    while ttt.playing:
        if ttt.player == game.HUMAN:
            print('Go human...')
            print(ttt.b)

            while True:
                move = input('>')
                if ttt.b.play(int(move), ttt.PLAYERS[game.HUMAN]):
                    break
                else:
                    print('invalid move, try again')

        # If it is the computer's turn, let them compute the best move
        elif ttt.player == game.CPU:
            # Run computer turn
            print('CPU is thinking...')
            cpu_move = ttt.cpu_turn()
            print('The CPU played on spot {}'.format(cpu_move))

        else:
            print('Player selection error! Aborting!!!!!')
            exit()

        state = ttt.check_state()
        if state:
            print(state)
            input()

        ttt.next_player()
