#!/usr/bin/python3
"""the user routes"""
from flask import Blueprint, request, jsonify
from Backend.models import db
from Backend.models.user import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

user_bp = Blueprint('user_bp', __name__)


# Helper function for validating input data
def validate_user_data(data, keys):
    for key in keys:
        if key not in data or not data[key]:
            return False, f"Missing or empty {key}"
    return True, ""

# Register Route
@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    is_valid, message = validate_user_data(data, ['name', 'password'])
    if not is_valid:
        return jsonify({'message': message}), 400

    if User.query.filter_by(name=data['name']).first():
        return jsonify({'message': 'User already exists'}), 400

    new_user = User(name=data['name'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'})

# Login Route
@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    is_valid, message = validate_user_data(data, ['name', 'password'])
    if not is_valid:
        return jsonify({'message': message}), 400

    user = User.query.filter_by(name=data['name']).first()
    if user and user.check_password(data['password']):
        access_token = create_access_token(identity={'id': user.id, 'name': user.name})
        return jsonify(access_token=access_token)
    return jsonify({'message': 'Invalid credentials'}), 401

# CRUD Operations
@user_bp.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@user_bp.route('/users/<user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    user = db.session.get(User, user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(user.to_dict())

@user_bp.route('/users', methods=['POST'])
@jwt_required()
def create_user():
    data = request.get_json()
    is_valid, message = validate_user_data(data, ['name', 'password'])
    if not is_valid:
        return jsonify({'message': message}), 400

    if User.query.filter_by(name=data['name']).first():
        return jsonify({'message': 'User already exists'}), 400

    new_user = User(name=data['name'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

@user_bp.route('/users/<user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    user = db.session.get(User, user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    data = request.get_json()
    is_valid, message = validate_user_data(data, ['name', 'password'])
    if not is_valid:
        return jsonify({'message': message}), 400

    user.name = data['name']
    user.set_password(data['password'])
    db.session.commit()
    return jsonify(user.to_dict())

@user_bp.route('/users/<user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    user = db.session.get(User, user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})
