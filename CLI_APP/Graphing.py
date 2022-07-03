import numpy 
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import yfinance as y
from plotly.subplots import make_subplots


class Graphing:

    def simple_line(hist):
        fig = go.Figure(data=go.Scatter(x=hist.index,y=hist['Close'], mode='lines'))
        fig.show()

    def simple_line_with_markers(hsit):
        fig = go.Figure(data=go.Scatter(x=hist.index,y=hist['Close'], mode='lines+markers'))
        fig.show()

    def line_with_volume(hist):
        fig2 = make_subplots(specs=[[{"secondary_y": True}]])
        fig2.add_trace(go.Scatter(x=hist.index,y=hist['Close'],name='Price'),secondary_y=False)
        fig2.add_trace(go.Bar(x=hist.index,y=hist['Volume'],name='Volume'),secondary_y=True)
        fig2.show()

    def candle_stick():
        pass
    

aapl = y.Ticker("AAPL")
hist = aapl.history(period='1y')







        