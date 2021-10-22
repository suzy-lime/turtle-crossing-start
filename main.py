import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen set up
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Objects
car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

# Listen
screen.listen()
screen.onkeypress(fun=player.move, key="w")

# Game time
game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()

    # Starting cars
    car_manager.create_car()
    car_manager.move_cars()

    # Level up
    if player.ycor() > 290:
        player.new_level()
        scoreboard.level_up()
        car_manager.increase_speed()

    # Detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
