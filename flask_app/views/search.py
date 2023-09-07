from flask import Blueprint, render_template, request, redirect
from flask_login import login_user, logout_user, login_required, current_user
from flask_app import db
from flask_app.models import Food

search_bp = Blueprint('search', __name__, url_prefix='/search')


# レシピを検索する
@search_bp.route("/", methods=["GET", "POST"])
@login_required
def search():
    if request.method == "POST":
        checked_food_id_list = request.form.getlist('checkbox')
        url = "https://cookpad.com/search/"
        for x in checked_food_id_list:
            search_food = db.session.query(Food.food_name).filter_by(id=int(x)).scalar()
            url = url + search_food + " "
        return redirect(url)
    else:
        return redirect("/food-list")