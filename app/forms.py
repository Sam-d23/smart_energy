from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class RegistrationForm(FlaskForm):
    """
    Form for user registration.

    Attributes:
    -----------
    username : StringField
        A field for the user's username. Requires input with a length
        between 4 and 64 characters.

    password : PasswordField
        A field for the user's password. Requires input with a minimum
        length of 8 characters.

    password2 : PasswordField
        A field for repeating the password. Must match the value of the
        'password' field.

    submit : SubmitField
        A submit button for the form labeled 'Register'.
    """
    username = StringField(
            'Username', validators=[DataRequired(), Length(min=4, max=64)])
    password = PasswordField(
            'Password', validators=[DataRequired(), Length(min=8)])
    password2 = PasswordField(
            'Repeat Password',
            validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    """
    Form for user login.

    Attributes:
    -----------
    username : StringField
        A field for the user's username. Requires input.

    password : PasswordField
        A field for the user's password. Requires input.

    submit : SubmitField
        A submit button for the form labeled 'Login'.
    """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
