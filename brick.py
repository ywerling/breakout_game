from turtle import Turtle

START_X = 140
START_Y = 180

class Brick(Turtle):
    """ Brick """
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(START_X, START_Y)
        self.shape("square")
        self.color("red")
        self.setheading(0)
        self.shapesize(1, 3)
