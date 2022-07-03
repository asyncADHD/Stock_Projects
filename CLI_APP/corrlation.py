import math 
from numpy import mean
from numpy import std
import numpy as np
import pandas as pd
import yahoo_fin.stock_info as si
import yfinance as yf
from matplotlib import pyplot
from scipy.stats import spearmanr



# cov(X, Y) = (sum (x - mean(X)) * (y - mean(Y)) ) * 1/(n-1)

# (one day - pervious day) / previous day

# ([0]/[1] - 1) // ittrate 

''' 
The slope i.e. beta won't change even if you subtract  
the risk free return from both Apple and S&P's return
(Assuming the risk free rate hasn't changed over the period). 
As long as all X's are changed by the same amount in the same direction, 
and/or all the Y's are changed by the same amount in the same direction, 
the slope of the line does not change. Hence the beta would be the same.
'''


ticker = yf.Ticker("aapl")
ticker2 = yf.Ticker("^gspc")



appl_hist = ticker.history(period='5y')
sp500_hist = ticker2.history(period='5y')

df = pd.DataFrame(appl_hist)
df2 = pd.DataFrame(sp500_hist)

data_quality = False

num_of_nuls = df.isnull().sum()
num_of_nuls2 = df2.isnull().sum()
sum_nulls = num_of_nuls.sum() + num_of_nuls2.sum()

if sum_nulls == 0:
    data_quality = True

if data_quality == True:
    # calculate the mean of the high and low prices
    high_array_unclean = df['High']
    low_array_unclean = df['Low']
    high2_array_unclean = df2['High']
    low2_array_unclean = df2['Low']

    length = len(high_array_unclean)

    high_array = []
    low_array = []
    high2_array = []
    low2_array = []

    x = 0 

    for i in range(length):
        high_array.append(high_array_unclean[x])
        low_array.append(low_array_unclean[x])
        high2_array.append(high2_array_unclean[x])
        low2_array.append(low2_array_unclean[x])
        x = x + 1

    mean_arr = []
    mean_arr_2 = []

    j = 0

    for i in range (length):
        mean_val = (high_array[j] + low_array[j]) / 2
        mean_arr.append(mean_val)
        mean_val_2 = (high2_array[j] + low2_array[j]) / 2
        mean_arr_2.append(mean_val_2)
        j = j + 1




    mean_val_stock = mean(mean_arr)
    mean_val_sp500 = mean(mean_arr_2)


    print (mean_val_stock, "\n", mean_val_sp500)
    corrlation = spearmanr(mean_arr, mean_arr_2)
    print (corrlation)

    stad = np.std(mean_arr)
    stad_2 = np.std(mean_arr_2)

    print (corrlation[0] * (stad / stad_2))

   



       












