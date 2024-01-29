from turtle import Screen
from bat import Bat
from ball import Ball
from brick import Brick, BrickWall
from scoreboard import Scoreboard
import time

X_MAX = 300
Y_MAX = 200
BALL_MOVE_RATE = 0.1
COLLISION_INTERVAL = 15

# initialize the screen
screen = Screen()
screen.setup(width=2*X_MAX, height=2*Y_MAX)
screen.bgcolor("black")
screen.title("Breakout game")
screen.tracer(0)

bat = Bat()
ball = Ball()
# brick = Brick()
scoreboard = Scoreboard()
wall = BrickWall()

screen.listen()
screen.onkey(bat.move_left, "Left")
screen.onkey(bat.move_right, "Right")

game_is_on = True
game_is_won = False
while game_is_on:
    screen.update()
    time.sleep(BALL_MOVE_RATE)
    ball.move()

    # Detect collision of the ball with the wall.
    if ball.xcor() > (X_MAX-COLLISION_INTERVAL) or ball.xcor() < -(X_MAX-COLLISION_INTERVAL):
        ball.bounce_x()
    if ball.ycor() > (Y_MAX-COLLISION_INTERVAL):
        ball.bounce_y()
    if ball.ycor() < -(Y_MAX-COLLISION_INTERVAL):
        game_is_on = False

    # Detect collision of the ball with the bat
    if ball.distance(bat) < (2*COLLISION_INTERVAL):
        print("collision with bat")
        ball.bounce_y()

    # Detect collision of the ball with the brick
    # if ball.distance(brick) < (2*COLLISION_INTERVAL):
    #     print("collision with brick")
    #     scoreboard.increase_score(ball.value)
    #     ball.bounce_y()

    # Detect collision of the ball with the wall
    for brick in wall.bricks:
        if (ball.distance(brick) < (2 * COLLISION_INTERVAL)) and brick.isvisible():
            scoreboard.increase_score(brick.value)
            brick.hideturtle()
            # wall.brick_count-=1
            ball.bounce_y()

    if wall.wall_is_empty():
        game_is_won = True
        game_is_on = False

    # if wall.brick_count < 1:
    #     game_is_won = True
    #     game_is_on = False

if game_is_won:
    scoreboard.game_won()
else:
    scoreboard.game_over()

screen.exitonclick()
