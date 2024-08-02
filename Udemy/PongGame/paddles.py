from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.width(20)
        self.height(100)
        self.settiltangle(90)
        self.setposition(-400,0)
        



    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    
    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)