def validate_integer(message):
  try:
    return int(input(message))
    
  except:
    print("Parameter must be integer.")
