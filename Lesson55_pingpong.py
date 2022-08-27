import turtle

winndow = turtle.Screen()
winndow.title('Ping-Pong')
winndow.setup(width=1.0, height=1.0)
winndow.bgcolor('black')
winndow.tracer(1)

border = turtle.Turtle()
border.hideturtle()
border.speed(0)
border.color('green')
border.begin_fill()
border.up()
border.goto(-500,300)
border.down()
border.goto(500,300)
border.goto(500,-300)
border.goto(-500,-300)
border.goto(-500,300)
border.end_fill()

border.goto(0,300)
border.color('white')
border.setheading(270)
for i in range(25):
    if not i%2:
        border.forward(24)
    else:
        border.up()
        border.forward(24)
        border.down()

rockets=[]
#for i in range(-1, 2, 2):
rocket = turtle.Turtle()
rocket.hideturtle()
rocket.color('white')
rocket.shape('square')
rocket.shapesize(stretch_len=1, stretch_wid=5)
rocket.up()
rocket.goto(-450,0)
rocket.showturtle()
#    rockets.append(rocket)

def move_up():
    y = rocket.ycor() + 10
    if y > 250:
        y = 250
    rocket.sety(y)

def move_down():
    y = rocket.ycor() - 10
    if y < -250:
        y = -250
    rocket.sety(y)


winndow.listen()
winndow.onkeypress(move_up(), "w")
winndow.onkeypress(move_down(), "s")
#winndow.onkeypress(move_up(rockets[1]), "Up")
#winndow.onkeypress(move_down(rockets[1]), "Down")
winndow.mainloop()