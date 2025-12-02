#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response.
If HTTP status code >= 400, prints: Error code: followed by status code.
"""

import requests
import sys


def main():
    """Main function to fetch URL and handle error codes"""
    # Get URL from command line argument
    if len(sys.argv) < 2:
        return
    url = sys.argv[1]
    # Send GET request
    response = requests.get(url)
    # Check if status code is an error (>= 400)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        # Display response body for successful requests
        print(response.text)


if __name__ == "__main__":
    main()
