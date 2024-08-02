from turtle import Turtle, Screen
from paddles import Paddle

screen = Screen()
middle_line = Turtle()

paddle_one = Paddle()

screen.screensize(800, 600)
screen.bgcolor("black")
middle_line.goto(0, 350)
middle_line.color("white")
middle_line.speed("fastest")
middle_line.right(90)
middle_line.width(5)
middle_line.forward(700)




screen.exitonclick()
