import matplotlib.pyplot as plt
import numpy as np
import csv
import time

data = [20,25,30,45,45,50,50,53,20,14,
		24,12,8,2,15,16,18,19,30,50,55,
		56,57,90,88,78,77,70,79,80,99,2,3,4,5,40]

weight_factor = [0.5,0.5]

cash_wallet = 200000.0
eth_wallet = 0
window_size = 10
threshold = 0.5
x = []
y = []

def buy(price):
	global cash_wallet
	global eth_wallet
	if (cash_wallet > 0):
		cash_wallet = cash_wallet - float(price)
		eth_wallet = eth_wallet + 1

	print "---------buy----------"

def sell(price):
	global eth_wallet
	global cash_wallet
	cash_wallet = cash_wallet + float(price)
	eth_wallet = eth_wallet - 1
	print "---------sell--------"

#average window value vs. current value
def buyConditionOne(data):
	value_sum = np.average(data)
	if (data[-1] < value_sum):
		# print "buy %s" % (data[-1])
		return True
	else:
		return False

#average window derivative value vs. current derivative value
def buyConditionTwo(data):
	slope_array = np.diff(data)
	slope_sum = np.average(slope_array)
	last_slope = data[-1] - data[-2]
	# print "average slope %s, last slope %s" % (slope_sum, last_slope)
	if (last_slope < slope_sum):
		# print "buy %s" % (data[-1])
		return True
	else:
		return False

def sellCondition(current_price, buy_price_list):

	if (len(buy_price_list) == 0):
		return False

	for index, item in enumerate(buy_price_list):
		if ( current_price > 1.5*item ):
			print "sell price %s bought price %s" % (current_price, item)
			buy_price_list.pop(index)
			sell(current_price)
			return True
		else:
			return True


def percentageCalculator(data):
	percent = float((data[len(data) - 1] - data[0]))/float(data[0])
	return percent

count = 0
price_list = []
buy_price_list = []
# for price in data:
# 	if (len(price_list) >= window_size ):
# 		price_list.pop(0)
# 	price_list.append(price)
#
# 	if (count >= window_size):
# 		print price_list
# 		buy_cond_one = buyConditionOne(price_list)
# 		buy_cond_two = buyConditionTwo(price_list)
# 		if (buy_cond_one and buy_cond_two):
# 			print "buy"
# 			buy_price_list.append(price)
# 			buy(price)
# 		sell_cond = sellCondition(price, buy_price_list)
# 	count = count + 1
count = 0
with open('data/hourlybitcoin.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter =',')
	for row in readCSV:
		price = float(row[4])
		if (len(price_list) >= window_size ):
			price_list.pop(0)
		price_list.append(price)

		if (count >= window_size):
			# print price_list
			buy_cond_one = buyConditionOne(price_list)
			buy_cond_two = buyConditionTwo(price_list)
			if (buy_cond_one and buy_cond_two):
				buy_price_list.append(price)
				buy(price)
			sell_cond = sellCondition(price, buy_price_list)
		count = count + 1
		print "cash on hand %s bitcoin on hand %s " % (cash_wallet, eth_wallet)
		print cash_wallet + eth_wallet*price
		count = count + 1
		x.append(count)
		y.append(cash_wallet + eth_wallet*price)



plt.plot(x,y)
plt.show()
# print cash_wallet + eth_wallet
