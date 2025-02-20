from utils.db import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(500), unique=False, nullable=False)
    tasks = db.relationship('Task', backref='user', lazy=True) #lazy = 'dynamic',cascade = "all, delete, delete-orphan"

    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user,
            'password': self.password,
        }

    def __init__(self, user, password):
        self.user = user
        self.password = password