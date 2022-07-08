
import yahoo_fin.options as yf
import pandas as pd
import numpy as np
from datetime import date
import yfinance as yf



class Option:
    def get_exp_date(ticker):
        get_expration_dates = yf.get_expiration_dates(ticker)
        return get_expration_dates

    def get_opt_calls(ticker, date):
        chain = yf.get_options_chain(ticker)
        chain["calls"]
        return chain["calls"]

    def calculate_vol(ticker, period):
        
        # Set date for the data to be retrieved
        date_today = date.today() - pd.DateOffset(days=1)
        date_minus_1 = date_today - pd.DateOffset(days=period)
        date_minus_1 = date_minus_1.strftime("%Y-%m-%d")
        date_today = date_today.strftime("%Y-%m-%d")

        # Get the data from Yahoo Finance
        Data = yf.download(ticker, start=date_minus_1, end=date_today)
        Data = pd.DataFrame(Data)

        # Remove unnecessary columns
        Data.drop(["Open", "High", "Low", "Close","Volume"], axis=1, inplace=True)
        Data["PTC"] = Data["Adj Close"].pct_change()
        
        # Calculate the volatility
        Data_PTC = Data["PTC"].iloc[1:]
        vol = Data_PTC
        vol = np.std(vol, ddof=1)
        vol = vol * np.sqrt(len(Data_PTC))

        return vol






