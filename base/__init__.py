from flask import Flask as F
from flask_sqlalchemy import SQLAlchemy
from socket import gethostname

app = F(__name__)
<<<<<<< HEAD

if 'liveconsole' not in gethostname():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flask:flask@localhost/flask_db'
else:
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="trung8358573",
    password="flaskflask",
    hostname="trung8358573.mysql.pythonanywhere-services.com",
    databasename="trung8358573$flask")

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
=======
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flask:flask@localhost/flask_db'

>>>>>>> 57f0a9480076ec88060e82a8a57133c9f4688212
app.config['SECRET_KEY'] = 'hard to guess string'
db = SQLAlchemy(app)

from base import views