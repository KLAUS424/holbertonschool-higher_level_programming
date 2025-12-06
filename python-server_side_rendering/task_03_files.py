#!/usr/bin/env python3
"""
Task 03: Displaying Data from JSON or CSV Files in Flask
Reads and displays product data from JSON or CSV files with filtering.
"""

from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)


def create_data_files():
    """Create sample JSON and CSV files if they don't exist"""
    # Create products.json
    if not os.path.exists('products.json'):
        json_data = [
            {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
            {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99},
            {"id": 3, "name": "Wireless Mouse", "category": "Electronics", "price": 29.99},
            {"id": 4, "name": "Desk Lamp", "category": "Home Goods", "price": 45.50},
            {"id": 5, "name": "Python Programming Book", "category": "Books", "price": 39.99}
        ]
        with open('products.json', 'w') as f:
            json.dump(json_data, f, indent=2)
    # Create products.csv
    if not os.path.exists('products.csv'):
        csv_data = [
            ["id", "name", "category", "price"],
            ["6", "Smartphone", "Electronics", "699.99"],
            ["7", "Notebook", "Office Supplies", "4.99"],
            ["8", "Headphones", "Electronics", "129.99"],
            ["9", "Water Bottle", "Sports", "24.99"],
            ["10", "Backpack", "Travel", "59.99"]
        ]
        with open('products.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(csv_data)


def create_template():
    """Create the product display template"""
    os.makedirs('templates', exist_ok=True)
    template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Display</title>
</head>
<body>
    <h1>Product Display</h1>
    {% if error %}
        <p style="color: red;">{{ error }}</p>
    {% endif %}
    {% if products %}
        <table border="1">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Category</th>
                    <th>Price</th>
                </tr>
            </thead>
            <tbody>
                {% for product in products %}
                <tr>
                    <td>{{ product.id }}</td>
                    <td>{{ product.name }}</td>
                    <td>{{ product.category }}</td>
                    <td>${{ "%.2f"|format(product.price) }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    {% elif not error %}
        <p>No products to display.</p>
    {% endif %}
</body>
</html>'''
    with open('templates/product_display.html', 'w') as f:
        f.write(template)


def read_json_products():
    """Read products from JSON file"""
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_csv_products():
    """Read products from CSV file"""
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert string values to appropriate types
                product = {
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                }
                products.append(product)
    except (FileNotFoundError, KeyError, ValueError):
        return []
    return products


@app.route('/products')
def display_products():
    """Display products from JSON or CSV file with optional filtering"""
    # Get query parameters
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')
    # Validate source parameter
    if not source:
        return render_template('product_display.html',
                             error="Missing source parameter. Please specify 'source=json' or 'source=csv'")
    if source not in ['json', 'csv']:
        return render_template('product_display.html',
                             error="Wrong source")
    # Read products based on source
    if source == 'json':
        products = read_json_products()
    else:  # source == 'csv'
        products = read_csv_products()
    # Handle empty product list
    if not products:
        return render_template('product_display.html',
                             error=f"No products found in {source.upper()} file")
    # Filter by ID if specified
    if product_id:
        try:
            target_id = int(product_id)
            filtered_products = [p for p in products if p['id'] == target_id]
            if filtered_products:
                products = filtered_products
            else:
                return render_template('product_display.html',
                                     error="Product not found")
        except ValueError:
            return render_template('product_display.html',
                                 error=f"Invalid ID format: '{product_id}'. ID must be a number")
    return render_template('product_display.html', products=products)


@app.route('/')
def home():
    """Simple home page"""
    return '''
    <h1>Product Display App</h1>
    <p>Test URLs:</p>
    <ul>
        <li><a href="/products?source=json">/products?source=json</a></li>
        <li><a href="/products?source=csv">/products?source=csv</a></li>
        <li><a href="/products?source=json&id=1">/products?source=json&id=1</a></li>
        <li><a href="/products?source=json&id=999">/products?source=json&id=999</a> (Product not found)</li>
        <li><a href="/products?source=xml">/products?source=xml</a> (Wrong source)</li>
    </ul>
    '''


if __name__ == '__main__':
    # Create necessary files
    create_data_files()
    create_template()
    # Run the application
    app.run(debug=True, port=5000)
