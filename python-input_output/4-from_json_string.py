#!/usr/bin/python3
"""
Module 4-from_json_string
Contains a function that returns an object (Python data structure)
represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Returns the Python data structure represented by a JSON string.

    Args:
        my_str (str): The JSON formatted string to be deserialized.

    Returns:
        The Python object (dict, list, string, int, etc.) derived from
        the JSON string.
    """

    return json.loads(my_str)
