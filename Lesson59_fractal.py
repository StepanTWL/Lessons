"""
gens = 10
axiom = 'A'
rules = {
    'A': 'AB',
    'B': 'A'
}


def apple_rules(s: str) -> str:
    res = ''
    for chr in s:
        res += rules[chr]
    return res


for gen in range(gens):
    print(f'generation {gen}: {axiom}')
    axiom = apple_rules(axiom)


import turtle

# L-system setting
gens = 18
axiom = 'A'
rules = {
    'A': 'AB',
    'B': 'A'
}

# screen setting
WIDTH, HEIGHT = 1600, 900
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.screensize(3 * WIDTH, 3 * HEIGHT)  # размер поля в 9 раз больше окна
screen.bgcolor('black')
screen.delay(0)

# turtle setting
STEP, ANGLE = 50, 60
leo = turtle.Turtle()
leo.pensize(3)
leo.speed(0)
leo.color('orange')


def apple_rules(s: str) -> str:
    return ''.join([rules[chr] for chr in s])


def get_result(gens, axiom):
    for gen in range(gens):
        axiom = apple_rules(axiom)
    return axiom


turtle.pencolor('white')
turtle.goto(-WIDTH // 2 + 60, -HEIGHT // 2 + 60)
turtle.clear()
turtle.write(f'generation: {gens}', font=('Arial', 60, 'normal'))
turtle.hideturtle()


axiom = get_result(gens, axiom)
for chr in axiom:
    if chr == 'A':  # плохо сделано!!!
        leo.left(ANGLE)
        leo.forward(STEP)
    else:
        leo.right(ANGLE)
        leo.forward(STEP)

leo.hideturtle()
screen.exitonclick()


import turtle

# L-system setting
gens = 8
axiom = 'F'
chr_1, rule_1 = 'F', 'F-G+F+G-F'
chr_2, rule_2 = 'G', 'GG'

# screen setting
WIDTH, HEIGHT = 1600, 900
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.screensize(3 * WIDTH, 3 * HEIGHT)  # размер поля в 9 раз больше окна
screen.bgcolor('black')
screen.delay(0)

# turtle setting
STEP, ANGLE = 1, 120
leo = turtle.Turtle()
leo.pensize(3)
leo.speed(0)
leo.setpos(-WIDTH//3, -HEIGHT//2)
leo.color('green')



def apple_rules(s: str) -> str:
    return ''.join([rule_1 if chr == chr_1 else rule_2 if chr == chr_2 else chr for chr in s])


def get_result(gens, axiom):
    for gen in range(gens):
        axiom = apple_rules(axiom)
    return axiom


turtle.pencolor('white')
turtle.goto(-WIDTH // 2 + 60, HEIGHT // 2 - 100)
turtle.clear()
turtle.write(f'generation: {gens}', font=('Arial', 60, 'normal'))
#turtle.hideturtle()


axiom = get_result(gens, axiom)
for chr in axiom:
    if chr == chr_1 or chr == chr_2:
        leo.forward(STEP)
    elif chr == '+':
        leo.right(ANGLE)
    elif chr == '-':
        leo.left(ANGLE)


screen.exitonclick()


#dragon
import turtle

# L-system setting
gens = 13
axiom = 'XY'
chr_1, rule_1 = 'X', 'X+YF+'
chr_2, rule_2 = 'Y', '-FX-Y'

# screen setting
WIDTH, HEIGHT = 1600, 900
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.screensize(3 * WIDTH, 3 * HEIGHT)  # размер поля в 9 раз больше окна
screen.bgcolor('black')
screen.delay(0)

# turtle setting
STEP, ANGLE = 4, 90
leo = turtle.Turtle()
leo.pensize(3)
leo.speed(0)
leo.setpos(WIDTH//4, -HEIGHT//4-25)
leo.color('green')



def apple_rules(s: str) -> str:
    return ''.join([rule_1 if chr == chr_1 else rule_2 if chr == chr_2 else chr for chr in s])


def get_result(gens, axiom):
    for gen in range(gens):
        axiom = apple_rules(axiom)
    return axiom


turtle.pencolor('white')
turtle.goto(-WIDTH // 2 + 60, HEIGHT // 2 - 100)
turtle.clear()
turtle.write(f'generation: {gens}', font=('Arial', 60, 'normal'))
#turtle.hideturtle()


axiom = get_result(gens, axiom)
for chr in axiom:
    if chr == chr_1 or chr == chr_2:
        leo.forward(STEP)
    elif chr == '+':
        leo.right(ANGLE)
    elif chr == '-':
        leo.left(ANGLE)


screen.exitonclick()



#снежинка коха
import turtle

# L-system setting
gens = 6
axiom = 'F++F++F'
chr_1, rule_1 = 'F', 'F-F++F-F'

# screen setting
WIDTH, HEIGHT = 1600, 900
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.screensize(3 * WIDTH, 3 * HEIGHT)  # размер поля в 9 раз больше окна
screen.bgcolor('black')
screen.delay(0)

# turtle setting
STEP, ANGLE = 1, 60
leo = turtle.Turtle()
leo.pensize(3)
leo.speed(0)
leo.setpos(-WIDTH//6, HEIGHT//6)
leo.color('green')



def apple_rules(s: str) -> str:
    return ''.join([rule_1 if chr == chr_1 else chr for chr in s])


def get_result(gens, axiom):
    for gen in range(gens):
        axiom = apple_rules(axiom)
    return axiom


turtle.pencolor('white')
turtle.goto(-WIDTH // 2 + 60, HEIGHT // 2 - 100)
turtle.clear()
turtle.write(f'generation: {gens}', font=('Arial', 60, 'normal'))
#turtle.hideturtle()


axiom = get_result(gens, axiom)
for chr in axiom:
    if chr == chr_1:
        leo.forward(STEP)
    elif chr == '+':
        leo.right(ANGLE)
    elif chr == '-':
        leo.left(ANGLE)


screen.exitonclick()






#Ветка
import turtle

# L-system setting
gens = 6
axiom = 'XY'
chr_1, rule_1 = 'F', 'FF'
chr_2, rule_2 = 'X', 'F[+X]F[-X]+X'

# screen setting
WIDTH, HEIGHT = 1600, 900
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.screensize(3 * WIDTH, 3 * HEIGHT)  # размер поля в 9 раз больше окна
screen.bgcolor('black')
screen.delay(0)

# turtle setting
STEP, ANGLE = 7, 20
stack = []
leo = turtle.Turtle()
leo.pensize(3)
leo.speed(0)
#leo.setpos(0, -HEIGHT//2) рисовать вверх
leo.setpos(0, HEIGHT//2)
leo.color('green')



def apple_rules(s: str) -> str:
    return ''.join([rule_1 if chr == chr_1 else rule_2 if chr == chr_2 else chr for chr in s])


def get_result(gens: int, axiom: str) -> str:
    for gen in range(gens):
        axiom = apple_rules(axiom)
    return axiom


turtle.pencolor('white')
turtle.goto(-WIDTH // 2 + 60, HEIGHT // 2 - 100)
turtle.clear()
turtle.write(f'generation: {gens}', font=('Arial', 60, 'normal'))
turtle.hideturtle()


axiom = get_result(gens, axiom)
#leo.left(90) рисовать вверх
leo.right(90)
for chr in axiom:
    if chr == chr_1:
        leo.forward(STEP)
    elif chr == '+':
        leo.right(ANGLE)
    elif chr == '-':
        leo.left(ANGLE)
    elif chr == '[':
        angle_, pos_ = leo.heading(), leo.pos()
        stack.append((angle_, pos_))
    elif chr == ']':
        angle_, pos_ = stack.pop()
        leo.setheading(angle_)
        leo.penup()
        leo.goto(pos_)
        leo.pendown()

screen.exitonclick()
"""

