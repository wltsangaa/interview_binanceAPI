#!/usr/bin/env python
# coding: utf-8

# In[16]:


附件为未经处理的btc500小时k线图。
请完成如下任务:
1.算出SMA(7hour),SMA(25hour),Bollinger Band(15H),RSI曲线,并用在同一张k线蜡烛图表中绘制出来。（30%）
2.请根据上面得到的indicator或其他indicator设计一个单因子或多因子的策略，并回测出策略的Maximum Drawdown,Profit_and Loss,Sharp ratio。（40%）
3.附件中附带了一个test-monitor api的json文件，请仅使用requests库和其他数学库获得此api对应账户的BTCUSDT永续合约和ETHUSDT永续合约持仓模式（参考币安文档：GET /fapi/v1/positionSide/dual）（30%）
4.（附加题目）使用 asyncio 模块将第三部分设计成60s循环一次的单线程任务。保存log文件。 （20%）

Data_Path:'./BTCusdt_test.csv'
credentials_path:'./test.json'
部分参考网页：'https://binance-docs.github.io/apidocs/futures/cn/'
            'https://pypi.org/project/mplfinance/'

