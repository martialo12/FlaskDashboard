# -*- encoding: utf-8 -*-
"""
Argon Dashboard - coded in Flask

Author  : AppSeed App Generator
Design  : Creative-Tim.com
License : MIT 
Support : https://appseed.us/support 
"""

import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

	"""Set Flask configuration vars from .env file."""

	# General Config
	SECRET_KEY = os.environ.get('SECRET_KEY')
	FLASK_APP = os.environ.get('FLASK_APP')
	FLASK_ENV = os.environ.get('FLASK_ENV')
	FLASK_DEBUG = os.environ.get('FLASK_DEBUG')

	# Database
	# SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
	SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
	# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
	SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/db_canabis'



