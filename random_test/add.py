#!/usr/bin/python3
# ask a user to input two numbers and store it in a variable
num1, num2 = input('Enter two numbers: ').split()
# make the string inputed into a number integer
num1 = int(num1)
num2 = int(num2)
# add the two digit and save in another variable named add
add = num1 + num2
# print out the information to the user
print(f"{num1} + {num2} = {add}")
