from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.color("black")
        self.score = 0
        self.sety(260)
        self.setx(-290)
        self.write(f"Score: {self.score}", move=False, align='left', font=FONT)

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", move=False, align='left', font=FONT)

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", False, "center", FONT)

