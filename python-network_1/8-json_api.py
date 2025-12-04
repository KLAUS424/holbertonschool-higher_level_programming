#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user with a letter as a parameter
"""

import sys
import requests


def search_user(letter):
    """
    Sends a POST request with the letter and processes the JSON response
    Args:
        letter (str): The letter to search for
    """
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": letter}
    try:
        response = requests.post(url, data=data)
        # Try to parse the response as JSON
        try:
            json_response = response.json()
            # Check if JSON is not empty
            if json_response:
                print(f"[{json_response.get('id')}] {json_response.get('name')}")
            else:
                print("No result")
        except ValueError:
            # Response is not valid JSON
            print("Not a valid JSON")
    except requests.RequestException as e:
        # Handle network errors
        print(f"Error: {e}")


if __name__ == "__main__":
    # Get the letter from command line arguments
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    # Send the request
    search_user(letter)
