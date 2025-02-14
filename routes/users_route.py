from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import datetime
from utils.db import db
from models.user import User

users_bp = Blueprint('users', __name__)

@users_bp.route("/new_user", methods=['POST'])
def new_user():
    req = request.get_json(force=True)
    user = req.get('user')
    password = req.get('password')
    if user and password:
        hash_password = generate_password_hash(password)
        new_user = User(user, hash_password)
        db.session.add(new_user)
        db.session.commit()
        return "New user registered"
    else:
        return "Data required is not complete"

@users_bp.route("/login_user", methods=['POST'])
def login_user():
    req = request.get_json(force=True)
    user = req.get('user')
    user_db = User.query.filter_by(user=user).first()
    password = req.get('password')
    if user and check_password_hash(user_db.password, password):
        access_token = create_access_token(identity=user, expires_delta=datetime.timedelta(hours=1))
        return jsonify(access_token=access_token), 200
    return "Invalid credentials"

@users_bp.route("/get_users", methods=['GET'])
@jwt_required()
def get_users():
    current_user = get_jwt_identity()
    print(current_user)
    users = User.query.all()
    users_data = [user.to_dict() for user in users]
    response = {"status": 200, "users": users_data}
    return response

@users_bp.route("/edit_user/<id>", methods=['PUT'])
@jwt_required()
def edit_user(id):
    current_user = get_jwt_identity()
    user = User.query.get(id)
    req = request.get_json(force=True)
    print(req)
    if req.get("user"):
        print("Nuevo usuario")
        user.user = req.get('user')
    if req.get('password'):
        print("Nuevo password")
        new_password = req.get('password')
        hash_new_password = generate_password_hash(new_password)
        user.password = hash_new_password
    print("USER")
    print(user)
    print(user.user)
    print(user.password)
    db.session.commit()
    return "User updated"

@users_bp.route("/delete_user/<id>", methods=['DELETE'])
@jwt_required()
def delete_user(id):
    current_user = get_jwt_identity()
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return "User deleted"