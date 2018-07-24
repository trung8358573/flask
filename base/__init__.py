from flask import Flask as F
from flask_sqlalchemy import SQLAlchemy

app = F(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flask:flask@localhost/flask_db'
app.config['SECRET_KEY'] = 'hard to guess string'
db = SQLAlchemy(app)

from base import views