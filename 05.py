#%%
import time
a = time.time()
print(a)
print(time.ctime())
#%%

for i in range(10):
    print(i)
    time.sleep(1)
    
#%%
import random
dir(time)
dir(random)
#%%

import os
os.getcwd()
os.listdir()
a = [1,2,34]
os.listdir('c:\\')

def abc():
    pass
    

dir()

#%%

abc = {'a':1, 'bb':2}
abc['a']
abc['bb']

#%%
class BusinessCard:
    def set_info(self, name, email, addr):
            self.name = name
            self.email = email
            self.addr = addr

card1 = BusinessCard()
card1
type(card1)
card1.set_info('name2', 'gmail', 'add1')
card1.name

card1.__dict__
#%%
