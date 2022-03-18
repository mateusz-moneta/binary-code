import random

class BinaryGrid:
  def __init__(self, a, b, c, d, l):
    self.a = a
    self.b = b
    self.c = c
    self.d = d
    self.l = l
    self.length = pow(2, l) - 1

  def create(self):
    self.ab_interval = (self.b - self.a) / self.length
    self.cd_interval = (self.d - self.c) / self.length
    self.grid_ab = {}
    self.grid_cd = {}

    for i in range(0, self.length + 1):
      self.grid_ab[self.a + i * self.ab_interval] = bin(i)[2:].zfill(self.l)
      self.grid_cd[self.c + i * self.cd_interval] = bin(i)[2:].zfill(self.l)

  def decode(self):
    # Generating a random binary string
    binary = ''

    for i in range(2 * self.l):
      binary += str(random.randint(0, 1))

    print("\nBinary string: " + binary)

    x_dec = int(binary[:self.l], 2)
    y_dec = int(binary[self.l:], 2)
    max = pow(2, self.l) - 1

    return "x = " + str(self.a + x_dec * (self.b - self.a) / max) + ", y = " + str(self.c + y_dec * (self.d - self.c) / max)

  def encode(self):
    # Generating random points on a given interval
    x = random.uniform(self.a, self.b)
    y = random.uniform(self.c, self.d)
    print("\nRandomly point: (" + str(x) + ", " + str(y) + ")")

    x_binary = self.grid_ab[self.find_closest_key(x, self.grid_ab)]
    y_binary = self.grid_cd[self.find_closest_key(y, self.grid_cd)]

    return str(x_binary) + str(y_binary)  

  def find_closest_key(self, coordinate, grid):
    self.grid_keys = list(grid.keys())

    for key_index in range(len(self.grid_keys)):
      if coordinate == self.grid_keys[key_index]:
        return self.grid_keys[key_index]

      if coordinate < self.grid_keys[key_index]:
          if coordinate - self.grid_keys[key_index - 1] < self.grid_keys[key_index] - coordinate:
            return self.grid_keys[key_index - 1]
          else:
            return self.grid_keys[key_index]
