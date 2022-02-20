from typing import Dict, Union

from ..models import db, User


def user_register(username: str, email: str, password: str) -> Dict[str, Union[str, bool]]:
    existing_user: User = User.query.filter_by(email=email).all()
    if existing_user:
        return {
            "result": False,
            "error": "Пользователь с таким email уже зарегистрирован"
        }

    user = User(username=username, email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return {
        "result": True,
        "error": ""
    }
