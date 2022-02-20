from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id_user = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    is_logged_in = db.Column(db.Boolean, nullable=False, default=False)
    carts = db.relationship("Cart", backref="user", lazy=True)

    def __repr__(self):
        return f"User {self.username}"


class Cart(db.Model):
    id_cart = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey("user.id_user"), nullable=False)
    cart_contents = db.relationship("CartContent", backref="cart", lazy=True)

    def __repr__(self):
        return f"Cart {self.id_cart} by {self.id_user.username}"


class Article(db.Model):
    id_article = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    cart_contents = db.relationship("CartContent", backref="article", lazy=True)

    def __repr__(self):
        return f"Article {self.name}"


class CartContent(db.Model):
    id_cart_content = db.Column(db.Integer, primary_key=True)
    id_cart = db.Column(db.Integer, db.ForeignKey("cart.id_cart"), nullable=False)
    id_article = db.Column(db.Integer, db.ForeignKey("article.id_article"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"CartContent cart: {self.id_cart}, article: {self.id_article}"


if __name__ == "__main__":
    db.create_all()
