import urllib2, sys
from bs4 import BeautifulSoup
import time
import matplotlib.pyplot as plt
import numpy as np


# webscraper config
quote_page = 'https://coinmarketcap.com/currencies/ethereum/'
hdr = {'User-Agent': 'Mozilla/5.0'}
req = urllib2.Request(quote_page,headers=hdr)

# initial variables
run = True
count = 0

buy_sell_cash = 100.0
transaction_rate = 0.04

capital = 1000.0
ether = 0.0

current_price = 0
price = 0

price_array = []
time_array = [] 


while(run):

	page = urllib2.urlopen(quote_page)
	soup = BeautifulSoup(page, 'html.parser')
	name_box = soup.find('span', attrs={'class': 'text-large2'})
	current_price = float(name_box.text.strip())
	# print current_price

	rate = (price - current_price)
	# print price - current_price

	price = current_price
	price_array.append(price)
	time_array.append(count)

	if (count > 1000):
		run = False

	count = count + 1

plt.plot(time_array,price_array)
plt.show()

#buy from market everytime
def buyCrypto(price):
	global ether
	global capital
	ether = ether + buy_sell_cash/price
	transaction = buy_sell_cash*transaction_rate
	capital = capital - transaction - buy_sell_cash


#sell from market
def sellCrypto(price):
	global ether
	global capital
	sell_ether = ether*0.5
	ether = ether - sell_ether
	transaction = sell_ether*price*transaction_rate
	capital = capital - transaction + sell_ether*price
