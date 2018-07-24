from flask import Flask as F
from flask import request, render_template
from flask_sqlalchemy import SQLAlchemy

app = F(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'posgresql://flask:flask@localhost/flask_db'
db = SQLAlchemy(app)

@app.route('/')
def front_page():
    r = request
    return render_template('index.html')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(64))
    post_ids = db.relationship('Post')

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode)
    link = db.Column(db.String(64))
    description = db.Column(db.UnicodeText)
    user_id = db.relationship('User')

app.run(debug=True)

