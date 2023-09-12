from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# appの設定
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

# DBの設定
db = SQLAlchemy(app)
from flask_app import models

# ログインの設定
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'