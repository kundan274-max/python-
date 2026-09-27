"""
==============================
        UTILITY FUNCTIONS
==============================
"""

from tkinter import *
from settings import *


# ---------------- Center Window ---------------- #

def center_window(window):

    window.update_idletasks()

    width = GAME_WIDTH
    height = GAME_HEIGHT + 40 # Score Label ke liye

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    window.geometry(f"{width}x{height}+{x}+{y}")


# ---------------- Draw Grid ---------------- #

def draw_grid(canvas):

    # Vertical Lines
    for x in range(0, GAME_WIDTH, SPACE_SIZE):

        canvas.create_line(
            x,
            0,
            x,
            GAME_HEIGHT,
            fill=GRID_COLOR
        )

    # Horizontal Lines
    for y in range(0, GAME_HEIGHT, SPACE_SIZE):

        canvas.create_line(
            0,
            y,
            GAME_WIDTH,
            y,
            fill=GRID_COLOR
        )


# ---------------- Show Message ---------------- #

def show_message(canvas, text, color="white", size=30):

    canvas.create_text(
        GAME_WIDTH // 2,
        GAME_HEIGHT // 2,
        text=text,
        fill=color,
        font=("Arial", size, "bold")
    )


# ---------------- Clear Canvas ---------------- #

def clear_canvas(canvas):

    canvas.delete("all")