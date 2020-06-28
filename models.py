import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_login import LoginManager
from flask import Flask
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)


    def __repr__(self):
       return f"User('{self.username}', '{self.email}')"

class Books(db.Model):
    __tablename__ = "Books"
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(50), unique=True)
    title = db.Column(db.String(60), nullable=False)
    author = db.Column(db.String(60), nullable=False)
    year = db.Column(db.String(50), nullable=False)



    def __repr__(self):
        return f"Books('{self.isbn}', '{self.title}','{self.author}', '{self.year}' )"
