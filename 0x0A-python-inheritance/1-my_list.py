#!/usr/bin/python3

"""
This module contains a function that sorts a list
in ascending form
"""


class MyList(list):

    """
    This class is inherted from another class list
    """

    def __init__(self):
        """a subclass of list"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
