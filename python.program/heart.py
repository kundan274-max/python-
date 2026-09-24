import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title(" my name is kundan")
pen = turtle.Turtle()
pen.speed(5)
pen.color("red")
pen.pensize(3)
pen.begin_fill()
pen.left(140)
pen.forward(180)
pen.circle(-90, 200)
pen.left(120)
pen.circle(-90, 200)
pen.forward(180)
pen.end_fill()

pen.penup()
pen.goto(0, -20)
pen.color("white")
pen.write(
    "kundan singh",
    align="center",
    font=("Arial", 24, "bold")
)

pen.hideturtle()

turtle.done()