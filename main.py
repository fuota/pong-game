from turtle import Turtle, Screen
from line import Line
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

game_is_on = False
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

# Draw middle line
line = Line()
line.middle()

# Create ball
ball = Ball()

# Score:
score_left = ScoreBoard((-100, 200))
score_right = ScoreBoard((100, 200))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 300 or ball.distance(l_paddle) > 10 and ball.xcor() < -300:
        ball.bounce_x()

    if ball.xcor() > 380:

        time.sleep(0.7)
        ball.reset_position()
        score_left.increase_score()

    if ball.xcor() < -380:
        score_right.increase_score()
        time.sleep(0.7)
        ball.reset_position()
        score_right.increase_score()
        
screen.exitonclick()
