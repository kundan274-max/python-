from tkinter import *
import random

# ---------------- SETTINGS ---------------- #

GAME_WIDTH = 600
GAME_HEIGHT = 600
SPACE_SIZE = 20
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"
SPEED = 120

direction = "down"
score = 0
paused = False

# ---------------- WINDOW ---------------- #

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

label = Label(
    window,
    text="Score : 0",
    font=("Arial", 20)
)

label.pack()

canvas = Canvas(
    window,
    bg=BACKGROUND_COLOR,
    height=GAME_HEIGHT,
    width=GAME_WIDTH
)

canvas.pack()


# ---------------- CLASSES ---------------- #

class Snake:

    def __init__(self):

        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:

            square = canvas.create_rectangle(
                x,
                y,
                x + SPACE_SIZE,
                y + SPACE_SIZE,
                fill=SNAKE_COLOR,
                tag="snake"
            )

            self.squares.append(square)


class Food:

    def __init__(self):

        while True:

            x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE

            # Food snake ke body ke andar na aaye
            if [x, y] not in snake.coordinates:
                break

        self.coordinates = [x, y]

        canvas.create_oval(
            x,
            y,
            x + SPACE_SIZE,
            y + SPACE_SIZE,
            fill=FOOD_COLOR,
            outline="white",
            width=2,
            tag="food"
        )

    

def check_collisions(snake):

    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True

    if y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


def game_over():

    canvas.delete(ALL)

    canvas.create_text(
        GAME_WIDTH/2,
        GAME_HEIGHT/2-40,
        text="GAME OVER",
        fill="red",
        font=("Consolas",40,"bold")
    )

    canvas.create_text(
        GAME_WIDTH/2,
        GAME_HEIGHT/2+10,
        text=f"Score : {score}",
        fill="white",
        font=("Arial",20)
    )

    canvas.create_text(
        GAME_WIDTH/2,
        GAME_HEIGHT/2+60,
        text="Press R to Restart",
        fill="yellow",
        font=("Arial",18)
    )


def restart(event=None):

    global snake
    global food
    global score
    global direction

    score = 0
    direction = "down"

    label.config(text="Score : 0")

    canvas.delete(ALL)

    snake = Snake()
    food = Food()

    next_turn(snake, food)


def next_turn(snake, food):

    global score
    global paused 
    if paused:
        return

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE

    elif direction == "down":
        y += SPACE_SIZE

    elif direction == "left":
        x -= SPACE_SIZE

    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, [x, y])

    if check_collisions(snake):
        game_over()
        return

    square = canvas.create_rectangle(
        x,
        y,
        x + SPACE_SIZE,
        y + SPACE_SIZE,
        fill=SNAKE_COLOR
    )

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        score += 1

        label.config(text="Score : {}".format(score))

        canvas.delete("food")

        food = Food()

    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if not paused:
        window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):

    global direction

    if new_direction == "left" and direction != "right":
        direction = new_direction

    elif new_direction == "right" and direction != "left":
        direction = new_direction

    elif new_direction == "up" and direction != "down":
        direction = new_direction

    elif new_direction == "down" and direction != "up":
        direction = new_direction


def pause_game(event=None):

    global paused

    paused = not paused

    if paused:

        canvas.create_text(
            GAME_WIDTH//2,
            GAME_HEIGHT//2,
            text="PAUSED",
            fill="yellow",
            font=("Arial",35,"bold"),
            tag="pause"
        )

    else:

        canvas.delete("pause")

        # Resume Game
        next_turn(snake, food)


snake = Snake()
food = Food()
window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))
window.bind("r", restart)
window.bind("R", restart)
window.bind("p", pause_game)
window.bind("P", pause_game)

next_turn(snake, food)

window.bind("R", restart)
window.bind("p", pause_game)
window.bind("P", pause_game)
window.mainloop()
