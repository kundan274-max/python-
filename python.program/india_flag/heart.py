import turtle
import math
import random

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Heart with Colorful Stars")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Function to draw heart
def draw_heart():
    t.penup()
    t.goto(0, -180)
    t.pendown()
    t.color("red")
    t.begin_fill()

    for i in range(361):
        angle = math.radians(i)
        x = 16 * math.sin(angle) ** 3
        y = (13 * math.cos(angle)
             - 5 * math.cos(2 * angle)
             - 2 * math.cos(3 * angle)
             - math.cos(4 * angle))

        x *= 12
        y *= 12

        if i == 0:
            t.penup()
            t.goto(x, y)
            t.pendown()
        else:
            t.goto(x, y)

    t.end_fill()

# Function to draw a star
def draw_star(x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)

    t.end_fill()

# Draw Heart
draw_heart()

# Star colors
colors = ["yellow", "cyan", "pink", "white", "orange", "green", "violet", "gold"]

# Draw colorful stars
for _ in range(80):
    x = random.randint(-350, 350)
    y = random.randint(-250, 250)

    # Avoid placing stars inside heart
    if abs(x) < 150 and abs(y) < 180:
        continue

    size = random.randint(8, 18)
    color = random.choice(colors)

    draw_star(x, y, size, color)

turtle.done()