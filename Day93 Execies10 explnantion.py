#Exercise 10
# Use the NewsAPI and the requests module 
# to fetch the daily news related to different 
# topics. Go to: https://newsapi.org/ 
# and explore the various options to 
# build you application


# Exercise 10: News Fetcher Using NewsAPI

"""
This program fetches daily news articles based on user-provided keywords by utilizing the NewsAPI service 
and the `requests` module to make HTTP requests. It offers an interactive experience where users can choose 
a topic, view a list of articles, and select one to read in more detail.

1. Imports and API Key:
   - The program imports the `requests` module to handle HTTP requests and `json` to process JSON data.
   - The API key is stored in a separate module called `key` to enhance security by keeping sensitive 
     information like `NewsApi.newsapi` private.

2. User Input for Query:
   - A user is prompted to input a keyword (e.g., "technology," "sports") to specify the topic of news 
     they are interested in.
   - This `query` is then used to construct the request URL, with the `apikey` retrieved from the `key` module.

3. Request to NewsAPI:
   - The program builds the request URL using the base URL from NewsAPI, the user’s search keyword (`q`), 
     and the API key (`apiKey`).
   - It sends a `GET` request to the API using `requests.get(url)` and decodes the response JSON using 
     `json.loads(r.text)`.

4. Displaying Articles:
   - If `totalResults` (the number of articles returned by the API) is non-zero, the program enters a loop 
     where it enumerates and prints the titles of the articles.
   - Each article is prefixed with a number for easy selection.

5. Selecting an Article to Read:
   - After listing the articles, the user can select an article by inputting its corresponding number.
   - The program verifies that the chosen number is within the valid range of articles and displays the title, 
     description, and URL of the selected article.
   - For a better user experience, a message prompts the user to Ctrl+click the URL to read the full article online.

6. Error Handling:
   - If `totalResults` is zero, the program informs the user that no articles were found.
   - If an invalid article number is entered, an "Invalid article number" message is displayed.

Dependencies: 
   Ensure that the `requests` library is installed and that the `NewsApi` key is correctly configured in 
   the `key` module. Also, sign up on https://newsapi.org/ to obtain an API key.
"""


import requests
import json
from key import NewsApi

query = input("What would you like to read today: ")
# category = input("Enter the category: ")
apikey = NewsApi.newsapi

url = f"https://newsapi.org/v2/top-headlines?q={query}&apiKey={apikey}"
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