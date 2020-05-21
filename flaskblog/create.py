import os

from flask import Flask, render_template, request
from flaskblog.models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def table():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        table()
