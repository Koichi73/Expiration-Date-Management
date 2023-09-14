from flask import Blueprint, render_template, request, redirect

index_bp = Blueprint('index', __name__, url_prefix='/')


@index_bp.route("/", methods=["GET", "POST"])
def index():
    return redirect("/signup")