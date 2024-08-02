from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=0.5,stretch_len=2)
        self.settiltangle(90)
        self.xcor()


    def f(self):
        self.left(10)