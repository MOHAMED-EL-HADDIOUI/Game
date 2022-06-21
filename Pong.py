#                                        Simple Pong in Python 3 for Beginners
#                                              By @EL HADDIOUI MOHAMED
#                                              Part 1 :Getting Started
import turtle
from tkinter import *
import  winsound

window=turtle.Screen()
window.title("Pong Game")

window.bgpic('im.png')
window.setup(width=800,height=600)
window.tracer(0)

# Score
Score_a=0
Score_b=0
# Paddle A

paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("#FFFFFF")
paddle_a.shapesize(stretch_wid=4,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B

paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("#FFFFFF")
paddle_b.shapesize(stretch_wid=4,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball

Ball=turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.color("#FFFFFF")
Ball.penup()
Ball.goto(0,0)
Ball.dx = 0.25
Ball.dy = 0.25

# Pen
Pen = turtle.Turtle()
Pen.speed(0)
Pen.color("#FFFFFF")
Pen.penup()
Pen.hideturtle()
Pen.goto(0,260)
Pen.write("Player A : {}                   Player B : {}".format(Score_a, Score_b), align='center', font=("Courier", 19, "bold"))

# Function
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)
def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)
def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)
def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)
# Keyboard binding
window.listen()
window.onkeypress(paddle_a_up,"Right")
window.onkeypress(paddle_a_down,"Left")
window.onkeypress(paddle_b_up,"Up")
window.onkeypress(paddle_b_down,"Down")


#Main gane loop
while True:
    window.update()
    # Move the ball
    Ball.setx(Ball.xcor()+Ball.dx)
    Ball.sety(Ball.ycor()+Ball.dy)
    # Border Checking
    if Ball.ycor()>290:
        Ball.sety(290)
        Ball.dy*=-1
    if Ball.ycor()<-290:
        Ball.sety(-290)
        Ball.dy*=-1
    if Ball.xcor()>390:
        Ball.goto(0,0)
        Ball.dx*=-1
        Score_a +=1
        Pen.clear()
        Pen.write("Player A : {}          Player B : {}".format(Score_a, Score_b), align='center',font=("Courier", 19, "bold"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if Ball.xcor()<-390:
        Ball.goto(0,0)
        Ball.dx*=-1
        Score_b += 1
        Pen.clear()
        Pen.write("Player A : {}          Player B : {}".format(Score_a, Score_b), align='center',font=("Courier", 19, "bold"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Paddle and Ball collisions
    if (Ball.xcor()>340 and Ball.xcor()<350) and (Ball.ycor()<paddle_b.ycor()+40) and (Ball.ycor()>paddle_b.ycor()-40):
        Ball.setx(340)
        Ball.dx*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if (Ball.xcor()<-340 and Ball.xcor()>-350) and (Ball.ycor()<paddle_a.ycor()+40) and (Ball.ycor()>paddle_a.ycor()-40):
        Ball.setx(-340)
        Ball.dx*=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

