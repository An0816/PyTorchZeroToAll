import requests
from bs4 import BeautifulSoup
from decimal import Decimal

query = input('Enter product: ')
free_shipping = input('Enter Free Shipping : ')
max_price = Decimal(input('Enter Maximum price : '))

for page in range(1, 6):
    print('page : ' + str(page))
    if free_shipping == 'Y' or free_shipping == 'y':
        website = requests.get('https://www.ebay.com/sch/i.html?_nkw=' + query + 'rt=nc&LH_FS=1' + '&_pgn=' + str(page))
        soup = BeautifulSoup(website.text, 'html.parser')
    else:
        website = requests.get('https://www.ebay.com/sch/i.html?_nkw=' + query + '&_pgn=' + str(page))
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
