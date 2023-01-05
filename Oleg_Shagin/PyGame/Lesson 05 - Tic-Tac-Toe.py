import time
from tkinter import *
from tkinter import messagebox

tk = Tk()
app_running = True

size_x = 3
size_y = 3
size_window_x = 720
size_window_y = 720
step_x = size_window_x//size_x
step_y = size_window_y//size_y



def draw_table():
    for i in range(size_x):
        canvas.create_line(0, i*(size_window_x//size_x), size_window_x, i*(size_window_y//size_y))
    for i in range(size_y):
        canvas.create_line(i*(size_window_x//size_x), 0, i*(size_window_y//size_y), size_window_y)

def on_closing():
    global app_running
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        app_running = False
        tk.destroy()


tk.protocol("WM_DELETE_WINDOW", on_closing)#получает два аргумента: название события и функцию, которая будет вызываться при наступлении указанного события

tk.title('Tic-Tac-Toe')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)#поверх всех окон
canvas = Canvas(tk, width=size_window_x, height=size_window_y, bd=0, highlightthickness=0)#bd - задний фон, highlightthickness - толщина кромки
canvas.pack()
tk.update()

points = []
draw_table()

class Point:
    def __init__(self, x ,y, type):
        self.x = x
        self.y = y
        self.type = type

def draw_point(x, y, type):
    size = 25
    color = 'blue'
    if type:
        color = 'red'
    id = canvas.create_oval(x*step_x, y*step_y, (x+1)*step_x, (y+1)*step_y, fill=color)


def add_to_points(event):
    type = 0
    if event.num == 3:
        type = 1
    points.append(Point(event.x // (size_window_x//size_x), event.y // (size_window_y//size_y), type))
    draw_point(event.x // (size_window_x//size_x), event.y // (size_window_y//size_y), type)

canvas.bind_all("<Button-1>", add_to_points)
canvas.bind_all("<Button-1>", add_to_points)

while True:
    if app_running:
        tk.update_idletasks()
        tk.update()
    time.sleep(0.005)
