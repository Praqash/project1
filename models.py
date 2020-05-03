from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()




class users(db.Model):
    __tablename__ = "users"
    Name = db.Column(db.String(20), nullable=False)
    Username = db.Column(db.String(20),  primary_key=True, nullable=False)
    Password = db.Column(db.String(60), nullable=False)
    isbn_book_reviewed = db.Column(db.Integer)

    def __repr__(self):
        return f"User('{self.Username}', '{self.Name}', {self.Password})"
