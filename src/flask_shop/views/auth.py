from flask import Blueprint, redirect, render_template, request, session, url_for

from ..controllers.users import user_register
from ..forms import RegistrationForm

auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")


def login_required(view):
    def check_login(**kwargs):
        if session.get("user"):
            return view(**kwargs)

        return view(**kwargs)

    return check_login


@auth_blueprint.route("/login")
def login():
    return render_template("login.html")


@auth_blueprint.route("/register", methods=["GET", "POST"])
def register_user():
    form = RegistrationForm()

    if request.method == "GET":
        return render_template("register.html", form=form)
    elif request.method == "POST":
        if form.validate_on_submit():
            result = user_register(
                request.form["username"],
                request.form["email"],
                request.form["password"]
            )
        else:
            result = {
                "result": False,
                "err": "Некорректно заполнены поля: %s" % ", ".join(form.errors)
            }

        if result["result"]:
            return redirect(url_for("auth.login"))
        else:
            return result


@auth_blueprint.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("views.index"))
