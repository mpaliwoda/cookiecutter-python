import pytest

from app import create_app

_app = create_app(testing=True)


@pytest.fixture
def test_client():
    with _app.test_client() as client:
        yield client
