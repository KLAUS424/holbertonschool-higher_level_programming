#!/usr/bin/env python3
"""
Task 04: Extending Dynamic Data Display to Include SQLite in Flask
Reads product data from JSON, CSV, or SQLite database.
"""

from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)


def create_data_files():
    """Create sample data files and database if they don't exist"""
    # Create products.json
    if not os.path.exists('products.json'):
        json_data = [
            {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
            {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99},
            {"id": 3, "name": "Wireless Mouse", "category": "Electronics", "price": 29.99}
        ]
        with open('products.json', 'w') as f:
            json.dump(json_data, f, indent=2)
    # Create products.csv
    if not os.path.exists('products.csv'):
        csv_data = [
            ["id", "name", "category", "price"],
            ["4", "Smartphone", "Electronics", "699.99"],
            ["5", "Notebook", "Office Supplies", "4.99"],
            ["6", "Headphones", "Electronics", "129.99"]
        ]
        with open('products.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(csv_data)
    # Create SQLite database
    if not os.path.exists('products.db'):
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        # Create Products table
        cursor.execute('''
            CREATE TABLE Products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        # Insert sample data
        products = [
            (7, 'Tablet', 'Electronics', 299.99),
            (8, 'Desk Lamp', 'Home Goods', 45.50),
            (9, 'Python Book', 'Books', 39.99),
            (10, 'Backpack', 'Travel', 59.99)
        ]
        cursor.executemany(
            'INSERT INTO Products (id, name, category, price) VALUES (?, ?, ?, ?)',
            products
        )
        conn.commit()
        conn.close()


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
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin-top: 20px;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        .error {
            color: red;
            padding: 10px;
            background-color: #ffe6e6;
            border: 1px solid red;
            border-radius: 4px;
        }
        .nav {
            margin: 20px 0;
        }
        .nav a {
            margin-right: 10px;
            padding: 8px 16px;
            background-color: #4CAF50;
            color: white;
            text-decoration: none;
            border-radius: 4px;
        }
        .nav a:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <h1>Product Display</h1>
    <div class="nav">
        <a href="/products?source=json">JSON</a>
        <a href="/products?source=csv">CSV</a>
        <a href="/products?source=sql">SQLite</a>
        <a href="/products?source=json&id=1">JSON ID 1</a>
        <a href="/products?source=sql&id=7">SQL ID 7</a>
        <a href="/products?source=invalid">Invalid Source</a>
    </div>
    {% if error %}
        <div class="error">
            {{ error }}
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
        <p>Total products displayed: {{ products|length }}</p>
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
            products = json.load(f)
        return products
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_csv_products():
    """Read products from CSV file"""
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
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


def read_sql_products():
    """Read products from SQLite database"""
    products = []
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products ORDER BY id')
        rows = cursor.fetchall()
        for row in rows:
            product = {
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
            }
            products.append(product)
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
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
            h1 { color: #333; }
            ul { line-height: 1.8; }
            a { color: #0066cc; text-decoration: none; }
            a:hover { text-decoration: underline; }
            .source { margin: 20px 0; padding: 15px; background-color: #f0f0f0; border-radius: 5px; }
        </style>
    </head>
    <body>
        <h1>Product Display Application</h1>
        <p>This Flask application can display product data from multiple sources.</p>
        <div class="source">
            <h2>Available Data Sources:</h2>
            <ul>
                <li><strong>JSON</strong>: Static JSON file with sample products</li>
                <li><strong>CSV</strong>: Comma-separated values file with different products</li>
                <li><strong>SQLite</strong>: Database with additional products</li>
            </ul>
        </div>
        <h2>Test URLs:</h2>
        <ul>
            <li><a href="/products?source=json">JSON Source</a></li>
            <li><a href="/products?source=csv">CSV Source</a></li>
            <li><a href="/products?source=sql">SQLite Source</a></li>
            <li><a href="/products?source=json&id=1">JSON Product ID 1</a></li>
            <li><a href="/products?source=sql&id=7">SQL Product ID 7</a></li>
            <li><a href="/products?source=xml">Invalid Source Test</a></li>
            <li><a href="/products?source=sql&id=999">Non-existent Product ID</a></li>
        </ul>
    </body>
    </html>
    '''


@app.route('/products')
def display_products():
    """Display products from JSON, CSV, or SQLite with optional filtering"""
    # Get query parameters
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')
    # Validate source parameter
    if not source:
        return render_template('product_display.html',
                             error="Missing source parameter. Please specify 'source=json', 'source=csv', or 'source=sql'")
    # Check for valid source
    valid_sources = ['json', 'csv', 'sql']
    if source not in valid_sources:
        return render_template('product_display.html', error="Wrong source")
    # Read products based on source
    if source == 'json':
        products = read_json_products()
    elif source == 'csv':
        products = read_csv_products()
    else:  # source == 'sql'
        products = read_sql_products()
    # Handle empty product list
    if not products:
        return render_template('product_display.html',
                             error=f"No products found in {source.upper()} source")
    # Filter by ID if specified
    if product_id:
        try:
            target_id = int(product_id)
            filtered_products = [p for p in products if p['id'] == target_id]
            if filtered_products:
                products = filtered_products
            else:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.html',
                                 error=f"Invalid ID format: '{product_id}'. ID must be a number")
    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    # Create necessary files and database
    create_data_files()
    create_template()
    # Run the application
    app.run(debug=True, port=5000)
