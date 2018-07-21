from flask import Flask as F
from flask import request, render_template
from flask_sqlalchemy import SQLAlchemy

app = F(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'posgresql://flask:flask@localhost/flask_db'
db = SQLAlchemy(app)

@app.route('/')
def front_page():
    r = request
    return render_template('base.html')

@app.route('/<name>')
def hi(name):
    return('<h1>hello %s</h1> !@') % name

app.run(debug=True)

