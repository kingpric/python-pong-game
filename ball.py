from turtle import Turtle
from constants import *
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.color(COLOR)
        self.shapesize(stretch_wid=BALL_SIZE[0], stretch_len=BALL_SIZE[1])
        self.setheading(random.randint(0, 360))

    def move(self):
        self.fd(BALL_SPEED)

    def bounce(self):
        angle = self.heading()
        new_angle = 540 - angle
        self.setheading(new_angle)

    def bounce_vertical(self):
        angle = self.heading()
        new_angle = 360 - angle
        self.setheading(new_angle)

    def check_boundary(self):
        # if self.xcor() >= self.getscreen().window_width() / 2 \
        #         or self.xcor() <= -self.getscreen().window_width() / 2:
        #     self.bounce()

        if self.ycor() + 10 >= self.getscreen().window_height() / 2 \
                or self.ycor() - 10 <= -self.getscreen().window_height() / 2:
            self.bounce_vertical()

    def restart(self):
        self.setpos(0, 0)
        self.setheading(random.randint(0, 360))
