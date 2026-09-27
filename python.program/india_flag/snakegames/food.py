"""
==============================
          FOOD CLASS
==============================
"""

import random
from settings import *


class Food:

    def __init__(self, canvas, snake, game=None):
        self.food_type = "normal"
        self.food_count = 0
        self.canvas = canvas
        self.snake = snake
        self.game = game
        self.timer = None
        self.food = None
        self.position = [0, 0]

        self.spawn()

    # ---------------- Spawn Food ---------------- #

    def spawn(self, force_type=None):
        if self.food:
            self.canvas.delete(self.food)

        self.food_count += 1

        if force_type == "normal":
            self.food_type = "normal"
            color = FOOD_COLOR
            outline = "white"
            if self.timer and self.game:
                self.game.window.after_cancel(self.timer)
                self.timer = None
        elif self.food_count % 5 == 0:
            self.food_type = "golden"
            color = "#FFD700"
            outline = "#FFFF00"
            if self.game:
                if self.timer:
                    self.game.window.after_cancel(self.timer)
                self.timer = self.game.window.after(5000, self.remove_golden)
        else:
            self.food_type = "normal"
            color = FOOD_COLOR
            outline = "white"
            if self.timer and self.game:
                self.game.window.after_cancel(self.timer)
                self.timer = None

        while True:
            x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE

            # Food snake ke body ke andar nahi aayega
            if [x, y] not in self.snake.body:
                break

        self.position = [x, y]

        # Food draw karo
        self.food = self.canvas.create_oval(
            x + 2,
            y + 2,
            x + SPACE_SIZE - 2,
            y + SPACE_SIZE - 2,
            fill=color,
            outline=outline,
            width=2
        )

    # ---------------- Position ---------------- #

    def get_position(self):
        return self.position

    # ---------------- Remove Golden ---------------- #

    def remove_golden(self):
        if self.food_type == "golden":
            self.food_type = "normal"
            self.spawn(force_type="normal")