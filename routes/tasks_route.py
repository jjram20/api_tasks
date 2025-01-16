from flask import Blueprint, jsonify
from models.task import Task

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route("/get_tasks", methods=['GET'])
def get_tasks():
    return "get_tasks"

@tasks_bp.route("/new_task", methods=['POST'])
def new_task():
    return "new_task"

@tasks_bp.route("/edit_task/<id>", methods=['PUT'])
def edit_task():
    return "edit_task"

@tasks_bp.route("/delete_task/<id>", methods=['DELETE'])
def delete_task():
    return "delete_task"