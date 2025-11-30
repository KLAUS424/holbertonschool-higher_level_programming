#!/usr/bin/python3
"""
Module 1-write_file
Contains a function that writes a string to a text file (UTF8)
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8 encoded) and returns the
    number of characters written.

    The file is created if it does not exist, and its content is
    overwritten if it already exists.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string content to be written to the file.

    Returns:
        int: The number of characters written.
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
