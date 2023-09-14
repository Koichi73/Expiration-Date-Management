from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    # appの設定
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')

    # DBの設定
    db.init_app(app)
    from flask_app import models

    # ログインの設定
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # Blueprintの登録
    from flask_app.views.index import index_bp
    from flask_app.views.food_list import food_list_bp
    from flask_app.views.delete import delete_bp
    from flask_app.views.search import search_bp
    from flask_app.views.edit import edit_bp
    from flask_app.views.regist import regist_bp
    from flask_app.views.receipt import receipt_bp
    from flask_app.views.auth import auth_bp
    from flask_app.views.how_to_use import how_to_use_bp
    app.register_blueprint(index_bp)
    app.register_blueprint(food_list_bp)
    app.register_blueprint(delete_bp)
    app.register_blueprint(search_bp)
    app.register_blueprint(edit_bp)
    app.register_blueprint(regist_bp)
    app.register_blueprint(receipt_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(how_to_use_bp)

    return app
