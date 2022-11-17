from app.modules.user.router import bp as bp_user
from flask import Flask


def init_routers(app: Flask):
    app.register_blueprint(bp_user)
