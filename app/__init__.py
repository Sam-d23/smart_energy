from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app():
    """
    Create and configure the Flask application.

    This function initializes a Flask application, configures it using
    the settings from the `Config` class, and sets up the database,
    migration, and login manager. It also registers blueprints for the
    application's routes.

    Returns:
        Flask: The configured Flask application.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    with app.app_context():
        from . import routes, auth, energy

        app.register_blueprint(routes.routes)
        app.register_blueprint(auth.bp)
        app.register_blueprint(energy.bp)

    return app
