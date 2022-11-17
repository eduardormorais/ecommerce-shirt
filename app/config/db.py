from flask import Flask
from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()


def init_db(app: Flask):
    database.init_app(app)
