import requests
import os
from dotenv import load_dotenv

load_dotenv()
SHEETY = os.getenv("SHEETY")

class DataManager:
    def __init__(self):
        self.destination_data={}
        
    def get_destination_data(self):
        response = requests.get(url=SHEETY)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price":{
                    "iataCode":city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY}/{city['id']}",json=new_data)
            print(response.text)