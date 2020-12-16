import pytest
from httpx import AsyncClient
from weather_api import app


@pytest.mark.asyncio
async def test_root():
    # async with AsyncClient(app=app, base_url="http://test/") as ac:
    #     response = await ac.get("/root")

    async with AsyncClient(app=app, base_url="https://api.openweathermap.org/") as ac:
        response = await ac.get("//data/2.5/weather?id=498817&units=metric&appid=5035ea0ef5717ae9fcb28a5dcf21178e&lang=ru")
    # response = await ac.request(method="get",
    #                             url="https://api.openweathermap.org/data/2.5/weather?id=498817&units=metric&appid=5035ea0ef5717ae9fcb28a5dcf21178e&lang=ru")
    assert response.status_code == 200
    assert response.json() == {"message": "Tomato"}