import requests
from bs4 import BeautifulSoup

# scraping할 website 불러오기
website = requests.get('https://quotes.toscrape.com/')
# print(website) # Response [200]
# print(website.text) # website의 whole html을 불러올 수 있음

soup = BeautifulSoup(website.text, 'html.parser')
# 이렇게 해놓고 나서야 extract 를 할 수 있음

# title 불러오기
title = soup.find('title')
# print(title) # <title>Quotes to Scrapes</title>
# print(title.text) # Quotes to Scrape

# 첫번째 link를 불러오기
link = soup.find('a')
# print(link) # 이거 안돼..

# class 가져오기
quote = soup.find(class_='text')
# print(quote)

# 여러개 link를 가져오고 싶을 때는 findall method 사용 (find - first element만 가져옴)
links = soup.find_all('a')
# print(links) 
# for link in links:
#     print(link.text) # link만 따로 가져오는 것


quotes = soup.find_all(class_= 'text')
# print(quotes)

login_link = soup.find(href= '/login')
# print(login_link.text)

# quote 랑 author 가져오기
quote = soup.find(class_= 'quote') # 일단 div 를 가져오고
quote_text = quote.find_all(class_='text')
quote_author = quote.find_all(class_='author')

# print(quote_text.text)
# print(quote_author.text)

#####################################################################################

quote_text = soup.select('.text') # css selector
# print(quote_text)

# select_one : 하나만 가져옴
# select : find_all

##################################################

'''
quotes = soup.select('.quote') # class quote를 의미
for quote in quotes:
    text = quote.select_one('.text')
    author = quote.select_one('.author')
    tags = quote.select('.tag') # tag가 여러개라서 그냥 select 써줌
    print(text.text)
    print(author.text)
    for tag in tags:
        print(tag.text)
    print('==================================================')

'''

###########################################################

# next_button = soup.select_one('.next > a') # next page가 있는지 확인 : next class의 a href를 select
page = 1
next_button = True
while next_button:
    website = requests.get('https://quotes.toscrape.com/page/' + str(page))
    soup = BeautifulSoup(website.text, 'html.parser')
    next_button = soup.select_one('.next > a')
    quotes = soup.select('.quote')
    for quote in quotes:
        text = quote.select_one('.text')
        author = quote.select_one('.author')
        tags = quote.select('.tag')
        print(text.text)
        print(author.text)
        for tag in tags:
            print(tag.text)
        print('===================================================')
    print('scraped page ' + str(page))
    page += 1

