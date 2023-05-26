from screen import PongScreen, Screen
from scoreboard import Scoreboard, Turtle
from player import Player
from ball import Ball
from constants import *

import time

screen = PongScreen(SCREEN_SIZE).screen
player_1_scoreboard = Scoreboard(LEFT)
player_2_scoreboard = Scoreboard(RIGHT)
ball = Ball()

player_1 = Player(LEFT)
player_2 = Player(RIGHT)
screen.update()
screen.listen()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(.1)
    ball.check_boundary()
    ball.move()
    screen.update()

    # Check paddle hit the ball by player 1
    if ball.distance(player_1) < 50 and ball.xcor() < player_1.xcor() + 15:
        ball.bounce()
        continue

    # Check paddle hit the ball by player 2
    if ball.distance(player_2) < 50 and ball.xcor() > player_2.xcor() - 15:
        ball.bounce()
        continue

    # check if ball surpass either paddle
    if ball.xcor() > player_2.xcor() + player_2.x_delta:
        player_1_scoreboard.increase_score()
        ball.restart()
    elif ball.xcor() < player_1.xcor() - player_1.x_delta:
        player_2_scoreboard.increase_score()
        ball.restart()

Screen().exitonclick()
