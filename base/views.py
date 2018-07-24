from flask import request, render_template
from base import app
from base.forms import PostForm
from base.models import User, Post

@app.route('/')
def front_page():
    r = request
    return render_template('index.html')