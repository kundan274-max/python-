
import turtle
import math
screen = turtle.Screen()
screen.title("🇮🇳 Animated Indian Flag")
screen.bgcolor("skyblue")
screen.setup(1100, 700)
screen.tracer(0)

flag = turtle.Turtle()
flag.hideturtle()
flag.speed(0)

chakra = turtle.Turtle()
chakra.hideturtle()
chakra.speed(0)

pole = turtle.Turtle()
pole.hideturtle()
pole.speed(0)

cloud = turtle.Turtle()
cloud.hideturtle()
cloud.speed(0)

grass = turtle.Turtle()
grass.hideturtle()
grass.speed(0)

sun = turtle.Turtle()
sun.hideturtle()
sun.speed(0)

sun.penup()
sun.goto(360,230)
sun.color("yellow")
sun.begin_fill()
sun.circle(45)
sun.end_fill()
def draw_cloud(x,y):
    cloud.penup()
    cloud.goto(x,y)
    cloud.color("white")
    cloud.begin_fill()

    for i in range(5):
        cloud.circle(20)
        cloud.forward(20)

    cloud.end_fill()

draw_cloud(-430,220)
draw_cloud(-120,250)
draw_cloud(150,180)
grass.penup()
grass.goto(-550,-250)
grass.color("#3CB043")
grass.begin_fill()

grass.goto(550,-250)
grass.goto(550,-350)
grass.goto(-550,-350)
grass.goto(-550,-250)

grass.end_fill()

pole.pensize(8)
pole.color("#444")

pole.penup()
pole.goto(-330,220)
pole.pendown()
pole.goto(-330,-200)

pole.penup()
pole.goto(-355,-200)
pole.pendown()
pole.pensize(6)
pole.forward(50)

pole.penup()
pole.goto(-330,230)
pole.dot(18,"gold")

FLAG_WIDTH=420
FLAG_HEIGHT=210

START_X=-330
START_Y=180

ROWS=60

wave=0
angle=0

running=True


def draw_chakra(cx,cy,radius,rot):

    chakra.clear()

    chakra.penup()
    chakra.goto(cx,cy-radius)
    chakra.setheading(0)

    chakra.pendown()
    chakra.color("#054187")
    chakra.pensize(2)
    chakra.circle(radius)

    spokes=24

    for i in range(spokes):

        chakra.penup()
        chakra.goto(cx,cy)
        chakra.setheading(rot+i*(360/spokes))
        chakra.forward(radius*0.15)

        chakra.pendown()
        chakra.forward(radius-radius*0.15)


def draw_flag(offset):

    flag.clear()

    stripe=FLAG_HEIGHT/3

    for row in range(ROWS):

        y=START_Y-row*(FLAG_HEIGHT/ROWS)

        shift=math.sin((row/6)+offset)*14

        # SAFFRON
        flag.penup()
        flag.goto(START_X+shift,y)
        flag.pendown()

        if row<ROWS/3:
            flag.color("#FF9933")

        elif row<2*ROWS/3:
            flag.color("white")

        else:
            flag.color("#138808")

        flag.begin_fill()

        flag.goto(START_X+FLAG_WIDTH+shift,y)
        flag.goto(START_X+FLAG_WIDTH+shift,y-FLAG_HEIGHT/ROWS)
        flag.goto(START_X+shift,y-FLAG_HEIGHT/ROWS)
        flag.goto(START_X+shift,y)

        flag.end_fill()

    flag.color("black")
    flag.pensize(2)

    points=[]

    for row in range(ROWS+1):

        y=START_Y-row*(FLAG_HEIGHT/ROWS)

        shift=math.sin((row/6)+offset)*14

        points.append((START_X+shift,y))

    flag.penup()
    flag.goto(points[0])

    flag.pendown()
    for p in points:
        flag.goto(p)
    for p in reversed(points):
        flag.goto(p[0]+FLAG_WIDTH,p[1])

    flag.goto(points[0])

def toggle(x,y):

    global running

    running=not running

screen.onclick(toggle)


def animate():

    global wave
    global angle

    if running:

        wave+=0.20
        angle=(angle+6)%360

        draw_flag(wave)
        center_shift = math.sin((ROWS/2)/6 + wave) * 14
        cx = START_X + FLAG_WIDTH * (2/5) + center_shift
        cy = START_Y - FLAG_HEIGHT / 2
        r = int(FLAG_HEIGHT * 0.133)

        draw_chakra(cx, cy, r, angle)

        screen.update()

    screen.ontimer(animate,30)

animate()

screen.mainloop()

