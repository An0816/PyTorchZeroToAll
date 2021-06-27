# scraping a movie from IMDB

import requests
from bs4 import BeautifulSoup
import csv

website = requests.get('https://www.imdb.com/title/tt0770828/')
soup = BeautifulSoup(website.text, 'html.parser')

# print(soup.title.text)
title = soup.select_one('.title_wrapper > h1').contents[0]
# print(title.split('(')[0])
print(title) 

runtime = soup.select_one('time').text.strip()
print(runtime)

# plot = soup.find(attrs = {')
# print(plot)

plot = soup.find(attrs = {'data-testid': 'plot'})
print(plot)