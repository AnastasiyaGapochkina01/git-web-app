import random
import json
from flask import Flask
from flask_sqlachemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///web.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Web(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(45))
    timestamp = db.Column(db.DateTine, default=datetime.utcnow)

with app.app_context():
    db.create_all()

# FIX some bug
@app.route('/health')
def health():
    return {"server": "alive"}

@app.route('/main')
def main():
    return {"msg": "hello"}

@app.route('/api', methods=["GET"])
def api_get():
    logs = Web.query.all()
    return {"status": "db not ready", "logs": logs}

@app.route('/api', methods=["POST"])
def api_post():
    return {"status": "logged"}, 201

@app.route('/pay', methods=["POST"])
def create_payment():
    fake_order = {
        "order_id": 156,
        "status": "created",
        "amount": 10000
    }
    return jsonify(fake_order), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5100)