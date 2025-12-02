#!/usr/bin/python3
"""
Python script that fetches a URL and displays information about the response body.
Uses the 'urllib' package and a 'with' statement.
"""
import urllib.request

def fetch_hbtn_status(url="https://intranet.hbtn.io/status"):
    """
    Fetches the content from the given URL and prints the response body details
    in the required format.
    """
    try:
        # Use the 'with' statement to handle the request and automatically close
        # the response object upon completion.
        with urllib.request.urlopen(url) as response:
            # Read the entire body of the response
            body = response.read()

            # Decode the bytes content to UTF-8
            utf8_content = body.decode('utf-8')

            # Print the required output format
            print("Body response:")
            # Use tabulation (\t) before the hyphen (-)
            print(f"\t- type: {type(body)}")
            print(f"\t- content: {body}")
            print(f"\t- utf8 content: {utf8_content}")
    except urllib.error.URLError as e:
        print(f"Error fetching URL: {e.reason}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    fetch_hbtn_status()
