from app import app
from utils.db import db

with app.app_context():
    db.create_all()

PORT = 8000

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = PORT, debug=True)