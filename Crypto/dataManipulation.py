# ---------------STRATEGY ONE - SLOPES ---------------------------------------------
# This trading strategy calculates the slope and stores the last x number of points. 
# If the slope over a certain continues to rise or continues to fall, 
# a buy or sell is executed

import matplotlib.pyplot as plt
import numpy as np
import csv

def slope(y2,y1,x2,x1):
	slope = (float(y2)-float(y1))/((x2-x1))
	return slope

def buy(price):
	global cash_wallet
	global eth_wallet
	cash_wallet = cash_wallet - float(price)
	eth_wallet = eth_wallet + float(price)

	print "---------buy----------"


def sell(price):
	global eth_wallet
	global cash_wallet
	cash_wallet = cash_wallet + float(price)
	eth_wallet = eth_wallet - float(price)
	print "---------sell--------"


# instantiate variables
x = []
y = []
count = 0
collect_price_fall = []
collect_price_rise = []
cash_wallet = 10000.0
eth_wallet = 0

with open('data/etherprice.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter =',')
	for row in readCSV:
		x.append(count)
		y.append(row[2])

		if (count > 1):
			m = slope(y[count], y[count - 1], count, count - 1)
			print m
			
			if (m < -5 and m_store < -5):
				collect_price_fall.append(m)
				if (len(collect_price_fall) > 4 ):
					buy(y[count])
					collect_price_fall = []

			if (m > 2 and m_store > 2):
				collect_price_rise.append(m)
				if(len(collect_price_rise) > 4 ):
					sell(y[count])
					collect_price_rise = []
			m_store = m

		count = count + 1			

plt.plot(x,y)
# plt.show()

print "TOTAL CASH VALUE IS : " + str(cash_wallet)
# print "TOTAL ETHEREUM VALUE IS: " +str(eth_wallet)