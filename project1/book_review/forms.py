from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class RegisterForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(), Length(min=5, max=30)])
    email = StringField("email", validators=[DataRequired(), Email(), Length(max=50)])
    password = PasswordField("password", validators=[DataRequired(), Length(min=5, max=20)])
    submit = SubmitField('submit')


class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    submit = SubmitField('submit')


class ReviewForm(FlaskForm):
    review = TextAreaField('review', validators=[DataRequired(), Length(min=1, max=2000)])
    rating = SelectField('rating', validators=[DataRequired()], coerce=int,
                         choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=5)
    submit = SubmitField('Post review')


class SearchForm(FlaskForm):
    search = StringField('search', validators=[DataRequired()])
    submit = SubmitField('submit')
