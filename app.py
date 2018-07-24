from flask import Flask as F
from flask_sqlalchemy import SQLAlchemy
import source

app = F(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'posgresql://flask:flask@localhost/flask_db'
db = SQLAlchemy(app)

app.run(debug=True)

