from flask import Blueprint, jsonify, request
from utils.db import db
from models.user import User

users_bp = Blueprint('users', __name__)

@users_bp.route("/new_user", methods=['POST'])
def new_user():
    req = request.get_json(force=True)
    print(req)
    user = req['user']
    password = req['password']
    new_user = User(user, password)
    db.session.add(new_user)
    db.session.commit()
    return "New user registered"

@users_bp.route("/get_users", methods=['GET'])
def get_users():
    users = User.query.all()
    users_data = [user.to_dict() for user in users]
    response = {"status": 200, "users": users_data}
    return response

@users_bp.route("/edit_user/<id>", methods=['PUT'])
def edit_user(id):
    user = User.query.get(id)
    req = request.get_json(force=True)
    if req['new_user']:
        new_user = req['new_user']
        user.user = new_user
    if req['new_password']:
        new_password = req['new_password']
        user.password = new_password
    db.session.commit()
    return "User updated"

@users_bp.route("/delete_user/<id>", methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return "User deleted"