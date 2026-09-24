"""
==============================
      PROFESSIONAL SNAKE GAME
==============================
"""

from tkinter import *

from settings import *
from snake import Snake
from food import Food
from score import Score
from utils import center_window, draw_grid


class Game:

    def __init__(self):
        # ---------------- Window ---------------- #

        self.window = Tk()
        self.window.title(WINDOW_TITLE)
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.window.destroy)
        self.window.geometry(f"{GAME_WIDTH}x{GAME_HEIGHT+40}")

        # ---------------- Variables ---------------- #

        self.running = True
        self.paused = False
        self.speed = INITIAL_SPEED
        # ---------------- Lives ---------------- #

        self.lives = 3

        # ---------------- Score ---------------- #

        self.score = Score()

        self.score_label = Label(
            self.window,
            text=f"❤️ {self.lives}    Score : {self.score.get_score()}    High Score : {self.score.get_high_score()}",
            font=SCORE_FONT,
            bg=BACKGROUND_COLOR,
            fg="white",
            pady=8
        )

        self.score_label.pack(fill=X)

        # ---------------- Canvas ---------------- #

        self.canvas = Canvas(
            self.window,
            width=GAME_WIDTH,
            height=GAME_HEIGHT,
            bg=BACKGROUND_COLOR,
            highlightthickness=0
        )

        self.canvas.pack()

        draw_grid(self.canvas)

        # ---------------- Game Objects ---------------- #

        self.snake = Snake(self.canvas)
        self.food = Food(self.canvas, self.snake)

        # ---------------- Keyboard ---------------- #

        self.window.bind("<Up>", lambda e: self.snake.change_direction("Up"))
        self.window.bind("<Down>", lambda e: self.snake.change_direction("Down"))
        self.window.bind("<Left>", lambda e: self.snake.change_direction("Left"))
        self.window.bind("<Right>", lambda e: self.snake.change_direction("Right"))

        self.window.bind("p", self.pause_game)
        self.window.bind("P", self.pause_game)

        self.window.bind("r", self.restart_game)
        self.window.bind("R", self.restart_game)

    # ---------------- Update Score ---------------- #

    def update_score(self):
        self.score_label.config(
            text=f"❤️ {self.lives}    Score : {self.score.get_score()}    High Score : {self.score.get_high_score()}"
        )

    # ---------------- Pause ---------------- #

    def pause_game(self, event=None):
        if not self.running:
            return

        self.paused = not self.paused

        if self.paused:
            self.canvas.create_text(
                GAME_WIDTH // 2,
                GAME_HEIGHT // 2,
                text="PAUSED",
                fill="yellow",
                font=("Arial", 40, "bold"),
                tag="pause"
            )
        else:
            self.canvas.delete("pause")

    # ---------------- Restart ---------------- #

    def restart_game(self, event=None):
        self.running = True
        self.paused = False
        self.speed = INITIAL_SPEED
        self.lives = 3
        self.update_score()
        self.canvas.delete("all")
        draw_grid(self.canvas)

        self.snake = Snake(self.canvas)
        self.food = Food(self.canvas, self.snake)
        self.food.game = self
        self.score.reset() 
        self.food = Food(self.canvas, self.snake)
        self.food.game = self
        self.update_score()

        self.update()

    # ---------------- Game Over ---------------- #

    def game_over(self):
        self.running = False
        self.score.save_high_score()

        self.canvas.create_rectangle(
            100,
            200,
            GAME_WIDTH - 100,
            GAME_HEIGHT - 200,
            fill="#111111",
            outline="white",
            width=3
        )

        self.canvas.create_text(
            GAME_WIDTH // 2,
            GAME_HEIGHT // 2 - 70,
            text="GAME OVER",
            fill="red",
            font=GAMEOVER_FONT
        )

        self.canvas.create_text(
            GAME_WIDTH // 2,
            GAME_HEIGHT // 2 - 20,
            text=f"Score : {self.score.get_score()}",
            fill="white",
            font=("Arial", 20, "bold")
        )

        self.canvas.create_text(
            GAME_WIDTH // 2,
            GAME_HEIGHT // 2 + 20,
            text=f"High Score : {self.score.get_high_score()}",
            fill="cyan",
            font=("Arial", 20, "bold")
        )

        self.canvas.create_text(
            GAME_WIDTH // 2,
            GAME_HEIGHT // 2 + 70,
            text="Press R to Restart",
            fill="yellow",
            font=("Arial", 18)
        )

    # ---------------- Main Loop ---------------- #

    def update(self):
        if not self.running:
            return

        if self.paused:
            self.window.after(100, self.update)
            return

        self.snake.move()

        if self.snake.get_head() == self.food.get_position():
            self.snake.grow()

            if self.food.food_type == "golden":
                for _ in range(5):
                    self.score.increase()
            else:
                self.score.increase()

            self.food.spawn()
            self.update_score()

            if self.speed > MIN_SPEED:
                self.speed -= SPEED_INCREASE

        if self.snake.hit_wall() or self.snake.hit_self():
            self.lives -= 1
            self.update_score()

            if self.lives <= 0:
                self.game_over()
                return

            self.snake.reset()
            self.window.after(1000, self.update)
            return

        self.window.after(self.speed, self.update)

    def run(self):
        self.update()
        self.window.mainloop()