from flask import request, render_template, url_for, abort
from base import app, db
from base.models import User, Post, Channel
import json
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user
from flask import redirect


@app.route('/')
def front_page():
    posts = json.dumps([
        {
            'title': 'LPT: How to Wake Up in the Morning',
            'url': '../static/post2.jpg',
            'user': {
                'name': 'tim tran',
                'pic': '../static/user.jpg',
            },
            'channel': {
                'name': 'memes',
                'pic': '../static/channel.png'
            },
            'vote': 100,
            'time': '2018-08-13 00:55:05.828713',
            'description': ''
        }
    ])
    channels = json.dumps([
        {
            'title': 'Funny',
            'url': '#',
            'pic': '../static/channel.png',
        },
        {
            'title': 'Animals',
            'url': '#',
            'pic': '../static/channel.png',
        },
    ])
    return render_template('index.html', posts=posts, channels=channels)


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
        return json.dumps({'status': 'success'})


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
        return json.dumps({'status': 'success', 'msg': 'Sign up successful! Please login now.'})
    else:
        response = {'status': 'failed', 'msg': ''}
        if user_db:
            response['msg'] += 'This username already exists. '
        if email_db:
            response['msg'] += 'This email already exists. '
        return json.dumps(response)


@app.route('/create_channel', methods=['POST'])
def create_channel():
    vals = dict(request.form)
    for key, val in vals.items():
        vals[key] = val[0]

    title = vals.get('title')
    description = vals.get('description')
    private = vals.get('private')
    if private == 'true':
        private = True
    elif private == 'false':
        private = False

    if current_user.is_authenticated:
        channel = Channel(
            title=title,
            description=description,
            private=private,
            admin_id=current_user.id
        )
        db.session.add(channel)
        db.session.commit()
        return json.dumps({'status': 'success'})
    else:
        response = {'status': 'failed'}
        return json.dumps(response)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files and current_user.is_authenticated:
        filename = photos.save(request.files['photo'])
        rec = photos(filename=filename, user=current_user.id)
        rec.store()
        return redirect(url_for('show', id=rec.id))
    return render_template('index.html')


@app.route('/photo/<id>')
def show(id):
    photo = photos.load(id)
    if photo is None:
        abort(404)
    url = photos.url(photo.filename)
    return render_template('show.html', url=url, photo=photo)
