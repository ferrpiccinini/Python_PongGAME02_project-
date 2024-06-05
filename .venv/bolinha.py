from turtle import *

class Bolinha():

    def __init__(self):
        self.bol_list = []
        bol = Turtle("circle")
        bol.color("white")
        bol.penup()
        bol.shapesize(1,1)
        self.bol_list.append(bol)

