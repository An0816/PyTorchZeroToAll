import requests

from bs4 import BeautifulSoup

website = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(website.text, 'html.parser')

# title of website
title = soup.find('title')
# print(title.text)

# get the first link
link = soup.find('a')
# print(link)

# find : only returns the first element
quote = soup.find(class_='text')
#print(quote)

# scrape many lengths - as an array
links = soup.find_all('a')
#print(links)

#for link in links:
#    print(link.text)


quotes = soup.find_all(class_ = 'text')
# print(quotes)

login_link = soup.find(href = '/login')
#print(login_link)

quote = soup.find(class_='quote')
quote_text = quote.find(class_= 'text')
quote_author = quote.find(class_ = 'author')

# print(quote_text.text)
# print(quote_author.text)

quote_text = soup.select('.text')
print(quote_text)
