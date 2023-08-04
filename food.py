from turtle import Turtle
from random import randint


class Food:
    def __init__(self):
        self.food = Turtle("circle")
        self.food.penup()
        self.food.color("green")
        self.food.shapesize(0.5, 0.5)
        self.food.goto(randint(-280, 280), randint(-280, 280))

    def spawn_food(self):
        self.food.goto(randint(-280, 280), randint(-280, 280))

    def get_x(self):
        return self.food.xcor()

    def get_y(self):
        return self.food.ycor()
