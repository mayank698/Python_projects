from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
import sheety

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]
    data_manager.city_codes = flight_search.get_destination_code(city_names)
    data_manager.update_destination_codes()
    sheet_data = data_manager.get_destination_data()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    print(flight.price)
    if flight is None:
        continue

print("Welcome to the flight club.\n")
first_name = input("Enter your first name: ").title()
last_name = input("Enter your last name: ").title()

email1 = "email1"
email2 = "email2"

while email1 != email2:
    email1 = input("Enter your email: ")
    if email1.lower() == "quit" or email1.lower() == "exit":
        exit()
    email2 = input("Re enter your email: ")
    if email2.lower() == "quit" or email2.lower() == "exit":
        exit()
print("Congratulations. You are in the club")
sheety.post_new_row(first_name, last_name, email1)
