from turtle import*
from colorsys import hsv_to_rgb
bgcolor("black")
tracer(50)
pensize(1.5)

h=0.2
for i in range(150):
    goto(0, 0)
    color(hsv_to_rgb(h,1,1))
    h +=0.0009
    forward(i *0.8)
    left(270)
    circle(300 - i * 0.5, 45)
    update()

done()