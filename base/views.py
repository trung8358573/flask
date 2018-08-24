from flask import request, render_template
from base import app, db
from base.forms import RegisterForm
from base.models import User, Post
import json
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user


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
        login_user(user_db, remember=True)
        print('yessssss')
    return 'aaaaaaaaaaaaaa'

@app.route('/logout')
def logout():
    logout_user()


@app.route('/post', methods=['POST'])
def post():
    vals = dict(request.form)
    for key, val in vals.items():
        vals[key] = val[0]

    title = vals.get('title'),
    url = vals.get('url'),
    description = vals.get('description')

    post = Post(
        title=title,
        url=url,
        description=description
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
    print(vals)

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


@app.route('/get', methods=['POST'])
def get():
    r = request
    print(request.form)
    print(request.values)
    form = RegisterForm()
    return render_template('index.html')
