from turtle import Turtle

START_X = 0
START_Y = 0
STEP_SIZE = 3

class Ball(Turtle):
    """ Represent the ball """
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(START_X, START_Y)
        self.shape("circle")
        self.color("cyan")
        self.setheading(45)
        self.shapesize(1, 1)
        self.x_move = STEP_SIZE
        self.y_move = STEP_SIZE

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def getx(self):
        return self.xcor()

    def gety(self):
        return self.ycor()

    def bounce_y(self):
        self.y_move *= -1


    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.bounce_x()
