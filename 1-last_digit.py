#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    lastDigit = number % 10
else:
    lastDigit = number % -10
    
print("Last digit of",number,"is",lastDigit,end=" ")
if lastDigit == 0:
    print("and is 0")
elif lastDigit < 6:
    print("and is less than 6 and not 0")
else:
    print("and is greater than 5")