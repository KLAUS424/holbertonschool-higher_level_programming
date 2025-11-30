#!/usr/bin/python3
"""
Module 2-append_write
Contains a function that appends a string at the end of a text file (UTF8)
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF-8 encoded) and returns
    the number of characters added.

    If the file does not exist, it will be created.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string content to be appended to the file.

    Returns:
        int: The number of characters successfully appended.
    """

    with open(filename, mode='a', encoding='utf-8') as f:

        return f.write(text)
