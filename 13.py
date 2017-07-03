#%%
from pandas import Series, DataFrame

kakao = Series([92600, 92400, 92100, 94300, 92300])
print(kakao)

print(kakao[0])
print(kakao[2])
print(kakao[4])

print(type(kakao))

kakao2 = Series([92600, 92400, 92100, 94300, 92300], index=['2016-02-19',
                                                            '2016-02-18',
                                                            '2016-02-17',
                                                            '2016-02-16',
                                                            1])
#print(kakao2)
#print(kakao2['2016-02-19'])
#%%
#print(kakao2[2])
#print(kakao2.index)
#print(type(kakao2.index))

#%%
mine   = Series([10, 20, 30, 40], index=['naver', 'sk', 'kt', 'hh'])
friend = Series([10, 30, 20], index=['kt', 'naver', 'sk'])

#print(mine)

merge = mine + friend
print(merge)
print(merge['hh'])
#%%
raw_data = {'col0': [1, 2, 3, 4],
            'col1': [10, 20, 30, 40],
            'col2': [100, 200, 300, 400]}

data = DataFrame(raw_data)
print(data)

data['col0']
print(type(data['col0']))

#%%
daeshin = {'open':  [11650, 11100, 11200, 11100, 11000],
           'high':  [12100, 11800, 11200, 11100, 11150],
           'low' :  [11600, 11050, 10900, 10950, 10900],
           'close': [11900, 11600, 11000, 11100, 11050]}

daeshin_day = DataFrame(daeshin, columns=['open', 'high', 'low', 'close'])
print(daeshin_day)
for i in daeshin_day.values:
    print(i)
    
date = ['16.02.29', '16.02.26', '16.02.25', '16.02.24', '16.02.23']
daeshin_day = DataFrame(daeshin, columns=['open', 'high', 'low', 'close'], index=date)
daeshin_day
for i in daeshin_day:
    print(i)

daeshin_day['open'][0]

daeshin_day.ix['16.02.24']

print('columns', daeshin_day.columns)
print('index', daeshin_day.index)
print('values', daeshin_day.values)

#%%
import pandas_datareader.data as web
import datetime
start = datetime.datetime(2016, 2, 19)
end = datetime.datetime(2016, 3, 4)
print(start)
print(end)

#gs = web.DataReader("KRX:000660", "google", start, end)
gs = web.DataReader("KRX:000660", "google")
gs.info()

#%%
import matplotlib.pyplot as plt
#plt.plot(gs['Close'])
plt.plot(gs.index, gs['Close'])
plt.show()


