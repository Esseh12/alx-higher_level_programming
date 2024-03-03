#!/usr/bin/python3


"""
This module contains a function that writes a object to text
"""

import json


def save_to_json_file(my_obj, filename):

    """
    Returns an Object to a text file, using a JSON representation

    Args:
        my_obj: the object to be converted
        filename: the file to be creates

    Return:
        none
    """

    json_file = json.dumps(my_obj)

    with open(filename, 'w') as f:
        f.write(json_file)
