from random import shuffle
import tkinter as tk
from tkinter.messagebox import showerror, showinfo

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
    ROW = 10
    COLUMN = 10
    MINES = 15
    IS_GAME_OVER = False
    IS_FIRST_CLICK = True

    def __init__(self) -> None:
        self.buttons = []
        for i in range(MineSweeper.ROW+2):
            temp = []
            for j in range(MineSweeper.COLUMN+2):
                btn = MyButton(MineSweeper.window, x=i, y=j)
                btn.config(command=lambda button=btn: self.click(button))
                btn.bind('<Button-3>', self.right_click)
                temp.append(btn)
            self.buttons.append(temp)

    def right_click(self, event):
        if MineSweeper.IS_GAME_OVER:
            return
        cur_btn = event.widget
        if cur_btn['state']=='normal':
            cur_btn['state']='disable'
            cur_btn['text']='🚩'
            cur_btn['disabledforeground']='red'
        elif cur_btn['text']=='🚩':
            cur_btn['text']=''
            cur_btn['state']='normal'

    def click(self, clicked_button:MyButton):

        if MineSweeper.IS_GAME_OVER:
            return

        if MineSweeper.IS_FIRST_CLICK:
            self.insert_mines(clicked_button.number)
            self.count_mines_in_buttons()
            MineSweeper.IS_FIRST_CLICK = False

        if clicked_button.is_mine:
            clicked_button.config(text='*', background='red', disabledforeground='black')
            clicked_button.is_open = True
            MineSweeper.IS_GAME_OVER = True
            showinfo('Game over', 'Вы проиграли!')
            for i in range(1, MineSweeper.ROW+1):
                for j in range(1, MineSweeper.COLUMN+1):
                    clicked_button = self.buttons[i][j]
                    if clicked_button.is_mine:
                        clicked_button['text'] = '*'
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
        [child.destroy() for child in self.window.winfo_children()]
        self.__init__()
        self.create_widgets()
        MineSweeper.IS_FIRST_CLICK = True
        MineSweeper.IS_GAME_OVER = False

    def create_settings_win(self):
        win_settings = tk.Toplevel(self.window)
        win_settings.wm_title('Настройки')
        tk.Label(win_settings, text='Количество строк').grid(row=0, column=0, stick='w')
        tk.Label(win_settings, text='Количество колонок').grid(row=1, column=0, stick='w')
        tk.Label(win_settings, text='Количество мин').grid(row=2, column=0, stick='w')
        row_entry = tk.Entry(win_settings)
        row_entry.insert(0, MineSweeper.ROW)
        row_entry.grid(row=0, column=1, padx=20, pady=20)
        column_entry = tk.Entry(win_settings)
        column_entry.insert(0, MineSweeper.COLUMN)
        column_entry.grid(row=1, column=1, padx=20, pady=20)
        mines_entry = tk.Entry(win_settings)
        mines_entry.insert(0, MineSweeper.MINES)
        mines_entry.grid(row=2, column=1, padx=20, pady=20)
        save_btn = tk.Button(win_settings, text='Применить', command=lambda :self.change_settings(row_entry, column_entry, mines_entry))
        save_btn.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

    def change_settings(self, row: tk.Entry, column: tk.Entry, mines: tk.Entry):
        try:
            int(row.get()), int(column.get()), int(mines.get())
        except:
            showerror('Ошибка', 'Вы ввели неправельные значения!')
            return
        MineSweeper.ROW = int(row.get())
        MineSweeper.COLUMN = int(column.get())
        MineSweeper.MINES = int(mines.get())
        self.reload()

    def create_widgets(self):

        menubar = tk.Menu(self.window)
        self.window.config(menu=menubar)
        settings_menu = tk.Menu(menubar, tearoff=0)
        settings_menu.add_command(label='Играть', command=self.reload)
        settings_menu.add_command(label='Настройки', command=self.create_settings_win)
        settings_menu.add_command(label='Выход', command=self.window.destroy)
        menubar.add_cascade(label='Файл', menu=settings_menu)

        count = 1
        for i in range(1, MineSweeper.ROW+1):
            for j in range(1, MineSweeper.COLUMN+1):
                btn = self.buttons[i][j]
                btn.number = count
                btn.grid(row=i, column=j, stick='nsew')
                count += 1

        for i in range(1, MineSweeper.ROW+1):
            tk.Grid.rowconfigure(self.window, i, weight=1)

        for i in range(1, MineSweeper.COLUMN+1):
            tk.Grid.columnconfigure(self.window, i, weight=1)

    def start(self):
        self.create_widgets()
        MineSweeper.window.mainloop()

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
