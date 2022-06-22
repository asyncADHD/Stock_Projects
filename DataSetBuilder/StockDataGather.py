import yfinance as yf

import pandas as pd
import time 

import yahoo_fin.stock_info as si





def price_getter( stock):

    price = si.get_live_price(stock)
    price_f = "{:,.2f}".format(price)
    return price_f

def get_info(stock):
    msft = yf.Ticker(stock)
    info = msft.info
    return info
    

print (get_info("aapl"))
    

x = 1

asset_arr = []
 
# while x > 0:
#     asset_arr.append(price_getter("AAPL"))
#     x = x - 1
#     time.sleep(1)
#     print (asset_arr)








