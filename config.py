import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv(
            'DATABASE_URI',
            'mysql+pymysql://username:your_password@localhost:3306/energy_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
