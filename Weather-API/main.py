import asyncio

# import requests
from fastapi import requests, FastAPI, Request
from fastapi.testclient import TestClient
from requests import request

import weather_api

app = FastAPI()


if __name__ == '__main__':
    a = asyncio.run(get_weather_by_city(city="Москва", api_key="5035ea0ef5717ae9fcb28a5dcf21178e"))
    # //a = request(method="get", url="https://api.openweathermap.org/data/2.5/weather?id=498817&units=metric&appid=5035ea0ef5717ae9fcb28a5dcf21178e&lang=ru")
    print(a.text)
