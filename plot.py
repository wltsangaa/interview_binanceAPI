from pandas.core.indexes.base import Index
import mplfinance as mpf
import pandas as pd
from pyti.bollinger_bands import upper_bollinger_band as bb_up
from pyti.bollinger_bands import middle_bollinger_band as bb_mid
from pyti.bollinger_bands import lower_bollinger_band as bb_low
from pyti.relative_strength_index import relative_strength_index as rsi

# def serial_date_to_string(srl_no):
#     new_date = dt.datetime(1970,1,1,0,0) + dt.timedelta(srl_no - 1)
#     return new_date.strftime("%Y-%m-%d")





daily = pd.read_csv('BTCusdt_test1.csv',index_col=0,parse_dates=True)
daily.index.name = 'Date'
daily.shape
daily.head(3)
daily.tail(3)
# need to change daily.index to datetime format
daily.index=pd.DatetimeIndex(daily.index)


data = daily['Close'].values.tolist()
BBperiod = 20
bb_up = bb_up(data,BBperiod)
bb_mid = bb_mid(data,BBperiod)
bb_low = bb_low(data,BBperiod)
daily['bb_up'] = bb_up
daily['bb_mid'] = bb_mid
daily['bb_low'] = bb_low


rsiPeriod = 20
daily['rsi'] = rsi(daily['Close'].values.tolist(), rsiPeriod)

addin = [mpf.make_addplot(daily[['bb_up', 'bb_mid', 'bb_low']]),
mpf.make_addplot(daily['rsi'],panel='lower',color='g')]



mpf.plot(daily, type='candle', addplot=addin, volume=True, mav= (7, 25))




