import math
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
import yfinance as y
import numpy as np


# Make the moving average 10 days and 1 day moving average


class EMA:


    def ema(hist, days):
        ''' function to calculate a exponetial moving avarage '''
        ema = pd.Series(hist['Close'].ewm(span=days,min_periods=days-1,adjust=True,ignore_na=False).mean())
        return ema

    def calculate_ema(prices, days, smoothing=2):
        ema = [sum(prices[:days]) / days]
        for price in prices[days:]:
            ema.append((price * (smoothing / (1 + days))) + ema[-1] * (1 - (smoothing / (1 + days))))
        return ema


