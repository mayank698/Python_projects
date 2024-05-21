import requests
import os
from dotenv import load_dotenv

load_dotenv()
SHEETY = os.getenv("SHEETY")
BEARER = os.getenv("SHEETY_BEARER")


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        headers = {
            "Authorization": f"Bearer {BEARER}"
        }
        response = requests.get(url=SHEETY, headers=headers)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            headers = {
                "Authorization": f"Bearer {BEARER}",
                "Content-Type": "application/json"
            }
            response = requests.put(
                url=f"{SHEETY}/{city['id']}",
                headers=headers,
                json=new_data
            )
            print(response.text)
