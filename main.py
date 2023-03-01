from turtle import Screen
from ball import Ball
from paddle import Paddle
from scores import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
score = Score()

screen.listen()

screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()

    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < - 320:
        ball.bounce_x()

    if ball.xcor() > 390:
        score.left_score += 1
        ball.ball_reset()

    elif ball.xcor() < - 390:
        score.right_score += 1
        ball.ball_reset()
        
    if ball.speed() < 0:
        ball.ball_speed = 0
        
    score.clear()
    score.show_l_score()
    score.show_r_score()
    ball.speed(ball.ball_speed)


screen.exitonclick()
