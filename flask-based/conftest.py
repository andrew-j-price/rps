import pytest
from app import my_app


@pytest.fixture
def app():
    app = my_app()
    app.debug = True
    return app
