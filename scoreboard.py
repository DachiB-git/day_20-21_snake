from turtle import Turtle


class Scoreboard:
    def __init__(self, screen):
        self.score = 0
        self.board = None
        self.screen = screen
        self.display_score(self.screen)

    def update_score(self):
        self.score += 1
        self.board.clear()
        self.board.write(f"Score: {self.score}", align="center", font=('Arial', 15, 'normal'))

    def display_score(self, screen):
        board = Turtle()
        board.goto(0, screen.window_height() / 2 - 40)
        board.color("white")
        board.write(f"Score: {self.score}", align="center", font=('Arial', 15, 'normal'))
        board.hideturtle()
        self.board = board

    def display_end_screen(self):
        # self.screen.reset()
        end_screen_text = Turtle()
        end_screen_text.goto(0, self.screen.window_height()/2 - 100)
        end_screen_text.color("white")
        end_screen_text.write("GAME OVER", align="center", font=('Arial', 20, 'normal'))
        end_screen_text.hideturtle()
        self.screen.update()