#!/usr/bin/python3
"""Display GitHub user ID using API"""

import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    user = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"
    # Create Basic Authentication
    auth = (user, token)
    try:
        response = requests.get(url, auth=auth)
        # Check if request was successful
        if response.status_code == 200:
            try:
                data = response.json()
                user_id = data.get('id')
                if user_id:
                    print(user_id)
                else:
                    print("None")
            except ValueError:
                print("None")
        else:
            print("None")
    except requests.RequestException:
        print("None")
