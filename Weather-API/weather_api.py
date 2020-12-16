import requests
import uvicorn as uvicorn
from fastapi import FastAPI
from httpx import AsyncClient
from requests import request

app = FastAPI()
HTTPS = "https://"
BASE_URL = "api.openweathermap.org/"
PATH = "data/2.5/"
P_WEATHER = "weather?"


# def get_weather():
#     return request(method="get",
#             url="https://api.openweathermap.org/data/2.5/weather?id=498817&units=metric&appid=5035ea0ef5717ae9fcb28a5dcf21178e&lang=ru")

    # async with AsyncClient(app=app, base_url=base_url) as ac:
    #     return await ac.get("/data/2.5/weather?id=498817&units=metric&appid=5035ea0ef5717ae9fcb28a5dcf21178e&lang=ru")


# @app.get("/weather/city")
def get_weather_by_city(city: str, api_key):
    return request(method="get", url=f"{HTTPS}{BASE_URL}{PATH}{P_WEATHER}q={city}&appid={api_key}")


# @app.get("/weather/city")
# async def root(q: str, appid: str):
#     return request(method="get", url=f{protocol}"api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}")




    # return await response
