# ---------------STRATEGY TWO - MOVING AVERAGE------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
import time


movingAveragePeriod = 60
currentMovingAverage = 0
data = []
counter = 0
buy_status = True
sell_status = False

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


def movingAverage(values, window):
	weights = np.repeat(1.0, window)/window
	smas = np.convolve(values,weights, 'valid')
	return smas

cash_wallet = 10000.0
eth_wallet = 0

with open('data/hourlybitcoin.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter =',')
	for row in readCSV:
		if (counter > 0):
			print row[4]
			coin_price = float(row[4])
			data.append(coin_price)
			if (counter > movingAveragePeriod):
				avg = movingAverage(data,movingAveragePeriod)
				currentMovingAverage = avg[len(avg) - 1]
				print "Moving Avg:" + str(currentMovingAverage) + "  Price  " + str(coin_price)
				# time.sleep(1)
				if ((last_coin_price > currentMovingAverage) and (last_coin_price > coin_price) and sell_status):
					sell(coin_price)
					sell_status = False
					buy_status = True
				elif ((last_coin_price < currentMovingAverage) and (last_coin_price < coin_price) and buy_status):
					buy(coin_price)
					buy_status = False
					sell_status = True
			last_coin_price = coin_price

		counter = counter + 1

print "TOTAL CASH VALUE IS : " + str(cash_wallet)
