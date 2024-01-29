from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")
X_POS = -200
Y_POS = -100


class Scoreboard(Turtle):
    """ Tracking the player's score using Turtle """

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("yellow")
        self.penup()
        self.goto(X_POS, Y_POS)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Points: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def game_won(self):
        self.goto(0, 0)
        self.color("cyan")
        self.write("CONGRATULATIONS YOU WON!", align=ALIGNMENT, font=FONT)

    def increase_score(self,increment):
        self.score += increment
        self.clear()
        self.update_scoreboard()
