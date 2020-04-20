# -*- encoding: utf-8 -*-
"""
Argon Dashboard - coded in Flask

Author  : martialo12
Design  : Creative-Tim.com
License : MIT 
Support : https://appseed.us/support 
"""
from datetime import datetime

from app import db, lm
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    lastname = db.Column(db.String(64), nullable=False, unique=False)
    firstname = db.Column(db.String(646), nullable=False, unique=False)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(500))
    is_admin = db.Column(db.Boolean, default=False)
    created_on = db.Column(db.DateTime, index=False, unique=False, nullable=False)

    def __init__(self, lastname, firstname, email, password):
        self.lastname = lastname
        self.firstname = firstname
        self.password = password
        self.email = email
        self.is_admin = False
        self.created_on = datetime.now()

    def set_password(self, password):
        """create hashed password."""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User %r - %s>' % (self.id) % (self.email)

    def save(self):

        # inject self into db session    
        db.session.add(self)
        # commit change and save the object
        db.session.commit()

        return self


class HarvestedCanabis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transaction_date = db.Column(db.DateTime)
    product_name = db.Column(db.String(80), nullable=False)
    product_batch = db.Column(db.Integer, nullable=False)
    net_weight_received = db.Column(db.Integer, nullable=False)
    balance = db.Column(db.Integer, nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    # category = db.relationship('Category', backref=db.backref('event', lazy='dynamic'))

    def __init__(self,
                 product_name,
                 product_batch,
                 net_weight_received,
                 balance,
                 # category,
                 category_id,
                 transaction_date
                 ):
        if transaction_date is None:
            transaction_date = datetime.utcnow()
        self.transaction_date = transaction_date
        self.product_name = product_name
        self.product_batch = product_batch
        self.net_weight_received = net_weight_received
        self.balance = balance
        self.category_id = category_id
        # self.category = category

    def save(self):

        # inject self into db session
        db.session.add(self)
        # commit change and save the object
        db.session.commit()

        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return '<HarvestedCanabis %r>' % self.product_name


class PackagedCanabis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transaction_date = db.Column(db.DateTime)
    product_name = db.Column(db.String(80), nullable=False)
    product_batch = db.Column(db.Integer, nullable=False)
    net_weight_received = db.Column(db.Integer, nullable=False)
    balance = db.Column(db.Integer, nullable=False)
    source = db.Column(db.String(80), nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    # category = db.relationship('Category', backref=db.backref('event', lazy='dynamic'))

    def __init__(self,
                 product_name,
                 product_batch,
                 net_weight_received,
                 balance,
                 source,
                 category_id,
                 transaction_date
                 ):
        if transaction_date is None:
            transaction_date = datetime.utcnow()
        self.transaction_date = transaction_date
        self.product_name = product_name
        self.product_batch = product_batch
        self.net_weight_received = net_weight_received
        self.balance = balance
        self.category_id = category_id
        self.source = source

    def save(self):

        # inject self into db session
        db.session.add(self)
        # commit change and save the object
        db.session.commit()

        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return '<PackagedCanabis %r>' % self.product_name


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name


class Stats(db.Model):

    id = db.Column(db.Integer,     primary_key=True)
    key = db.Column(db.String(64),  unique=True)
    val = db.Column(db.Integer)
    val_s = db.Column(db.String(256))

    def __init__(self, key):
        self.key = key

        db_obj = Stats.query.filter_by(key=key).first()
        if db_obj:
            self.id = db_obj.id
            self.key = db_obj.key
            self.val = db_obj.val
            self.val_s = db_obj.val_s

        else:

            db.session.add ( self )

            self.val = 0
            self.val_s = ''

    def __repr__(self):
        return '<Stats %s / %r / %s >' % ( self.key, self.val, self.val_s )

    def save(self):

        db_obj = Stats.query.filter_by(key=self.key).first()

        # update the existing db object
        if db_obj:

            db_obj.val = self.val
            db_obj.val_s = self.val_s

        # commit change and save the object
        db.session.commit()

        return self

# provide login manager with load_user callback
@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
