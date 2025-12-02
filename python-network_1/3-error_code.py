#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
Handles HTTPError exceptions and prints the error code.
"""

import urllib.request
import urllib.error
import sys


def main():
    """Main function to fetch URL and handle errors"""
    # Get URL from command line argument
    if len(sys.argv) < 2:
        return
    url = sys.argv[1]
    try:
        # Use with statement to open URL
        with urllib.request.urlopen(url) as response:
            # Read and decode response body
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        # Handle HTTP errors
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    main()
