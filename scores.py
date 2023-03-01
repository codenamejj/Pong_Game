from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()

    def show_l_score(self):
        self.goto(x=-100, y=200)
        self.write(f"{self.left_score}", False, align=ALIGNMENT, font=FONT)

    def show_r_score(self):
        self.goto(x=100, y=200)
        self.write(f"{self.right_score}", False, align=ALIGNMENT, font=FONT)





