import requests
from datetime import datetime
import smtplib
import time

LATITUDE = 26.846695
LONGITUDE = 80.946167

MY_EMAIL = "EMAIL"
MY_PASSWORD = "PASSWORD"

def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = data["iss_position"]["latitude"]
    iss_longitude = data["iss_position"]["longitude"]

    if LATITUDE-5<=iss_latitude<=LONGITUDE+5 and LONGITUDE-5<=iss_longitude<=LONGITUDE+5:
        return True

def is_night():
    parameters = {"lat": LATITUDE, "lng": LONGITUDE}

    response = requests.get(
        url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split(":")[0])
    sunset = int(data["results"]["sunset"].split(":")[0])
    time_now = datetime.now().hour
    if time_now>=sunset or time_now<=sunrise:
        return True

while True:
    time.sleep() 
    if iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(to_addrs=MY_EMAIL,from_addr=MY_EMAIL,msg="Subject:Look up❤\n\nThe ISS is above you.")
