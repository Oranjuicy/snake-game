from turtle import Turtle, Screen

MOVE_DISTANCE = 20
screen = Screen()
screen.setup(600, 600)
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for part in range(3):
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(part * -20, 0)
            self.snake_body.append(snake)

    def new_part(self):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(self.snake_body[-1].position())
        self.snake_body.append(snake)

    def move(self):
        for snakes in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[snakes].goto(self.snake_body[snakes - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def is_listening(self):
        screen.listen()
        screen.onkey(self.up, "Up")
        screen.onkey(self.down, "Down")
        screen.onkey(self.left, "Left")
        screen.onkey(self.right, "Right")

    def reset(self):
        for snakes in self.snake_body:
            snakes.hideturtle()
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

