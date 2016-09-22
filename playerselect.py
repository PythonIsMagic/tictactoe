from tkinter import *
#  from tkinter import ttk


class PlayerSelect(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)

        self.pack()
        Label(self, text="Select your symbol")

        self.var = StringVar()

        Radiobutton(self, text="O", font='size, 15', variable=self.var, value='O').pack(anchor=W)
        Radiobutton(self, text="X", font='size, 15', variable=self.var, value='X').pack(anchor=W)
        self.var.set('O')

        Button(self, text="Play", font='size, 15', command=self.send).pack(anchor=S)

    def send(self):
        self.selection = self.var.get()
        self.destroy()

if __name__ == "__main__":
    PlayerSelect().mainloop()
