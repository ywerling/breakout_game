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
        """
        Displays the current score on the screen
        :return: N/A
        """
        self.write(f"Points: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """
        Handles the end of the game in case of loss
        :return: N/A
        """
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def game_won(self):
        """
        Handles the end of the game in case of victry
        :return: N/A
        """
        self.goto(0, 0)
        self.color("cyan")
        self.write("CONGRATULATIONS YOU WON!", align=ALIGNMENT, font=FONT)

    def increase_score(self,increment):
        """
        Increases the score
        :param increment: amount to increase the score with
        :return: N/A
        """
        self.score += increment
        self.clear()
        self.update_scoreboard()
