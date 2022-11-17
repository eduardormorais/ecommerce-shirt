from app.modules.core.exceptions import InvalidData
from app.config.settings import init_app
from app.config.db import database
from flask import jsonify

app = init_app()


@app.cli.command()
def create_db():
    """Create database"""
    database.create_all()


@app.cli.command()
def drop_db():
    """Cleans database"""
    database.drop_all()


@app.errorhandler(InvalidData)
def invalid_data_user(e):
    return jsonify(e.to_dict()), e.status_code
