from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.width(20)
        self.shapesize(stretch_wid=None, stretch_len=5)
        self.settiltangle(90)
        self.setposition(-350,0)

    
    def setup(self, x_position):
        self.penup()
        self.goto(x_position, 0)
        self.setheading(90)
        



    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    
    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)