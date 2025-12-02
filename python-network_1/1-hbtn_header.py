#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in
the header of the response.
"""

import urllib.request
import sys


def main():
    """Main function to fetch and display X-Request-Id header"""
    # Check if URL is provided
    if len(sys.argv) < 2:
        return
    url = sys.argv[1]
    # Use with statement to open URL
    with urllib.request.urlopen(url) as response:
        # Get the headers from the response
        headers = response.info()
        # Get the X-Request-Id header value
        x_request_id = headers.get('X-Request-Id')
        # Print the value if it exists
        if x_request_id:
            print(x_request_id)


if __name__ == "__main__":
    main()
