from turtle import Turtle, Screen
from paddles import Paddle

screen = Screen()
line = Turtle()
right_paddle = Paddle()
left_paddle = Paddle()


right_paddle.setup(350)
left_paddle.setup(-350) 

screen.screensize(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")

def create_dotted_line():
    line = Turtle()
    line.color("white")
    line.width(2)
    line.hideturtle()
    line.speed("fastest")
    line.penup()
    line.goto(0, -300)
    line.setheading(90)
    
    for _ in range(31):
        line.pendown()
        line.forward(10)
        line.penup()
        line.forward(10)
    
    

create_dotted_line()



screen.onkeypress(left_paddle.move_up, "Up")
screen.onkeypress(left_paddle.move_down, "Down")

screen.listen()




screen.exitonclick()
