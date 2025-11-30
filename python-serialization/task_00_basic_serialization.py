#!/usr/bin/env python3
"""
Module task_00_basic_serialization
Provides basic functions for serializing a Python dictionary to a JSON file
and deserializing a JSON file back into a Python dictionary.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to JSON and saves it to a specified file.
    If the output file already exists, it will be replaced.

    Args:
        data (dict): The Python dictionary containing the data to be serialized.
        filename (str): The filename of the output JSON file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:

            json.dump(data, f)
    except IOError as e:
        print(f"Error saving to file {filename}: {e}")
    except TypeError as e:
        print(f"Error serializing data: {e}")


def load_and_deserialize(filename):
    """
    Loads and deserializes JSON data from a file into a Python dictionary.

    Args:
        filename (str): The filename of the input JSON file.

    Returns:
        dict: The Python dictionary with the deserialized JSON data, or an
              empty dictionary if an error occurs.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:

            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found at {filename}")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from file {filename}")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {}
