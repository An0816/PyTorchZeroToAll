import requests
from bs4 import BeautifulSoup
import csv

website = requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')
soup = BeautifulSoup(website.text, 'html.parser')
csv_data = [['rank', 'country', 'population', 'percentage', 'source']]

wikitable = soup.select_one('.wikitable')
table = wikitable.select('tr')[1:]

for row in table[:-1]:
    rank = row.select_one('th').text.strip()
    data = row.select('td')
    name = data[0].select_one('a').text
    population = data[1].text
    percentage = data[2].text
    date = data[3].text
    source = data[4].text.strip().split('[')[0]
    csv_data.append([rank, name, population, percentage, date, source])


with open('wikipractice.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)

