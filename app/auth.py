from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from .forms import LoginForm, RegistrationForm
from .models import User, db


bp = Blueprint('auth', __name__)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle user registration.

    This view function handles the registration process for new users.
    It validates the registration form, creates a new user, hashes the
    password, and saves the user to the database. Upon successful
    registration, it flashes a success message and redirects the user
    to the login page.

    Returns:
        str: The rendered registration template if the form is not
        submitted or is invalid. Redirects to the login page on success.
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle user login.

    This view function handles the login process for users. It validates
    the login form, checks the user's credentials, and logs them in if
    the credentials are correct. If the credentials are invalid, it
    flashes an error message and redirects the user back to the login page.

    Returns:
        str: The rendered login template if the form is not submitted
        or is invalid. Redirects to the dashboard on successful login.
    """
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', 'danger')
            return redirect(url_for('auth.login'))
        login_user(user)
        return redirect(url_for('energy.dashboard'))
    return render_template('login.html', form=form)


@bp.route('/logout')
@login_required
def logout():
    """
    Handle user logout.

    This view function logs out the currently logged-in user, flashes an
    informational message, and redirects the user to the login page.

    Returns:
        werkzeug.wrappers.response.Response: Redirects to the login page.
    """
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))
