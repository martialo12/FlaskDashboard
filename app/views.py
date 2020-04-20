# -*- encoding: utf-8 -*-
"""
Argon Dashboard - coded in Flask

Author  : AppSeed App Generator
Design  : Creative-Tim.com
License : MIT
Support : https://appseed.us/support
"""
import requests

from flask import render_template, request, url_for, redirect, send_from_directory
from flask_login import login_user, logout_user
from werkzeug.exceptions import HTTPException, NotFound, abort

import os, logging

from app import app, lm, db, bc
from app.models import User
from app.forms import LoginForm, RegisterForm


@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'sitemap.xml')


@app.route('/googlee35aa2f2fd7b0c5b.html')
def google():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'googlee35aa2f2fd7b0c5b.html')


@app.route('/print')
def printMsg():
    app.logger.warning('testing warning log')
    app.logger.error('testing error log')
    app.logger.info('testing info log')
    return "Check your console"


# provide login manager with load_user callback
@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# authenticate user
@app.route('/logout.html')
def logout():
    logout_user()
    return redirect(url_for('index'))


# register user
@app.route('/register.html', methods=['GET', 'POST'])
def register():
    # declare the Registration Form
    form = RegisterForm(request.form)

    msg = None

    if request.method == 'GET':
        return render_template('layouts/auth-default.html',
                               content=render_template('pages/register.html', form=form, msg=msg))

    # check if both http method is POST and form is valid on submit
    if form.validate_on_submit():

        # assign form data to variables
        username = request.form.get('username', '', type=str)
        password = request.form.get('password', '', type=str)
        email = request.form.get('email', '', type=str)

        # filter User out of database through username
        user = User.query.filter_by(user=username).first()

        # filter User out of database through username
        user_by_email = User.query.filter_by(email=email).first()

        if user or user_by_email:
            msg = 'Error: User exists!'

        else:

            pw_hash = bc.generate_password_hash(password)

            user = User(username, email, pw_hash)

            user.save()

            msg = 'User created, please <a href="' + url_for('login') + '">login</a>'

    else:
        msg = 'Input error'

    return render_template('layouts/auth-default.html',
                           content=render_template('pages/register.html', form=form, msg=msg))


# authenticate user
@app.route('/login.html', methods=['GET', 'POST'])
def login():
    # login calling api
    # r = requests.get('http://localhost:8888/api/#!/user_auth/post_login_item')

    # check if both http method is POST and form is valid on submit
    form = LoginForm(request.form)
    if form.validate_on_submit():
        r = requests.get('http://localhost:8888/api/#!/user_auth/post_login_item')

    # Declare the login form
    form = LoginForm(request.form)
    # Flask message injected into the page, in case of any errors
    msg = None
    # check if both http method is POST and form is valid on submit
    if form.validate_on_submit():
        # assign form data to variables
        username = request.form.get('username', '', type=str)
        password = request.form.get('password', '', type=str)
        # filter User out of database through username
        user = User.query.filter_by(user=username).first()
        if user:

            if bc.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('index'))
            else:
                msg = "Wrong password. Please try again."
        else:
            msg = "Unkkown user"

    return render_template('layouts/auth-default.html',
                           content=render_template('pages/login.html', form=form, msg=msg))


# Render the icons page
@app.route('/icons.html')
def icons():
    return render_template('layouts/default.html',
                           content=render_template('pages/icons.html'))


# Render the profile page
@app.route('/profile.html')
def profile():
    return render_template('layouts/default.html',
                           content=render_template('pages/profile.html'))


# Render the tables page
@app.route('/tables.html')
def tables():
    return render_template('layouts/default.html',
                           content=render_template('pages/tables.html'))


# App main route + generic routing
@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path>')
def index(path):
    content = None

    try:

        # try to match the pages defined in -> pages/<input file>
        return render_template('layouts/default.html',
                               content=render_template('pages/' + path))
    except:

        return render_template('layouts/auth-default.html',
                               content=render_template('pages/404.html'))
