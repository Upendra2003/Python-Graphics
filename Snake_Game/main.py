from turtle import Screen,Turtle
import time
from snake import Snake

screen = Screen()
screen.bgcolor('black')
screen.setup(width=500,height=500)
screen.title("Snake Game")
segments=[]
screen.tracer(0)

snake=Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
        
        
        




screen.exitonclick()