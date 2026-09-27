"""
==============================
        SCORE CLASS
==============================
"""

import os
from settings import *


class Score:

    def __init__(self):

        self.score = 0
        self.high_score = self.load_high_score()

    # ---------------- Current Score ---------------- #

    def increase(self):
        self.score += 1

        if self.score > self.high_score:
            self.high_score = self.score

    # ---------------- Reset ---------------- #

    def reset(self):
        self.score = 0

    # ---------------- Get Score ---------------- #

    def get_score(self):
        return self.score

    def get_high_score(self):
        return self.high_score

    # ---------------- Save ---------------- #

    def save_high_score(self):

        with open(HIGH_SCORE_FILE, "w") as file:
            file.write(str(self.high_score))

    # ---------------- Load ---------------- #

    def load_high_score(self):

        if not os.path.exists(HIGH_SCORE_FILE):

            with open(HIGH_SCORE_FILE, "w") as file:
                file.write("0")

            return 0

        try:

            with open(HIGH_SCORE_FILE, "r") as file:
                return int(file.read())

        except:

            return 0