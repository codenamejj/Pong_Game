from turtle import Turtle

POSITION = (0, 0)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(POSITION)
        self.add_num_y = 10
        self.add_num_x = 10
        self.ball_speed = 0.1

    def move(self):
        x_position = self.xcor() + self.add_num_x
        y_position = self.ycor() + self.add_num_y
        self.goto(x_position, y_position)

    def bounce_y(self):
        self.add_num_y *= -1

    def bounce_x(self):
        self.add_num_x *= -1
        self.ball_speed *= 0.7

    def ball_reset(self):
        self.goto(POSITION)
        self.bounce_x()
        self.ball_speed = 0.1






