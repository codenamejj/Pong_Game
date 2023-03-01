from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("yellow")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.shape("square")
        self.goto(position)

    def move_up(self):
        y_position = self.ycor() + 20
        self.goto(self.xcor(), y_position)

    def move_down(self):
        y_position = self.ycor() - 20
        self.goto(self.xcor(), y_position)







