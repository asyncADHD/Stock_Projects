from tracemalloc import start
import numpy
import math 
import pandas as pd
import yfinance as yf
import _datetime as datetime
import time 
import yahoo_fin.stock_info as si

# - volatility over today's price
# - volatility over x days 
# - volatility over x months
# - volatility over x years

'''
aapl_historical = aapl.history(start="2020-06-02", end="2020-06-07", interval="1m")
aapl_historical
'''


class Volatility:

    def twenty_four_volatility_std(stock):
        '''
        Calculate the volatility of the stock over the last 24 hours
        '''
        hist = yf.Ticker(stock).history(period='2d')
        hist_arr = []
        for i in range(len(hist)):
            hist_arr.append(hist.iloc[i]['Close'])
        prev_close = hist_arr[0]
        live_price = si.get_live_price(stock)
        stock_mean = numpy.mean(prev_close)
        deviation = live_price - stock_mean 
        deviation_squared = deviation ** 2
        variance = numpy.mean(deviation_squared)
        volatility = math.sqrt(variance)
        print (live_price, stock_mean, deviation, prev_close)
        return volatility

    def bata_coefficient():
        '''
        - The beta of a stock is the ratio of the returns of the stock to the returns of the benchmark.

        One measure of the relative volatility of a particular stock to 
        the market is its beta (β). 
        A beta approximates the overall 
        volatility of a security's returns against the returns of a relevant benchmark 
        (usually the S&P 500 is used). 
        For example, a stock with a 
        beta value of 1.1 has historically moved 110% for every 
        100% move in the benchmark, based on price level.


        What to calc?

        - The β of the stock 
        - The β of either the s&p 500 or the nasdaq 100.


        Equation:

        Beta = Covariance(Stock, Benchmark) / Variance(Benchmark)
        
        where:
        Covariance=Measure of a stock's return relative
        to that of the market
        Variance=Measure of how the market moves relative
        to its mean


        THIS NEED ANOTHER CLASS TO BE PULLED IN TO CALCULATE THE CORRLATION
        '''
        pass








print (Volatility.twenty_four_volatility_std("strax-usd"))
