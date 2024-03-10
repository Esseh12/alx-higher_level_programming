#!/usr/bin/python3


"""
This module comtains a class that that returns True 
if the object is exactly an instance of the specified class ; otherwise False.
"""

def is_same_class(obj, a_class):
    """
     a function that returns True if the object is exactly an 
     instance of the specified class ; otherwise False
    """
    my_obj = obj()
    if isinstance(my_obj, obj) == True:
        return True
    else:
        return False

