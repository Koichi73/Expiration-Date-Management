from flask import Blueprint, render_template, request, redirect
from flask_login import login_user, logout_user, login_required, current_user
from flask_app import db
from flask_app.models import Food
import datetime

food_list_bp = Blueprint('food_list', __name__, url_prefix='/food-list')


@food_list_bp.route("/", methods=["GET", "POST"])
@login_required
def food_list():
    user_id = current_user.id
    food_data = db.session.query(Food.id, Food.food_name, Food.limit_date) \
                                .filter(Food.user_id == user_id) \
                                .order_by(Food.limit_date, Food.id) \
                                .all()
    food_list = []
    today = datetime.datetime.today().date()
    today_str = today.strftime('%Y-%m-%d')
    for row in food_data: # 期限が今日以前にはTrue、明日以降にはFalseを加える
        food_list.append([
            row.id,
            row.food_name,
            row.limit_date,
            True if row.limit_date <= today_str else False
        ])

    return render_template("food-list.html", food_list=food_list)