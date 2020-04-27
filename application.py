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
from wtforms import FlaskForm, Form, TextField, TextAreaField, validators, StringField, SubmitField
from Flask-WTF import FlaskForm



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
    return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='register', form=form)




@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='login', form=form)





class RegistrationForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Sign Up')



class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Submit')




@app.route("/Submit",methods=['GET', 'POST'])
def submit():

    form = LoginForm()

    return render_template('Submit.html', title='Submit', form=form)





if __name__ == '__main__':
    app.run(debug=True)
