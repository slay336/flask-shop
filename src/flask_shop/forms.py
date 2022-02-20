from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators


class RegistrationForm(FlaskForm):
    username = StringField("Имя пользователя", [validators.Length(min=5, max=80, message="Слишком короткое имя")])
    email = StringField("Email", [validators.Email(message="Некорректный email")])
    password = StringField("Пароль", [validators.Length(min=7, max=100, message="Некорректный пароль")])
