#!/usr/bin/python3
"""The tasks routes"""
from flask import Blueprint, request, jsonify
from models.task import Task
from models import db
from datetime import datetime
from flask_jwt_extended import jwt_required, get_jwt_identity

task_bp = Blueprint('task_bp', __name__)

# CRUD Operations
# Get all tasks of a user
@task_bp.route('/users/<user_id>/tasks', methods=['GET'])
@jwt_required()
def get_tasks(user_id):
    current_user = get_jwt_identity()
    if current_user['id'] != user_id:
        return jsonify({'message': 'Permission denied'}), 403
    tasks = Task.query.filter_by(user_id=user_id).all()
    return jsonify([task.to_dict() for task in tasks])

# Get a specific task for a user
@task_bp.route('/users/<user_id>/tasks/<task_id>', methods=['GET'])
@jwt_required()
def get_task(user_id, task_id):
    current_user = get_jwt_identity()
    if current_user['id'] != user_id:
        return jsonify({'message': 'Permission denied'}), 403
    task = Task.query.filter_by(id=task_id, user_id=user_id).first_or_404()
    return jsonify(task.to_dict())

# Create a new task for a user
@task_bp.route('/users/<user_id>/tasks', methods=['POST'])
@jwt_required()
def create_task(user_id):
    current_user = get_jwt_identity()
    if current_user['id'] != user_id:
        return jsonify({'message': 'Permission denied'}), 403

    data = request.get_json()

    # Convert the due_date string to a datetime object
    try:
        due_date = datetime.fromisoformat(data['due_date'])
    except ValueError:
        return jsonify({'message': 'Invalid date format'}), 400

    new_task = Task(
        title=data['title'],
        description=data['description'],
        due_date=due_date,  # Now it's a datetime object
        user_id=user_id
    )

    db.session.add(new_task)
    db.session.commit()

    return jsonify(new_task.to_dict()), 201


@task_bp.route('/users/<user_id>/tasks/<task_id>', methods=['PATCH'])
@jwt_required()
def update_task(user_id, task_id):
    current_user = get_jwt_identity()
    if current_user['id'] != user_id:
        return jsonify({'message': 'Permission denied'}), 403

    task = db.session.get(Task, task_id)
    if not task:
        return jsonify({'message': 'Task not found'}), 404

    data = request.get_json()
    if 'title' in data:
        task.title = data['title']
    if 'description' in data:
        task.description = data['description']
    if 'due_date' in data:
        try:
            task.due_date = datetime.fromisoformat(data['due_date'])
        except ValueError:
            return jsonify({'message': 'Invalid date format'}), 400

    if 'completed' in data:
        task.completed = data['completed']

    db.session.commit()
    return jsonify(task.to_dict()), 200

@task_bp.route('/users/<user_id>/tasks/<task_id>', methods=['DELETE'])
@jwt_required()
def delete_task(user_id, task_id):
    current_user = get_jwt_identity()
    if current_user['id'] != user_id:
        return jsonify({'message': 'Permission denied'}), 403
    task = Task.query.filter_by(id=task_id, user_id=user_id).first_or_404()
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully'})
