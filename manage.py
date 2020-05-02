
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
@app.before_first_request
def create_user():
    db.create_all()
    #user_datastore.create_user(email='matt@nobien.net', password='password')
    print ('111')
class users(db.Model):
    Name = db.Column(db.String(20), nullable=False)
    Username = db.Column(db.String(20),  primary_key=True, nullable=False)
    Password = db.Column(db.String(60), nullable=False)
    isbn_book_reviewed = db.Column(db.Integer)

    def __repr__(self):
        return f"User('{self.Username}', '{self.Name}', {self.Password})"

if __name__ == '__main__':
    manager.run()
