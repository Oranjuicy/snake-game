from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.get_high_score()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 265)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, "center", ("Courier New", 30, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as new_score:
                new_score.write(f"{self.high_score}")
        self.score = 0
        self.show_score()

    def add_score(self):
        self.score += 1
        self.show_score()

    def get_high_score(self):
        with open("data.txt") as high_score:
            self.high_score = int(high_score.read())







