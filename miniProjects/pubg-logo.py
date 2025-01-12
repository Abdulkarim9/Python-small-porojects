import turtle
import time


turtle.bgcolor("black")
turtle.title("PUBG LOGO")
t = turtle.Turtle()
t.hideturtle()
t.speed(1)
t.pencolor("white")
t.pensize(8)
t.penup()
t.goto(-100, 0)
t.pendown()
for i in range(2):
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(90)

t.penup()
t.goto(-100, 20)
t.pendown()
t.forward(-20)

t.penup()
t.goto(100, 20)
t.pendown()
t.forward(20)

t.penup()
t.goto(-100, 75)
t.pendown()
t.forward(-20)

t.penup()
t.goto(100, 75)
t.pendown()
t.forward(20)

t.penup()
t.goto(0, 25)
t.pendown()
t.write("PUBG", align="center", font=("Rockwell Extra Bold", 30, "normal"))
time.sleep(5)
