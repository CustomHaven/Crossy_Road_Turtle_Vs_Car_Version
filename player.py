from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
  """Player blueprint"""
  def __init__(self) -> None:
    super().__init__()
    self.shape("turtle")
    self.setheading(90)
    self.move_y = STARTING_POSITION[1]
    self.penup()
    self.refresh()
  
  def refresh(self):
    """Restarts the player's position."""
    self.move_y = STARTING_POSITION[1]
    self.goto(STARTING_POSITION)
  
  def move(self):
    """Enable movements."""
    self.move_y += MOVE_DISTANCE
    self.goto(0, self.move_y)
    
  def detect_finish_line(self) -> bool:
    """Finish line reached and returns a True if."""
    if self.ycor() >= FINISH_LINE_Y:
      self.refresh()
      return True
    else:
      return False