from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
#Application initiation
app = Flask(__name__)
app.config['SECRET_KEY'] = 'willbeaddedlater'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Database initiation:
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
#This is definition for login manager
login_manager = LoginManager(app)
#This redirects people to login page if they are trying to access protected page
login_manager.login_view = 'login'
#This is giving style to message comes from login manager
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'outgoing.itu.edu.tr'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'u@itu.edu.tr'
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEFAULT_SENDER'] = ''2''
mail = Mail(app)

from Blog import routes
