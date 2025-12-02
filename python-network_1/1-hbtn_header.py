#!/usr/bin/python3
"""
Python script that takes a URL as an argument,
 sends a request to the URL,
and displays the value of the X-Request-Id variable found
 in the response header.
Uses urllib and sys packages.
"""
import urllib.request
import sys

def get_x_request_id():
    """
    Fetches the URL provided as the first command-line argument and prints the
    value of the 'X-Request-Id' header from the response.
    """
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.headers.get('X-Request-Id')
            if x_request_id is not None:
                print(x_request_id)

    except urllib.error.URLError as e:
        print(f"Error accessing URL '{url}': {e.reason}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_x_request_id()
