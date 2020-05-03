import os
from flask import render_template
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from flask_wtf import FlaskForm
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, url_for, flash, redirect, request
from flask import Flask, render_template, request
from models import *






from flask import Flask
app = Flask(__name__)







app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def table():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        table()








app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
db = SQLAlchemy(app)


def table():
   db.create_all()

@app.route("/")
@app.route("/home")
def home():

    return render_template('home.html')


@app.route("/books")
def books():

    return render_template('books.html', title = 'Books')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():

        user = users(Username=form.username.data, Name=form.name.data, Password=form.password.data)
        temp = users.query.filter_by(Username=form.username.data).first()

        if temp:
           return f"account already exist"

        else:
             db.session.add(user)
             db.session.commit()
             flash('Your account has been created! You are now able to log in', 'success')
             return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)



@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

       user  = users(Username=form.username.data, Password = form.password.data)
       temp = users.query.filter_by(Username=form.username.data, Password=form.password.data).first()
       if temp:
          return render_template('books.html', name1 = f"Hello", name2= form.username.data)

       else:
            return render_template('login.html', title='Login', form=form)

    else:
          flash('Login Unsuccessful. Please check email and password', 'danger')
          return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True)
