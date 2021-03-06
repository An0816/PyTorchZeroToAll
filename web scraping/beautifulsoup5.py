# scrape each philosopher one by one
import requests
from bs4 import BeautifulSoup
import csv

page = requests.get('https://www.britannica.com/topic/list-of-philosophers-2027173')
soup = BeautifulSoup(page.text, 'html.parser')
links = soup.select('.topic-list .md-crosslink')

for link in links[:8]:
    try:
        website = requests.get(link.attrs['href'])
        soup = BeautifulSoup(website.text, 'html.parser')

        # get the single page scrape

        name = soup.select_one('h1').text
        description = soup.select_one('.topic-identifier').text
        summary = soup.select_one('.topic-paragraph').text.strip() # first paragraph
        try: 
            image = soup.select_one('.fact-box-picture img').attrs['src'] # image scrape
        except AttributeError as error:
            image = None # image가 없으면 None으로 그냥 하겠다
        birth = soup.find(attrs = {'data-label': 'born'}).find('dd').get_text(separator = ' | ').split('|')[0]
        death = soup.find(attrs = {'data-label': 'died'}).find('dd').get_text(separator = ' | ').split('|')[0]
        try:
            subjects_of_study = soup.find(attrs={'data-label': 'subjects of study'}).select_one('ul')
            subjects_items = subjects_of_study.select('li')
            subjects = ''
            for item in subjects_items:
                subjects += item.text.strip() + ', '
        except AttributeError as error:
            subjects = 'no data'

        print(f'{name}\n{description}\n{image}\n{summary}\n{birth}\n{death}\n{subjects}\n')
        print('=========================================================================')
    except:
        print('Something went wrong!')
        print('======================================================================')
        
