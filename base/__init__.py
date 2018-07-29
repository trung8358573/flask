from flask import Flask as F
from flask_sqlalchemy import SQLAlchemy
from socket import gethostname

app = F(__name__)

if 'liveconsole' in gethostname():
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="trung8358573",
    password="flaskflask",
    hostname="trung8358573.mysql.pythonanywhere-services.com",
    databasename="trung8358573$flask")
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flask:flask@localhost/flask_db'

app.config['SECRET_KEY'] = '86ae4018794e5f12f7ed6d5069393aed'
db = SQLAlchemy(app)

from base import views