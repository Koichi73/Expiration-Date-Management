from flask import Blueprint, render_template, request, redirect
from flask_login import login_user, logout_user, login_required, current_user
from flask_app import db
from flask_app.models import Food

edit_bp = Blueprint('edit', __name__, url_prefix='/edit')


# 編集画面の表示
@edit_bp.route("/", methods=["GET", "POST"])
@login_required
def edit():
    if request.method == "POST":
        checked_food_id_list = request.form.getlist('checkbox')
        edit_food_list = []
        for x in checked_food_id_list:
            checked_food = db.session.query(Food).filter_by(id=int(x)).first()
            edit_food_list.append([x, checked_food.food_name, checked_food.limit_date])
        return render_template("edit.html", edit_food_list=edit_food_list)
    else:
        return redirect("/food-list")
    

# 編集の実行
@edit_bp.route("/exe", methods=["GET", "POST"])
@login_required
def edit_exe():
    if request.method == "POST":
        edit_food_list = request.form.getlist("food-id")
        for x in edit_food_list:
            edit_food_name = request.form.get("food-name-" + x)
            edit_limit_date = request.form.get("limit-date-" + x)

            food_to_update = db.session.query(Food).filter_by(id=int(x)).first()
            food_to_update.food_name = edit_food_name
            food_to_update.limit_date = edit_limit_date        
        db.session.commit()
        
    return redirect("/food-list")