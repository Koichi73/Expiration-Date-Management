from flask import Blueprint, render_template, request, redirect, session
from flask_app import db
from flask_app import login_manager
from flask_app.models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__, url_prefix='/')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


#会員登録機能
@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        user_name = request.form.get("user-name")
        password = request.form.get("password")

        user_name_exist = User.query.filter_by(user_name=user_name).first()
        if user_name_exist:
            has_error = True
            return render_template("signup.html", has_error=has_error)
        else:
            signup_user = User(user_name=user_name, password=generate_password_hash(password))
            db.session.add(signup_user)
            db.session.commit()
            return redirect("/login")
    else:
        return render_template("signup.html")
    
#ログイン機能
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_name = request.form.get("user-name")
        password = request.form.get("password")
        
        user = User.query.filter_by(user_name=user_name).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            session['logged_in'] = True
            return redirect("/food-list")
        else:
            has_error = True
            return render_template("login.html", has_error=has_error)
    else:
        return render_template("login.html")
    
# ログアウト機能
@auth_bp.route("/logout")
def logout():
    logout_user()
    session.pop('logged_in', None)
    return redirect("/login")