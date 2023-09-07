from flask_app import db
from flask_login import UserMixin


#食材DB
class Food(db.Model):
    __tablename__ = "food"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    food_name = db.Column(db.String(255))
    limit_date = db.Column(db.String)

#ユーザー情報DB
class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(12))