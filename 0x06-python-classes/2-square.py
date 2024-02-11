#!/usr/bin/python3
"""
A class representing a shape square

This class is currently empty
"""


class Square:
    """
    how to create a class
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
