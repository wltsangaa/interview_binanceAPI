import os, sys, argparse
import pandas as pd
import backtrader as bt
from GoldenCross import GoldenCrossBBrsi
import pdb
from datetime import datetime


cerebro = bt.Cerebro()
cerebro.broker.setcash(100000)

btcusdt_prices = pd.read_csv('BTCusdt_test1.csv', index_col='Date', parse_dates=True)

pdb.set_trace()
feed = bt.feeds.PandasData(dataname=btcusdt_prices)

cerebro.adddata(feed)

cerebro.addstrategy(GoldenCrossBBrsi)

cerebro.run()

cerebro.plot
