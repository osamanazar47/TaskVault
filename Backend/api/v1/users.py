#!/usr/bin/python3
"""the user routes"""
from flask import Blueprint, request, jsonify
from Backend.models import storage, User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

user_bp = Blueprint('user_bp', __name__)

# Register Route
@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    new_user = User(name=data['name'])
    new_user.set_password(data['password'])
    storage.new(new_user)
    storage.save()
    return jsonify({'message': 'User registered successfully'})

# Login Route
@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
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

@user_bp.route('/users/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())

@user_bp.route('/users', methods=['POST'])
@jwt_required()
def create_user():
    data = request.get_json()
    new_user = User(name=data['name'])
    new_user.set_password(data['password'])
    storage.new(new_user)
    storage.save()
    return jsonify(new_user.to_dict()), 201

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    user.name = data['name']
    user.set_password(data['password'])
    storage.save()
    return jsonify(user.to_dict())

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    storage.delete(user)
    storage.save()
    return jsonify({'message': 'User deleted successfully'})
