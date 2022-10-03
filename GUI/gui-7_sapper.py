from random import shuffle
import tkinter as tk
from tkinter.messagebox import showinfo


#colors = ['#FFFFFF', '#0000FF', '#008200', '#FFFFFF', '#FF0000', '#000084', '#840000', '#008284', '#840084', '#000000']
colors = {
    1: 'blue',
    2: '#008200',
    3: '#FF0000',
    4: '#000084',
    5: '#840000',
    6: '#008284',
    7: '#840084',
    8: '#000000',
}

class MyButton(tk.Button):

    def __init__(self, master, x, y, number=0, *args, **kwargs):
        super(MyButton, self).__init__(master, width=3, font='Calibri 15 bold', *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.is_mine = False
        self.count_bomb = 0
        self.is_open = False

    def __repr__(self) -> str:
        return f"MyButton {self.x} {self.y} {self.number} {self.is_mine}"

class MineSweeper:

    window = tk.Tk()
    ROW = 5
    COLUMN = 7
    MINES = 7
    IS_GAME_OVER = False
    IS_FIRST_CLICK = True

    def __init__(self) -> None:
        self.buttons = []
        for i in range(MineSweeper.ROW+2):
            temp = []
            for j in range(MineSweeper.COLUMN+2):
                btn = MyButton(MineSweeper.window, x=i, y=j)
                btn.config(command=lambda button=btn: self.click(button))
                temp.append(btn)
            self.buttons.append(temp)

    def click(self, clicked_button:MyButton):

        if MineSweeper.IS_GAME_OVER:
            return None

        if MineSweeper.IS_FIRST_CLICK:
            self.insert_mines(clicked_button.number)
            self.count_mines_in_buttons()
            self.print_buttons()
            MineSweeper.IS_FIRST_CLICK = False

        if clicked_button.is_mine:
            clicked_button.config(text='*', background='red', disabledforeground='black')
            clicked_button.is_open = True
            MineSweeper.IS_GAME_OVER = True
            showinfo('Game over', 'Вы проиграли!')
            for i in range(1, MineSweeper.ROW+1):
                for j in range(1, MineSweeper.COLUMN+1):
                    clicked_button = self.buttons[i][j]
                    if btn.is_mine:
                        btn['text'] = '*'
        else:
            color = colors.get(clicked_button.count_bomb, 'black')
            if clicked_button.count_bomb:
                clicked_button.config(text=clicked_button.count_bomb, disabledforeground=color)
                clicked_button.is_open = True
            else:
                self.beradth_first_search(clicked_button)
        clicked_button.config(state='disable')
        clicked_button.config(relief=tk.SUNKEN)

    def beradth_first_search(self, btn: MyButton):
        queue = [btn]
        while queue:
            cur_btn = queue.pop()
            color = colors.get(cur_btn.count_bomb, 'black')
            if cur_btn.count_bomb:
                cur_btn.config(text=cur_btn.count_bomb, disabledforeground=color)
            else:
                cur_btn.config(text='', disabledforeground=color)
            cur_btn.is_open = True
            cur_btn.config(state='disable')
            cur_btn.config(relief=tk.SUNKEN)

            if cur_btn.count_bomb == 0:
                x, y = cur_btn.x, cur_btn.y
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        next_btn = self.buttons[x+dx][y+dy]
                        if not next_btn.is_open and 1<=next_btn.x<=MineSweeper.ROW and \
                             1<= next_btn.y <= MineSweeper.COLUMN and next_btn not in queue:
                             queue.append(next_btn)

    def reload(self):
        
    
    def create_widgets(self):

        menubar = tk.Menu(self.window)
        self.window.config(menu=menubar)
        settings_menu = tk.Menu(menubar, tearoff=0)
        settings_menu.add_command(label='Играть', command=self.reload)
        settings_menu.add_command(label='Настройки')
        settings_menu.add_command(label='Выход', command=self.window.destroy)
        menubar.add_cascade(label='Файл', menu=settings_menu)

        count = 1
        for i in range(1, MineSweeper.ROW+1):
            for j in range(1, MineSweeper.COLUMN+1):
                btn = self.buttons[i][j]
                btn.number = count
                btn.grid(row=i, column=j)
                count += 1

    def start(self):
        self.create_widgets()
        MineSweeper.window.mainloop()

    def print_buttons(self):
        for i in range(1,MineSweeper.ROW+1):
            for j in range(1,MineSweeper.COLUMN+1):
                btn = self.buttons[i][j]
                if btn.is_mine:
                    print('B', end='')
                else:
                    print(btn.count_bomb, end='')
            print()

    def insert_mines(self, number: int):
        index_mines = self.get_mines_places(number)
        for i in range(1,MineSweeper.ROW+1):
            for j in range(1,MineSweeper.COLUMN+1):
                btn = self.buttons[i][j]
                if btn.number in index_mines:
                    btn.is_mine = True

    def count_mines_in_buttons(self):
        for i in range(1,MineSweeper.ROW+1):
            for j in range(1,MineSweeper.COLUMN+1):
                btn = self.buttons[i][j]
                count_bomb = 0
                if not btn.is_mine:
                    for row_dx in [-1, 0, 1]:
                        for col_dx in [-1, 0, 1]:
                            neighbour = self.buttons[i+row_dx][j+col_dx]
                            if neighbour.is_mine:
                                count_bomb += 1
                btn.count_bomb = count_bomb


    @staticmethod
    def get_mines_places(exclude_number):
        indexes = list(range(1, MineSweeper.COLUMN*MineSweeper.ROW+1))
        indexes.remove(exclude_number)
        shuffle(indexes)
        return indexes[:MineSweeper.MINES]

game = MineSweeper()
game.start()
