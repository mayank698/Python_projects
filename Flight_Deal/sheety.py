import requests
import os
from dotenv import load_dotenv

load_dotenv()
BEARER = os.getenv("SHEETY_BEARER")
USERNAME = os.getenv("USERNAME_SHEETY")

PROJECT = "flightDeals"
SHEET = "users"

base_url = "https://api.sheety.co"


def post_new_row(first_name, last_name, email):
    endpoint_url = f"/{USERNAME}/{PROJECT}/{SHEET}"
    url = base_url+endpoint_url

    headers = {
        "Authorization": f"Bearer {BEARER}",
        "Content-Type": "application/json",
    }

    body = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email
        }
    }
    response = requests.post(url=url, headers=headers, json=body)
    response.raise_for_status()
    print(response.text)