# Ветка более сложная
import turtle
import random

# L-system setting
gens = 10
axiom = 'XY'
chr_1, rule_1 = 'X', 'F[@[-X]+X]'

# screen setting
WIDTH, HEIGHT = 1600, 900
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.screensize(3 * WIDTH, 3 * HEIGHT)  # размер поля в 9 раз больше окна
screen.bgcolor('black')
screen.delay(0)

# turtle setting
STEP, ANGLE = 80, lambda: random.randint(0, 45)
stack = []
color = [0.35, 0.2, 0.0]
thickness = 20#толщина
leo = turtle.Turtle()
leo.pensize(3)
leo.speed(0)
leo.setpos(0, -HEIGHT//2)
leo.color('green')


def apple_rules(s: str) -> str:
    return ''.join([rule_1 if chr == chr_1 else chr for chr in s])


def get_result(gens: int, axiom: str) -> str:
    for gen in range(gens):
        axiom = apple_rules(axiom)
    return axiom


turtle.pencolor('white')
turtle.goto(-WIDTH // 2 + 60, HEIGHT // 2 - 100)
turtle.clear()
turtle.write(f'generation: {gens}', font=('Arial', 60, 'normal'))
turtle.hideturtle()

axiom = get_result(gens, axiom)
leo.left(90)
leo.pensize(thickness)
for chr in axiom:
    leo.color(color)
    if chr == 'F' or chr == 'X':
        leo.forward(STEP)
    elif chr == '@':
        STEP -= 6
        color[1] += 0.04
        thickness -= 2
        thickness = max(1, thickness)
        leo.pensize(thickness)
    elif chr == '+':
        leo.right(ANGLE())
    elif chr == '-':
        leo.left(ANGLE())
    elif chr == '[':
        angle_, pos_ = leo.heading(), leo.pos()
        stack.append((angle_, pos_, thickness, STEP, color[1]))
    elif chr == ']':
        angle_, pos_, thickness, STEP, color[1] = stack.pop()
        leo.pensize(thickness)
        leo.setheading(angle_)
        leo.penup()
        leo.goto(pos_)
        leo.pendown()

screen.exitonclick()
