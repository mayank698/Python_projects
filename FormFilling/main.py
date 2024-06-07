from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_FORM = os.getenv("GOOGLE_FORM")

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}

data = requests.get("https://appbrewery.github.io/Zillow-Clone/", headers=header)
soup = BeautifulSoup(data.text, "html.parser")

# list of links
all_links_elements = soup.select(".StyledPropertyCardDataWrapper a")
all_links = [link["href"] for link in all_links_elements]

# list of prices
all_price_elements = soup.select(".PropertyCardWrapper span")
all_prices = [
    price.get_text().replace("/mo", "").split("+")[0]
    for price in all_price_elements
    if "$" in price.text
]

# list of addresses
all_addresses_elements = soup.select(".StyledPropertyCardDataWrapper address")
all_addresses = [
    address.get_text().replace(" | ", (" ")).strip()
    for address in all_addresses_elements
]
print(all_addresses)

# filling google form using selenium
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

for i in range(len(all_links)):
    driver.get(GOOGLE_FORM)
    time.sleep(2)
    address = driver.find_element(
        By.XPATH,
        value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input",
    )
    address.send_keys(all_addresses[i])
    price = driver.find_element(
        By.XPATH,
        value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input",
    )
    price.send_keys(all_prices[i])
    link = driver.find_element(
        By.XPATH,
        value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input",
    )
    link.send_keys(all_links[i])
    submit = driver.find_element(
        By.XPATH,
        value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input",
    )
    submit.click()
