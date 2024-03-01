import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
URL = os.getenv("URL")
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

parameters = {
    "lat": 26.846695,
    "lon": 80.946167,
    "appid": api_key
}

response = requests.get(URL, params=parameters)
response.raise_for_status()
data = response.json()
# print(data["list"][0]["weather"][0]["id"])
will_rain = False

for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,msg=f"Subject: Weather report\n\nBring umbrella☔.")
