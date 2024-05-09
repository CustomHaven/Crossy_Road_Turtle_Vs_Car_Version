from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
  """ScoreBoard blueprint"""
  def __init__(self) -> None:
    super().__init__()
    self.level = 1
    self.hideturtle()
    self.penup()
    self.goto(-260, 260)
    self.update_text()
  
  def update_text(self):
    """Writes on to the screen."""
    self.write(arg=f"Level: {self.level}", align="left", font=FONT)
  
  def increase_level(self):
    """Increases the level."""
    self.level += 1
    self.clear()
    self.update_text()
  
  def game_over(self):
    """Writes game over to the screen."""
    self.goto(0,0)
    self.write(f"GAME OVER", align="center", font=FONT)