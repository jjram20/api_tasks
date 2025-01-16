from utils.db import db
from .user import User

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    statement = db.Column(db.String(1000), unique=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    def __init__(self, statement, owner):
        self.statement = statement
        self.owner = owner