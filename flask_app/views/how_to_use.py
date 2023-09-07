from flask import Blueprint, render_template, request, redirect

how_to_use_bp = Blueprint('how-to-use', __name__, url_prefix='/how-to-use')


# レシピを検索する
@how_to_use_bp.route("/", methods=["GET", "POST"])
def how_to_use():
    return render_template("how-to-use.html")