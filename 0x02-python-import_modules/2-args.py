#!/usr/bin/python3
# importing sys module
import sys
argument_length = len(sys.argv)
if argument_length == 1:
    print(f"{argument_length - 1} arguments.")
elif argument_length == 2:
    print(f"{argument_length - 1} argument.")
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}:", arg)
elif argument_length >= 3:
    print(f"{argument_length - 1} arguments.")
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}:", arg)

