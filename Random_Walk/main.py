from turtle import Turtle,Screen
import random

pen = Turtle()

colors = ["CornflowerBlue","IndianRed","DeepSkyBlue","DarkOrchid","wheat","SeaGreen","SlateGray"]

directions = [0,90,180,270]

pen.pensize(10)
pen.speed("fastest")

for _ in range(200):
    pen.color(random.choice(colors))
    pen.forward(30)
    pen.setheading(random.choice(directions))

screen=Screen()
screen.exitonclick()