import pytest

from fixtures.common_fixtures import api_client
from src.pet import Pet


@pytest.fixture(scope="module")
def pet(api_client):
    return Pet(api_client)
