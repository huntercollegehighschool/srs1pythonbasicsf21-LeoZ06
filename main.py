from part1 import trianglearea
from part2 import twodigitodd
from part3 import isprime
from part4 import possibletriangle
from part5 import isotriangle

program = int(input("Which program (1, 2, 3, 4, or 5)?"))

if program == 1:
  base = float(input("Enter a base: "))
  height = float(input("Enter a height: "))
  print(trianglearea(base, height))
  
if program == 2:
  number = int(input("Enter a number: "))
  print(twodigitodd(number))

if program == 3:
   number = int(input("Input number: "))
   print(isprime(number))
  
if program == 4:
  side1 = float(input("Side 1: "))
  side2 = float(input("Side 2: "))
  side3 = float(input("Side 3: "))
  print(possibletriangle(side1, side2, side3))

if program == 5:
  leg = int(input("Leg length: "))
  isotriangle(leg)