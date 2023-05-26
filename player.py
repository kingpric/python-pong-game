from turtle import Turtle
from constants import *


class Player(Turtle):

    def __init__(self, side):
        super().__init__("square")
        self.__side = side
        self.__initialize()
        self.__listen_up()
        self.__listen_down()

    def __initialize(self):
        self.speed("fastest")
        self.penup()
        self.color(COLOR)
        self.shapesize(stretch_wid=PLAYER_SIZE_SCALE[0], stretch_len=PLAYER_SIZE_SCALE[1])
        screen_size = (self.getscreen().window_width(), self.getscreen().window_width())
        x_pos = -screen_size[0] / 2 + 12
        if self.__side == RIGHT:
            x_pos = screen_size[0] / 2 - 20
        self.setpos(x_pos, 0)

        self.x_delta = (PLAYER_SIZE_SCALE[1] / 2) * PLAYER_SIZE
        self.y_delta = (PLAYER_SIZE_SCALE[0] / 2) * PLAYER_SIZE
        print(self.x_delta)
        print(self.y_delta)

    def __up(self):
        if self.ycor() < TOP:
            self.setpos(self.xcor(), self.ycor() + MOVE_STEP)

    def __down(self):
        if self.ycor() > BOTTOM:
            self.setpos(self.xcor(), self.ycor() - MOVE_STEP)

    def __listen_up(self):
        key = PLAYER_LEFT_UP if self.__side == LEFT else PLAYER_RIGHT_UP
        self.getscreen().onkeypress(fun=self.__up, key=key)

    def __listen_down(self):
        key = PLAYER_LEFT_DOWN if self.__side == LEFT else PLAYER_RIGHT_DOWN
        self.getscreen().onkeypress(fun=self.__down, key=key)
