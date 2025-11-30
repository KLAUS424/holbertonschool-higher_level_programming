#!/usr/bin/python3
"""
Module 6-load_from_json_file
Contains a function that creates an Object from a “JSON file”.
"""
import json


def load_from_json_file(filename):
    """
    Creates a Python object from the contents of a JSON file.

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        The Python object (dict, list, string, int, etc.) derived from
        the JSON data in the file.
    """

    with open(filename, mode='r', encoding='utf-8') as f:

        return json.load(f)
