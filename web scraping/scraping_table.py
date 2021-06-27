import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

website = requests.get('https://www.worldometers.info/world-population/')
soup = BeautifulSoup(website.text, 'html.parser')

table = soup.find('table', class_ = 'table table-striped table-bordered table-hover table-condensed table-list')

header = table.find_all('th')

headers = []
for i in header:
    headers.append(i.text)


df = pd.DataFrame(columns = headers)

for j in table.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [tr.text for tr in row_data]
    length = len(df)
    df.loc[length] = row


# data = table.find_all('tr')[1:]
# row =[]
# for i in data:
#     # row_data = i.find_all('td')

#     # row = [tr.text for tr in row_data]
#     data_list = i.find_all('td')
#     for j in data_list:
#         row.append(j.text)
#     # data_list = [tr.text for tr in i.find_all('td')]

# print(row)

df.to_csv('scraped2.csv', mode = 'w')

