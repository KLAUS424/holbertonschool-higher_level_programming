#!/usr/bin/python3
"""
Module 0-read_file
Contains a function to read the contents of a text file
 and print them to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to standard output.

    Args:
        filename (str): The name of the file to read.
          Defaults to an empty string.

    Raises:
     (Does not manage exceptions for file permissions or non-existence,
     as per requirements. FileNotFoundError, for example, will propagate.)
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
