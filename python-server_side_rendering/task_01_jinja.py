#!/usr/bin/env python3
"""
Task 01: Creating a Basic HTML Template in Flask
Complete solution with templates embedded in the code.
"""

from flask import Flask, render_template_string
import os
import sys

app = Flask(__name__)

# Template content as strings
HEADER_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Flask App</title>
</head>
<body>
    <header>
        <h1>My Flask App</h1>
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/about">About</a></li>
                <li><a href="/contact">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>'''

FOOTER_TEMPLATE = '''    </main>
    <footer>
        <p>&copy; 2024 My Flask App</p>
    </footer>
</body>
</html>'''

INDEX_TEMPLATE = HEADER_TEMPLATE + '''
        <h1>Welcome to My Flask App</h1>
        <p>This is a simple Flask application.</p>
        <ul>
            <li>Flask</li>
            <li>HTML</li>
            <li>Templates</li>
        </ul>
''' + FOOTER_TEMPLATE

ABOUT_TEMPLATE = HEADER_TEMPLATE + '''
        <h1>About Us</h1>
        <p>This is the about page for My Flask App. We're building a simple web application using Flask and Jinja templates to learn server-side rendering.</p>
''' + FOOTER_TEMPLATE

CONTACT_TEMPLATE = HEADER_TEMPLATE + '''
        <h1>Contact Us</h1>
        <p>Feel free to reach out to us if you have any questions about our Flask application!</p>
''' + FOOTER_TEMPLATE


@app.route('/')
def home():
    """Render the home page"""
    return render_template_string(INDEX_TEMPLATE)


@app.route('/about')
def about():
    """Render the about page"""
    return render_template_string(ABOUT_TEMPLATE)


@app.route('/contact')
def contact():
    """Render the contact page"""
    return render_template_string(CONTACT_TEMPLATE)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
