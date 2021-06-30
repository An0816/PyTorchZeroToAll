import requests
from bs4 import BeautifulSoup
import pandas as pd

website = requests.get('https://www.nfl.com/standings/league/2020/REG')
soup = BeautifulSoup(website.text, 'lxml')

table = soup.find('div', class_ = "d3-l-col__col-12 flex-wrap")
title = table.find(class_ = 'd3-o-standings--table-header').text.strip()

head = soup.find('thead')
columns = head.find_all('th')

col_lst = []
for col in columns:
    col_lst.append(col.text.strip())

body = soup.find('tbody')
rows = body.find_all('tr')

df = pd.DataFrame(columns = col_lst)
for row in rows:
    row_data = row.find_all('td')
    row_lst = [tr.text for tr in row_data]
    length = len(df)
    df.loc[length] = row_lst

df.to_csv('nfl.csv')
