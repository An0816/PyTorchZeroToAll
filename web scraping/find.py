import requests
from bs4 import BeautifulSoup
import re

website = requests.get('https://webscraper.io/test-sites/e-commerce/allinone/phones/touch')
soup = BeautifulSoup(website.text, 'lxml')

#find : search throughout the html
# parameter : tag, attrs, comments,,

# print(soup.find('div', {'class': 'container test-site'}))
'''
print(soup.find('h4', {'class' : 'pull-right price'}).string)
print(soup.find('h4', class_ = 'pull-right price').string)
'''
# class attr의 경우 많이 쓰여서 이렇게 할 수 있는 것

# Find_all
# always,, tag 다음에 attribute


price = soup.find_all('h4', class_ = 'pull-right price')
name = soup.find_all('a', class_ = 'title')
review = soup.find_all('p', class_ = 'pull-right')


'''
print(soup.find_all(['h4', 'p', 'a'])) # tag

print(soup.find_all(id = True)) # id 를 attribute로 가지고 있는 것들을 다 return

print(soup.find_all(string = 'Iphone'))
print(soup.find_all(string = 'Nokia 123'))

print(soup.find_all(string = re.compile('Nokia')))

print(soup.find_all(class_ = re.compile('pull'))) # pull 과 matching되는거 다 return

print(soup.find_all('p', class_ = re.compile('pull')))

print(soup.find_all('p', class_ = re.compile('pull'), limit = 3)) # first 3개만 리턴
'''

