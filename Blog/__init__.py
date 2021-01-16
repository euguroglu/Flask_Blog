from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
#Application initiation
app = Flask(__name__)
app.config.from_pyfile('config.cfg')
#Database initiation:
db = SQLAlchemy(app)
migrate = Migrate(app,db)
bcrypt = Bcrypt(app)
#This is definition for login manager
login_manager = LoginManager(app)
#This redirects people to login page if they are trying to access protected page
login_manager.login_view = 'login'
#This is giving style to message comes from login manager
login_manager.login_message_category = 'info'

mail = Mail(app)

from Blog import routes
