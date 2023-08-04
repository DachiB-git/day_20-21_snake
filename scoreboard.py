from turtle import Turtle


class Scoreboard(Turtle):

    FONT = ('Arial', 15, 'normal')

    def __init__(self, screen):
        super().__init__()
        self.score = 0
        with open("high_score.txt", "r") as fh:
            self.high_score = int(fh.read())
        self.screen = screen
        self.goto(0, self.screen.window_height() / 2 - 40)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.high_score}", align="center", font=self.FONT)

    def reset(self):
        if self.score > self.high_score:
            with open('high_score.txt', 'w') as fh:
                self.high_score = self.score
                fh.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increment_score(self):
        self.score += 1
        self.update_scoreboard()
