from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()

        self.update_score()

    def l_increase_score(self):
        self.l_score += 1
        self.update_score()

    def r_increase_score(self):
        self.r_score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 200)
        self.write(f"{self.l_score} : {self.r_score}", align="center", font=("Courier", 16, "normal"))
        