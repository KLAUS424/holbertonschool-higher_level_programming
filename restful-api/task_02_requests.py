#!/usr/bin/python3
"""
Module for fetching and processing posts from JSONPlaceholder API
"""

import csv
import requests


def fetch_and_print_posts():
    """
    Fetches posts from JSONPlaceholder and prints the status code and titles
    """
    # Fetch data from JSONPlaceholder
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    # Print the status code
    print(f"Status Code: {response.status_code}")
    # Check if request was successful
    if response.status_code == 200:
        # Parse JSON data
        posts = response.json()
        # Print titles of all posts
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    Fetches posts from JSONPlaceholder and saves them to a CSV file
    """
    # Fetch data from JSONPlaceholder
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    # Check if request was successful
    if response.status_code == 200:
        # Parse JSON data
        posts = response.json()
        # Structure data into list of dictionaries
        structured_posts = []
        for post in posts:
            post_dict = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            structured_posts.append(post_dict)
        # Write to CSV file
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for post in structured_posts:
                writer.writerow(post)
