"""
    #Day 89 is about Request module in python...
        The Python Requests module is an HTTP library that 
        enables developers to send HTTP requests in Python. 
        This module enables you to send HTTP requests using 
        Python code and makes it possible to interact with 
        APIs and web services.

    bs4 module:
        By using bs4 module we can beautify the code provided 
        by requests...
"""
import requests# importing requests module
from bs4 import BeautifulSoup

url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
r = requests.get(url) # using .get method to get code of static html page
# print(req.text) # printing the provided code...

# the code is unreadable

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())

for li in soup.find_all("link"):
    print(li)