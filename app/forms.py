from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField
from .models import *


class TripForm(Form):
	tripname = StringField('tripname', validators=[DataRequired()])
	destination = StringField('destination', validators=[DataRequired()])
	friend = SelectField('friend', validators=[DataRequired()])
	submit = SubmitField('Create Trip')

	def set_choices(self):
		friends = getAvailableFriends()
		self.friend.choices = [(friend[0],friend[0]) for friend in friends]


class LoginForm(Form):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Log In')


class SignUpForm(Form):
	username = StringField('Username', validators=[DataRequired()])
	email = EmailField('Email', validators = [DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Sign Up')
