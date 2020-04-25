import os
from flask import render_template
from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from flask import Flask

my_awesome_app = Flask(__name__)


@my_awesome_app.route('/')
def hello_world():
    return 'HELLO EVERYONE HOW IS IT GOING'


if __name__ == '__main__':
    my_awesome_app.run()
