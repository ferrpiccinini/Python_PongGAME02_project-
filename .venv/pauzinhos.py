from turtle import *

screen = Screen()

class Pauzinho(Turtle):

    def __init__(self):
        super().__init__()
        self.pauzinho_list = []


    def creat_pau(self):
        pauzinho = Turtle("square")
        pauzinho.color("white")
        pauzinho.turtlesize(5,0.5)
        pauzinho.penup()
        pauzinho.speed("fastest")
        self.pauzinho_list.append(pauzinho)

    def paus(self):
        p1 = self.pauzinho_list[0]
        p2 = self.pauzinho_list[1]


    def move_upper1(self):
        self.pauzinho_list[0].goto(self.pauzinho_list[0].xcor(),(self.pauzinho_list[0].ycor()-30))

    def move_lower1(self):
        self.pauzinho_list[0].goto(self.pauzinho_list[0].xcor(),(self.pauzinho_list[0].ycor()+30))

    def move_upper2(self):
        self.pauzinho_list[1].goto(self.pauzinho_list[1].xcor(),(self.pauzinho_list[1].ycor()-30))

    def move_lower2(self):
        self.pauzinho_list[1].goto(self.pauzinho_list[1].xcor(),(self.pauzinho_list[1].ycor()+30))

    def move_pauzinho(self):
        screen.onkey(key="s", fun=self.move_upper1)
        screen.onkey(key="w", fun=self.move_lower1)
        screen.onkey(key="Down", fun=self.move_upper2)
        screen.onkey(key="Up", fun=self.move_lower2)