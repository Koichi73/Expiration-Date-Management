from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from dotenv import load_dotenv

load_dotenv() # 環境変数の読み込み

# appの設定
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
app.config['FLASK_ENV'] = os.environ.get('FLASK_ENV', 'development')

if app.config['FLASK_ENV'] == 'production':
    app.config.update(app.config['PRODUCTION_CONFIG'])
else:
    app.config.update(app.config['DEVELOPMENT_CONFIG'])

# DBの設定
db = SQLAlchemy(app)
from flask_app import models

# ログインの設定
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'