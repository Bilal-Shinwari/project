from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app) #making SQlite databse
bcrypt = Bcrypt(app) #for hashing of password
login_manager = LoginManager(app) #for handling the logins 
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from FlaskApp import routes