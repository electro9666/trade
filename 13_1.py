# -*- coding: utf-8 -*-
#%%
#이동평균선

import pandas as pd
import pandas_datareader.data as web
gs = web.DataReader("KRX:078930", "google", "2014-01-01", "2016-03-06")
gs
gs.head()
gs.tail()
gs.info()

ma5 = gs['Close'].rolling(window=5).mean()
gs['Volume'] != 0
  
new_gs = gs[gs['Volume'] !=0]
new_gs.info()

new_gs.insert(len(new_gs.columns), "MA5", ma5)

#%%
ma20 = new_gs['Close'].rolling(window=20).mean()
ma60 = new_gs['Close'].rolling(window=60).mean()
ma120 = new_gs['Close'].rolling(window=120).mean()
new_gs.insert(len(new_gs.columns), "MA20", ma20)
new_gs.insert(len(new_gs.columns), "MA60", ma60)
new_gs.insert(len(new_gs.columns), "MA120", ma120)

#%%
import matplotlib.pyplot as plt
plt.plot(new_gs.index, new_gs['Close'], label="Close")
plt.plot(new_gs.index, new_gs['MA5'], label="MA5")
plt.plot(new_gs.index, new_gs['MA20'], label="MA20")
plt.plot(new_gs.index, new_gs['MA60'], label="MA60")
plt.plot(new_gs.index, new_gs['MA120'], label="MA120")
plt.legend(loc='best')
plt.grid()