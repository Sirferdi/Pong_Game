from turtle import Turtle
FONT = ('courier', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(0, 230)
        self.write(f"{self.l_score} - {self.r_score}", align="center", font=FONT)

    def l_update(self):
        self.l_score += 1
        self.clear()
        self.write(f"{self.l_score} - {self.r_score}", align="center", font=FONT)

    def r_update(self):
        self.r_score += 1
        self.clear()
        self.write(f"{self.l_score} - {self.r_score}", align="center", font=FONT)

