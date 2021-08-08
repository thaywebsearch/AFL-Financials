#Import the modules necessary for this program

import bs4
import requests
from bs4 import BeautifulSoup

url = requests.get('https://finance.yahoo.com/quote/AFL?p=AFL')

soup = bs4.BeautifulSoup(url.text, features="html.parser")

price = soup.find_all("div", {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text

print(price)


