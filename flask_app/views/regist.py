from flask import Blueprint, render_template, request, redirect
from flask_login import login_user, logout_user, login_required, current_user
from flask_app import db
from flask_app.models import Food

regist_bp = Blueprint('regist', __name__, url_prefix='/regist')


# 手動登録画面の表示
@regist_bp.route("/", methods=["GET", "POST"])
@login_required
def regist():
    return render_template("regist.html")


# 手動登録の実行
@regist_bp.route("/exe", methods=["GET", "POST"])
@login_required
def regist_exe():
    if request.method == "POST":
        user_id = current_user.id
        food_names = request.form.getlist('food-name[]')
        limit_dates = request.form.getlist('limit-date[]')
        for food_name, limit_date in zip(food_names, limit_dates):
            new_food = Food(user_id=user_id, food_name=food_name, limit_date=limit_date)
            db.session.add(new_food)
        db.session.commit()
        
    return redirect("/food-list")