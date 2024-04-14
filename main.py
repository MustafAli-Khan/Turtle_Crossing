import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing - 🐢")
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.onkeypress(player.go_up, "Up")

game_is_on = True
counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect turtle successful crossing
    if player.is_at_finishline():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()







    counter += 1


screen.exitonclick()


# TODO:Create a Turtle that moves upward
# TODO:Create cars of 20px & 40px that randomly generate on y and move to the left
# TODO:No cars to be generated in top 50px and bottom 50px, a safe zone for turtle.
# TODO:Detect collision with the cars and game stops when the player collides with the car.
# TODO:Detect when the player reaches the top_edge, return the turtle to start and increase the speed of car.
# TODO:Create a scoreboard that tracks the level , on every crossing the level increases and on collision GAME OVER.

