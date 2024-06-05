from turtle import *

class Screenboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score0 = 0
        self.score1 = 0

    def creat_score_geral(self):
        self.goto(-50, 245)
        self.write(f"{self.score0}",  align="center", font=("Courier",36,"bold"))
        self.teleport(50, 245)
        self.write(f"{self.score1}", align="center", font=("Courier",36, "bold"))

    def add_score(self):
        self.clear()
        self.creat_score_geral()
        

    def creat_tracos(self):
        self.teleport(0, 245)
        self.setheading(270)
        self.pensize(5)
        self.shape("square")
        for _ in range(16):
            self.pendown()
            self.forward(25)
            self.penup()
            self.forward(25)
