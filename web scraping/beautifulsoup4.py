# Scrape list of philosophers in Britannica
# 각각의 author link를 scrape 할 예정

import requests
from bs4 import BeautifulSoup

'''
website = requests.get('https://www.britannica.com/biography/Mortimer-J-Adler')
soup = BeautifulSoup(website.text, 'html.parser')

# get the single page scrape

name = soup.select_one('h1').text
description = soup.select_one('.topic-identifier').text
summary = soup.select_one('.topic-paragraph').text.strip() # first paragraph
image = soup.select_one('.fact-box-picture img').attrs['src'] # image scrape
birth = soup.find(attrs = {'data-label': 'born'}).find('dd').get_text(separator = ' | ').split('|')[0]
death = soup.find(attrs = {'data-label': 'died'}).find('dd').get_text(separator = ' | ').split('|')[0]
subjects_of_study = soup.find(attrs={'data-label': 'subjects of study'}).select_one('ul')
subjects_items = subjects_of_study.select('li')
subjects = ''
for item in subjects_items:
    subjects += item.text.strip() + ', '

print(f'{name}\n{description}\n{image}\n{summary}\n{birth}\n')
# print(subjects)
# print(subjects_of_study)


# print(death)
# print(image)
# print(summary)
# print(name)
# print(description)
'''

## 다른 Author에 적용
try:
    website = requests.get('https://www.britannica.com/biography/William-of-Moerbeke')
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
except:
    print('Something went wrong!')
    
