#!/usr/bin/env python3
"""
Task 02: Creating a Dynamic Template with Loops and Conditions in Flask
Enhances Flask application with dynamic content from JSON.
"""

from flask import Flask, render_template
import json
import os

app = Flask(__name__)


def create_json_file():
    """Create items.json file if it doesn't exist"""
    if not os.path.exists('items.json'):
        data = {
            "items": ["Python Book", "Flask Mug", "Jinja Sticker"]
        }
        with open('items.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("Created items.json")


def create_templates():
    """Create template files if they don't exist"""
    os.makedirs('templates', exist_ok=True)
    # Create items.html template
    items_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Items List</title>
</head>
<body>
    <h1>Items List</h1>
    {% if items %}
        <p>Here are all the items:</p>
        <ul>
        {% for item in items %}
            <li>{{ item }}</li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No items found</p>
    {% endif %}
    <p><a href="/">Back to Home</a></p>
</body>
</html>'''
    with open('templates/items.html', 'w') as f:
        f.write(items_template)


@app.route('/')
def home():
    """Render the home page"""
    return "Welcome to the Flask Items App! Visit <a href='/items'>/items</a> to see the items list."


@app.route('/items')
def items():
    """Render the items page with data from JSON"""
    try:
        # Read items from JSON file
        with open('items.json', 'r') as f:
            data = json.load(f)
        items_list = data.get('items', [])
    except FileNotFoundError:
        # If file doesn't exist, use empty list
        items_list = []
    except json.JSONDecodeError:
        # If JSON is invalid, use empty list
        items_list = []
    # Pass items to template
    return render_template('items.html', items=items_list)


@app.route('/items/empty')
def empty_items():
    """Route to test with empty items list"""
    return render_template('items.html', items=[])


@app.route('/items/full')
def full_items():
    """Route to test with full items list"""
    full_list = ["Python Book", "Flask Mug", "Jinja Sticker", "HTML Guide", "CSS Manual"]
    return render_template('items.html', items=full_list)


if __name__ == '__main__':
    # Create necessary files
    create_json_file()
    create_templates()
    # Run the application
    app.run(debug=True, port=5000)
