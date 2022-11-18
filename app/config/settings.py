from dynaconf import FlaskDynaconf
from flask import Flask
from flask_marshmallow import Marshmallow

from app.config.db import init_db
from app.config.router import init_routers


def init_settings(app: Flask):
    FlaskDynaconf(app, ENV_FOR_DYNACONF=app.config.get("ENV"))


def init_serializers(app: Flask):
    Marshmallow(app)


def init_app() -> Flask:
    app = Flask(__name__)
    init_settings(app)
    init_serializers(app)
    init_db(app)
    init_routers(app)
    return app
