from turtle import Turtle

START_X = 140
START_Y = 180
BRICK_COLORS = ["red", "orange", "yellow", "green"]

class Brick(Turtle):
    """ Brick """
    def __init__(self, x, y, fill_colour="red", value=3):
        super().__init__()
        self.penup()
        self.goto(x, y)
        self.shape("square")
        self.color("black", fill_colour)
        self.setheading(0)
        self.shapesize(1, 3)
        self.value = value

class BrickWall():
    """ Group of bricks """
    def __init__(self):
        self.bricks = []
        self.create_wall()


    def create_wall(self):
        for row in range(0, 4):
            for col in range (0, 10):
                new_brick = Brick(60*col-280,180-25*row, BRICK_COLORS[row], 10-row)
                self.bricks.append(new_brick)

    def wall_is_empty(self):
        for brick in self.bricks:
            if brick.isvisible():
                return False
        return True




