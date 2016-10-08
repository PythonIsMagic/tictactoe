from tkinter import *

WIDTH = 4


class FieldUI(Canvas):
    def __init__(self, parent, size, variable):
        Canvas.__init__(self, parent, width=size, height=size, borderwidth=2, relief=GROOVE)
        self.size = size
        self.offset = int(size * .10)

        self.variable = variable
        self.variable.trace('w', self.update_display)
        self.update_display()

    def edge(self):
        return self.size - self.offset

    def update_display(self, *_args):
        self.delete(ALL)
        value = self.variable.get()
        if value == 'x':
            self.create_line(self.offset, self.offset, self.edge(), self.edge(), width=WIDTH)
            self.create_line(self.edge(), self.offset, self.offset, self.edge(), width=WIDTH)
        elif value == 'o':
            self.create_oval(self.offset, self.offset, self.edge(), self.edge(), width=WIDTH)

        elif value != '':
            raise ValueError("only 'x', 'o', and '' allowed")
