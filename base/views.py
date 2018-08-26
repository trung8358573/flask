from flask import request, render_template
from base import app, db
from base.forms import RegisterForm
from base.models import User, Post
import json
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user
from flask import redirect


@app.route('/')
def front_page():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    vals = dict(request.form)
    username = vals.get('username')[0]
    password = vals.get('password')[0]

    user_db = User.query.filter_by(username=username).first()
    if user_db and check_password_hash(user_db.password, password):
        login_user(user_db, remember=vals.get('remember'))
        return json.dumps({'status': 'success'})
    else:
        return json.dumps({'status': 'failed'})

@app.route('/logout')
def logout():
    logout_user()
    return redirect("/")


@app.route('/post', methods=['POST'])
def post():
    if current_user.is_authenticated:
        vals = dict(request.form)
        for key, val in vals.items():
            vals[key] = val[0]

        title = vals.get('title'),
        url = vals.get('url'),
        description = vals.get('description')
        votes = vals.get('votes')

        post = Post(
            user_id=current_user.id,
            title=title,
            url=url,
            description=description,
            votes=votes
        )
        db.session.add(post)
        db.session.commit()
        return json.dumps({'status': 'success', 'msg': 'Sign up successful!'})



@app.route('/signup', methods=['POST'])
def signup():
    vals = dict(request.form)
    for key, val in vals.items():
        vals[key] = val[0]

    email = vals.get('email')
    username = vals.get('username')

    user_db = User.query.filter_by(username=username).first()
    email_db = User.query.filter_by(email=email).first()

    if not user_db and not email_db:
        user = User(
            email=email,
            username=username,
            password=generate_password_hash(vals.get('password'))
        )
        db.session.add(user)
        db.session.commit()
        return json.dumps({'status': 'success', 'msg': 'Sign up successful!'})
    else:
        response = {'status': 'failed', 'msg': ''}
        if user_db:
            response['msg'] += 'This username already exists. '
        if email_db:
            response['msg'] += 'This email already exists. '
        return json.dumps(response)
