from flask import render_template, request, redirect
from flask_app import app

from flask_app.views.food_list import food_list_bp
from flask_app.views.delete import delete_bp
from flask_app.views.search import search_bp
from flask_app.views.edit import edit_bp
from flask_app.views.regist import regist_bp
from flask_app.views.receipt import receipt_bp
from flask_app.views.auth import auth_bp
from flask_app.views.how_to_use import how_to_use_bp

app.register_blueprint(food_list_bp)
app.register_blueprint(delete_bp)
app.register_blueprint(search_bp)
app.register_blueprint(edit_bp)
app.register_blueprint(regist_bp)
app.register_blueprint(receipt_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(how_to_use_bp)


@app.route("/")
def index():
    return redirect("/auth/signup")
