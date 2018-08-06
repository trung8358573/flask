from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from base import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    username = db.Column(db.String(64), unique=True, index=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    password_hash = db.Column(db.String(128))
    pic = db.Column(db.String(20), nullable=False, default='default.jpg')
    post_ids = db.relationship('Post', backref='author', lazy=True)

    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def create_post(self, vals):
        post = Post(
            title = vals.get('title'),
            url = vals.get('url'),
            description = vals.get('description'),
            user_id = self.id,
            channel_id = vals.get('channel'),
        )
        return post

    def create_channel(self, vals):
        channel = Post(
            title = vals.get('title'),
            description = vals.get('description'),
            admin_id = self.id,
        )
        return channel

    def  __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode(128), nullable=False)
    url = db.Column(db.String(256), nullable=False)
    description = db.Column(db.UnicodeText)
    votes = db.Column(db.Integer, nullable=False, default=1)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    channel_id = db.Column(db.Integer, db.ForeignKey('channels.id'), nullable=False)
    nsfw = db.Column(db.Boolean, default=False, nullable=False)    
    hidden = db.Column(db.Boolean, default=False, nullable=False)

    def delete(self):
        self.hidden = True

    def __repr__(self):
        return f"Post('{self.title}', '{self.timestamp}')"

class Channel(db.Model):
    __tablename__ = 'channels'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode(24), nullable=False)
    description = db.Column(db.UnicodeText)
    post_ids = db.relationship('Post', backref='channel', lazy=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    pic = db.Column(db.String(20), nullable=False, default='default.jpg')

    def __repr__(self):
        return f"Channel('{self.title}')"

