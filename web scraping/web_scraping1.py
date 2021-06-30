import requests
from bs4 import BeautifulSoup

website = requests.get('https://webscraper.io/test-sites')
soup = BeautifulSoup(website.text, 'lxml') 

# tags : purple
# navigable string (string) : black
# attribute : yellow  // 추가할 수 있음
# commnet : green // special type of navigable string


header = soup.select('header')
# ?tag = soup.header.p.string

tag = soup.header.a.attrs
# print(tag['data-toggle'])
tag['attribute new'] = 'this is a new attribute' # attribute 추가
# print(tag)
