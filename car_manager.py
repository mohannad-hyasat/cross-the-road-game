from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        x = 300
        for n in range(30):
            car = Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLORS))
            car.setheading(180)
            x += 40
            car.goto(x=random.randint(x, x+200), y=random.randint(-220, 220))
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.speed)
            if car.xcor() < -320:
                car.goto(x=random.randint(340, 600), y=random.randint(-260, 260))

    def level(self):
        self.speed += MOVE_INCREMENT

    def is_crash(self, tup):
        for car in self.cars:
            if car.distance(tup) < 20:
                return True
            else:
                return False

