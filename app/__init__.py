# -*- encoding: utf-8 -*-
"""
Argon Dashboard - coded in Flask

Author  : AppSeed App Generator
Design  : Creative-Tim.com
License : MIT 
Support : https://appseed.us/support 
"""

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from flask_bcrypt import Bcrypt

from flask_restful import Api
from flask_bootstrap import Bootstrap

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

api = Api(app)  # flask_restful

app.config.from_object('app.configuration.Config')

db = SQLAlchemy(app)  # flask-sqlalchemy
db.init_app(app)
bootstrap = Bootstrap(app)
# bc = Bcrypt(app)  # flask-bcrypt

lm = LoginManager()  # flask-loginmanager
lm.init_app(app)  # init the login manager


with app.app_context():
    # Import parts of our application
    from . import auth, models, routes
    from .restapi.stats import ApiStats

    app.register_blueprint(routes.main_bp)
    app.register_blueprint(auth.auth_bp)

    # Create Database Models
    db.create_all()

    # Create 'admin@example.com' user with 'Admin' and 'Agent' roles
    # if not User.query.filter(User.email == 'admin@gmail.com').first():
    #     user = User(
    #         email='admin@gmail.com',
    #         lastname='wafo',
    #         firstname='Martial',
    #         password=generate_password_hash('password')
    #     )
    #     user.roles.append(Role(name='Admin'))
    #     user.roles.append(Role(name='User'))
    #     db.session.add(user)
    #     db.session.commit()

    # Inject REST api
    api.add_resource(ApiStats, '/api/stats/<string:segment>')

