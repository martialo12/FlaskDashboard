"""Routes for user authentication."""

from flask import redirect, render_template, flash, Blueprint, request, url_for
from flask_login import login_required, logout_user, current_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import LoginForm, RegisterForm
from .models import db, User
from . import lm

# Blueprint configuration

auth_bp = Blueprint(
    'auth_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@auth_bp.route('/login.html', methods=['GET', 'POST'])
def login_page():
    """ User login page. """

    # Bypass login screen if user is logged in
    if current_user.is_authenticated:
        flash('you are already logged in')
        return redirect(url_for('main_bp.index'))

    login_form = LoginForm(request.form)
    # POST: create user and redirect them to the app
    msg = None

    if login_form.validate_on_submit():
        # Get form fields
        email = request.form.get('email', '', type=str)
        password = request.form.get('password', '', type=str)
        # Validate login attempt
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                next = request.args.get('next')
                return redirect(next or url_for('main_bp.index'))
            else:
                flash('wrong password. Please try again.')
        else:
            flash('Unknown user')

    # GET: Serve Log-in page
    return render_template('layouts/auth-default.html',
                           content=render_template('pages/login.html', form=login_form, msg=msg))


@auth_bp.route('/signup.html', methods=['GET', 'POST'])
def signup_page():
    """User sign-up page."""
    signup_form = RegisterForm(request.form)
    # POST: Sign user in
    msg = None

    if signup_form.validate_on_submit():
        # Get Form fields
        firstname = request.form.get('firstname', '', type=str)
        lastname = request.form.get('lastname', '', type=str)
        email = request.form.get('email', '', type=str)
        password = request.form.get('password', '', type=str)
        password_crypt = generate_password_hash(password)
        existing_user = User.query.filter_by(email=email).first()
        if existing_user is None:
            user = User(
                lastname=lastname,
                firstname=firstname,
                email=email,
                password=password_crypt
            )
            user.save()
            login_user(user)
            return redirect(url_for('auth_bp.login_page'))
        flash(' a user already exists with that email address')
        return redirect(url_for('auth_bp.signup_page'))

    return render_template('layouts/auth-default.html',
                           content=render_template('pages/register.html', form=signup_form, msg=msg))


@auth_bp.route('/logout')
@login_required
def logout_page():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth_bp.login_page'))


@lm.user_loader
def load_user(user_id):
    """check if user is logged in in every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@lm.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users Login page"""
    return redirect(url_for('auth_bp.login_page'))


# Render the icons page
@auth_bp.route('/icons.html')
@login_required
def icons():

    return render_template('layouts/default.html',
                           content=render_template('pages/icons.html') )


# Render the profile page
@auth_bp.route('/profile.html')
@login_required
def profile():

    return render_template('layouts/default.html',
                           content=render_template('pages/profile.html'))


# Render the tables page
@auth_bp.route('/tables.html')
@login_required
def tables():
    return render_template('layouts/default.html',
                           content=render_template('pages/tables.html', current_user=current_user))



