from flask import request, render_template
from base import app, db
from base.forms import PostForm, RegisterForm, LoginForm
from base.models import User, Post
import json


@app.route('/')
def front_page():
    r = request
    return render_template('index.html')


@app.route('/register')
def register():
    form = RegisterForm()
    return render_template('register.html', title='Register', form=form)


@app.route('/post', methods=['POST'])
def post():
    vals = dict(request.form)
    for key, val in vals.items():
        vals[key] = val[0]

    email = vals.get('email'),
    username = vals.get('username'),
    password = vals.get('password')
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
        return json.dumps({'status':'success'})
    else:
        response = {'status':'failed','except':[]}
        if user_db:
            response['except'].append('username')
        if email_db:
            response['except'].append('email')
        return json.dumps(response)


@app.route('/get', methods=['POST'])
def get():
    r = request
    print(request.form)
    print(request.values)
    form = RegisterForm()
    return render_template('index.html')
