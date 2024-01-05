#!/usr/bin/python3
# ask user to input two numbers and an operator, store the input in the variable named num1, num2 and operator
num1, operator, num2  = input("Enter calculation: ").split()
# change the trings into integers
num1 = int(num1)
num2 = int(num2)
# use a condition to complete task
if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == "/":
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
elif operator == "%":
    result = num1 % num2
    print(f"{num1} % {num2} = {result}")
else:
    print('error!!')


