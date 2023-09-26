import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()
turtle = Player()
manager = CarManager()
screen.onkey(turtle.move, "Up")

game_is_on = True
while game_is_on:
    manager.move()
    time.sleep(0.1)
    screen.update()

    tup = (turtle.xcor(), turtle.ycor())
    for car in manager.cars:
        if car.distance(tup) < 20:
            scoreboard.gameover()
            game_is_on = False

    if turtle.ycor() > 280:
        turtle.go_back()
        scoreboard.update()
        manager.level()

screen.exitonclick()
