from tkinter import *
#  from tkinter import ttk


class PlayerSelect(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        Label(self, text="Select your symbol")

        self.var = StringVar()

        Radiobutton(self, text="O", command=self.onPress, variable=self.var, value='O').pack(anchor=W)
        Radiobutton(self, text="X", command=self.onPress, variable=self.var, value='X').pack(anchor=W)
        self.var.set('O')

    def onPress(self):
        pass

if __name__ == "__main__":
    PlayerSelect().mainloop()
