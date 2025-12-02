#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
using the requests package.
"""

import requests


def main():
    """Main function to fetch and display status information"""
    # Fetch the URL
    response = requests.get('https://intranet.hbtn.io/status')
    # Display the formatted response information
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")


if __name__ == "__main__":
    main()
