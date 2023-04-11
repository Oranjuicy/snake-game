from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard


# Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("SnakeJazz Game")
screen.tracer(0)

# Creating a starting snake
snake = Snake()
food = Food()
scoreboard = Scoreboard()
snake.is_listening()

# Game Body
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.move()
        scoreboard.add_score()
        snake.new_part()

    # Detect collision with wall
    snake_x = snake.head.xcor()
    snake_y = snake.head.ycor()
    if snake_x > 300 or snake_x < -300 or snake_y > 300 or snake_y < -300:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for part in snake.snake_body[1:]:
        if snake.head.distance(part) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
