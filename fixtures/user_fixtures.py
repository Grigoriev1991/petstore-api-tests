import pytest

from fixtures.common_fixtures import api_client
from src.user import User


@pytest.fixture(scope="module")
def user(api_client):
    return User(api_client)
