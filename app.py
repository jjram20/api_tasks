from flask import Flask
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from utils.db import db
import os

if os.getenv('FLASK_ENV') == 'production':
    load_dotenv('.env.production')
else:
    load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')

db.init_app(app)

with app.app_context():
    jwt = JWTManager(app)
    
    from routes.users_route import users_bp
    from routes.tasks_route import tasks_bp

    app.register_blueprint(users_bp)
    app.register_blueprint(tasks_bp)