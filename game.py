from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


class Game:

    def __init__(self):
        self.screen = self.init_screen()
        self.snake = Snake()
        self.food = Food()
        self.scoreboard = Scoreboard(self.screen)
        self.is_alive = False

    def init_screen(self):
        screen = Screen()
        screen.setup(width=600, height=600)
        screen.bgcolor("black")
        screen.title("Snake")
        screen.tracer(0)
        screen.listen()
        screen.onkey(lambda: self.snake.change_direction("Up"), "Up")
        screen.onkey(lambda: self.snake.change_direction("Down"), "Down")
        screen.onkey(lambda: self.snake.change_direction("Left"), "Left")
        screen.onkey(lambda: self.snake.change_direction("Right"), "Right")
        screen.onkey(lambda: self.snake.change_direction("space"), "space")
        return screen

    def play(self):
        self.is_alive = True
        self.loop()

    def loop(self):
        while self.is_alive:
            self.snake.move()
            self.check_collision()
            self.screen.update()
            time.sleep(0.075)
        self.scoreboard.display_end_screen()
        self.screen.exitonclick()

    def check_collision(self):
        head = self.snake.body[0]
        if head.distance(self.food.food) < 15:
            self.eat_food()
        if any(head.distance(body_part) == 0 for body_part in self.snake.body[1:]) and len(self.snake.body) > 3:
            self.is_alive = False
        if abs(head.xcor()) > self.screen.window_width() / 2 - 20 or \
                abs(head.ycor()) > self.screen.window_height() / 2 - 20:
            self.is_alive = False

    def eat_food(self):
        self.scoreboard.update_score()
        self.food.spawn_food()
        self.snake.get_new_part()

