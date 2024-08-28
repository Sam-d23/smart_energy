from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db, login_manager


class User(UserMixin, db.Model):
    """
    User model for managing user data and authentication.

    Attributes:
    -----------
    id : int
        Unique identifier for the user, primary key.

    username : str
        Username of the user, unique and required.

    password_hash : str
        Hash of the user's password, required.

    energy_data : sqlalchemy.orm.relationships.RelationshipProperty
        Relationship to the EnergyData model, indicating a one-to-many
        relationship with the user as the parent.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    energy_data = db.relationship('EnergyData', backref='user', lazy=True)

    def set_password(self, password):
        """
        Set the password hash for the user.

        Parameters:
        -----------
        password : str
            The plain-text password to hash and set.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Check if the provided password matches the stored hash.

        Parameters:
        -----------
        password : str
            The plain-text password to verify.

        Returns:
        --------
        bool
            True if the password matches the hash, False otherwise.
        """
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    """
    Load a user by their unique identifier.

    Parameters:
    -----------
    user_id : int
        The unique identifier of the user.

    Returns:
    --------
    User
        The User object associated with the given user_id,
        or None if not found.
    """
    return User.query.get(int(user_id))


class EnergyData(db.Model):
    """
    Model for storing energy consumption data.

    Attributes:
    -----------
    id : int
        Unique identifier for the energy data record, primary key.

    timestamp : datetime
        Timestamp of the data record, defaults to the current UTC time.

    usage : float
        Energy usage value recorded.

    temperature : float
        Temperature value recorded.

    humidity : float
        Humidity value recorded.

    user_id : int
        Foreign key referencing the User model, indicating which user the
        data belongs to.
    """
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    usage = db.Column(db.Float, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
