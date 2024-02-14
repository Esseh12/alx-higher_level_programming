#!/usr/bin/python3

"""
This module appends a string to the end of a txt file
"""


def append_write(filename="", text=""):

    """
    Append a string to the end of a txt file

    Args:
        filename(str): The name of the file to read
        text (str): The string that's appended

    Return:
           The number of characters added
    """

    with open(filename, 'a', encoding="UTF8") as f:
        appended_file = f.write(text)
        return len(text)
