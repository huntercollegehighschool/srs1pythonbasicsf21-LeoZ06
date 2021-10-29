"""
The function below is supposed to return True if the integer entered as the argument is prime, and False if it's not. Fix the code so that it runs the way it's supposed to.
"""
import math

def isprime(number):
  if number == 2:
    return True
  for i in range(2, math.floor(math.sqrt(number)) + 1):
    if number % i == 0:
      return False
    else:
      return True