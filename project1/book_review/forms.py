from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Email, Length, NumberRange


class RegisterForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(), Length(min=5, max=30)])
    email = StringField("email", validators=[DataRequired(), Email(), Length(max=50)])
    password = StringField("password", validators=[DataRequired(), Length(min=5, max=20)])


class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = StringField("password", validators=[DataRequired()])


class ReviewForm(FlaskForm):
    review = TextAreaField('review', validators=[DataRequired(), Length(min=1, max=2000)])
    rating = IntegerField('rating', validators=[DataRequired(), NumberRange(min=1, max=5)])
