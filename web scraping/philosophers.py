import requests
from bs4 import BeautifulSoup
import csv


# website = requests.get('https://www.britannica.com/topic/list-of-philosophers-2027173')
try:
    website = requests.get('https://www.britannica.com/biography/Allan-Bloom')
    soup = BeautifulSoup(website.text, 'html.parser')

    name = soup.select_one('h1').text
    description = soup.select_one('.topic-identifier').text
    summary = soup.select_one('.topic-paragraph').text
    try:
        image = soup.select_one('.fact-box-picture img').attrs['src']
    except AttributeError as error:
        image = 'No Image'
    birth = soup.find(attrs = {'data-label': 'born'}).get_text(separator = '|').split('|')[1]
    death = soup.find(attrs = {'data-label': 'died'}).get_text(separator = '|').split('|')[1]
    try:
        subject_of_study = soup.find(attrs = {'data-label': 'subjects of study'}).select_one('ul')
        subjects_item = subject_of_study.select('li')
        subjects = ''
        for item in subjects_item:
            subjects += item.text.strip() + ', '
    except AttributeError as error:
        subjects = 'Not Found'

    print(f'Name : {name}\nDescription : {description}\nSummary : {summary}\nBirth : {birth}\nDeath : {death}\nSubjects : {subjects}\n')
except:
    print('Something went wrong!')
