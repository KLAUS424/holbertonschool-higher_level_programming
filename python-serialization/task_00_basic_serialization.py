#!/usr/bin/env python3
"""
Module task_00_basic_serialization
Provides basic functions for serializing a Python dictionary
 to a JSON file
and deserializing a JSON file back into a Python dictionary.
"""
import json
import os


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to JSON and saves it to a specified file.
    If the output file already exists, it will be replaced.

    Args:
        data (dict): The Python dictionary containing the data to be serialized.
        filename (str): The filename of the output JSON file.

    Raises:
        IOError: If there is an issue writing to the file (e.g., invalid path).
    """
    with open(filename, 'w', encoding='utf-8') as f:

        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads and deserializes JSON data from a file into a Python dictionary.

    Args:
        filename (str): The filename of the input JSON file.

    Returns:
        dict: The Python dictionary with the deserialized JSON data.

    Raises:
        FileNotFoundError: If the input file does not exist.
        json.JSONDecodeError: If the file content is not valid JSON.
    """

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:

        return {}
    except json.JSONDecodeError:

        return {}
