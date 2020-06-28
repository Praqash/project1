import csv
import os
from flask import Flask
from models import Books
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
db.init_app(app)


def main():
    f = open("/Users/prakashtiwari/Desktop/project1/books.csv")
    reader = csv.reader(f)
    for isbn, title, author, year in reader:
        books = Books (isbn = isbn, title = title, author = author, year = year)
        db.session.add(books)
        print(f"Added books isbn = {isbn} title =  {title} author = {author} year = {year}.")
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()
