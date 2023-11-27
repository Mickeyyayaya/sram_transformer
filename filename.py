import os
a = os.listdir('card_new')
print(a)

c = len(a)

for i in range(0,c+1):
    if i <= 12:
        os.rename(f'./card_new/{a[i]}',f'./card_new/club_{i+1}.png')
    elif i > 12 and i <= 25:
        os.rename(f'./card_new/{a[i]}',f'./card_new/diamond_{i-12}.png')
    elif i > 25 and i <= 38:
        os.rename(f'./card_new/{a[i]}',f'./card_new/heart_{i-25}.png')
    elif i > 39 and i <= 52:
        os.rename(f'./card_new/{a[i]}',f'./card_new/spade_{i-39}.png')
    elif i == 53:
        os.rename(f'./card_new/{a[i]}',f'./card_new/card_back.png')