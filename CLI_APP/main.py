
from more_itertools import strip
import yahoo_fin.stock_info as si
from Colors import colors
import traceback
import yfinance as y
from moving_av import EMA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import log, sqrt, pi, exp
from scipy.stats import norm


def d1 (S, K, T, r, sigma): 
    """
    Inputs
    #S = Current stock Price
    #K = Strike Price
    #T = Time to maturity 1 year = 1, 1 months = 1/12
    #r = risk free interest rate
    #q = dividend yield  is assumed as zero
    # sigma = volatility
    Output
     # d1 = d1(S,K,T,r,q,sigma)
    """
    return(log(S/K) + (r + sigma**2/2.)*T)/(sigma*sqrt(T))
def d2(S,K,T,r,sigma): 
    """
    Inputs
    #S = Current stock Price
    #K = Strike Price
    #T = Time to maturity 1 year = 1, 1 months = 1/12
    #r = risk free interest rate
    # sigma = volatility
    Output
    # d2 = d2(S,K,T,r,sigma)
    """
    return d1(S,K,T,r,sigma)-sigma*sqrt(T)

def BlackScholesCall(S,K,T,r,sigma):
    return S*norm.cdf(d1(S,K,T,r,sigma))-K*exp(-r*T)*norm.cdf(d2(S,K,T,r,sigma))
    
def BlackScholesPut(S,K,T,r,sigma):
    return K*exp(-r*T)-S+BlackScholesCall(S,K,T,r,sigma)


class CLI():
    def __init__(self):
        self.commands = {
            "help": self.help,
            "exit": self.exit,
            "-g": self.get,
            "-mav": self.mva,
        }

    def cli_welcome(self):
        print (colors.pt.yellow + "-"* 47)
        print (colors.pt.pink + "|" + colors.bold, colors.pt.cyan + "  Welcome to the Stock Price Analyzer CLI  " + colors.pt.pink + "|")
        print (colors.pt.pink + "|" + " " * 5 + colors.pt.green + "Type 'help' for a list of commands" + " " * 5 + colors.pt.pink + "|")
        print (colors.pt.yellow + "-" * 47 )


    def help(self):
        print (colors.pt.cyan + "--Commands List--")
        print (colors.pt.lightgrey + "help" + colors.pt.pink + " | " + colors.pt.green + "Shows this list of commands")
        print (colors.pt.lightgrey + "exit" + colors.pt.pink + " | " + colors.pt.green + "Exits the CLI")
        print (colors.pt.lightgrey + "-g" + colors.pt.pink + " | " + colors.pt.green + "-g <symbol> - Gets the current price of a stock")
        print (colors.pt.lightgrey + "-mav" + colors.pt.pink + " | " + colors.pt.green + "-mav  promt <time> <ticker> - Calculates the moving average of a stock")
    
    def exit(self):
        print("Exiting CLI")
        exit()
    
    def get(self, symbol):
        try:

            price = si.get_live_price(symbol)
            price = "{:,.2f}".format(price)
            print (colors.pt.lightblue + "The current price of " + symbol + " is $" + colors.pt.lightred + price )
        except Exception:
            print (colors.pt.lightred + "Error: " + colors.pt.lightblue + "The stock " + symbol + " is not recognized try checking the spelling")


    def mva(self, time , ticker):
        stock = y.Ticker(ticker)
        df = stock.history(period=time)
        ema = EMA.calculate_ema(df['Close'], 10)
        price_X = np.arange(df.shape[0])
        ema_X = np.arange(10, df.shape[0]+1)
        plt.xlabel('Days')
        plt.ylabel('Price')
        plt.plot(price_X, df['Close'], label='Closing Prices ')
        plt.plot(ema_X, ema, label='EMA')





    

if __name__ == "__main__":
    cli = CLI()
    cli.cli_welcome()
    while True:
        command = input(colors.pt.green + ">> ")
        if command == "help":
            cli.help()
        elif command == "exit":
            cli.exit()
        elif "-g" in command:
            symbol = command.strip("-g ")
            cli.get(symbol)
        elif "-mva" in command:
            print (colors.pt.blue + "Enter a time period: 10d, 20d, 30d, 60d, 1y")
            time = input(colors.pt.yellow + ">>")
            ticker = input(colors.pt.yellow + ">>")
            cli.mva(time, ticker)
            plt.legend()
            plt.show()
        elif "-BSC" in command:

            s = input(float(colors.pt.yellow + "Input Current Price>> "))
            k = input(float(colors.pt.yellow + "Input Strike Price>> "))
            t = input(float(colors.pt.yellow + "Input Time to Maturity>> "))
            r = input(float(colors.pt.yellow + "Input Risk Free Interest Rate>> "))
            sigma = input(float(colors.pt.yellow + "Input Volatility>> "))
            r = 0
            print (BlackScholesCall(s,k,t,r,sigma))
            
        else:
            print (colors.pt.red + command + " Not Recognized")


    


