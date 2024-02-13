#!/usr/bin/python3


""" 
    This module reads from a file
"""


def read_file(filename=""):


""" 
This funtion reads from a file

Args:
        filename (str): The name of the file to read. If not provided, it reads "my_file_0.txt".


Returns:
None
"""

    with open("my_file_0.txt", encoding="UTF8") as f:
        for line in f:
            print(line, end="")
