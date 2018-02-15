import numpy as numpy
import pandas as pd 
import matplotlib.pyplot as plt
plt.style.use('ggplot')

data = pd.read_csv('http://hilpisch.com/tr_eikon_eod_data.csv', index_col=0, parse_dates = True)
# print type(data)
# print data.info()

print data['AAPL.O'].plot(figsize=(10,6))