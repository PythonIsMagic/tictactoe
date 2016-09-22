# coding: utf-8
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from playerselect import PlayerSelect
import ttt


class TicTacToeBoard(Frame):
    def __init__(self, parent=None, game=None):
        Frame.__init__(self, parent)
        self.game = game

        mainframe = ttk.Frame(root, padding=(12, 12, 12, 12))
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        self.symbol = game.sym()
        self.strVars = [StringVar() for x in range(9)]

        buttons = []
        for i, s in enumerate(self.strVars):
            func = (lambda i=i: self.btn_press(i))

            b = Button(mainframe, textvariable=s, command=func)
            b.config(height=5, width=10, )
            buttons.append(b)

        for x in range(3):
            for y in range(3):
                buttons.pop(0).grid(row=x, column=y)

        # Config padding
        for child in mainframe.winfo_children():
            child.grid_configure(padx=2, pady=2, sticky='EWNS')
            child.config(font='size, 15')

        self.check_cpu()

    def check_cpu(self):
        # Check if it is the CPU's turn and run their turn.
        if self.game.player == ttt.CPU:
            cpu_move = self.game.cpu_turn()
            self.strVars[cpu_move].set(self.game.sym())
            self.assess()
            self.game.next_player()

    def btn_press(self, i):
        # Human turn
        result = self.game.b.play(i, self.game.sym())
        if result:
            self.strVars[i].set(self.game.sym())
            self.assess()
            self.game.next_player()
            self.check_cpu()

    def assess(self):
        state = self.game.check_state()
        if state:
            messagebox.showinfo("Game over!", state)
            #  self.quit()
            exit()  # Immediately exit

if __name__ == "__main__":
    root = Tk()
    root.title("TicTacToe")
    root.config(bg='black')
    root.resizable(width=False, height=False)

    # Get player selection
    inputDialog = PlayerSelect(root)
    root.wait_window(inputDialog)
    playerpick = inputDialog.selection
    print('symbol: {}'.format(inputDialog.selection))

    tttgame = ttt.TicTacToe(pick=playerpick)
    TicTacToeBoard(root, tttgame)

    root.mainloop()
