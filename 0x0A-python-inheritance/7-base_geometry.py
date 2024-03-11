#!/usr/bin/python3

"""
This module contains a class BaseGeometry
"""


class BaseGeometry:
    """
    a class BaseGeometry
    """

    def area(self):
        """
        a public instance method that raises an Exception with
        the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        A method that validates value

        args:
        name: a string
        value: an integer
        """

        if isinstance(value, int) == False:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
