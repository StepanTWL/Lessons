import random
import time
from tkinter import *
from tkinter import messagebox

tk = Tk()
app_running = True

size_canvas_x = 800
size_canvas_y = 800
cell_x = cell_y = 10
step_x = size_canvas_x // cell_x
step_y = size_canvas_y // cell_y
size_canvas_x = cell_x * step_x
size_canvas_y = cell_y * step_y
ships = cell_x // 2
ship_len1 = cell_x // 5
ship_len2 = cell_x // 3
ship_len3 = cell_x // 2
enemy_ships = [[0] * (cell_y+1)] * (cell_x+1)
print(enemy_ships)


def on_closing():
    global app_running
    if messagebox.askokcancel('Выход из игры', "Хотите выйти из игры?"):
        app_running = False
        tk.destroy()


tk.protocol('WM_DELETE_WINDOW', on_closing)
tk.title('Sea Battle')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=size_canvas_x, height=size_canvas_y, bd=0, highlightthickness=0)
canvas.create_rectangle(0, 0, size_canvas_x, size_canvas_y, fill='white')
canvas.pack()
tk.update()


def draw_table():
    for i in range(cell_x + 1):
        canvas.create_line(step_x * i, 0, step_x * i, size_canvas_y)
    for i in range(cell_y + 1):
        canvas.create_line(0, step_y * i, size_canvas_x, step_y * i)


draw_table()


def add_to_all(event):
    click_type = 0
    if event.num == 3:
        click_type = 1
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()  # почему так???
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    position_mouse_x = mouse_x // step_x
    position_mouse_y = mouse_y // step_y


canvas.bind_all('<Button-1>', add_to_all)
canvas.bind_all('<Button-3>', add_to_all)

def generate_enemy_ships():
    global enemy_ships
    ships_list = []
    # генерируем список случайных длин кораблей
    for i in range(0, ships):
        ships_list.append(random.choice([ship_len1, ship_len2, ship_len3]))
    #print(ships_list)

    # подсчет суммарной длины кораблей
    sum_1_all_ships = sum(ships_list)
    sum_1_enemy = 0

    while sum_1_enemy != sum_1_all_ships:
        # обнуляем массив кораблей врага
        enemy_ships = [[0] * (cell_y+1)] * (cell_x+1)  # +1 для доп. линии справа и снизу, для успешных проверок генерации противника

        for i in range(0, ships):
            len = ships_list[i]
            horizont_vertikal = random.randrange(1, 3)  # 1- горизонтальное 2 - вертикальное

            primerno_x = random.randrange(0, cell_x)
            if primerno_x + len > cell_x:
                primerno_x = primerno_x - len

            primerno_y = random.randrange(0, cell_y)
            if primerno_y + len > cell_y:
                primerno_y = primerno_y - len

            # print(horizont_vertikal, primerno_x,primerno_y)
            if horizont_vertikal == 1:
                if primerno_x + len <= cell_x:
                    for j in range(0, len):
                        try:
                            check_near_ships = 0
                            check_near_ships = enemy_ships[primerno_y][primerno_x - 1] + \
                                               enemy_ships[primerno_y][primerno_x + j] + \
                                               enemy_ships[primerno_y][primerno_x + j + 1] + \
                                               enemy_ships[primerno_y + 1][primerno_x + j + 1] + \
                                               enemy_ships[primerno_y - 1][primerno_x + j + 1] + \
                                               enemy_ships[primerno_y + 1][primerno_x + j] + \
                                               enemy_ships[primerno_y - 1][primerno_x + j]
                            # print(check_near_ships)
                            if check_near_ships == 0:  # записываем в том случае, если нет ничего рядом
                                enemy_ships[primerno_y][primerno_x + j] = i + 1  # записываем номер корабля
                        except Exception:
                            pass
            if horizont_vertikal == 2:
                if primerno_y + len <= cell_y:
                    for j in range(0, len):
                        try:
                            check_near_ships = 0
                            check_near_ships = enemy_ships[primerno_y - 1][primerno_x] + \
                                               enemy_ships[primerno_y + j][primerno_x] + \
                                               enemy_ships[primerno_y + j + 1][primerno_x] + \
                                               enemy_ships[primerno_y + j + 1][primerno_x + 1] + \
                                               enemy_ships[primerno_y + j + 1][primerno_x - 1] + \
                                               enemy_ships[primerno_y + j][primerno_x + 1] + \
                                               enemy_ships[primerno_y + j][primerno_x - 1]
                            # print(check_near_ships)
                            if check_near_ships == 0:  # записываем в том случае, если нет ничего рядом
                                enemy_ships[primerno_y + j][primerno_x] = i + 1  # записываем номер корабля
                        except Exception:
                            pass

        # делаем подсчет 1ц
        sum_1_enemy = 0
        for i in range(0, cell_x):
            for j in range(0, cell_y):
                if enemy_ships[j][i] > 0:
                    sum_1_enemy = sum_1_enemy + 1

        # print(sum_1_enemy)
        # print(ships_list)
        print(enemy_ships)

generate_enemy_ships()

while app_running:
    if app_running:
        tk.update_idletasks()
        tk.update()
    time.sleep(0.005)
