import requests
from bs4 import BeautifulSoup
import re

website = requests.get('https://webscraper.io/test-sites/e-commerce/allinone/phones/touch')
soup = BeautifulSoup(website.text, 'lxml')

product_name = soup.find_all('a', class_ = 'title')
prices = soup.find_all('h4', class_ = 'pull-right price')
reviews = soup.find_all('p', class_ = 'pull-right')
descriptions = soup.find_all('p', class_ = 'description')
# print(descriptions)
# print(product_name)
# print(prices)
# print(reviews)

products = []
price = []
review = []
description = []
for i in product_name:
    products.append(i.text)
for i in prices:
    price.append(i.text)
for i in reviews:
    review.append(i.text)
for i in descriptions:
    description.append(i.text)
# print(description)
# print(review)
# print(price)
# print(products)

import pandas as pd

table = pd.DataFrame({'Product Name' : products, 'Prices': price, 'Review' : review, 'Description' : description})
print(table)