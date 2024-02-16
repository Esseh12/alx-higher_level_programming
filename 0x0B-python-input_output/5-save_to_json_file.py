#!/usr/bin/python3

"""
This module writes an Object to a text file, using a JSON representation
"""

import json


def save_to_json_file(my_obj, filename):

    """
    writes an object to a text file, using a JSON rep

    Args:
        filename(str): name of the file
        my_obj: the object

    Returns:
        None
    """

    # changing the data into a string
    json_data = json.dumps(my_obj)

    # open the file in write mode
    with open(filename, "w") as f:
        # Write the JSON string to the file
        f.write(json_data)
