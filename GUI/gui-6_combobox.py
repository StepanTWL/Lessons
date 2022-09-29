import tkinter as tk
from tkinter import ttk

def show_day():
    print(combo.get())

weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

win = tk.Tk()
win.geometry(f'300x400+100+200')
win.title('My Radiobutton')

combo = ttk.Combobox(win, values=weekdays)
ttk.Button(win, text='show_day',command=show_day).pack()
combo.current(0)
combo.pack()

win.mainloop() 