from turtle import Turtle

START_X = 0
START_Y = -180

class Bat(Turtle):
    """ Bat that will be used to hit the ball """
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(START_X, START_Y)
        self.shape("square")
        self.color("white")
        self.setheading(0)
        self.shapesize(1, 3)

    def move_right(self):
        """ Moves the bat one step to the right """
        self.forward(10)
        print("left")

    def move_left(self):
        """ Moves the bat one step to the left """
        self.backward(10)
        print("right")