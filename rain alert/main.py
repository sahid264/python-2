import requests
from twilio.rest import Client


OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "a20414d22cde2824ba6cd2572ace1b29"
account_sid = 'ACd44e3af3d24daf28ac513279dddefd34'
auth_token = "a63b9826cf626e0c91695d7045cfb9f1"

weather_params = {
    "lat":10.850516,
    "lon":76.271080,
    "appid":api_key,
    "cnt":4,
}



response = requests.get(OWN_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code)< 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+14638886362",
        to="+919961607841"
    )
    print(message.status)

    

