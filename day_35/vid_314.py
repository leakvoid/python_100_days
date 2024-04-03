import requests
import os
from twillio.rest import Client

OWM_endpoint = "https://api.openweatherapp.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")

account_sid = "sid"
auth_token = "token"

weather_params = {
    "lat": 55.661011,
    "lon": 39.868069,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(response.status_code)

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body = "It's going to rain today. Remember to bring an umbrella",
        from_ = "+123456",
        to = "+178910"
    )
    print(message.status)