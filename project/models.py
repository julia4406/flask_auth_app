'''модель отражает, что означает наличие пользователя для
нашего приложения. У нас есть поля адреса эл. почты, пароля
и имени. В приложении вы можете указать, хотите ли хранить
больше информации для каждого пользователя.'''

from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
