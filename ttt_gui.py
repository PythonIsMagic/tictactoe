# coding: utf-8
from tkinter import *
from tkinter import ttk


class TicTacToeBoard(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        mainframe = ttk.Frame(root, padding=(12, 12, 12, 12))
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        buttons = [Button(mainframe, text='{}'.format(x)) for x in range(9)]

        for b in buttons:
            # Worked for text labels
            b.config(height=5, width=10)

        for x in range(3):
            for y in range(3):
                buttons.pop(0).grid(column=y, row=x)

        # Config padding
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5, sticky='EWNS')

root = Tk()
root.title("TicTacToe")
root.config(bg='black')
root.resizable(width=False, height=False)

TicTacToeBoard(root)

root.mainloop()
