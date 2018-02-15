# ---------------STRATEGY TWO - MOVING AVERAGE------------------------------------------
import numpy as np
import csv
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

def slopeCondition(price_list):


cash_wallet = 10000.0
eth_wallet = 0
price_list = []
count = 0

with open('data/hourlybitcoin.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter =',')
	for row in readCSV:
        price_list.append(row[1])
        count = count + 1
        if (count > 60):
            price_list.pop(0)
            conditionOne = slopeCondition()
