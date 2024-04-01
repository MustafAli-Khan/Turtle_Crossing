from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(random.choice(COLORS))
        new_y = random.randint(-250, 250)
        self.goto(x=250, y=new_y)
        self.setheading(180)



    def move_forward(self):
        self.forward(MOVE_INCREMENT)

