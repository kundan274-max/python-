"""
==============================
         SNAKE CLASS
==============================
"""
from settings import *

class Snake:

    def __init__(self, canvas):
        self.canvas = canvas

        # Initial direction
        self.direction = "Right"

        # Initial body
        self.body = [
            [100, 100],
            [80, 100],
            [60, 100]
        ]

        # Canvas objects
        self.parts = []
        self.grow_pending = 0
        self.draw()

    # ---------------- Draw Snake ---------------- #

    def draw(self):

        # Old snake delete
        for part in self.parts:
            self.canvas.delete(part)

        self.parts.clear()

        # Draw new snake
        for index, (x, y) in enumerate(self.body):

            if index == 0:
                color = "#00FF00"      # Head
            else:
                color = "#00CC00"      # Body

            square = self.canvas.create_rectangle(
                x,
                y,
                x + SPACE_SIZE,
                y + SPACE_SIZE,
                fill=color,
                outline="#006600"
            )

            self.parts.append(square)

    # ---------------- Move ---------------- #

    def move(self):

        head_x, head_y = self.body[0]

        if self.direction == "Up":
            head_y -= SPACE_SIZE

        elif self.direction == "Down":
            head_y += SPACE_SIZE

        elif self.direction == "Left":
            head_x -= SPACE_SIZE

        elif self.direction == "Right":
            head_x += SPACE_SIZE

        self.body.insert(0, [head_x, head_y])

        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.body.pop()

        self.draw()

    # ---------------- Grow ---------------- #

    def grow(self):
        self.grow_pending += 1

    # ---------------- Direction ---------------- #

    def change_direction(self, direction):

        if direction == "Up" and self.direction != "Down":
            self.direction = direction

        elif direction == "Down" and self.direction != "Up":
            self.direction = direction

        elif direction == "Left" and self.direction != "Right":
            self.direction = direction

        elif direction == "Right" and self.direction != "Left":
            self.direction = direction

    # ---------------- Head Position ---------------- #

    def get_head(self):
        return self.body[0]

    # ---------------- Collision ---------------- #

    def hit_wall(self):

        x, y = self.get_head()

        if x < 0:
            return True

        if x >= GAME_WIDTH:
            return True

        if y < 0:
            return True

        if y >= GAME_HEIGHT:
            return True

        return False

    def hit_self(self):
        return self.get_head() in self.body[1:]

    # ---------------- Reset ---------------- #

    def reset(self):  
        self.grow_pending = 0
        self.direction = "Right"
        self.body = [
            [100, 100],
            [80, 100],
            [60, 100]
        ]
        self.draw()