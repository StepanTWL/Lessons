"""
import turtle

def sq(a):
    for i in range(4):
        joe.color(colors[i])
        joe.forward(a)
        joe.left(90)

colors=['red','brown','green','blue']

joe=turtle.Turtle()
joe.speed(100)

line=40
for i in range(60):
    sq(line)
    line+=5
    joe.right(10)


import turtle
def rightMNOG(n: int, line: int) -> None:
    sumAngle=(n-2)*180
    if sumAngle%n==0:
        angle=sumAngle//n
        for i in range(n):
            pen.forward(line)
            pen.left(180-angle)

pen=turtle.Turtle()
pen.speed(10)
pen.up()
pen.setposition(-30, -30)
pen.down()
for i in range(3,25):
    rightMNOG(i,50)


import turtle, time

def starFILL(n: int, line: int) -> None:
    joe.begin_fill()
    star(n,line)
    joe.end_fill()

def star(n: int, line: int) -> None:
    if n%2:
        for i in range(n):
            joe.forward(line)
            angle=n//2*360/n
            joe.left(angle)

joe = turtle.Turtle()
for i in range(5,26,2):
    joe.speed(10)
    starFILL(i,200)
    time.sleep(1)
    joe.reset()


import random
import turtle, time

def starFILL(n: int, line: int) -> None:
    joe.begin_fill()
    star(n,line)
    joe.end_fill()

def star(n: int, line: int) -> None:
    if n%2:
        for i in range(n):
            joe.forward(line)
            angle=n//2*360/n
            joe.left(angle)

window = turtle.Screen()
window.bgcolor('black')
window.setup(700,500)
joe = turtle.Turtle()
joe.speed(0)
joe.color('yellow')
for i in range(50):
    x = random.randint(-320, 320)
    y = random.randint(-220, 220)
    joe.up()
    joe.setposition(x,y)
    joe.down()
    size = random.randint(10, 20)
    vershina=random.choice([5,7])
    starFILL(vershina, size)
time.sleep(5)


import turtle, random

def starFILL(n: int, line: int) -> None:
    joe.begin_fill()
    star(n,line)
    joe.end_fill()

def star(n: int, line: int) -> None:
    joe.left(random.randint(0,360))
    if n%2:
        for i in range(n):
            joe.forward(line)
            angle=n//2*360/n
            joe.left(angle)

def move(x: int, y: int):
    joe.up()
    joe.setposition(x,y)
    joe.down()
    size = random.randint(10, 20)
    vershina=random.choice([5,7])
    starFILL(vershina, size)

window = turtle.Screen()
window.bgcolor('black')
window.setup(700,500)
joe = turtle.Turtle()
joe.speed(0)
joe.color('yellow')
joe.hideturtle()
window.onclick(move)
window.listen()#слушать события
window.mainloop()#не дает программе закрыится



import turtle

def moveUp() -> None:
    x,y = pen.position()
    pen.setposition(x,y+5)

def moveDown() -> None:
    x,y = pen.position()
    pen.setposition(x,y-5)

def moveLeft() -> None:
    x,y = pen.position()
    pen.setposition(x-5,y)

def moveRight() -> None:
    x,y = pen.position()
    pen.setposition(x+5,y)

window = turtle.Screen()
pen = turtle.Turtle()

window.onkey(moveUp, "Up")
window.onkey(moveDown, "Down")
window.onkey(moveLeft, "Left")
window.onkey(moveRight, "Right")
window.listen()
window.mainloop()

import turtle

europe = turtle.Turtle()
africa = turtle.Turtle()
america = turtle.Turtle()
asia = turtle.Turtle()
australia = turtle.Turtle()

for i in [europe,africa,america,asia,australia]:
    i.up()

europe.goto(-100,100)
africa.goto(0,100)
america.goto(100,100)
asia.goto(-50,50)
australia.goto(50,50)

for i in [europe,africa,america,asia,australia]:
    i.down()
    i.pensize(4)

europe.color('blue')
africa.color('black')
america.color('red')
asia.color('yellow')
australia.color('green')

for i in [europe,africa,america,asia,australia]:
    i.circle(50)

import random
import turtle

border=turtle.Turtle()
window=turtle.Screen()
border.speed()
border.up()
border.hideturtle()
border.pensize(5)
border.color('red')
border.goto(300,300)
border.down()
border.goto(300,-300)
border.goto(-300,-300)
border.goto(-300,300)
border.goto(300,300)

balls=[]
count=10
for i in range(count):
    ball = turtle.Turtle()
    ball.hideturtle()
    ball.shape('circle')
    dx=random.randint(-5,5)
    dy=random.randint(-5,5)
    ball.color(random.random(), random.random(), random.random())
    ball.up()
    ball.speed()
    ball.setposition(random.randint(-293,293), random.randint(-293,293))
    ball.showturtle()
    balls.append([ball, dx, dy])
while True:
    for i in range(count):
        x,y = balls[i][0].position()
        if x+balls[i][1]>=293 or x+balls[i][1]<=-293:
            balls[i][1]=-balls[i][1]
        if y+balls[i][2]>=293 or y+balls[i][2]<=-293:
            balls[i][2]=-balls[i][2]
        balls[i][0].goto(x+balls[i][1],y+balls[i][2])

window.mainloop()
"""

import random
import turtle
border = turtle.Turtle()
border.hideturtle()
border.speed(100)
border.pensize(5)
border.up()
border.goto(-250, 250)
border.down()
border.goto(-250,-250)
border.goto(250,-250)
border.goto(250,250)

winndow=turtle.Screen()
winndow.bgcolor('yellow')
winndow.tracer(20)

balls=[]
count=25
forms=['circle','square','triangle']

for i in range(count):
    ball = turtle.Turtle(shape=random.choice(forms))
    ball.speed(0)
    ball.up()
    ball.color(random.random(),random.random(),random.random())
    ball.goto(random.randint(-150,150),random.randint(100,220))
    ball.speedY = 0
    ball.speedX = random.randint(-5,5)
    ball.angle = random.randint(-5,5)
    ball.gravitation = random.randint(10,20)*0.01
    balls.append(ball)

while True:
    winndow.update()
    for ball in balls:
        ball.left(ball.angle)
        ball.speedY -= ball.gravitation
        ball.goto(ball.xcor()+ball.speedX, ball.ycor()+ball.speedY)
        if ball.ycor() < -240:
            ball.sety(-240)
            ball.speedY = -ball.speedY
        if ball.xcor() > 240 or ball.xcor() < -240:
            ball.speedX = -ball.speedX