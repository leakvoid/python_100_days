import requests
from datetime import datetime, timedelta

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "SOGATAAE5OGJCZBD"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

NEWS_API_KEY = "NEWS_API_KEY"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
r = requests.get(STOCK_ENDPOINT, params=stock_params)

two_days_ago = datetime.now() - timedelta(4)
t1 = datetime.strftime(two_days_ago, '%Y-%m-%d')
closing_1 = float(r.json()['Time Series (Daily)'][t1]['4. close'])
print("closing_1: ", closing_1)

#TODO 2. - Get the day before yesterday's closing stock price
three_days_ago = datetime.now() - timedelta(5)
t2 = datetime.strftime(three_days_ago, '%Y-%m-%d')
closing_2 = float(r.json()['Time Series (Daily)'][t2]['4. close'])
print("closing_2: ", closing_2)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(closing_1 - closing_2)
print("difference: ", difference)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
ratio = closing_1 / closing_2
if ratio > 1:
    ratio = 1 / ratio
percentage = (1 - ratio) * 100
print("percentage: ", percentage)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage > 5:
    print("Get News")

## STEP 2: https://newsapi.org/ 
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
url = NEWS_ENDPOINT + f"?q=tesla&from={t1}&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
r = requests.get(url)
# import json
# with open('news.json', 'w') as f:
#    json.dump(r.json(), f)


#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
articles = r.json()['articles'][:3]


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
formatted_articles = [(item['title'], item['description']) for item in articles]
print(formatted_articles)


#TODO 9. - Send each article as a separate message via Twilio. 
from twilio.rest import Client

TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"
VIRTUAL_TWILIO_NUMBER = "your virtual twilio number"
VERIFIED_NUMBER = "your own phone number verified with Twilio"

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

for article in formatted_articles:
    message = client.messages.create(
        body = article,
        from_ = VIRTUAL_TWILIO_NUMBER,
        to = VERIFIED_NUMBER
    )

#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

