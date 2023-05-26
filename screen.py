from turtle import Screen, Turtle
from constants import *


class PongScreen:

    def __init__(self, screen_size: tuple[int, int]):
        self.screen = Screen()
        self.screen.tracer(0)
        self.screen.setup(width=screen_size[0], height=screen_size[1])
        self.screen_size = screen_size
        self.screen.bgcolor("black")
        self.__initialize()
        # self.screen.tracer(1)

    def __initialize(self):
        turtle = Turtle()
        turtle.speed(0)
        turtle.pencolor(COLOR)
        turtle.hideturtle()
        turtle.penup()
        y = -self.screen_size[1] / 2
        turtle.setpos(0, y)

        while y < self.screen_size[1] / 2:
            turtle.pendown()
            y += DASH_LENGTH
            turtle.setpos(0, y)
            turtle.penup()
            y += DASH_LENGTH
            turtle.setpos(0, y)


