#!/usr/bin/python3

"""
This module contains a function that returns  an object (Python data structure)
"""

import json


def from_json_string(my_str):

    """
    Returns an object represented by a JSON string

    Args:
        my_str: the string to be returned

    Returns:
            an object represented by a JSON string
    """

    return (json.loads(my_str))
