import pytest

from fixtures.common_fixtures import api_client
from src.store import Store


@pytest.fixture(scope="module")
def store(api_client):
    return Store(api_client)
