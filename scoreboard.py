from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
  """ScoreBoard blueprint"""
  def __init__(self, position, text=None) -> None:
    super().__init__()
    self.score = 0
    self.hideturtle()
    self.penup()
    self.goto(position)
    text_arg = f"Level: {self.score}" if text == None else text
    self.write_text(text_arg, t_align="center" if text == "GAME OVER" else "left")
  
  def write_text(self, text, t_align):
    """Writes on to the screen."""
    self.write(arg=text, align=t_align, font=FONT)
  
  def increase_score(self):
    """Increases the score."""
    self.score += 1
    self.clear()
    self.write_text(f"Level: {self.score}", "left")