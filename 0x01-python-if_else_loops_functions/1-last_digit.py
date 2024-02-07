#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
elif last_digit > 0 and last_digit <= 5:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
else:
    print(f"THE NUMBER IS {number}")



'''print(last_digit)
print(f"the number is {number} and the last digit is {last_digit}")'''
