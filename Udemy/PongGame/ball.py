from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = 10
        self.dy = 10
        self.x_move = 15
        self.y_move = 15
        self.move_speed = 0.03

    def move(self):
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

    def bounce_x(self):
        self.dx *= -1
        self.move_speed *= 0.9

    def bounce_y(self):
        self.dy *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.dx *= -1
        self.dy = random.choice([self.y_move, -self.y_move])

