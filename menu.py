from binary_grid import BinaryGrid
from utils.validate_integer import validate_integer

class Menu:
  def __init__(self):
    self.init_options()

    while True: 
      options = self.menu.keys()
      
      for entry in options: 
        print(entry, self.menu[entry])

      print("\n")
      selection = input("Please select option: ")

      print("\n")
      print("x | y ([a, b] x [c, d])")
      print("\n")

      l = validate_integer("Enter l: ")
      a = validate_integer("Enter a: ")
      b = validate_integer("Enter b: ")
      c = validate_integer("Enter c: ")
      d = validate_integer("Enter d: ")

      match selection:
        case '1':
          binary_grid = BinaryGrid(a, b, c, d, l)
          binary_grid.create()

          print("\n")
          print("Binary string value: " + binary_grid.encode() + "\n")

          input("Press any key to continue...")
          break

        case '2':
          binary_grid = BinaryGrid(a, b, c, d, l)
          binary_grid.create()

          print("\n")
          print("Decoding result: " + binary_grid.decode())

          input("Press any key to continue...")
          break

        case _:
          print("\n")
          print('Unknown option selected!')
          break   

  def init_options(self):
    self.menu = {}
    self.menu['1'] = "Binary encoding" 
    self.menu['2'] = "Decoding a binary number by the binary grid method"
