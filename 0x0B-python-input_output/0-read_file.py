#!/usr/bin/python3

"""
This module provides a function to read from a file
"""


def read_file(filename=""):

    """
    Read the conetnt of te file and prints them to stdout

    Args:
        filename (str): The name of the file to read. it reads "my_file_0.txt".

    Returns:
        None
    """

    with open("my_file_0.txt", encoding="UTF8") as open_file:
        for line in open_file:
            print(line, end="")
