import math 
import backtrader as bt


class GoldenCrossBBrsi(bt.Strategy):
   #BB under bottom line  , RSI under 20, MA cross  buy up vice versa
	params = (('fast', 7), ('slow', 25), ('order_percentage', 0.95), ('ticker', 'BTCUSDT'), ('bb_period', 20),('bbsd',2), ('rsi_period', 20) )

	def __init__(self):
		self.fast_moving_average = bt.indicators.SMA(
			self.data.close, period=self.params.fast, plotname='7 day moving average'
		)

		self.slow_moving_average = bt.indicators.SMA(
			self.data.close, period=self.params.slow, plotname='25 dat moving average'
		)
		

		self.corssover = bt.indicators.CrossOver(self.fast_moving_average, self.slow_moving_average)

		#bolliger band
		self.bb = bt.indicators.BollingerBands(self.data.close, self.params.bb_period, self.params.bbsd)
		self.bbPriceCross = bt.indicators.BollingerBandsPct(self.data.close)

		#RsI
		self.rsi = bt.indicators.RelativeStrengthIndex(self.data.close, self.params.rsi_period , 20, 80)
		

	def next(self):
		pass