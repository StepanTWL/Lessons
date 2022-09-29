import tkinter as tk

levels = {
    1: 'Easy',
    2: 'Middle',
    3: 'Hard',
}

def select_level():
    level = level_var.get()
    level_text.set(f'Вы выбрали {level} уровень')

def select_race():
    race = race_var.get()

win = tk.Tk()
win.geometry(f'300x400+100+200')
win.title('My Radiobutton')

level_var = tk.IntVar()
level_text = tk.StringVar()

race_var = tk.IntVar()

tk.Label(win, text='Select level').pack()
for level in sorted(levels):
    tk.Radiobutton(win, text=levels[level], variable=level_var, value=level, command=select_level).pack()
tk.Label(win,textvariable=level_text).pack()

tk.Label(win, text='Select race').pack()
tk.Radiobutton(win, text='Elf', variable=race_var, value=1, command=select_race).pack()
tk.Radiobutton(win, text='Human', variable=race_var, value=2, command=select_race).pack()
tk.Radiobutton(win, text='Org', variable=race_var, value=3, command=select_race).pack()

win.mainloop()