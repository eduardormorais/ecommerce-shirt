import pytest as pytest
from app.app import init_app
import os

from app.config.db import database


@pytest.fixture(scope="session")
def flask_app():
    os.environ["FLASK_ENV"] = "testing"
    app = init_app()
    app.test_request_context().push()
    database.create_all()
    client = app.test_client()
    return client
