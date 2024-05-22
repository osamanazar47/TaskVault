#!/usr/bin/python3
"""The tasks routes"""
from flask import Blueprint, request, jsonify
from Backend.models import storage, Task
from flask_jwt_extended import jwt_required, get_jwt_identity

task_bp = Blueprint('task_bp', __name__)

# CRUD Operations
@task_bp.route('/users/<int:user_id>/tasks', methods=['GET'])
@jwt_required()
def get_tasks(user_id):
    current_user = get_jwt_identity()
    if current_user['id'] != user_id:
        return jsonify({'message': 'Permission denied'}), 403
    tasks = Task.query.filter_by(user_id=user_id).all()
    return jsonify([task.to_dict() for task in tasks])

@task_bp.route('/users/<int:user_id>/tasks', methods=['POST'])
@jwt_required()
def create_task(user_id):
    current_user = get_jwt_identity()
    if current_user['id'] != user_id:
        return jsonify({'message': 'Permission denied'}), 403
    data = request.get_json()
    new_task = Task(title=data['title'], description=data['description'], user_id=user_id)
    storage.new(new_task)
    storage.save()
    return jsonify(new_task.to_dict()), 201

@task_bp.route('/users/<int:user_id>/tasks/<int:task_id>', methods=['GET'])
@jwt_required()
def get_task(user_id, task_id):
    current_user = get_jwt_identity()
    if current_user['id'] != user_id:
        return jsonify({'message': 'Permission denied'}), 403
    task = Task.query.filter_by(id=task_id, user_id=user_id).first_or_404()
    return jsonify(task.to_dict())

@task_bp.route('/users/<int:user_id>/tasks/<int:task_id>', methods=['PUT'])
@jwt_required()
def update_task(user_id, task_id):
    current_user = get_jwt_identity()
    if current_user['id'] != user_id:
        return jsonify({'message': 'Permission denied'}), 403
    task = Task.query.filter_by(id=task_id, user_id=user_id).first_or_404()
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    storage.save()
    return jsonify(task.to_dict())

@task_bp.route('/users/<int:user_id>/tasks/<int:task_id>', methods=['DELETE'])
@jwt_required()
def delete_task(user_id, task_id):
    current_user = get_jwt_identity()
    if current_user['id'] != user_id:
        return jsonify({'message': 'Permission denied'}), 403
    task = Task.query.filter_by(id=task_id, user_id=user_id).first_or_404()
    storage.delete(task)
    storage.save()
    return jsonify({'message': 'Task deleted successfully'})
