from turtle import Turtle, Screen
from constants import *


class Scoreboard(Turtle):

    def __init__(self, side):
        super().__init__()
        self.hideturtle()
        self.color(COLOR)
        self.penup()
        self.score_side = side
        self.screen_size = (Screen().window_width(), Screen().window_height())
        self.score = 0
        self.__set_location()
        self.update_score()

    def __set_location(self):
        y_drift = self.screen_size[1] / 2 - 25
        if self.score_side == LEFT:
            self.setpos(-X_DRIFT, y_drift)
        else:
            self.setpos(X_DRIFT, y_drift)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)
