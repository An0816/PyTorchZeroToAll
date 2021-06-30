import requests
from bs4 import BeautifulSoup
import csv

website = requests.get('https://en.wikipedia.org/wiki/List_of_countries_by_average_wage')
soup = BeautifulSoup(website.text, 'html.parser')

wikitable = soup.select_one('.wikitable')

title = wikitable.find('caption')
# print(title.text)

table = wikitable.select('tr')
csv_data = [['index', 'country', '2000', '2005', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']]

index = 0
for row in table[:]:
    index += 1
    data = row.select('td')[1:]
    country = row.select_one('td')
    year1 = data[0].text
    year2 = data[1].text
    year3 = data[2].text
    year4 = data[3].text
    year5 = data[4].text
    year6 = data[5].text
    year7 = data[6].text
    year8 = data[7].text
    year9 = data[8].text
    year10 = data[9].text

    # csv_data.append([index, country, year1, year2, year3, year4, year5, year6, year7, year8, year9, year10])

# with open('countries_by_average_wage.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerows(csv_data)
