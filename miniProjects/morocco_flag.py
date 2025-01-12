import turtle
import time


turtle.bgcolor("black")
ok = turtle.Turtle()

ok.speed(1)
ok.pensize(5)
ok.forward(-80)
ok.hideturtle()
ok.begin_fill()
ok.color("red")
ok.penup()
ok.goto(-150, 150)
ok.pendown()
for i in range(2):
    ok.forward(300)
    ok.left(-90)
    ok.forward(300)
    ok.left(-90)


ok.end_fill()
ok.color("green")
ok.penup()
ok.goto(-80, -20)
ok.pendown()

for i in range(5):
    ok.forward(160)
    ok.left(144)


time.sleep(2)
