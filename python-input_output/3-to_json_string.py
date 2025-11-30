#!/usr/bin/python3
"""
Module 3-to_json_string
Contains a function that returns the JSON representation of an object (string).
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation (string) of a Python object.

    Args:
        my_obj: The Python object (list, dictionary, string, int, etc.)
                to be serialized to a JSON string.

    Returns:
        str: The JSON string representation of the object.
    """

    return json.dumps(my_obj)
