import aiohttp
import pytest
import pytest_asyncio
from fastapi.testclient import TestClient

from app.main import app

API_BASEURL = "http://localhost:8000"

client = TestClient(app)


@pytest.mark.parametrize("url", ["/annotators", "/skills", "/distribution"])
def test_get_list_of_items(url):
    response = client.get(url)
    assert response.status_code == 200
