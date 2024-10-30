#Execise 10
# Use the NewsAPI and the requests module 
# to fetch the daily news related to different 
# topics. Go to: https://newsapi.org/ 
# and explore the various options to 
# build you application

import requests
import json
from key import newsApi

query = input("What would you like to read today: ")
category = input("Enter the category: ")
apikey = newsApi.newsapi

url = f"https://newsapi.org/v2/top-headlines?q={query}&country=in&category={category}&apiKey={apikey}"
r = requests.get(url)
news = json.loads(r.text)

if news['totalResults'] != 0:
    for index,article in enumerate(news['articles'],start=1):
        print(f"Articale {index}: {article['title']}")
else:
    print("No articles found.")

if news['totalResults'] != 0:
    article_no = int(input("Enter artical number you want to read: "))

    if 0 < article_no <= len(news['articles']):
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}")
        print("Ctrl + click on the link to read the full article.")
    else:
        print("Invalid article number.")