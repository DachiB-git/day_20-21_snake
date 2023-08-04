from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.shapesize(0.5, 0.5)
        self.goto(randint(-280, 280), randint(-280, 280))

    def spawn_food(self):
        self.goto(randint(-280, 280), randint(-280, 280))

    def get_x(self):
        return self.xcor()

    def get_y(self):
        return self.ycor()
