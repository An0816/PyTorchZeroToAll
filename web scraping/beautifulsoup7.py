import requests
from bs4 import BeautifulSoup
import csv

website = requests.get('https://www.ebay.com/sch/i.html?&_nkw=watch')
soup = BeautifulSoup(website.text, 'html.parser')

items = soup.select('.srp-results .s-item')

for item in items:
    title = item.select_one('.s-item__title').text

    price = item.select_one('.s-item__price').text
    try:
        top_rate = item.select_one('.s-item__etrs-text').text
    except:
        top_rate = 'Not Recommended'
    shipping = item.select_one('.s-item__shipping').text
    location = item.select_one('.s-item__location').text
    try:
        sold = item.select_one('.s-item__hotness').text
    except:
        sold = 'Not Sold'
    
    print(f'title : {title}\nprice : {price}\nTop_rate : {top_rate}\nShipping : {shipping}\nLocation : {location}\nSold : {sold}\n')


for page in range(1, 6):
    print('page : ' + str(page))
    website = requests.get('https://www.ebay.com/sch/i.html?_nkw=watch&_pgn=' + str(page))
    soup = BeautifulSoup(website.text, 'html.parser')
    items = soup.select('.srp-results .s-item')

    for item in items:
        title = item.select_one('.s-item__title').text

        price = item.select_one('.s-item__price').text
        try:
            top_rate = item.select_one('.s-item__etrs-text').text
        except:
            top_rate = 'Not Recommended'
        shipping = item.select_one('.s-item__shipping').text
        location = item.select_one('.s-item__location').text
        try:
            sold = item.select_one('.s-item__hotness').text
        except:
            sold = 'Not Sold'
        
        print(f'title : {title}\nprice : {price}\nTop_rate : {top_rate}\nShipping : {shipping}\nLocation : {location}\nSold : {sold}\n')
    print('===============================================================')
