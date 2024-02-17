#!/usr/bin/python3


"""
This module contains a function that creates an object rom a JSON file
"""


import json


def load_from_json_file(filename):

    """
    This function  creates an Object from a “JSON file”

    Args:
        filename(str): the name of the file

    Return:
    """

    with open(filename, 'r') as json_file:
        my_obj = json.load(json_file)

    return my_obj
