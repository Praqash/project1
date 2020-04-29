import os
from flask import render_template
from flask import Flask, session
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



from flask import Flask
app = Flask(__name__)


# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



@app.route("/")
@app.route("/home")
def home():
    form = RegistrationForm()
    return render_template('register.html', form=form)


@app.route("/books")
def books():
    return render_template('books.html', title='Books')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
         u = form.username.data
         p = form.password.data
         flash(f'Account created for {form.username.data}!', 'success')
         return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'admin@.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('books'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True)
