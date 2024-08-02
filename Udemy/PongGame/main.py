from turtle import Turtle, Screen
from paddles import Paddle

screen = Screen()
line = Turtle()
paddle_one = Paddle()

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



screen.onkeypress(paddle_one.move_up, "Up")
screen.onkeypress(paddle_one.move_down, "Down")
screen.listen()




screen.exitonclick()
