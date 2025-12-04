#!/usr/bin/python3
"""
Flask web application for a simple user management API
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}


@app.route('/', methods=['GET'])
def home():
    """Root endpoint - welcome message"""
    return "Welcome to the Flask API!"


@app.route('/data', methods=['GET'])
def get_data():
    """Return list of all usernames"""
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route('/status', methods=['GET'])
def get_status():
    """API status endpoint"""
    return "OK"


@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    """Get user by username"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user"""
    # Check if request contains valid JSON
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400
    data = request.get_json()
    # Check if username is provided
    if 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    username = data['username']
    # Check if username already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    # Add the new user
    users[username] = {
        "username": username,
        "name": data.get('name', ''),
        "age": data.get('age', ''),
        "city": data.get('city', '')
    }
    # Return success response
    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == '__main__':
    app.run(debug=True)
