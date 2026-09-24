import turtle
import time

# Screen Setup
screen = turtle.Screen()
screen.bgcolor("black")

# Turtle Setup
t = turtle.Turtle()
t.speed(0)
t.pensize(2)
t.hideturtle()

angle = 0

while True:
    t.clear()
    t.penup()
    t.goto(-50, 0)
    t.setheading(angle)
    t.pendown()

    t.color("red", "pink")
    t.begin_fill()

    for i in range(200):
        t.right(1)
        t.forward(1)
        t.backward(1)
        t.left(140)
        t.forward(111.65)
        t.backward(111.65)   # Return to the previous position

    t.end_fill()

    angle += 5
    screen.update()
    time.sleep(0.05)