from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
#Application initiation
app = Flask(__name__)
app.config['SECRET_KEY'] = 'willbeaddedlater'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#Database initiation:
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from Blog import routes
