#!/usr/bin/python3
"""
0-lookup: Module that provides a function to list attributes of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Uses the built-in dir() function to retrieve the list of valid attributes
    for the given object.

    Args:
        obj (object): The object whose attributes are to be looked up.

    Returns:
        list: A list of strings representing the object's attributes and methods.
    """
    return dir(obj)
