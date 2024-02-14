#!/usr/bin/python3

"""
This modules writes into a file and overwrites the existing file
"""


def write_file(filename="", text=""):

    """Writes into a file (UTF8) and returns the number of characters written

    Args:
        filename (str): the name of the txt file that writes creates
        text (str): the text to be wriiten in the file

    Return:
        The number of character written
    """

    with open(filename, 'w', encoding="UTF8") as f:
        written_characters = f.write(text)
        lenght_of_text = len(text)
        return lenght_of_text
