import os


class Config:
    """
    Configuration class for the application, storing essential settings.

    Attributes:
    -----------
    SECRET_KEY : str
        A secret key for the application, used for session management and
        security purposes. It is fetched from the environment variable
        'SECRET_KEY', or defaults to 'your_secret_key' if the variable
        is not set.

    SQLALCHEMY_DATABASE_URI : str
        The database connection URI for SQLAlchemy. It is fetched from the
        environment variable 'DATABASE_URI', or defaults to a MySQL database
        URI if the variable is not set. The default URI points to a MySQL
        database running locally with the provided credentials.

    SQLALCHEMY_TRACK_MODIFICATIONS : bool
        A configuration setting to disable the tracking of modifications to
        objects in the SQLAlchemy session, which is unnecessary and incurs
        additional overhead. Set to False by default.
    """

    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URI',
        'mysql+pymysql://username:your_password@localhost:3306/energy_db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
