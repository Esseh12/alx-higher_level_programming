#!/usr/bin/python3
a = 10
b = 0
try:
    print(a/b)
except ZeroDivisionError:
    print("cannot divide a number by zero")
