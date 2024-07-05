import pytest

from src.api_client import ApiClient


@pytest.fixture(scope="module")
def api_client():
    return ApiClient(base_url="https://petstore.swagger.io/v2")
