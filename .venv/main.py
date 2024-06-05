from turtle import *
from pauzinhos import Pauzinho
from screenboard import Screenboard
from bolinha import Bolinha
import time

screen = Screen()
pauzinho = Pauzinho()
screenboard = Screenboard()
bolinha = Bolinha()
screen.tracer(0)

screen.listen()
screen.setup(800,600)
screen.bgcolor("black")
screenboard.creat_score_geral()
screenboard.creat_tracos()


game_is_on = True

for _ in range(2):
    pauzinho.creat_pau()
pauzinho_1 = pauzinho.pauzinho_list[0]
pauzinho_2 = pauzinho.pauzinho_list[1]
bolinha = bolinha.bol_list[0]
pauzinho_1.goto(-350,0)
pauzinho_2.goto(350,0)
pauzinho.move_pauzinho()
NUMBER = 180
SPEED = 0.05

bolinha.setheading(30)

while 4<5:
    screen.update()
    time.sleep(SPEED)
    bolinha.fd(10)
    if pauzinho_2.distance(bolinha) < 50 and bolinha.xcor() > 340:
        bolinha.setheading(bolinha.heading()-NUMBER)
        NUMBER += 10
        if SPEED != 0.03:
            SPEED -= 0.001

    elif pauzinho_1.distance(bolinha) < 50 and bolinha.xcor() > -340:
        bolinha.setheading(bolinha.heading()+NUMBER)
        NUMBER += 10
        if SPEED != 0.03:
            SPEED -= 0.001

    elif bolinha.distance(bolinha.xcor(),280) < 10:
        bolinha.setheading(bolinha.heading()*-1)
        if SPEED != 0.03:
            SPEED -= 0.001

    elif bolinha.distance(bolinha.xcor(),-280) < 10:
        bolinha.setheading(bolinha.heading()*-1)
        if SPEED != 0.03:
            SPEED -= 0.001

    elif bolinha.distance(400,bolinha.ycor()) < 10 or bolinha.distance(-400,bolinha.ycor()) < 10:
        if bolinha.xcor() < 380:
            screenboard.score1 += 1
            screenboard.clear()
            screenboard.creat_tracos()
            screenboard.creat_score_geral()
        else:
            screenboard.score0 += 1
            screenboard.clear()
            screenboard.creat_tracos()
            screenboard.creat_score_geral()
        bolinha.goto(0,0)
        SPEED = 0.05


# while game_is_on == True:
















screen.exitonclick()