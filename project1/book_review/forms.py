from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, Length


class RegisterForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(), Length(min=5, max=30)])
    email = StringField("email", validators=[DataRequired(), Email(), Length(max=50)])
    password = StringField("password", validators=[DataRequired(), Length(min=5, max=20)])


class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = StringField("password", validators=[DataRequired()])
