# from tkinter import *
"""
  " Popup window that allows the user to select which Tic Tac Toe symbol they want.
  """
from tkinter import Frame, Label, Radiobutton, Button, StringVar
from tkinter import S, W


class PlayerSelect(Frame):
    """ Tkinter popup window """
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        self.var = StringVar()
        self.selection = None

        Label(self, text="Select your symbol", font='size, 15').pack()
        Radiobutton(self, text="O", font='size, 15', variable=self.var, value='O').pack(anchor=W)
        Radiobutton(self, text="X", font='size, 15', variable=self.var, value='X').pack(anchor=W)
        self.var.set('O')

        Button(self, text="Play", font='size, 15', command=self.send).pack(anchor=S)

    def send(self):
        self.selection = self.var.get()
        self.destroy()
