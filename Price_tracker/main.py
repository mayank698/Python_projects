import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
URL = os.getenv("URL")
BUY_PRICE = os.getenv("BUY_PRICE")

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}
url = URL

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
title = soup.find(id="productTitle").get_text().split(",")[0]
print(title)
price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("₹")[1]
price_as_float = float(price_without_currency.replace(",", ""))

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8"),
        )
