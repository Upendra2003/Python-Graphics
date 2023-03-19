from turtle import Turtle,Screen

pen=Turtle()
screen=Screen()

def move_forward():
    pen.forward(25)

def move_backward():
    pen.backward(25)

def turn_right():
    pen.setheading(pen.heading()+10)

def turn_left():
    pen.setheading(pen.heading()-10)

def clear():
    pen.clear()
    pen.up()
    pen.home()
    pen.down()

screen.listen()
screen.onkey(key='w',fun=move_forward)
screen.onkey(key='s',fun=move_backward)
screen.onkey(key='d',fun=turn_right)
screen.onkey(key='a',fun=turn_left)
screen.onkey(key='c',fun=clear)
screen.exitonclick()