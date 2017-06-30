#%%
#4-1
for i in range(0, 4):
    print('*', end='')
    
#%%
for i in range(0, 4):
    for j in range(0, 5):
        print('*', end='')
    print('')
#%%
for i in range(1, 6):
    for j in range(0, i):
        print('*', end='')
    print('')
#%%
for i in range(1, 6):
    for j in range(0, 6-i):
        print('*', end='')
    print('')
#%%
apart = [[101, 102, 103, 104],[201, 202, 203, 204],[301, 302, 302, 303], [401, 402, 403, 404]]
arrears = [101, 203, 301, 404]
for floor in apart:
    for house in floor:
        if house in arrears:
            continue
        else:
            print("Newspaper delivery: ", house)