#!/usr/bin/python3
"""
Flask API with Basic Authentication and JWT Authentication
"""

from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity, get_jwt
)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['JWT_SECRET_KEY'] = 'super-secret-jwt-key'

# Initialize authentication modules
basic_auth = HTTPBasicAuth()
jwt = JWTManager(app)

# In-memory user storage
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# Basic Authentication verification callback
@basic_auth.verify_password
def verify_password(username, password):
    """Verify username and password for Basic Authentication"""
    if username in users:
        user = users[username]
        if check_password_hash(user['password'], password):
            return username
    return None


# JWT Error Handlers
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing token"""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid token"""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handle expired token"""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handle revoked token"""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handle needs fresh token"""
    return jsonify({"error": "Fresh token required"}), 401


# Routes
@app.route('/')
def home():
    """Home endpoint"""
    return "Welcome to the Flask API with Authentication!"


@app.route('/basic-protected', methods=['GET'])
@basic_auth.login_required
def basic_protected():
    """Basic Authentication protected endpoint"""
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """JWT login endpoint"""
    # Check if request contains JSON
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400
    data = request.get_json()
    # Validate required fields
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Missing username or password"}), 400
    username = data['username']
    password = data['password']
    # Check if user exists
    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401
    # Verify password
    user = users[username]
    if not check_password_hash(user['password'], password):
        return jsonify({"error": "Invalid credentials"}), 401
    # Create JWT token with identity and additional claims
    access_token = create_access_token(
        identity=username,
        additional_claims={"role": user['role']}
    )
    return jsonify({
        "access_token": access_token
    }), 200


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """JWT protected endpoint"""
    return "JWT Auth: Access Granted"


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """Admin-only endpoint with role-based access control"""
    current_user = get_jwt_identity()
    # Get user role from token claims
    jwt_data = get_jwt()
    current_user_role = jwt_data.get('role', None)
    # Check if user is admin
    if current_user_role != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
