from flask import request, render_template
from base import app, db
from base.forms import PostForm, RegisterForm, LoginForm
from base.models import User, Post
import json
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/')
def front_page():
    r = request
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    vals = dict(request.form)
    username = vals.get('username')
    password = vals.get('password')
    print(username, password)

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        print('aaaaaaaaaaaaaa')


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

    email = vals.get('email'),
    username = vals.get('username'),
    password = generate_password_hash(vals.get('password'))
    print(vals)

    user_db = User.query.filter_by(username=username).first()
    email_db = User.query.filter_by(email=email).first()

    if not user_db and not email_db:
        user = User(
            email=email,
            username=username,
            password=password
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
