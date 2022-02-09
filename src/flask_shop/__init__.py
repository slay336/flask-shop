from flask import Flask

from .views import views_blueprint
from .views.auth import auth_blueprint

app = Flask(__name__)
app.secret_key = "SOME_REALLY_SECRET_KEY"
app.register_blueprint(views_blueprint)
app.register_blueprint(auth_blueprint)

app.add_url_rule("/", endpoint="views.index")
