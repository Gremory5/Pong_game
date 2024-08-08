from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time



screen = Screen()
line = Turtle()
right_paddle = Paddle()
left_paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()


right_paddle.setup(350)
left_paddle.setup(-350) 

screen.screensize(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

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
screen.listen()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")


game_is_on = True
while game_is_on:
    
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # Detect collision with wall

    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()
    if ball.xcor() > 400 or ball.xcor() < -400:
        ball.reset_position()
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.left_point()
    if ball.xcor() < -390:     
        ball.reset_position() 
        scoreboard.right_point()
    
        

    




screen.exitonclick()
