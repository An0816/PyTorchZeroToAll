import requests
from bs4 import BeautifulSoup
import csv

website = requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')
soup = BeautifulSoup(website.text, 'html.parser')

# table = soup.select_one('.wikitable')

# columns = table.select('tr')[0]
# print(columns.text) 
# rows = table.select('tr')[1:]
# print(rows)
'''
wikitable = soup.select_one('.wikitable')
table_rows = wikitable.select('tr')
for table in table_rows[1:]:
    rank = table.select_one('th').text.strip()
    data = table.select_one('td')
    country = data[0].find('a').text
    print(country)
'''

wikitable = soup.select_one('.wikitable')

table_rows = wikitable.select('tr')[1:]

for row in table_rows[:-1]:
    rank = row.find('th').text.strip()
    data = row.select('td')
    name = data[0].find('a').text
    population = data[1].text
    percentage = data[2].text
    date = data[3].text
    source = data[4].text.strip().split('[')[0]

    print(name)
    print(population)
    print(percentage)
    print(date)
    print(source)
    print('=====================================================')