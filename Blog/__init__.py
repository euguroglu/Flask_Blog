from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Application initiation
app = Flask(__name__)
app.config['SECRET_KEY'] = 'willbeaddedlater'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#Database initiation:
db = SQLAlchemy(app)

from Blog import routes
