import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_item():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/items/", json={"name": "Test Item", "description": "Test Description"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item"
    assert response.json()["description"] == "Test Description"

@pytest.mark.asyncio
async def test_read_items():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
