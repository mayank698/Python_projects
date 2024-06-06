import requests
from dotenv import load_dotenv
import os

load_dotenv()


STOCK_API_KEY=os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
STOCK_URL = os.getenv("STOCK_URL")
NEWS_URL = os.getenv("NEWS_URL")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TCS",
    "apikey": STOCK_API_KEY
}

# Previous day price
stock_response = requests.get(url=STOCK_URL, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]    
yesterday = stock_data_list[0]
yesterday_closing_price = yesterday["4. close"]
print(yesterday_closing_price)

# Closing price
day_before_yesterday_data = stock_data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

# Difference between yesterday and day_before yesterday closing price
difference = abs(float(yesterday_closing_price) -
                 float(day_before_yesterday_closing_price))
print(difference)

# Percentage difference
diff_percent = (difference/float(yesterday_closing_price))*100
print(diff_percent)

# Getting news if stock price change is more than 5 percent
if diff_percent > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": "TCS",

    }
    news_response = requests.get(url=NEWS_URL, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]
    print(news_data)
    three_articles = news_data[:3]
    formatted_article = [f"Headline:{article['title']},\nBrief:{
        article['description']}" for article in three_articles]
    print(formatted_article)
