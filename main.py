from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.Up, 'Up')
screen.onkey(snake.Down, 'Down')
screen.onkey(snake.Left, 'Left')
screen.onkey(snake.Right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        scoreboard.score += 1
        food.refresh()

screen.exitonclick()