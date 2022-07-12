from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("SAMPON KA MOSA - BHUKHA SAMP")
screen.tracer(0)
screen.listen()
snake = Snake()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


food=Food()
scoreboard=ScoreBoard()
t=0.1
game_is_on=True
while game_is_on:
    screen.update()

    time.sleep(t)
    snake.move()
    if snake.head.distance(food)<15:
        scoreboard.incscore()
        food.refresh()
        snake.addsegment()
        if t>0.3:    
            t-=0.01
        
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    for snakesegment in range(1,len(snake.a)):
        if snake.a[snakesegment].pos()==snake.a[0].pos():
            scoreboard.reset()
            snake.reset()












screen.exitonclick()