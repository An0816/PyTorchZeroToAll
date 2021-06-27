import requests
from bs4 import BeautifulSoup

# single page scrape

website = requests.get('https://www.britannica.com/biography/Mortimer-J-Adler')
soup = BeautifulSoup(website.text, 'html.parser')
name = soup.select_one('h1').text
description = soup.select_one('.topic-identifier').text
summary = soup.select_one('.topic-paragraph').text.strip()
img = soup.select_one('.fact-box-picture img').attrs['src']
birth = soup.find(attrs = {'data-label': 'born'}).find('dd').get_text(separator = ' | ').split('|')[0]
death = soup.find(attrs = {'data-label': 'died'}).find('dd').get_text(separator = ' | ').split('|')[0]
subject_of_study = soup.find(attrs = {'data-label': 'subjects of study'}).select_one('ul')
subjects = subject_of_study.select('li')
subject = ''
for item in subjects:
    subject += item.text.strip() + ','

print(f'name : {name}\ndescription : {description}\nsummary : {summary}\nbirth : {birth}\ndeath : {death}\nsubjects : {subject}\n')

