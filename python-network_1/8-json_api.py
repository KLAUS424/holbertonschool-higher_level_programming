#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user
with a letter as a parameter
"""

import sys
import requests


if __name__ == "__main__":
    # Get the letter from command line or set to empty string
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    # Prepare the POST request
    url = "http://0.0.0.0:5000/search_user"
    payload = {"q": q}
    try:
        response = requests.post(url, data=payload)
        # Try to parse as JSON
        try:
            json_data = response.json()
            if json_data:
                # JSON is not empty
                user_id = json_data.get('id')
                user_name = json_data.get('name')
                print(f"[{user_id}] {user_name}")
            else:
                # JSON is empty
                print("No result")
        except ValueError:
            # Not valid JSON
            print("Not a valid JSON")
    except requests.exceptions.RequestException:
        # Handle connection errors silently
        pass
