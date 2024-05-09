import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
  """Car blueprint"""
  def __init__(self, position: tuple) -> None:
    super().__init__()
    self.shape("square")
    self.color(COLORS[random.randint(0, 5)])
    self.penup()
    self.shapesize(stretch_wid=1, stretch_len=2)
    self.setheading(180) # WEST
    self.move_x = STARTING_MOVE_DISTANCE
    self.create_car(position)
  
  def create_car(self, position):
    """Creates a new car"""
    self.goto(position)
  
  def move_car(self):
    """Moves the car"""
    self.goto(self.xcor() - self.move_x, self.ycor())

  def new_level(self):
    """Speed up the car"""
    self.move_x += MOVE_INCREMENT
  
  def reuse_car_car(self):
    """If car exits screen reuses the car back into the screen."""
    self.goto(310, random.randint(-250, 250))