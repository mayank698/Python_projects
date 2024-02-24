from datetime import *
import pandas
import random
import smtplib

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

today = (datetime.now().month, datetime.now().day)
data = pandas.read_csv("Automated_wisher/birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"Automated_wisher/letter_templates/letter_{
        random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]",birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL,MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs=birthday_person["email"],msg=f"Subject:Happy Birthday\n\n{contents}")
