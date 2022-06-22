import math
import requests
import json
import requests
import yfinance as yf
import pandas as pd
import numpy as np
import datetime 
import warnings
import yahoo_fin.stock_info as si




def strRed(skk):         return "\033[91m {}\033[00m".format(skk)
def strGreen(skk):       return "\033[92m {}\033[00m".format(skk)
def strYellow(skk):      return "\033[93m {}\033[00m".format(skk)
def strLightPurple(skk): return "\033[94m {}\033[00m".format(skk)
def strPurple(skk):      return "\033[95m {}\033[00m".format(skk)
def strCyan(skk):        return "\033[96m {}\033[00m".format(skk)
def strLightGray(skk):   return "\033[97m {}\033[00m".format(skk)
def strBlack(skk):       return "\033[98m {}\033[00m".format(skk)
def strBold(skk):        return "\033[1m {}\033[0m".format(skk)


def cli_welcome():
    print (strYellow("-" * 47 ))
    print (strPurple("|") + strBold(strCyan("  Welcome to the Stock Price Analyzer CLI  ")) + strPurple("|"))
    print (strPurple("|") + (" " * 5 ) + strGreen("Type 'help' for a list of commands")+ (" " * 5) + strPurple("|"))
    print (strYellow("-" * 47 ))


def cli_help():
    print (strCyan("-Commands List-"))
    print (strLightGray("help") + strPurple(" - ") + strGreen("Shows this list of commands"))
    print (strLightGray("exit") + strPurple(" - ") + strGreen("Exits the CLI"))
    print (strLightGray("get_price") + strPurple(" - ") + strGreen("Gets the current price of a stock"))
    print (strLightGray("get_o_c") + strPurple(" - ") + strGreen("Gets the option chain for a stock"))
    print (strLightGray("get_historical_data") + strPurple(" - ") + strGreen("Gets the historical data of a stock"))
    print (strLightGray("get_news") + strPurple(" - ") + strGreen("Gets the news of a stock"))
    print (strLightGray("get_quote") + strPurple(" - ") + strGreen("Gets the quote of a stock"))
    print (strLightGray("get_chart") + strPurple(" - ") + strGreen("Gets the chart of a stock"))
    print (strLightGray("get_company") + strPurple(" - ") + strGreen("Gets the company info of a stock"))
    print (strLightGray("get_logo") + strPurple(" - ") + strGreen("Gets the logo of a stock"))




def option_chain(symbol):
    tk = yf.Ticker(symbol)
    exps = tk.options

    # Get options for each expiration
    options = pd.DataFrame()
    for e in exps:
        warnings.filterwarnings("ignore")
        opt = tk.option_chain(e)
        opt = pd.DataFrame().append(opt.calls).append(opt.puts)
        opt['expirationDate'] = e
        options = options.append(opt, ignore_index=True)

    # Bizarre error in yfinance that gives the wrong expiration date
    # Add 1 day to get the correct expiration date
    options['expirationDate'] = pd.to_datetime(options['expirationDate']) + datetime.timedelta(days = 1)
    options['dte'] = (options['expirationDate'] - datetime.datetime.today()).dt.days / 365
    
    # Boolean column if the option is a CALL
    options['CALL'] = options['contractSymbol'].str[4:].apply(
        lambda x: "C" in x)
    
    options[['bid', 'ask', 'strike']] = options[['bid', 'ask', 'strike']].apply(pd.to_numeric)
    options['mark'] = (options['bid'] + options['ask']) / 2 # Calculate the midpoint of the bid-ask
    
    # Drop unnecessary and meaningless columns
    options = options.drop(columns = ['contractSize', 'currency', 'change', 'percentChange', 'lastTradeDate', 'lastPrice'])

    return options


def get_price(symbol):
    price = si.get_live_price(symbol)
    price = "{:,.2f}".format(price)
    print (strGreen("The current price of " + symbol + " is $" + strBold(strLightPurple(str(price)))))



df = option_chain("AAPL")

def main():
    cli_welcome()
    while True:
        command = input(strBold(strLightPurple(">> ")))
        if command == "help":
            cli_help()
        elif command == "get_o_c":
            ticker = input(strBold(strLightPurple("STOCK CODE: ")))
            df = option_chain(ticker)
            print (df)
        elif command == "get_price":
            ticker = input(strBold(strLightPurple("STOCK CODE: ")))
            get_price(ticker)
        elif command == "exit":
            x = 1
        



running = True
x = 0
if x == 1:
    running = False

while running:
    main()




    