from flask import request, render_template
from base import app
from base.forms import PostForm, RegisterForm, LoginForm
from base.models import User, Post

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
    r = request
    print(request.form)
    print(request.values)
    form = RegisterForm()
    return render_template('index.html')