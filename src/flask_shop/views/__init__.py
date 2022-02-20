from flask import Blueprint, render_template, session

views_blueprint = Blueprint("views", __name__)


@views_blueprint.route("/index")
def index():
    return render_template("index.html")


@views_blueprint.route("/cart")
def cart():
    return render_template("cart.html")
