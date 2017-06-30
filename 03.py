#3-1
naver_end_price =  [474500, 461500, 501000, 500500, 488500]
#3-2
print('max', max(naver_end_price))
#3-3
print('min', min(naver_end_price))
#3-4
print('diff', max(naver_end_price) - min(naver_end_price))
#3-5
print(naver_end_price[2])
#3-6
naver_end_price2 = {"09/07":naver_end_price[0]
, "09/08":naver_end_price[1]
, "09/09":naver_end_price[2]
, "09/10":naver_end_price[3]
, "09/11":naver_end_price[4]
}
print(naver_end_price2)
print(naver_end_price2['09/09'])

#%% : Ctrl + Enter
a = 1
b = 2
c = 3
print(a+b)

#%%
#%clear
a = list(range(0, 10))
for i in a:
    print(i)
print(1)
b = 21
#%%
#%clear
interest_stocks = ["Naver", "Samsung", "SK Hynix"]
for company in interest_stocks:
    print("%s: Buy 10" % company)
    
#%%
interest_stocks = {"Naver":10, "Samsung":5, "SK Hynix":30}
#for key, value in interest_stocks.items():
#    print(key)
for d in interest_stocks:
    print(d)

#%%
while 1:
    print(1)
    break;
    
#%%
def print_ntimes():
    print("대신증권")
    
#%%
print_ntimes();    
#%%
def cal_upper(price):
    increment = price * 0.3
    upper_price = price + increment
    return [upper_price, 1]
    
#%%
print(cal_upper(10000)) 
#%%
import stock
print(stock.author)



