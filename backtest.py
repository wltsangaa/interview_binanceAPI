import backtrader
import datetime
from strategies import TestStrategy


cerebro = backtrader.Cerebro()
cerebro.broker.set_cash(1000000)

# Create a Data Feed
data = backtrader.feeds.YahooFinanceCSVData(
	dataname='gold.csv',
	# Do not pass values before this date
	fromdate=datetime.datetime(1995, 3, 1),
	# Do not pass values after this date
	todate=datetime.datetime(2020, 6, 10),
	reverse=False)


cerebro.adddata(data)

cerebro.addstrategy(TestStrategy)

print ('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final Portfolio Vaule: %.2f' % cerebro.broker.getvalue())

cerebro.plot()