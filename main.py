import time
from turtle import Screen
from scoreboard import Scoreboard

from player import Player
from car_manager import CarManager


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.go_to,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carmanager.create_car()
    carmanager.move_cars()
    for car in carmanager.all_cars:
        if car.distance(player)<20:
            game_is_on = False
            scoreboard.gameover()

    if player.is_at_finish():
        player.goto_start()
        carmanager.increase_speed()

        scoreboard.updatescore()







screen.exitonclick()