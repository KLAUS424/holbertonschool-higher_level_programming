#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id header in the response.
"""

import requests
import sys


def main():
    """Main function to fetch and display X-Request-Id header"""
    # Get URL from command line argument
    if len(sys.argv) < 2:
        return
    url = sys.argv[1]
    # Send GET request
    response = requests.get(url)
    # Get X-Request-Id header value
    x_request_id = response.headers.get('X-Request-Id')
    # Print the value if it exists
    if x_request_id:
        print(x_request_id)


if __name__ == "__main__":
    main()
