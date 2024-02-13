#!/usr/bin/python3


def read_file(filename=""):
    """Reads the contents of a text file and prints them to the standard output.

    Args:
        filename (str): The name of the file to read. If not provided, it reads "my_file_0.txt".

    Returns:
        None
    """

    with open("my_file_0.txt", encoding="UTF8") as f:
        for line in f:
            print(line, end="")
