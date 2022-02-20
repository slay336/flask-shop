import os

from flask import Flask

from .models import db
from .views import views_blueprint
from .views.auth import auth_blueprint

app: Flask = Flask(__name__)
app.secret_key = "SOME_REALLY_SECRET_KEY"
app.register_blueprint(views_blueprint)
app.register_blueprint(auth_blueprint)

db_location: str = os.environ.get("GOODSHOP_DB_URI", "/tmp/goodshop.db")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_location}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
os.makedirs(os.path.dirname(db_location), exist_ok=True)
db.init_app(app)
with app.app_context():
    db.create_all()

app.add_url_rule("/", endpoint="views.index")
