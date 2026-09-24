import turtle

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.speed(0)
turtle.tracer(4,0)

t.color("redl")
t.width(1)

for i in range(400):
 t.circle(i*0.3,90)
t.left(91)
t.forward(i*0.2)
t.circle(i*0.1,90)
t.up()
t.goto(0,0)
t.down()
turtle.done()
