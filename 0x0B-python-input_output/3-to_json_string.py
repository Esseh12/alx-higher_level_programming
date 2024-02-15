#!/usr/bin/python3
import json

"""
This module conatins a function that returns a JSON rep of a string
"""


def to_json_string(my_obj):

    """
    Returns the JSON reprsention of an object(string)

    Args:
        my_obj: the list to be printed

    Return:
        The JSON rep of a string
    """

    return json.dumps(my_obj)
