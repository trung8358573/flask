from flask import Flask as F
from flask import request, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


app = F(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'posgresql://flask:flask@localhost/flask_db'
db = SQLAlchemy(app)


@app.route('/')
def front_page():
    r = request
    return render_template('index.html')

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    username = db.Column(db.String(64), unique=True, index=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    password_hash = db.Column(db.String(128))
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    post_ids = db.relationship('Post')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

        
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode, nullable=False)
    link = db.Column(db.String(64), nullable=False)
    description = db.Column(db.UnicodeText)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

        def __repr__(self):
            return f"Post('{self.title}', '{self.timestamp}')"


class PostForm(Form):
    body = TextAreaField("What's on your mind?", validators=[Required()])
    submit = SubmitField('Submit')

app.run(debug=True)

