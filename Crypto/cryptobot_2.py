# ---------------STRATEGY THREE - SLOPE CALCULATION------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
import csv
import time

data = [20,25,30,45,45,50,50,53,20,14,
		24,12,8,2,15,16,18,19,30,50,55,
		56,57,90,88,78,77,70,79,80,99]

weight_factor = [0.5,0.5]

cash_wallet = 10000.0
eth_wallet = 0
window_size = 10
threshold = 0.5

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

#average window value vs. current value
def buyConditionOne(data, i):
	slope_sum = np.average(data)
	if (data[i-1] < slope_sum):
		print "buy %s" % (data[i-1])
		return True
	else:
		return False

def buyConditionTwo(data,i):
	slope_array = np.diff(data)


def percentageCalculator(data):
	percent = float((data[len(data) - 1] - data[0]))/float(data[0])
	return percent

count = 0
price_list = []
for price in data:
	if (len(price_list) >= window_size ):
		price_list.pop(0)
	price_list.append(price)

	if (count >= window_size):
		cond_one = buyConditionOne(price_list, count)

	count = count + 1
