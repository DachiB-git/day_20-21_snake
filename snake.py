from turtle import Turtle


class Snake:

    START_POSITION_X = 20
    START_POSITION_Y = 0

    def __init__(self):
        self.body = []
        self.direction = (1, 0)
        self.last_key = None
        self.init_body()

    def init_body(self):
        for i in range(3):
            self.get_new_part()

    def get_new_part(self):
        last_part_x = self.body[-1].xcor() if self.body else Snake.START_POSITION_X
        last_part_y = self.body[-1].ycor() if self.body else Snake.START_POSITION_Y
        dir_x, dir_y = self.direction
        body_part = Turtle("square")
        body_part.penup()
        body_part.color("white")
        body_part.goto(last_part_x + 20 * dir_x, last_part_y + 20 * dir_y)
        self.body.append(body_part)

    def reset(self):
        for part in self.body:
            part.reset()
        self.body = []
        self.direction = (1, 0)
        self.init_body()

    def move(self):
        head = self.body[0]
        dir_x, dir_y = self.direction
        for i in range(len(self.body)-1, 0, -1):
            last_part = self.body[i]
            next_part = self.body[i-1]
            last_part.goto(next_part.pos())
        else:
            head_cords = (head.xcor() + 20 * dir_x, head.ycor() + 20 * dir_y)
            head.goto(head_cords)

    def change_direction(self, key):
        match key:
            case "Up":
                if self.last_key != "Down":
                    self.direction = (0, 1)
                    self.last_key = key
            case "Down":
                if self.last_key != "Up":
                    self.direction = (0, -1)
                    self.last_key = key
            case "Left":
                if self.last_key != "Right":
                    self.direction = (-1, 0)
                    self.last_key = key
            case "Right":
                if self.last_key != "Left":
                    self.direction = (1, 0)
                    self.last_key = key
