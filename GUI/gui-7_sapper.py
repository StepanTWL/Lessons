from random import shuffle
import tkinter as tk


color = ['#FFFFFF', '#0000FF', '#008200', '#FFFFFF', '#FF0000', '#000084', '#840000', '#008284', '#840084', '#000000']


class MyButton(tk.Button):

    def __init__(self, master, x, y, number, *args, **kwargs):
        super(MyButton, self).__init__(master, width=3, font='Calibri 15 bold', *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.is_mine = False

    def __repr__(self) -> str:
        return f"MyButton {self.x} {self.y} {self.number} {self.is_mine}"

class MineSweeper:

    window = tk.Tk()
    ROW = 5
    COLUMN = 7
    MINES = 15

    def __init__(self) -> None:
        self.buttons = []
        count = 1
        for i in range(MineSweeper.ROW):
            temp = []
            for j in range(MineSweeper.COLUMN):
                btn = MyButton(MineSweeper.window, x=i, y=j, number=count)
                temp.append(btn)
                count += 1
            self.buttons.append(temp)

    def create_widgets(self):
        for i in range(MineSweeper.ROW):
            for j in range(MineSweeper.COLUMN):
                btn = self.buttons[i][j]
                btn.grid(row=i, column=j)

    def start(self):
        self.create_widgets()
        self.insert_mines()
        self.print_buttons()
        MineSweeper.window.mainloop()

    def print_buttons(self):
        for row_btn in self.buttons:
            print(row_btn)

    def insert_mines(self):
        index_mines = self.get_mines_places()
        for row_btn in self.buttons:
            for btn in row_btn:
                if btn.number in index_mines:
                    btn.is_mine = True

    @staticmethod
    def get_mines_places():
        indexes = list(range(1, MineSweeper.COLUMN*MineSweeper.ROW+1))
        shuffle(indexes)
        return indexes[:MineSweeper.MINES]

game = MineSweeper()
game.start()
