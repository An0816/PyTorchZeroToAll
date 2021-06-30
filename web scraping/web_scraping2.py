import requests
from bs4 import BeautifulSoup
import pandas as pd

website = requests.get('https://webscraper.io/test-sites/e-commerce/allinone/phones/touch')
soup = BeautifulSoup(website.text, 'lxml')

boxes = soup.find_all('div', class_ = 'col-sm-4 col-lg-4 col-md-4')[6] # list 로 정렬
# print(boxes[2])

# print(boxes.find('p', class_ = 'description').text)

box2 = soup.find_all('ul', class_ = 'nav', id = 'side-menu')[0]

print(box2.find_all('li')[2].text.strip())
