import requests
from bs4 import BeautifulSoup

website = requests.get('https://www.britannica.com/topic/list-of-philosophers-2027173')
soup = BeautifulSoup(website.text, 'html.parser')
links = soup.select('.topic-list .md-crosslink')

for link in links[:20]:
    try:
        website = requests.get(link.attrs['href'])
        soup = BeautifulSoup(website.text, 'html.parser')

        name = soup.select_one('h1').text
        description = soup.select_one('.topic-identifier').text
        summary = soup.select_one('.topic-paragraph').text.strip()
        try:
            image = soup.select_one('.fact-box-picture img').attrs['src']
        except AttributeError as error:
            image = 'No Image'
        birth = soup.find(attrs = {'data-label': 'born'}).find('dd').get_text(separator = '|').split('|')[0]
        death = soup.find(attrs = {'data-label': 'died'}).find('dd').get_text(separator = '|').split('|')[0]
        try:
            subjects_of_study = soup.find(attrs = {'data-label': 'subjects of study'}).get_text('ul')
            subject_items = subjects_of_study.select('li')
            subjects = ''
            for item in subject_items:
                subjects += item.text.strip() + ','
        except AttributeError as error:
            subjects = 'Not Found'
        print(f'Name : {name}\nDescription : {description}\nSummary : {summary}\nBirth : {birth}\nDeath : {death}\nSubject of study : {subjects}\n')
        print('======================================================================================')
    except:
        print('No data Available')
        print('====================================================================')

        
