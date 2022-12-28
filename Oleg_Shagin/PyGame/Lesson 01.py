from tkinter import *

tk = Tk() #создание объекта для работы с tkinter

canvas = Canvas(tk, width=500, height=500) #область рисования
canvas.pack()
canvas.create_arc(150, 150, 350, 350, extent=270, style=ARC)#дуга
canvas.create_polygon(10, 10, 70, 70, 10, 70, fill='red')#красный треугольник
canvas.create_text(250, 50, text='Hi world', fill='black', font=('Arial', 20))


def move_fish(event):
    if event.keysym == 'Up':
        canvas.move(id_img, 0, -2)
    elif event.keysym == 'Down':
        canvas.move(id_img, 0, 2)
    elif event.keysym == 'Left':
        canvas.move(id_img, -2, 0)
    elif event.keysym == 'Right':
        canvas.move(id_img, 2, 0)

canvas.bind_all('KeyPress-Up', move_fish)#фиксирование нажатия клавиш
canvas.bind_all('KeyPress-Down', move_fish)
canvas.bind_all('KeyPress-Left', move_fish)
canvas.bind_all('KeyPress-Right', move_fish)

tk.mainloop()