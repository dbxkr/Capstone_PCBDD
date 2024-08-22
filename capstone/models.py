import pytz

from capstone import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=False, nullable=False)
    userid = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    authority = db.Column(db.Integer, nullable=False)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, nullable=False)
    image = db.Column(db.LargeBinary, nullable=False)
    result = db.Column(db.LargeBinary, nullable=True)
    type = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now(pytz.timezone('Asia/Seoul')), nullable=False)

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, nullable=False)
    image = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String(20000))
