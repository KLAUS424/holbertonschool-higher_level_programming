#!/usr/bin/env python3
"""
Module task_02_csv
Contains a function to convert data from a CSV file into a JSON file.
"""
import csv
import json
import os


def convert_csv_to_json(csv_filename):
    """
    Reads data from a CSV file and serializes it to a JSON file named 'data.json'.

    Args:
        csv_filename (str): The path to the input CSV file.

    Returns:
        bool: True if conversion is successful, False otherwise (e.g., file not found).
    """
    data = []


    try:

        with open(csv_filename, mode='r', encoding='utf-8') as csvfile:

            reader = csv.DictReader(csvfile)

            for row in reader:
                data.append(row)

    except FileNotFoundError:
        print(f"Error: The file '{csv_filename}' was not found.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred during CSV reading: {e}")
        return False


    json_filename = "data.json"
    try:

        with open(json_filename, mode='w', encoding='utf-8') as jsonfile:

            json.dump(data, jsonfile, indent=4)
        return True
    except IOError as e:
        print(f"Error: Failed to write JSON data to '{json_filename}'. Error: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred during JSON writing: {e}")
        return False


if __name__ == '__main__':

    sample_csv_data = """name,age,city
John,28,New York
Alice,24,Los Angeles
Bob,22,Chicago
Eve,30,San Francisco
"""
    csv_file = "data.csv"
    with open(csv_file, 'w', encoding='utf-8') as f:
        f.write(sample_csv_data)

    print(f"Attempting to convert data from {csv_file}...")

    if convert_csv_to_json(csv_file):
        print("Conversion successful.")

        try:
            with open("data.json", 'r', encoding='utf-8') as f:
                json_content = f.read()
                print("\nContent of data.json:")
                print(json_content)
        except Exception as e:
            print(f"Could not read data.json for verification: {e}")
    else:
        print("Conversion failed.")

    print("\nTesting conversion with non-existent file...")
    if not convert_csv_to_json("non_existent_file.csv"):
        print("Conversion correctly failed for non_existent_file.csv.")


    try:
        os.remove(csv_file)
        if os.path.exists("data.json"):
            os.remove("data.json")
    except OSError:
        pass
