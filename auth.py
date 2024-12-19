from flask import Blueprint, jsonify, request
from functools import wraps
from dotenv import load_dotenv
import os

load_dotenv()
auth_routes = Blueprint('auth', __name__)
SECRET_TOKEN = os.getenv('SECRET_KEY') 

# Decorator for token-based authentication
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or token != f"Bearer {SECRET_TOKEN}":
            return jsonify({"message": "Token is missing or invalid"}), 403
        return f(*args, **kwargs)
    return decorated

# Login endpoint
@auth_routes.route('/auth/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    # Simple credential validation (no database for this example)
    if username == "admin" and password == "password":
        return jsonify({"token": SECRET_TOKEN}), 200
    return jsonify({"message": "Invalid credentials"}), 401

# Example of a protected route
@auth_routes.route('/secure-data', methods=['GET'])
@token_required
def secure_data():
    return jsonify({"data": "This is secure data"}), 200
