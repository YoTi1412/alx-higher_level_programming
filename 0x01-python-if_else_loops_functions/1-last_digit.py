#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = number % 10 if number > 0 else number % -10
m = "greater than 5" if ld > 5 else ld if ld == 0 \
       else "less than 6 and not 0"
print(f"Last digit of {number} is {ld} and is {m}")
