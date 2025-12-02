#!/usr/bin/python3
"""
Python script that takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and displays the body of
the response.
"""

import requests
import sys


def main():
    """Main function to send POST request with email"""
    # Get URL and email from command line arguments
    if len(sys.argv) < 3:
        return
    url = sys.argv[1]
    email = sys.argv[2]
    # Prepare the data to be sent
    data = {'email': email}
    # Send POST request
    response = requests.post(url, data=data)
    # Display the response body
    print(response.text)


if __name__ == "__main__":
    main()
