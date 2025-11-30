#!/usr/bin/python3
"""
Script that adds all command-line arguments to a Python list,
and then saves them to a file named 'add_item.json'
as a JSON representation.
If the file does not exist, it is created.
"""
import sys
# Import functions using the required __import__ style
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_items_to_json_file():
    """
    Loads list data from add_item.json, appends command-line arguments,
    and saves the updated list back to the file.
    """
    filename = "add_item.json"
    # 1. Load existing data or initialize an empty list
    try:
        # Load the list from the file
        data_list = load_from_json_file(filename)
    except FileNotFoundError:
        # If the file does not exist, start with an empty list
        data_list = []
    # 2. Add command-line arguments (sys.argv[1:] excludes the script name)
    new_items = sys.argv[1:]
    data_list.extend(new_items)
    # 3. Save the updated list back to the file
    save_to_json_file(data_list, filename)


if __name__ == "__main__":
    add_items_to_json_file()
