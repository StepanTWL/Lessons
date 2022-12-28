import time
from tkinter import *

tk = Tk()  # создание объекта для работы с tkinter
tk.resizable(0, 0)
tk.title('Game')
tk.attributes('-topmost', 1)  # поверх окон

canvas = Canvas(tk, width=500, height=500, bd=0,
                highlightthickness=0)  # последние два параметра для того чтобы не было рамок у холста
canvas.pack()
canvas.update()


class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)  # сохраняем объект
        self.canvas.move(self.id, 250, 250)

    def draw(self):
        self.canvas.move(self.id, 0, -1)

ball = Ball(canvas, 'red')

while True:
    ball.draw()
    #tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

tk.mainloop()
