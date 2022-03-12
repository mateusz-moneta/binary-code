from utils.random_value import random_value

class BinaryGrid:
  def __init__(self, a, b, c, d, l):
    self.a = a
    self.b = b
    self.c = c
    self.d = d
    self.l = l

  def create(self):
    self.x = random_value(self.a, self.b)
    self.y = random_value(self.c, self.d)
    print(self.x)