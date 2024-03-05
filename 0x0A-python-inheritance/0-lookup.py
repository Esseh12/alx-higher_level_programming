#!/usr/bin/python3

"""
module contains a function that  returns the list of available
attributes and methods of an object
"""


def lookup(obj):

    """
    function returns the list of available attributes and methods of an object

    args:
        obj(the class name)
    returns:
         returns the list of available attributes and methods of an object
    """

    return dir(obj)
