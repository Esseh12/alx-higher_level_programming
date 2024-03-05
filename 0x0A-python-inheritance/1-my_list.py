#!/usr/bin/python3

"""
This module contains a function that sorts a list
in ascending form
"""


class MyList(list):

    """
    This class is inherted from another class list
    """

    def print_sorted(self):

        """
        A function that prints the list, but sorted (ascending sort)
        """

        sorted_list = sorted(self)
        print(sorted_list)
