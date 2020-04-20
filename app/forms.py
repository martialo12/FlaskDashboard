# -*- encoding: utf-8 -*-
"""
Argon Dashboard - coded in Flask

Author  : AppSeed App Generator
Design  : Creative-Tim.com
License : MIT 
Support : https://appseed.us/support 
"""

from datetime import datetime

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, IntegerField, DateTimeField
from wtforms.validators import InputRequired, Email, DataRequired, Length, EqualTo
from wtforms.fields.html5 import DateTimeLocalField, DateField


class LoginForm(FlaskForm):
	"""User Login Form."""
	email = StringField(
		u'Email',
		validators=[
			DataRequired('Please enter a valid email address'),
			Email('Please enter a valid email address')
		])
	password = PasswordField(u'Password', validators=[DataRequired()])
	submit = SubmitField('Log In')


class RegisterForm(FlaskForm):
	"""User Signup Form."""
	lastname = StringField(
		u'Lastname',
		validators=[DataRequired(message='Please enter Your lastname')])

	firstname = StringField(
		u'Firstname',
		validators=[DataRequired(message='please enter your firstname')])

	password = PasswordField(
		u'Password',
		validators=[DataRequired(message='Please enter a password.'),
		Length(min=8, message='Please select a strong password'),
		EqualTo('confirm', message='Passwords must match')])

	confirm = PasswordField('Confirm Your Password')

	email = StringField(
		u'Email',
		validators=[
		Length(min=6, message='please enter a valid email address.'),
		DataRequired(message='Please enter a valid email address'),
		Email(message='Please enter a valid email address')
	])


class HarvestedCanabisForm(FlaskForm):
	"""User Signup Form."""
	product_name = StringField(
		u'Product_name',
		validators=[DataRequired(message='Please enter product name')])

	product_batch = IntegerField(
		u'Product_batch',
		validators=[DataRequired(message='please enter product_batch')])

	net_weight_received = IntegerField(
		u'net_weight_received',
		validators=[DataRequired(message='Please enter net weight.')])

	balance = IntegerField(
		u'balance',
		validators=[DataRequired(message='Please enter a valid email address')])

	"""
	category = StringField(
		u'category',
		validators=[DataRequired(message='Please enter category')])"""

	transaction_date = DateTimeField(
		u'transaction_date',
		validators=[DataRequired(message='Please enter valid date')])
	product_id = IntegerField(
		u'product_id',
		validators=[DataRequired(message='Please enter a valid product id')])


class CreateHarvestedCanabisForm(FlaskForm):
	"""User Signup Form."""
	product_name = StringField(
		u'Product_name',
		validators=[DataRequired(message='Please enter product name')])

	product_batch = IntegerField(
		u'Product_batch',
		validators=[DataRequired(message='please enter product_batch')])

	net_weight_received = IntegerField(
		u'net_weight_received',
		validators=[DataRequired(message='Please enter net weight.')])

	balance = IntegerField(
		u'balance',
		validators=[DataRequired(message='Please enter a valid email address')])

	"""
	category = StringField(
		u'category',
		validators=[DataRequired(message='Please enter category')])"""

	category_id = StringField(
		u'category_id',
		validators=[DataRequired(message='Please enter category')])

	transaction_date = DateField(
		u'transaction_date',
		format='%Y-%m-%d',
		default=datetime.today,  # Now it will call it everytime.
		validators=[DataRequired(message='Please, this field is required')])
	product_id = IntegerField(
		u'product_id',
		validators=[DataRequired(message='Please enter a valid product id')])

	submit = SubmitField('Add')


class EditHarvestedCanabis(FlaskForm):
	"""User Signup Form."""
	product_name = StringField(
		u'Product_name',
		validators=[DataRequired(message='Please enter product name')])

	product_batch = IntegerField(
		u'Product_batch',
		validators=[DataRequired(message='please enter product_batch')])

	net_weight_received = IntegerField(
		u'net_weight_received',
		validators=[DataRequired(message='Please enter net weight.')])

	balance = IntegerField(
		u'balance',
		validators=[DataRequired(message='Please enter a valid email address')])

	category_id = StringField(
		u'category_id',
		validators=[DataRequired(message='Please enter category')])

	transaction_date = DateField(
		u'transaction_date',
		format='%Y-%m-%d',
		default=datetime.today,  # Now it will call it everytime.
		validators=[DataRequired(message='Please, this field is required')])

	submit = SubmitField('Edit')


"""
	Packaged Canabis
"""


class PackagedCanabisForm(FlaskForm):
	"""User Signup Form."""
	source = StringField(
		u'source',
		validators=[DataRequired(message='Please enter valid source name')])

	product_name = StringField(
		u'Product_name',
		validators=[DataRequired(message='Please enter product name')])

	product_batch = IntegerField(
		u'Product_batch',
		validators=[DataRequired(message='please enter product_batch')])

	net_weight_received = IntegerField(
		u'net_weight_received',
		validators=[DataRequired(message='Please enter net weight.')])

	balance = IntegerField(
		u'balance',
		validators=[DataRequired(message='Please enter a valid email address')])

	category_id = StringField(
		u'category_id',
		validators=[DataRequired(message='Please enter category')])

	transaction_date = DateField(
		u'transaction_date',
		format='%Y-%m-%d',
		default=datetime.today,  # Now it will call it everytime.
		validators=[DataRequired(message='Please, this field is required')])
	product_id = IntegerField(
		u'product_id',
		validators=[DataRequired(message='Please enter a valid product id')])

	submit = SubmitField('Add')


class EditPackagedCanabisForm(FlaskForm):
	"""User Signup Form."""
	source = StringField(
		u'source',
		validators=[DataRequired(message='Please enter source name')])

	product_name = StringField(
		u'Product_name',
		validators=[DataRequired(message='Please enter product name')])

	product_batch = IntegerField(
		u'Product_batch',
		validators=[DataRequired(message='please enter product_batch')])

	net_weight_received = IntegerField(
		u'net_weight_received',
		validators=[DataRequired(message='Please enter net weight.')])

	balance = IntegerField(
		u'balance',
		validators=[DataRequired(message='Please enter a valid email address')])

	category_id = StringField(
		u'category_id',
		validators=[DataRequired(message='Please enter category')])

	transaction_date = DateField(
		u'transaction_date',
		format='%Y-%m-%d',
		default=datetime.today,  # Now it will call it everytime.
		validators=[DataRequired(message='Please, this field is required')])

	submit = SubmitField('Edit')


class CreatePackagedCanabisForm(FlaskForm):
	"""User Signup Form."""
	source = StringField(
		u'source',
		validators=[DataRequired(message='Please enter product name')])

	product_name = StringField(
		u'Product_name',
		validators=[DataRequired(message='Please enter product name')])

	product_batch = IntegerField(
		u'Product_batch',
		validators=[DataRequired(message='please enter product_batch')])

	net_weight_received = IntegerField(
		u'net_weight_received',
		validators=[DataRequired(message='Please enter net weight.')])

	balance = IntegerField(
		u'balance',
		validators=[DataRequired(message='Please enter a valid email address')])

	"""
	category = StringField(
		u'category',
		validators=[DataRequired(message='Please enter category')])"""

	category_id = StringField(
		u'category_id',
		validators=[DataRequired(message='Please enter category')])

	transaction_date = DateField(
		u'transaction_date',
		format='%Y-%m-%d',
		default=datetime.today,  # Now it will call it everytime.
		validators=[DataRequired(message='Please, this field is required')])
	product_id = IntegerField(
		u'product_id',
		validators=[DataRequired(message='Please enter a valid product id')])

	submit = SubmitField('Add')
