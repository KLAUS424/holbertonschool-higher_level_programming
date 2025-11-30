#!/usr/bin/python3
"""
Module 5-save_to_json_file
Contains a function that writes an Object to a text file,
using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file in JSON format.

    Args:
        my_obj: The Python object to be serialized and saved.
        filename (str): The name of the file to write to.
    """

    with open(filename, mode='w', encoding='utf-8') as f:

        json.dump(my_obj, f)
