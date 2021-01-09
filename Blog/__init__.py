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
#This is definition for login manager
login_manager = LoginManager(app)
#This redirects people to login page if they are trying to access protected page
login_manager.login_view = 'login'
#This is giving style to message comes from login manager
login_manager.login_message_category = 'info'

from Blog import routes
