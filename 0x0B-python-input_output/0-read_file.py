#!/usr/bin/python3

""" 
    This module reads from a file
"""

def read_file(filename=""):

""" 
    This funtion reads from a file
"""

    with open("my_file_0.txt", encoding="UTF8") as f:
        for line in f:
            print(line, end="")
