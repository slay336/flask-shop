from flask import Blueprint, render_template, session, url_for

auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")


def login_required(view):
    def check_login(**kwargs):
        if g.user:
            return view(**kwargs)

        return view(**kwargs)

    return check_login


@auth_blueprint.route("/login")
def login():
    session["user"] = "test"
    return render_template("login.html")


@auth_blueprint.route("/logout")
def logout():
    session.__delattr__("user")
    return url_for("index")
