import turtle

player = turtle.Turtle()
screen = turtle.Screen()

player.shape("turtle")
player.shapesize(1)
player.color("green")
player.penup()

screen.listen()


def move_up():
    player.setheading(90)
    player.forward(10)


def move_right():
    player.setheading(0)
    player.forward(10)


def move_left():
    player.setheading(180)
    player.forward(10)


def move_down():
    player.setheading(270)
    player.forward(10)


turtle.onkey(fun=move_up, key="Up")
turtle.onkey(fun=move_right, key="Right")
turtle.onkey(fun=move_down, key="Down")
turtle.onkey(fun=move_left, key="Left")


screen.exitonclick()

