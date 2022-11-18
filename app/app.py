from app.config.settings import init_app
from app.config.db import database

app = init_app()


@app.cli.command()
def create_db():
    """Create database"""
    database.create_all()


@app.cli.command()
def drop_db():
    """Cleans database"""
    database.drop_all()


