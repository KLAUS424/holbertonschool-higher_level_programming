#!/usr/bin/python3
"""
Module 8-class_to_json
Contains a function that returns the dictionary description
with simple data structure for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization
    of an instance of a Class.

    Args:
        obj: An instance of a Class. Assumes all attributes are serializable.

    Returns:
        dict: A dictionary representation of the object's attributes.
    """

    return obj.__dict__
