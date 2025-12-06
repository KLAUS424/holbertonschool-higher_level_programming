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
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f5f5f5;
        }
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            border-bottom: 2px solid #4CAF50;
            padding-bottom: 10px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th {
            background-color: #4CAF50;
            color: white;
            text-align: left;
            padding: 12px;
        }
        td {
            border: 1px solid #ddd;
            padding: 12px;
        }
        tr:nth-child(even) {
            background-color: #f2f2f2;
        }
        tr:hover {
            background-color: #ddd;
        }
        .error {
            color: #d32f2f;
            background-color: #ffebee;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid #d32f2f;
            margin: 20px 0;
        }
        .success {
            color: #388e3c;
            background-color: #e8f5e8;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid #388e3c;
            margin: 20px 0;
        }
        .info {
            color: #1976d2;
            background-color: #e3f2fd;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid #1976d2;
            margin: 20px 0;
        }
        .filter-info {
            margin: 20px 0;
            padding: 15px;
            background-color: #e8eaf6;
            border-radius: 5px;
        }
        a {
            color: #1976d2;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .nav-links {
            margin: 20px 0;
        }
        .nav-links a {
            margin-right: 15px;
            padding: 8px 16px;
            background-color: #4CAF50;
            color: white;
            border-radius: 4px;
        }
        .nav-links a:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Product Display</h1>
        <div class="nav-links">
            <a href="/products?source=json">View JSON Products</a>
            <a href="/products?source=csv">View CSV Products</a>
            <a href="/products?source=json&id=1">JSON Product ID 1</a>
            <a href="/products?source=csv&id=6">CSV Product ID 6</a>
            <a href="/products?source=xml">Invalid Source Test</a>
        </div>
        {% if error %}
        <div class="error">
            <strong>Error:</strong> {{ error }}
        </div>
        {% endif %}
        {% if message %}
        <div class="info">
            {{ message }}
        </div>
        {% endif %}
        {% if filter_info %}
        <div class="filter-info">
            {{ filter_info }}
        </div>
        {% endif %}
        {% if products %}
        <table>
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
        <p>Total products: {{ products|length }}</p>
        {% endif %}
        {% if not products and not error %}
        <div class="info">
            No products to display. Please select a valid data source.
        </div>
        {% endif %}
        <div style="margin-top: 30px; padding-top: 20px; border-top: 1px solid #ddd;">
            <h3>Test URLs:</h3>
            <ul>
                <li><a href="/products?source=json">All JSON products</a></li>
                <li><a href="/products?source=csv">All CSV products</a></li>
                <li><a href="/products?source=json&id=3">JSON product ID 3</a></li>
                <li><a href="/products?source=csv&id=8">CSV product ID 8</a></li>
                <li><a href="/products?source=json&id=999">Non-existent ID</a></li>
                <li><a href="/products?source=xml">Invalid source</a></li>
            </ul>
        </div>
    </div>
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


@app.route('/')
def home():
    """Home page with instructions"""
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Product Display App</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .container { max-width: 800px; margin: 0 auto; }
            h1 { color: #333; }
            ul { line-height: 1.8; }
            a { color: #0066cc; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Product Display Application</h1>
            <p>This Flask application demonstrates reading and displaying data from JSON and CSV files.</p>
            <h2>Available Routes:</h2>
            <ul>
                <li><a href="/products?source=json">/products?source=json</a> - Display all JSON products</li>
                <li><a href="/products?source=csv">/products?source=csv</a> - Display all CSV products</li>
                <li><a href="/products?source=json&id=1">/products?source=json&id=1</a> - Display JSON product with ID 1</li>
                <li><a href="/products?source=csv&id=6">/products?source=csv&id=6</a> - Display CSV product with ID 6</li>
            </ul>
            <h2>Query Parameters:</h2>
            <ul>
                <li><strong>source</strong> (required): 'json' or 'csv'</li>
                <li><strong>id</strong> (optional): Filter by product ID</li>
            </ul>
            <h2>Test Edge Cases:</h2>
            <ul>
                <li><a href="/products?source=xml">Invalid source parameter</a></li>
                <li><a href="/products?source=json&id=999">Non-existent product ID</a></li>
                <li><a href="/products">Missing source parameter</a></li>
            </ul>
        </div>
    </body>
    </html>
    '''


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
                             error=f"Wrong source: '{source}'. Please use 'json' or 'csv'")
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
    message = ""
    filter_info = ""
    if product_id:
        try:
            target_id = int(product_id)
            filtered_products = [p for p in products if p['id'] == target_id]
            if filtered_products:
                products = filtered_products
                filter_info = f"Filtered by ID: {product_id}"
            else:
                return render_template('product_display.html', 
                                     error=f"Product with ID {product_id} not found in {source.upper()} file",
                                     products=[])
        except ValueError:
            return render_template('product_display.html',
                                 error=f"Invalid ID format: '{product_id}'. ID must be a number")
    # Prepare display message
    if len(products) == 1:
        message = f"Displaying 1 product from {source.upper()} file"
    else:
        message = f"Displaying {len(products)} products from {source.upper()} file"
    return render_template('product_display.html',
                         products=products,
                         message=message,
                         filter_info=filter_info)


if __name__ == '__main__':
    # Create necessary files
    create_data_files()
    create_template()
    # Run the application
    app.run(debug=True, port=5000)
