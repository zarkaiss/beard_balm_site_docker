from marshmallow import fields, Schema
from app import db, login
from datetime import datetime
from flask_admin.contrib.sqla import ModelView
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from wtforms.fields import SelectField
from time import time
import jwt
from flask import current_app


class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean(), nullable=False, default=False)
    is_active = db.Column(db.Boolean(), default=True)
    last_login = db.Column(db.DateTime, default=datetime.utcnow)
    confirmed = db.Column(db.Boolean, default=False, nullable=True)
    role = db.relationship('Role', backref='User', lazy='dynamic')
   # token = db.Column(db.String(32), index=True, unique=True)
   # token_expiration = db.Column(db.DateTime)


    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def _is_admin(self):
        if self.role == "Admin":
            return True
        else:
            return False

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
                {'reset_password': self.id, 'exp': time() + expires_in},
                current_app.config['SECRET_KEY'],
                algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'],
                    algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)


    @staticmethod
    def get_all_users():
        print(User.query.all())
        return User.query.all()

    @staticmethod
    def get_one_user(id):
        return User.query.get(id)

    def __repr__(self):
        return '<id {}>'.format(self.id)

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    last_login = fields.DateTime(dump_only=True)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Role(db.Model):
    roleId = db.Column(db.Integer, primary_key=True)
    username_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    users_role = db.Column(db.String(128), nullable=True)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    last_modified = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, data=''):
        if data =='':
            pass
        else:
            self.username_id = data.get("username_id")
            self.users_role = data.get("users_role")
            self.created_on = data.get("created_on")
            self.last_modified = data.get("last_modified")

    def current_role(self, users_role):
        if users_role == "Admin":
            return "Admin-Authenticated"
        if users_role == "Customer":
            return "Customer-Authenticated"
        if users_role == "Staff":
            return "Staff-Authenticated"
        else:
            return "Error"


    def __repr__(self):
        return f"<id {self.roleId}>"






class Product(db.Model):
    productid = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    price = db.Column(db.DECIMAL) # might want to put nullable=False
    available = db.Column(db.Boolean(), default=True)
    category = db.Column(db.String(100), nullable=False)
    product_rating = db.Column(db.DECIMAL) # nullable=True-- be explicit in the db models
    product_review = db.Column(db.String(100), nullable=True)


    def __repr__(self):
        return f"Product('{self.productid}','{self.product_name}','{self.description}','{self.image}','{self.price}')"

    @staticmethod
    def get_all_products():
        print(Product.query.all())
        return Product.query.all()

    @staticmethod
    def get_one_product():
        return Product.query.get(id)

class ProductSchema(Schema):
   productid = fields.Int(dump_only=True)
   product_name = fields.Str(required=True)
   description = fields.Str(required=True)
   image = fields.Str(required=True)
   price = fields.Int(dump_only=True)
   category1 = fields.Str(required=True)


#Class to limit choices on category from product model
class ProductModelView(ModelView):

    form_overrides = dict(
        category=SelectField
    )
    form_args = dict(
        category=dict(
            choices=[
                ('BALM','Balm'),
                ('WAX','Wax'),
                ('CREAM', 'Cream'),
                ('ACCESSORY', 'Accessory'),
                ('CONDITIONER', 'Conditioner'),
                ('SOFTENER', 'Softener')
            ]
        )
    )

    def __init__(self):
        super(ProductModelView, self).__init__(Product, db.session)




class Feedback(db.Model):
    feedbackid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email1 = db.Column(db.String(255), nullable=False)
    subject= db.Column(db.String(255), nullable=False)
    message = db.Column(db.String(255), nullable=False)
    approved = db.Column(db.Boolean(), default=False)


    def __init__(self, name, email1,subject, message):
        self.name = name
        self.email1 = email1
        self.subject = subject
        self.message = message


class Poll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    question = db.Column(db.String(90))
    stamp = db.Column(db.DateTime)
    options = db.relationship('Option', backref='option', lazy='dynamic')

    def __init__(self, name, question, stamp=None):
        self.name = name
        self.question = question
        if stamp is None:
            stamp = datetime.utcnow()
        self.stamp = stamp

class Option(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(30))
    poll_id = db.Column(db.Integer, db.ForeignKey('poll.id'))
    poll = db.relationship('Poll', backref=db.backref('poll', lazy='dynamic'))
    votes = db.Column(db.Integer)

    def __init__(self, text, poll, votes):
        self.text = text
        self.poll = poll
        self.votes = votes

