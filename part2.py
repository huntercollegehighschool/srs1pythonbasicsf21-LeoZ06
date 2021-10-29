"""
Define a function twodigitodd that take a single integer argument (number). The function should return True if the number is a two digit odd number, and False if it is not.
"""

def twodigitodd(number):
  if number < 10 or number > 99:
    return False
  elif number % 10 % 2 == 1:
    return True
  else:
    return False