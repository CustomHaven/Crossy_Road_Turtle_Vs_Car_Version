import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Put 20 cars on the screen in the beginning, and initilise all the objects
car_positions = [( random.randint(-250, 250), random.randint(-250, 250) ) for _ in range(0, 20)]
cars = [CarManager(position=position) for position in car_positions]
player = Player()
score = Scoreboard((-260, 260))

screen.listen()
screen.onkey(player.move, "Up")

# Game vars
count = 0
game_is_on = True

while game_is_on:
  time.sleep(0.1)
  screen.update()

  # Move the cars.
  for car in cars:
    car.move_car()
    # If car goes off screen, then reuse that same car by sending it back to the other side.
    if car.xcor() < -310:
      car.reuse_car()

  # After long interval we make a new car to increase the difficulty
  if count % 500 == 0:
    cars.append(CarManager(( 310, random.randint(-250, 250) )))
  
  # If player reaches the finish line.
  if player.detect_finish_line():
    score.increase_score()
    for car in cars:
      car.new_level()

  # if car collides with player
  for car in cars:
    if car.distance(player) < 20:
      Scoreboard((0,0), text="GAME OVER")
      game_is_on = False

  count+=1

screen.exitonclick()