#!/usr/bin/python3
"""
Python script that takes a URL as an argument,
 sends a request to the URL,
and displays the value of the 'X-Request-Id' variable found
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
    # Check for the required argument
    if len(sys.argv) < 2:
        return

    url = sys.argv[1]

    try:
        # Use a 'with' statement for resource management
        with urllib.request.urlopen(url) as response:
            # The header is retrieved using response.headers.get() which
            # is case-insensitive for standard header fields.
            x_request_id = response.headers.get('X-Request-Id')
            if x_request_id is not None:
                print(x_request_id)

    except urllib.error.URLError as e:
        print(f"Error accessing URL '{url}': {e.reason}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    get_x_request_id()
