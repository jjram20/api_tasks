from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from utils.db import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'secret_key'

db.init_app(app)

with app.app_context():
    jwt = JWTManager(app)
    
    from routes.users_route import users_bp
    from routes.tasks_route import tasks_bp

    app.register_blueprint(users_bp)
    app.register_blueprint(tasks_bp)