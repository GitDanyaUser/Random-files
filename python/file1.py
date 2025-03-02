def chechifeven(number):
  """ Function for check if even
  Im just testing """
  if not isinstance(number, int):
    print("Number must be integer!")
  if number % 2 == 0:
    print(f"{number} is even")
    return True
  else:
    print(f"{number} is odd")
    return False

x = 11
print(checkifeven(x))
