from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from utils.db import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    from routes.users_route import users_bp
    from routes.tasks_route import tasks_bp

    app.register_blueprint(users_bp)
    app.register_blueprint(tasks_bp)