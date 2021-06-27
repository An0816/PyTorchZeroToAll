import requests
from bs4 import BeautifulSoup
import csv

website = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(website.text, 'html.parser')

title = soup.select_one('title').text
# print(title)

link = soup.find(href = '/login').text
# print(link)

links = soup.find_all('a')
# print(links)

# for link in links:
    # print(link.text)

quote = soup.find(class_ = 'text').text
# print(quote)

quotes = soup.find_all(class_ = 'text')

# for quote in quotes:
    # print(quote.text)

author = soup.find(class_ = 'author').text
# print(author)

authors = soup.find_all(class_ = 'author')

# for author in authors:
#     print(author.text)

######################################################################
'''
quote = soup.select('.quote')
for item in quote:
    quotes = item.select_one('.text')
    authors = item.select_one('.author')
    tags = item.select('.tags')
    print(quotes.text)
    print(authors.text)
    for tag in tags:
        print(tag.text)
    print('======================================================')
'''

# next_button = soup.select_one('.next')
# print(next_button.text)

next_button = True
page = 1
while(next_button):
    website = requests.get('https://quotes.toscrape.com/page/' + str(page))
    soup = BeautifulSoup(website.text, 'html.parser')
    next_button = soup.select_one('.next')
    quotes = soup.select('.quote')
    print(f'page: {page}')
    for quote in quotes:
        text = quote.select_one('.text')
        author = quote.select_one('.author')
        tags = quote.select('.tags')
        print(text.text)
        print(author.text)
        for tag in tags:
            print(tag.text)
        print('================================================================')
    page += 1
    

