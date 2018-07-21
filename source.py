from flask import Flask as F
from flask import request, render_template

app = F(__name__)

@app.route('/')
def front_page():
    r = request
    return render_template('base.html')

@app.route('/<name>')
def hi(name):
    return('<h1>hello %s</h1> !@') % name

app.run(debug=True)

