from functools import partial
from itertools import cycle
import tkinter as tk


class FieldUI(tk.Canvas):

    def __init__(self, parent, size, variable):
        tk.Canvas.__init__(self, parent, width=size, height=size)
        self.size = size
        self.variable = variable
        self.variable.trace('w', self.update_display)
        self.update_display()

    def update_display(self, *_args):
        self.delete(tk.ALL)
        value = self.variable.get()
        if value == 'x':
            self.create_line(5, 5, self.size - 5, self.size - 5, width=4)
            self.create_line(self.size - 5, 5, 5, self.size - 5, width=4)
        elif value == 'o':
            self.create_oval(5, 5, self.size - 5, self.size - 5, width=4)
        elif value != '':
            raise ValueError("only 'x', 'o', and '' allowed")


class GameUI(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, background='black')
        self.symbols = cycle('xo')
        self.field_vars = [tk.StringVar() for _ in range(9)]

        for i, field_var in enumerate(self.field_vars):
            field_ui = FieldUI(self, 50, field_var)
            field_ui.bind('<Button-1>', partial(self.on_click, i))
            column, row = divmod(i, 3)
            field_ui.grid(row=row, column=column, padx=1, pady=1)

    def on_click(self, field_index, _event=None):
        field_var = self.field_vars[field_index]
        if not field_var.get():
            field_var.set(next(self.symbols))


def main():
    root = tk.Tk()
    game_ui = GameUI(root)
    game_ui.pack()
    root.mainloop()


if __name__ == '__main__':
    main()
