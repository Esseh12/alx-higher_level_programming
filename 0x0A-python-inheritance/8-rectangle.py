#!/usr/bin/python3
"""
This module contains a class rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """
    This class inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        This is a costructor method
        """
        self.__width = width
        self.__height = height

        
