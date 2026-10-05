# Create a screen
from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
r_paddle.listen_to_keys("Up", "Down")
l_paddle.listen_to_keys("w", "s")
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    ball.check_collision_with_walls()
    ball.check_collision_with_paddle(r_paddle)
    ball.check_collision_with_paddle(l_paddle)
    missed = ball.paddle_miss()
    if missed == "right":
        scoreboard.l_increase_score()
        ball.reset_position()
    elif missed == "left":
        scoreboard.r_increase_score()
        ball.reset_position()
    scoreboard.update_score()




screen.exitonclick()