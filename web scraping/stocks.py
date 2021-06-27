import requests
from bs4 import BeautifulSoup
import pandas as pd

website = requests.get('https://www.marketwatch.com/investing/stock/aapl')
soup = BeautifulSoup(website.text, 'lxml')


company = [soup.find('h1', class_ = 'company__name').text]
dollar = soup.find('sup', class_ = 'character').text
price_ = soup.find('bg-quote', class_ = 'value').text
price = [dollar + price_]

close = [soup.find('td', class_ = 'table__cell u-semi').text.strip()]

range_header = soup.find_all('div', class_ = 'range__header')[2]
primary = range_header.find_all('span', class_ = 'primary')
low = primary[0].text
high = primary[1].text

week_range = [low + ' to ' + high]

analyst = [soup.find('li', class_ = 'analyst__option active').text]

stock = pd.DataFrame({'Company': company, 'Stock Price': price, 'Close Price': close, '52 Week Range': week_range, 'Analyst Rating': analyst})
