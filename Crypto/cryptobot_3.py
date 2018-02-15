import numpy as np
import csv

class PriceTracker:

    def __init__(self):
        pass

    def getValue(self, i):
        pass


class CsvTracker:
    def __init__(self, csv_file):
        self.current_row = 61
        self.csv_file_content = []
        self.csv_file = csv.reader(csv_file, delimiter =',')
        for line in self.csv_file:
            self.csv_file_content.append(line)
        pass

    def getValue(self, i):
        if i > 0:
            i = i * -1

        desired_row = self.current_row + i
        row = self.csv_file_content[desired_row]
        return row[1]

    def increment_time(self, i):
        self.current_row += i

class BuyBot:

    """
    @type PriceTracker
    """


    """
    Decides whether or not we want to buy. Another class will poll us
    """
    def __init__(self, price_tracker):
        self.price_tracker = None
        self.heuristics = []
        self.heuristic_weights = [0.25, 0.25, 0.25, 0.25]
        self.price_tracker = price_tracker
        self.heuristics.append(BuyDerivativeWindow(60, self.price_tracker))
        self.heuristics.append(BuyDerivativeWindow(15, self.price_tracker))
        self.heuristics.append(BuyPriceWindow(60, self.price_tracker))
        self.heuristics.append(BuyPriceWindow(15, self.price_tracker))

    def poll(self):
        current_price = self.price_tracker.getValue(0)
        result = 0
        i = 0
        for heuristic in self.heuristics:
            print "For Heuristic %s at time %s ouptut = %s" % (i, self.price_tracker.current_row, heuristic.getCurrentValue())
            result += heuristic.getCurrentValue() * self.heuristic_weights[i]
            i = i+1
        print "\tresult = %s and price = %s" % (result, current_price)

class BuyPriceWindow:
    def __init__(self, window, price_tracker):
        self.window = window
        self.price_tracker = price_tracker

    def getCurrentValue(self):
        price_values = []

        #store the values
        for i in range(0, self.window):
            price_values.append(float(self.price_tracker.getValue(self.window - i)))

        average = np.average(price_values)

        return average - price_values[-1]


class BuyDerivativeWindow:

    def __init__(self, window, price_tracker):
        self.window = window
        self.price_tracker = price_tracker

    def getCurrentValue(self):
        price_values = []
        derivative_values = []

        #store the values
        for i in range(0, self.window):
            price_values.append(self.price_tracker.getValue(self.window - i))

        #compute the derivatives
        length = len(price_values) - 1

        for i in range(0, length):
            derivative_values.append(float(price_values[i + 1]) - float(price_values[i]))

        average_derivative_value = np.average(derivative_values)
        last_derivative_value = derivative_values[-1]

        return average_derivative_value

def main():
    print 'asdf'
    file_path = './data/hourlybitcoin.csv'
    price_tracker = CsvTracker(open(file_path, 'r'))
    buy_bot = BuyBot(price_tracker)

    for i in range(0, 60):
        buy_bot.poll()
        price_tracker.increment_time(1)
    pass

if __name__ == "__main__":
    main()
