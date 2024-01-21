#!/usr/bin/python3
# importing sys module
import sys
argument_length = len(sys.argv)
if argument_length <= 2:
    print(f"{argument_length}")
elif argument_length >= 3:
    for i, arg in enumerate(sys.argv[1:], start=1):
        numeric_arguments = [float(arg) for arg in sys.argv[3:]]
        result = sum(numeric_arguments)
        print("Sum of arguments:", result)
