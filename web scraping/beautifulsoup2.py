# scrape table from wikipedia

import requests
from bs4 import BeautifulSoup

website = requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')

soup = BeautifulSoup(website.text, 'html.parser')

first_table = soup.select_one('.wikitable')
print(first_table)


table_rows = first_table.select('tr')[1:] # 위에 제목부분 안가져오게 하려고 [1:]
# print(table_rows[:3])
for row in table_rows[:5]:
    rank = row.find('th').text.strip() #whitespace 없애려고 strip()
    table_data = row.select('td')
    name = table_data[0].find('a').text # first element
    population = table_data[1].text
    percentage = table_data[2].text
    date = table_data[3].text
    source = table_data[4].text.strip().split('[')[0]
    print(name)
    print(population)
    print(percentage)
    print(date)
    print(source)
    print('================================================')
