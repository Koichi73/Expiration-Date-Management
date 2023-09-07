from flask import Blueprint, render_template, request, redirect
from flask_login import login_user, logout_user, login_required, current_user
from flask_app import db
from flask_app.models import Food

delete_bp = Blueprint('delete', __name__, url_prefix='/delete')


@delete_bp.route("/", methods=["GET", "POST"])
@login_required
def delete():
    if request.method == "POST":
        checked_food_id_list = request.form.getlist('checkbox')
        for x in checked_food_id_list:
            delete_food_list = db.session.query(Food).filter_by(id=int(x)).first()
            db.session.delete(delete_food_list)
        db.session.commit()

    return redirect("/food-list")