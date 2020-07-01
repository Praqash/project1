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
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, url_for, flash, redirect, request
from flask import Flask, render_template, request
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask import render_template, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm
from models import User, Books
from flask_login import login_user, current_user, logout_user, login_required
import requests



from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SESSION_TYPE"] = "filesystem"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
from models import User
from models import Books
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))
Session(app)
db = SQLAlchemy(app)


login_manager = LoginManager(app)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



@app.route("/")
@app.route("/home")
def home():
  return render_template('home.html')





@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    books = Books.query.all()
    return render_template('account.html', title='Account', books = books)



@app.route("/about" )

def about():
      return render_template('about.html')


@app.route("/reviews", methods = ['POST'] )

def reviews():
      r = requests.get("https://www.goodreads.com/book/review_counts.json",params={"key": 'LHWJHAL1SZGQk1zztVIxsw', "isbns": '0441172717'})
      print(r.json())
      data = print(r.json())
      return render_template('reviews.html', r= r)








if __name__ == '__main__':
    app.run(debug=True)
